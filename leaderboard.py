"""Sistema de tabla de puntuaciones — almacenamiento exclusivo en Google Sheets."""
import json
from datetime import datetime


# ── Google Sheets (almacenamiento principal y unico) ─────────────────────────

def _get_sheet():
    import streamlit as st
    import gspread
    from google.oauth2.service_account import Credentials
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    client = gspread.authorize(creds)
    return client.open_by_key(st.secrets["SHEET_ID"]).sheet1


def _load():
    """Carga todos los datos desde Google Sheets (celda A1 como JSON)."""
    try:
        sheet = _get_sheet()
        val = sheet.acell("A1").value
        if val:
            return json.loads(val)
    except Exception:
        pass
    return {}


def _save(data):
    """Guarda todos los datos en Google Sheets (celda A1 como JSON)."""
    try:
        sheet = _get_sheet()
        sheet.update("A1", [[json.dumps(data, ensure_ascii=False)]])
    except Exception:
        pass


DIFICULTADES_ORDEN = ["Facil", "Normal", "Dificil", "Super Dificil", "Mega Dificil"]
MATERIAS_ORDEN = ["Matematicas", "Ciencias", "Estudios Sociales", "Espanol"]

LOGROS = [
    {"id": "primera_vez",    "emoji": "🐣", "nombre": "Primera vez",   "desc": "Completar tu primera sesion",             "cond": lambda s: s["sesiones"] >= 1},
    {"id": "racha_5",        "emoji": "🔥", "nombre": "En llamas",      "desc": "Racha de 5 respuestas correctas",         "cond": lambda s: s["max_racha"] >= 5},
    {"id": "racha_10",       "emoji": "💥", "nombre": "Imparable",      "desc": "Racha de 10 respuestas correctas",        "cond": lambda s: s["max_racha"] >= 10},
    {"id": "racha_20",       "emoji": "⚡", "nombre": "Rayo",           "desc": "Racha de 20 respuestas correctas",        "cond": lambda s: s["max_racha"] >= 20},
    {"id": "xp_500",         "emoji": "⭐", "nombre": "Estrella",       "desc": "Acumular 500 XP en total",                "cond": lambda s: s["xp_total"] >= 500},
    {"id": "xp_2000",        "emoji": "🌟", "nombre": "Superestrella",  "desc": "Acumular 2000 XP en total",               "cond": lambda s: s["xp_total"] >= 2000},
    {"id": "xp_10000",       "emoji": "💎", "nombre": "Diamante",       "desc": "Acumular 10000 XP en total",              "cond": lambda s: s["xp_total"] >= 10000},
    {"id": "mult_x4",        "emoji": "🚀", "nombre": "Cohete",         "desc": "Alcanzar multiplicador x4",               "cond": lambda s: s["max_multiplicador"] >= 4},
    {"id": "100_respuestas", "emoji": "📚", "nombre": "Estudioso",      "desc": "Responder 100 preguntas en total",        "cond": lambda s: s["total_respuestas"] >= 100},
    {"id": "500_respuestas", "emoji": "🏆", "nombre": "Campeon",        "desc": "Responder 500 preguntas en total",        "cond": lambda s: s["total_respuestas"] >= 500},
    {"id": "90_pct",         "emoji": "🎯", "nombre": "Certero",        "desc": "Sesion con 90% o mas de efectividad",     "cond": lambda s: s["mejor_pct"] >= 90},
    {"id": "100_pct",        "emoji": "👑", "nombre": "Perfecto",       "desc": "Sesion con 100% de efectividad",          "cond": lambda s: s["mejor_pct"] >= 100},
]


def _dif_stats_default():
    return {"xp_total": 0, "sesiones": 0, "total_respuestas": 0,
            "total_correctas": 0, "mejor_sesion_xp": 0, "max_racha": 0}


def _materia_stats_default():
    return {"xp_total": 0, "sesiones": 0, "total_respuestas": 0,
            "total_correctas": 0, "mejor_sesion_xp": 0, "max_racha": 0}


def get_player(nombre):
    data = _load()
    if nombre not in data:
        data[nombre] = {
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
        }
        _save(data)
    return data[nombre]


def save_session(nombre, score, materia, temas, dificultad="Normal",
                 preguntas_fallidas=None, topic_stats_sesion=None):
    """Guarda una sesion terminada y actualiza stats en Google Sheets."""
    data = _load()
    if nombre not in data:
        get_player(nombre)
        data = _load()

    p = data[nombre]

    # Migrar jugadores sin campos nuevos
    for campo, default in [("por_dificultad", {}), ("por_materia", {}),
                            ("temas_stats", {}), ("preguntas_debiles", [])]:
        if campo not in p:
            p[campo] = default

    total = score["total"]
    correctas = score["correct"]
    pct = int(100 * correctas / total) if total > 0 else 0
    nuevos_logros = []

    # Stats globales
    p["xp_total"] += score["xp"]
    p["sesiones"] += 1
    p["total_respuestas"] += total
    p["total_correctas"] += correctas
    p["max_racha"] = max(p["max_racha"], score["max_streak"])
    p["max_multiplicador"] = max(p["max_multiplicador"], score["max_multiplier"])
    p["mejor_pct"] = max(p["mejor_pct"], pct)
    p["mejor_sesion_xp"] = max(p["mejor_sesion_xp"], score["xp"])

    # Stats por dificultad
    if dificultad not in p["por_dificultad"]:
        p["por_dificultad"][dificultad] = _dif_stats_default()
    d = p["por_dificultad"][dificultad]
    d["xp_total"] += score["xp"]
    d["sesiones"] += 1
    d["total_respuestas"] += total
    d["total_correctas"] += correctas
    d["mejor_sesion_xp"] = max(d["mejor_sesion_xp"], score["xp"])
    d["max_racha"] = max(d["max_racha"], score["max_streak"])

    # Stats por materia
    if materia not in p["por_materia"]:
        p["por_materia"][materia] = _materia_stats_default()
    m = p["por_materia"][materia]
    m["xp_total"] += score["xp"]
    m["sesiones"] += 1
    m["total_respuestas"] += total
    m["total_correctas"] += correctas
    m["mejor_sesion_xp"] = max(m["mejor_sesion_xp"], score["xp"])
    m["max_racha"] = max(m["max_racha"], score["max_streak"])

    # Precision por tema
    if topic_stats_sesion:
        for clave, ts in topic_stats_sesion.items():
            if clave not in p["temas_stats"]:
                p["temas_stats"][clave] = {
                    "materia": ts["materia"], "topic": ts["topic"],
                    "intentos": 0, "correctas": 0,
                }
            p["temas_stats"][clave]["intentos"] += ts["intentos"]
            p["temas_stats"][clave]["correctas"] += ts["correctas"]

    # Preguntas fallidas (ultimas 50)
    if preguntas_fallidas:
        p["preguntas_debiles"].extend(preguntas_fallidas)
        p["preguntas_debiles"] = p["preguntas_debiles"][-50:]

    # Historial (ultimas 20 sesiones)
    p["historial"].append({
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "materia": materia,
        "temas": temas,
        "dificultad": dificultad,
        "xp": score["xp"],
        "correctas": correctas,
        "total": total,
        "pct": pct,
        "racha": score["max_streak"],
        "mult": score["max_multiplier"],
    })
    p["historial"] = p["historial"][-20:]

    # Logros
    for logro in LOGROS:
        if logro["id"] not in p["logros"] and logro["cond"](p):
            p["logros"].append(logro["id"])
            nuevos_logros.append(logro)

    data[nombre] = p
    _save(data)
    return nuevos_logros


def get_all_players():
    return _load()


def get_ranking():
    """Ranking global por XP total."""
    data = _load()
    ranking = []
    for nombre, stats in data.items():
        pct = int(100 * stats["total_correctas"] / stats["total_respuestas"]) if stats["total_respuestas"] > 0 else 0
        ranking.append({
            "nombre": nombre,
            "xp_total": stats["xp_total"],
            "sesiones": stats["sesiones"],
            "total_respuestas": stats["total_respuestas"],
            "total_correctas": stats["total_correctas"],
            "pct": pct,
            "max_racha": stats["max_racha"],
            "max_multiplicador": stats["max_multiplicador"],
            "mejor_sesion_xp": stats["mejor_sesion_xp"],
            "logros": stats["logros"],
        })
    return sorted(ranking, key=lambda x: x["xp_total"], reverse=True)


def get_ranking_materia(materia):
    """Ranking por XP en una materia especifica."""
    data = _load()
    ranking = []
    for nombre, stats in data.items():
        m = stats.get("por_materia", {}).get(materia)
        if not m or m["sesiones"] == 0:
            continue
        pct = int(100 * m["total_correctas"] / m["total_respuestas"]) if m["total_respuestas"] > 0 else 0
        ranking.append({
            "nombre": nombre,
            "xp_total": m["xp_total"],
            "sesiones": m["sesiones"],
            "total_respuestas": m["total_respuestas"],
            "pct": pct,
            "max_racha": m["max_racha"],
            "mejor_sesion_xp": m["mejor_sesion_xp"],
            "logros": stats["logros"],
        })
    return sorted(ranking, key=lambda x: x["xp_total"], reverse=True)


def get_temas_stats(nombre):
    """Precision por tema de un estudiante."""
    data = _load()
    return data.get(nombre, {}).get("temas_stats", {})


def get_preguntas_debiles(nombre):
    """Preguntas fallidas recientes de un estudiante."""
    data = _load()
    return data.get(nombre, {}).get("preguntas_debiles", [])


def get_ranking_dificultad(dificultad):
    """Ranking por XP en una dificultad especifica."""
    data = _load()
    ranking = []
    for nombre, stats in data.items():
        d = stats.get("por_dificultad", {}).get(dificultad)
        if not d or d["sesiones"] == 0:
            continue
        pct = int(100 * d["total_correctas"] / d["total_respuestas"]) if d["total_respuestas"] > 0 else 0
        ranking.append({
            "nombre": nombre,
            "xp_total": d["xp_total"],
            "sesiones": d["sesiones"],
            "total_respuestas": d["total_respuestas"],
            "pct": pct,
            "max_racha": d["max_racha"],
            "mejor_sesion_xp": d["mejor_sesion_xp"],
            "logros": stats["logros"],
        })
    return sorted(ranking, key=lambda x: x["xp_total"], reverse=True)
