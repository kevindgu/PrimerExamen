"""
Sistema de tabla de puntuaciones.
- Almacenamiento primario: Google Sheets (múltiples hojas)
    · "datos"   → una fila por estudiante: [nombre, JSON_stats]
    · "examenes"→ una fila por estudiante: [nombre, JSON_examen_en_progreso]
- Fallback automático: JSON local (scores_local.json / examenes_local.json)
- Caché en memoria para evitar llamadas repetidas
"""
import json
import os
import math
import time
from datetime import datetime
import streamlit as st

# ── Fallback local ────────────────────────────────────────────
_LOCAL_FILE       = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scores_local.json")
_LOCAL_EXAMS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "examenes_local.json")

# ── Caché en memoria ──────────────────────────────────────────
_cache:      dict  = {}
_cache_ts:   float = 0.0
_exam_cache: dict  = {}
_exam_cache_ts: float = 0.0
_CACHE_TTL = 30  # segundos

# Conexión reutilizable a Google Sheets
_spreadsheet = None

DIFICULTADES_ORDEN = ["Fácil", "Normal", "Difícil", "💀 Super Difícil", "☠️ Mega Difícil"]
MATERIAS_ORDEN = ["Matemáticas", "Ciencias", "Estudios Sociales", "Español"]

LOGROS = [
    {"id": "primera_vez",    "emoji": "🐣", "nombre": "Primera vez",    "desc": "Completar tu primera sesión",            "cond": lambda s: s["sesiones"] >= 1},
    {"id": "racha_5",        "emoji": "🔥", "nombre": "En llamas",       "desc": "Racha de 5 respuestas correctas",        "cond": lambda s: s["max_racha"] >= 5},
    {"id": "racha_10",       "emoji": "💥", "nombre": "Imparable",       "desc": "Racha de 10 respuestas correctas",       "cond": lambda s: s["max_racha"] >= 10},
    {"id": "racha_20",       "emoji": "⚡", "nombre": "Rayo",            "desc": "Racha de 20 respuestas correctas",       "cond": lambda s: s["max_racha"] >= 20},
    {"id": "xp_500",         "emoji": "⭐", "nombre": "Estrella",        "desc": "Acumular 500 XP en total",               "cond": lambda s: s["xp_total"] >= 500},
    {"id": "xp_2000",        "emoji": "🌟", "nombre": "Superestrella",   "desc": "Acumular 2000 XP en total",              "cond": lambda s: s["xp_total"] >= 2000},
    {"id": "xp_10000",       "emoji": "💎", "nombre": "Diamante",        "desc": "Acumular 10000 XP en total",             "cond": lambda s: s["xp_total"] >= 10000},
    {"id": "mult_x4",        "emoji": "🚀", "nombre": "Cohete",          "desc": "Alcanzar multiplicador x4",              "cond": lambda s: s["max_multiplicador"] >= 4},
    {"id": "100_respuestas", "emoji": "📚", "nombre": "Estudioso",       "desc": "Responder 100 preguntas en total",       "cond": lambda s: s["total_respuestas"] >= 100},
    {"id": "500_respuestas", "emoji": "🏆", "nombre": "Campeón",         "desc": "Responder 500 preguntas en total",       "cond": lambda s: s["total_respuestas"] >= 500},
    {"id": "90_pct",         "emoji": "🎯", "nombre": "Certero",         "desc": "Sesión con 90%+ de efectividad",         "cond": lambda s: s["mejor_pct"] >= 90},
    {"id": "100_pct",        "emoji": "👑", "nombre": "Perfecto",        "desc": "Sesión con 100% de efectividad",         "cond": lambda s: s["mejor_pct"] >= 100},
    {"id": "examen_aprobado","emoji": "📝", "nombre": "Aprobado",        "desc": "Aprobar un examen con 70%+",             "cond": lambda s: s.get("mejor_pct_examen", 0) >= 70},
    {"id": "examen_honor",   "emoji": "🎓", "nombre": "Cuadro de honor", "desc": "Aprobar un examen con 90%+",             "cond": lambda s: s.get("mejor_pct_examen", 0) >= 90},
]


# ── Fórmula de puntuación balanceada ─────────────────────────
def calcular_score(xp_total: int, total_respuestas: int, pct: int) -> int:
    if total_respuestas == 0:
        return 0
    ef = math.sqrt(max(pct, 1) / 100)
    vol = math.log10(total_respuestas + 1)
    return int(xp_total * ef * vol)


# ── Google Sheets ─────────────────────────────────────────────

def _get_spreadsheet():
    global _spreadsheet
    if _spreadsheet is not None:
        return _spreadsheet
    import streamlit as st
    import gspread
    from google.oauth2.service_account import Credentials
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    client = gspread.authorize(creds)
    _spreadsheet = client.open_by_key(st.secrets["SHEET_ID"])
    return _spreadsheet


def _get_or_create_ws(title, rows=200, cols=2):
    """Retorna la hoja con ese título, creándola si no existe."""
    ss = _get_spreadsheet()
    try:
        return ss.worksheet(title)
    except Exception:
        return ss.add_worksheet(title=title, rows=rows, cols=cols)


def _ws_read_all(ws_title) -> dict:
    """Lee {nombre: dict} de una hoja. Col A = nombre, Col B = JSON."""
    ws = _get_or_create_ws(ws_title)
    rows = ws.get_all_values()
    result = {}
    for row in rows:
        if len(row) >= 2 and row[0] and row[1]:
            try:
                result[row[0]] = json.loads(row[1])
            except Exception:
                pass
    return result


def _ws_write_all(ws_title, data: dict):
    """Reescribe toda la hoja con los datos de 'data'. Una fila por estudiante."""
    ws = _get_or_create_ws(ws_title)
    ws.clear()
    rows = [[nombre, json.dumps(val, ensure_ascii=False)]
            for nombre, val in data.items()]
    if rows:
        # "A1" es obligatorio como primer argumento en gspread 5.x y 6.x
        ws.update("A1", rows, value_input_option='RAW')


def _ws_upsert(ws_title, nombre, val):
    """Actualiza la fila del estudiante, o la inserta si no existe."""
    ws = _get_or_create_ws(ws_title)
    json_str = json.dumps(val, ensure_ascii=False)
    try:
        cell = ws.find(nombre, in_column=1)
        ws.update_cell(cell.row, 2, json_str)
    except Exception:
        ws.append_row([nombre, json_str], value_input_option='RAW')


def _ws_delete_row(ws_title, nombre):
    """Elimina la fila del estudiante de la hoja."""
    try:
        ws = _get_or_create_ws(ws_title)
        cell = ws.find(nombre, in_column=1)
        if cell:
            ws.delete_rows(cell.row)
    except Exception:
        pass


# ── Migración del formato antiguo (todo en A1) ────────────────

def _migrate_from_sheet1():
    """
    Si Sheet1/A1 tiene datos en el formato viejo (un JSON gigante),
    los migra a las hojas 'datos' y 'examenes' y limpia A1.
    Solo se ejecuta una vez (detecta si 'datos' ya tiene filas).
    """
    try:
        ss = _get_spreadsheet()
        # Si 'datos' ya existe y tiene filas → ya se migró
        try:
            ws_datos = ss.worksheet("datos")
            if ws_datos.get_all_values():
                return
        except Exception:
            pass

        # Intentar leer el formato viejo
        old_sheet = ss.sheet1
        old_val = old_sheet.acell("A1").value
        if not old_val:
            return
        old_data = json.loads(old_val)
        if not old_data:
            return

        exam_data  = {}
        stats_data = {}
        for nombre, player in old_data.items():
            exam = player.pop("examen_en_progreso", None)
            if exam:
                exam_data[nombre] = exam
            stats_data[nombre] = player

        _ws_write_all("datos", stats_data)
        if exam_data:
            _ws_write_all("examenes", exam_data)

        # Limpiar A1 del sheet viejo para no migrar dos veces
        old_sheet.update("A1", [[""]])
    except Exception:
        pass


# ── Fallback local ─────────────────────────────────────────────

def _load_local() -> dict:
    if not os.path.exists(_LOCAL_FILE):
        return {}
    try:
        with open(_LOCAL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save_local(data: dict):
    try:
        with open(_LOCAL_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def _load_exams_local() -> dict:
    if not os.path.exists(_LOCAL_EXAMS_FILE):
        return {}
    try:
        with open(_LOCAL_EXAMS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save_exams_local(data: dict):
    try:
        with open(_LOCAL_EXAMS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


# ── Carga / Guardado de stats ──────────────────────────────────

def _load() -> dict:
    global _cache, _cache_ts
    now = time.time()
    if _cache and (now - _cache_ts) < _CACHE_TTL:
        return _cache
    try:
        _migrate_from_sheet1()
        data = _ws_read_all("datos")
        _cache = data
        _cache_ts = now
        _save_local(data)
        return data
    except Exception:
        data = _load_local()
        _cache = data
        _cache_ts = now
        return data


def _save(data: dict):
    """Guarda stats de todos los jugadores en la hoja 'datos'."""
    global _cache, _cache_ts
    # Nunca persistir examen_en_progreso en la hoja de stats
    clean = {n: {k: v for k, v in p.items() if k != "examen_en_progreso"}
             for n, p in data.items()}
    _cache = clean
    _cache_ts = time.time()
    _save_local(clean)
    try:
        _ws_write_all("datos", clean)
    except Exception:
        pass


def _invalidate_cache():
    global _cache_ts, _exam_cache_ts
    _cache_ts = 0.0
    _exam_cache_ts = 0.0


# ── Carga / Guardado de exámenes en progreso ───────────────────

def _load_exams() -> dict:
    global _exam_cache, _exam_cache_ts
    now = time.time()
    if _exam_cache and (now - _exam_cache_ts) < _CACHE_TTL:
        return _exam_cache
    try:
        data = _ws_read_all("examenes")
        _exam_cache = data
        _exam_cache_ts = now
        _save_exams_local(data)
        return data
    except Exception:
        data = _load_exams_local()
        _exam_cache = data
        _exam_cache_ts = now
        return data


def _persist_exam(nombre: str, exam_dict: dict):
    global _exam_cache, _exam_cache_ts
    _exam_cache[nombre] = exam_dict
    _exam_cache_ts = time.time()
    _save_exams_local(_exam_cache)
    try:
        _ws_upsert("examenes", nombre, exam_dict)
    except Exception:
        pass


def _remove_exam(nombre: str):
    global _exam_cache
    _exam_cache.pop(nombre, None)
    _save_exams_local(_exam_cache)
    try:
        _ws_delete_row("examenes", nombre)
    except Exception:
        pass


# ── Estructura de jugador ─────────────────────────────────────
def _player_default() -> dict:
    return {
        "xp_total": 0,
        "sesiones": 0,
        "total_respuestas": 0,
        "total_correctas": 0,
        "max_racha": 0,
        "max_multiplicador": 1,
        "mejor_pct": 0,
        "mejor_sesion_xp": 0,
        "logros": [],
        "historial": [],
        "por_dificultad": {},
        "por_materia": {},
        "temas_stats": {},
        "preguntas_debiles": [],
        "infinito": {
            "xp_total": 0, "sesiones": 0,
            "total_respuestas": 0, "total_correctas": 0,
            "max_racha": 0, "mejor_sesion_xp": 0,
        },
        "examen": {
            "xp_total": 0, "sesiones": 0,
            "total_respuestas": 0, "total_correctas": 0,
            "max_racha": 0, "mejor_sesion_xp": 0,
            "mejor_pct": 0,
        },
        "mejor_pct_examen": 0,
    }


def _migrate(p: dict) -> dict:
    """Agrega campos nuevos a jugadores existentes sin romper datos."""
    defaults = _player_default()
    for campo, val in defaults.items():
        if campo not in p:
            p[campo] = val
    return p


# ── API pública ───────────────────────────────────────────────
def get_player(nombre: str) -> dict:
    data = _load()
    if nombre not in data:
        data[nombre] = _player_default()
        _save(data)
    return _migrate(data[nombre])


def save_session(nombre: str, score: dict, materia: str, temas,
                 dificultad: str = "Normal", modo: str = "infinito",
                 preguntas_fallidas=None, topic_stats_sesion=None) -> list:
    """Guarda sesión. modo = 'infinito' | 'examen'"""
    data = _load()
    if nombre not in data:
        data[nombre] = _player_default()
    p = _migrate(data[nombre])

    total = score["total"]
    correctas = score["correct"]
    pct = int(100 * correctas / total) if total > 0 else 0
    nuevos_logros = []

    p["xp_total"] += score["xp"]
    p["sesiones"] += 1
    p["total_respuestas"] += total
    p["total_correctas"] += correctas
    p["max_racha"] = max(p["max_racha"], score["max_streak"])
    p["max_multiplicador"] = max(p["max_multiplicador"], score["max_multiplier"])
    p["mejor_pct"] = max(p["mejor_pct"], pct)
    p["mejor_sesion_xp"] = max(p["mejor_sesion_xp"], score["xp"])

    m_key = "examen" if modo == "examen" else "infinito"
    ms = p[m_key]
    ms["xp_total"] += score["xp"]
    ms["sesiones"] += 1
    ms["total_respuestas"] += total
    ms["total_correctas"] += correctas
    ms["max_racha"] = max(ms["max_racha"], score["max_streak"])
    ms["mejor_sesion_xp"] = max(ms["mejor_sesion_xp"], score["xp"])
    if modo == "examen":
        ms["mejor_pct"] = max(ms.get("mejor_pct", 0), pct)
        p["mejor_pct_examen"] = max(p.get("mejor_pct_examen", 0), pct)

    if dificultad not in p["por_dificultad"]:
        p["por_dificultad"][dificultad] = {
            "xp_total": 0, "sesiones": 0, "total_respuestas": 0,
            "total_correctas": 0, "mejor_sesion_xp": 0, "max_racha": 0}
    d = p["por_dificultad"][dificultad]
    d["xp_total"] += score["xp"]
    d["sesiones"] += 1
    d["total_respuestas"] += total
    d["total_correctas"] += correctas
    d["mejor_sesion_xp"] = max(d["mejor_sesion_xp"], score["xp"])
    d["max_racha"] = max(d["max_racha"], score["max_streak"])

    if materia not in p["por_materia"]:
        p["por_materia"][materia] = {
            "xp_total": 0, "sesiones": 0, "total_respuestas": 0,
            "total_correctas": 0, "mejor_sesion_xp": 0, "max_racha": 0}
    mat = p["por_materia"][materia]
    mat["xp_total"] += score["xp"]
    mat["sesiones"] += 1
    mat["total_respuestas"] += total
    mat["total_correctas"] += correctas
    mat["mejor_sesion_xp"] = max(mat["mejor_sesion_xp"], score["xp"])
    mat["max_racha"] = max(mat["max_racha"], score["max_streak"])

    if topic_stats_sesion:
        for clave, ts in topic_stats_sesion.items():
            if clave not in p["temas_stats"]:
                p["temas_stats"][clave] = {
                    "materia": ts["materia"], "topic": ts["topic"],
                    "intentos": 0, "correctas": 0}
            p["temas_stats"][clave]["intentos"] += ts["intentos"]
            p["temas_stats"][clave]["correctas"] += ts["correctas"]

    if preguntas_fallidas:
        p["preguntas_debiles"].extend(preguntas_fallidas)
        p["preguntas_debiles"] = p["preguntas_debiles"][-50:]

    p["historial"].append({
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "materia": materia,
        "modo": modo,
        "dificultad": dificultad,
        "xp": score["xp"],
        "correctas": correctas,
        "total": total,
        "pct": pct,
        "racha": score["max_streak"],
        "mult": score["max_multiplier"],
    })
    p["historial"] = p["historial"][-20:]

    for logro in LOGROS:
        if logro["id"] not in p["logros"] and logro["cond"](p):
            p["logros"].append(logro["id"])
            nuevos_logros.append(logro)

    data[nombre] = p
    _save(data)
    return nuevos_logros


def _build_entry(nombre: str, stats: dict, modo: str = "global") -> dict:
    if modo == "infinito":
        s = stats.get("infinito", {})
        tr = s.get("total_respuestas", 0)
        tc = s.get("total_correctas", 0)
        xp = s.get("xp_total", 0)
    elif modo == "examen":
        s = stats.get("examen", {})
        tr = s.get("total_respuestas", 0)
        tc = s.get("total_correctas", 0)
        xp = s.get("xp_total", 0)
    else:
        tr = stats.get("total_respuestas", 0)
        tc = stats.get("total_correctas", 0)
        xp = stats.get("xp_total", 0)
        s = stats

    pct = int(100 * tc / tr) if tr > 0 else 0
    score = calcular_score(xp, tr, pct)

    return {
        "nombre": nombre,
        "xp_total": xp,
        "score": score,
        "sesiones": s.get("sesiones", stats.get("sesiones", 0)),
        "total_respuestas": tr,
        "total_correctas": tc,
        "pct": pct,
        "max_racha": s.get("max_racha", stats.get("max_racha", 0)),
        "max_multiplicador": stats.get("max_multiplicador", 1),
        "mejor_sesion_xp": s.get("mejor_sesion_xp", stats.get("mejor_sesion_xp", 0)),
        "logros": stats.get("logros", []),
        "mejor_pct_examen": stats.get("mejor_pct_examen", 0),
    }


def get_ranking(modo: str = "global") -> list:
    data = _load()
    ranking = [_build_entry(n, _migrate(s), modo) for n, s in data.items()
               if _migrate(s).get("total_respuestas", 0) > 0]
    return sorted(ranking, key=lambda x: x["score"], reverse=True)


def get_ranking_materia(materia: str) -> list:
    data = _load()
    ranking = []
    for nombre, stats in data.items():
        m = _migrate(stats).get("por_materia", {}).get(materia)
        if not m or m.get("sesiones", 0) == 0:
            continue
        tr = m["total_respuestas"]
        tc = m["total_correctas"]
        pct = int(100 * tc / tr) if tr > 0 else 0
        ranking.append({
            "nombre": nombre,
            "xp_total": m["xp_total"],
            "score": calcular_score(m["xp_total"], tr, pct),
            "sesiones": m["sesiones"],
            "total_respuestas": tr,
            "pct": pct,
            "max_racha": m["max_racha"],
            "mejor_sesion_xp": m["mejor_sesion_xp"],
            "logros": stats.get("logros", []),
        })
    return sorted(ranking, key=lambda x: x["score"], reverse=True)


def get_ranking_dificultad(dificultad: str) -> list:
    data = _load()
    ranking = []
    for nombre, stats in data.items():
        d = _migrate(stats).get("por_dificultad", {}).get(dificultad)
        if not d or d.get("sesiones", 0) == 0:
            continue
        tr = d["total_respuestas"]
        tc = d["total_correctas"]
        pct = int(100 * tc / tr) if tr > 0 else 0
        ranking.append({
            "nombre": nombre,
            "xp_total": d["xp_total"],
            "score": calcular_score(d["xp_total"], tr, pct),
            "sesiones": d["sesiones"],
            "total_respuestas": tr,
            "pct": pct,
            "max_racha": d["max_racha"],
            "mejor_sesion_xp": d["mejor_sesion_xp"],
            "logros": stats.get("logros", []),
        })
    return sorted(ranking, key=lambda x: x["score"], reverse=True)


def get_all_players() -> dict:
    return _load()


def get_temas_stats(nombre: str) -> dict:
    return _load().get(nombre, {}).get("temas_stats", {})


def get_preguntas_debiles(nombre: str) -> list:
    return _load().get(nombre, {}).get("preguntas_debiles", [])


def add_correction_xp(nombre: str, xp_extra: int, materia: str):
    if xp_extra <= 0:
        return
    data = _load()
    if nombre not in data:
        return
    p = _migrate(data[nombre])
    p["xp_total"] += xp_extra
    p["mejor_sesion_xp"] = max(p.get("mejor_sesion_xp", 0), xp_extra)
    p["examen"]["xp_total"] += xp_extra
    if materia in p.get("por_materia", {}):
        p["por_materia"][materia]["xp_total"] += xp_extra
    data[nombre] = p
    _save(data)


# ── Examen en progreso ────────────────────────────────────────
# st.cache_resource crea un singleton compartido que sobrevive F5 y
# cambios de sesión mientras el servidor siga corriendo.
@st.cache_resource
def _get_exam_store() -> dict:
    """Almacén en memoria para exámenes en progreso. Sobrevive F5."""
    return {}


def save_exam_progress(nombre: str, materia: str, preguntas: list, respuestas: dict):
    """Guarda el examen en el store en memoria y en la hoja 'examenes'."""
    exam_dict = {
        "materia": materia,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "preguntas": preguntas,
        "respuestas": respuestas,
        "total": len(preguntas),
        "respondidas": sum(1 for v in respuestas.values() if v is not None),
    }
    # Primario: memoria compartida (inmediato, sobrevive F5)
    _get_exam_store()[nombre] = exam_dict
    # Respaldo: Google Sheets (persiste si el servidor se reinicia)
    _persist_exam(nombre, exam_dict)


def get_exam_progress(nombre: str) -> dict | None:
    """Retorna el examen en progreso si existe, None si no."""
    # 1) Memoria compartida (más rápido y confiable)
    stored = _get_exam_store().get(nombre)
    if stored:
        return stored
    # 2) Google Sheets (fallback si el servidor se reinició)
    return _load_exams().get(nombre)


def clear_exam_progress(nombre: str):
    """Borra el examen en progreso al entregar o cancelar."""
    _get_exam_store().pop(nombre, None)
    _remove_exam(nombre)
