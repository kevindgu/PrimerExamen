"""Sistema de tabla de puntuaciones y logros."""
import json
import os
from datetime import datetime

SCORES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scores.json")

# ── Google Sheets (si hay credenciales configuradas) ──────────────────────────
def _sheets_disponible():
    try:
        import streamlit as st
        return "gcp_service_account" in st.secrets and "SHEET_ID" in st.secrets
    except Exception:
        return False

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

LOGROS = [
    {"id": "primera_vez",    "emoji": "🐣", "nombre": "Primera vez",       "desc": "Completar tu primera sesión",              "cond": lambda s: s["sesiones"] >= 1},
    {"id": "racha_5",        "emoji": "🔥", "nombre": "En llamas",          "desc": "Racha de 5 respuestas correctas",          "cond": lambda s: s["max_racha"] >= 5},
    {"id": "racha_10",       "emoji": "💥", "nombre": "Imparable",          "desc": "Racha de 10 respuestas correctas",         "cond": lambda s: s["max_racha"] >= 10},
    {"id": "racha_20",       "emoji": "⚡", "nombre": "Rayo",               "desc": "Racha de 20 respuestas correctas",         "cond": lambda s: s["max_racha"] >= 20},
    {"id": "xp_500",         "emoji": "⭐", "nombre": "Estrella",           "desc": "Acumular 500 XP en total",                 "cond": lambda s: s["xp_total"] >= 500},
    {"id": "xp_2000",        "emoji": "🌟", "nombre": "Superestrella",      "desc": "Acumular 2000 XP en total",                "cond": lambda s: s["xp_total"] >= 2000},
    {"id": "xp_10000",       "emoji": "💎", "nombre": "Diamante",           "desc": "Acumular 10000 XP en total",               "cond": lambda s: s["xp_total"] >= 10000},
    {"id": "mult_x4",        "emoji": "🚀", "nombre": "Cohete",             "desc": "Alcanzar multiplicador x4",                "cond": lambda s: s["max_multiplicador"] >= 4},
    {"id": "100_respuestas", "emoji": "📚", "nombre": "Estudioso",          "desc": "Responder 100 preguntas en total",         "cond": lambda s: s["total_respuestas"] >= 100},
    {"id": "500_respuestas", "emoji": "🏆", "nombre": "Campeón",            "desc": "Responder 500 preguntas en total",         "cond": lambda s: s["total_respuestas"] >= 500},
    {"id": "90_pct",         "emoji": "🎯", "nombre": "Certero",            "desc": "Sesión con 90% o más de efectividad",      "cond": lambda s: s["mejor_pct"] >= 90},
    {"id": "100_pct",        "emoji": "👑", "nombre": "Perfecto",           "desc": "Sesión con 100% de efectividad",           "cond": lambda s: s["mejor_pct"] >= 100},
]


def _load_from_sheets():
    try:
        sheet = _get_sheet()
        val = sheet.acell("A1").value
        if val:
            return json.loads(val)
    except Exception:
        pass
    return {}


def _save_to_sheets(data):
    try:
        sheet = _get_sheet()
        sheet.update("A1", [[json.dumps(data, ensure_ascii=False)]])
    except Exception:
        pass


def _load():
    if _sheets_disponible():
        return _load_from_sheets()
    if not os.path.exists(SCORES_FILE):
        return {}
    try:
        with open(SCORES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save(data):
    if _sheets_disponible():
        _save_to_sheets(data)
        return
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


DIFICULTADES_ORDEN = ["Fácil", "Normal", "Difícil", "💀 Super Difícil", "☠️ Mega Difícil"]


def _dif_stats_default():
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
        }
        _save(data)
    return data[nombre]


def save_session(nombre, score, materia, temas, dificultad="Normal"):
    """Guarda una sesión terminada y actualiza stats globales y por dificultad."""
    data = _load()
    if nombre not in data:
        get_player(nombre)
        data = _load()

    p = data[nombre]
    # Migrar jugadores sin por_dificultad
    if "por_dificultad" not in p:
        p["por_dificultad"] = {}

    total = score["total"]
    correctas = score["correct"]
    pct = int(100 * correctas / total) if total > 0 else 0
    nuevos_logros = []

    # Actualizar stats globales
    p["xp_total"] += score["xp"]
    p["sesiones"] += 1
    p["total_respuestas"] += total
    p["total_correctas"] += correctas
    p["max_racha"] = max(p["max_racha"], score["max_streak"])
    p["max_multiplicador"] = max(p["max_multiplicador"], score["max_multiplier"])
    p["mejor_pct"] = max(p["mejor_pct"], pct)
    p["mejor_sesion_xp"] = max(p["mejor_sesion_xp"], score["xp"])

    # Actualizar stats por dificultad
    if dificultad not in p["por_dificultad"]:
        p["por_dificultad"][dificultad] = _dif_stats_default()
    d = p["por_dificultad"][dificultad]
    d["xp_total"] += score["xp"]
    d["sesiones"] += 1
    d["total_respuestas"] += total
    d["total_correctas"] += correctas
    d["mejor_sesion_xp"] = max(d["mejor_sesion_xp"], score["xp"])
    d["max_racha"] = max(d["max_racha"], score["max_streak"])

    # Historial (últimas 20 sesiones)
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

    # Verificar logros nuevos
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
    """Retorna lista ordenada por XP total (todas las dificultades)."""
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


def get_ranking_dificultad(dificultad):
    """Retorna lista ordenada por XP en una dificultad específica."""
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
