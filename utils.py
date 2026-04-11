"""Configuración central: estudiantes, materias, y check_answer."""
import re
from engine import generate_question
from datos.jaikel_ciencias import DATA as JAIKEL_CIENCIAS
from datos.jaikel_sociales import DATA as JAIKEL_SOCIALES
from datos.jaikel_espanol import DATA as JAIKEL_ESPANOL
from datos.jaikel_mate import DATA as JAIKEL_MATE
from datos.tyler_mate import DATA as TYLER_MATE
from datos.tyler_sociales import DATA as TYLER_SOCIALES
from datos.tyler_ciencias import DATA as TYLER_CIENCIAS
from datos.tyler_espanol import DATA as TYLER_ESPANOL
from datos.abby_mate import DATA as ABBY_MATE
from datos.abby_ciencias import DATA as ABBY_CIENCIAS

DIFICULTADES = ["Fácil", "Normal", "Difícil", "💀 Super Difícil", "☠️ Mega Difícil"]


def _make_generator(data):
    def gen(topic, dificultad="Normal"):
        return generate_question(data, topic, dificultad)
    return gen


ESTUDIANTES = {
    "TYLER": {
        "emoji": "👦", "grado": "6to año", "color": "#3498db",
        "materias": {
            "Estudios Sociales": {
                "emoji": "🌍",
                "topics": TYLER_SOCIALES["topics"],
                "generator": _make_generator(TYLER_SOCIALES),
            },
            "Ciencias": {
                "emoji": "🔬",
                "topics": TYLER_CIENCIAS["topics"],
                "generator": _make_generator(TYLER_CIENCIAS),
            },
            "Español": {
                "emoji": "📖",
                "topics": TYLER_ESPANOL["topics"],
                "generator": _make_generator(TYLER_ESPANOL),
            },
            "Matemáticas": {
                "emoji": "🧮",
                "topics": TYLER_MATE["topics"],
                "generator": _make_generator(TYLER_MATE),
            },
        },
    },
    "JAIKEL": {
        "emoji": "👦", "grado": "4to año", "color": "#2ecc71",
        "materias": {
            "Estudios Sociales": {
                "emoji": "🌍",
                "topics": JAIKEL_SOCIALES["topics"],
                "generator": _make_generator(JAIKEL_SOCIALES),
            },
            "Matemáticas": {
                "emoji": "🧮",
                "topics": JAIKEL_MATE["topics"],
                "generator": _make_generator(JAIKEL_MATE),
            },
            "Ciencias": {
                "emoji": "🔬",
                "topics": JAIKEL_CIENCIAS["topics"],
                "generator": _make_generator(JAIKEL_CIENCIAS),
            },
            "Español": {
                "emoji": "📖",
                "topics": JAIKEL_ESPANOL["topics"],
                "generator": _make_generator(JAIKEL_ESPANOL),
            },
        },
    },
    "ABBY": {
        "emoji": "👧", "grado": "1er grado", "color": "#e74c3c",
        "materias": {
            "Ciencias": {
                "emoji": "🔬",
                "topics": ABBY_CIENCIAS["topics"],
                "generator": _make_generator(ABBY_CIENCIAS),
            },
            "Matemáticas": {
                "emoji": "🧮",
                "topics": ABBY_MATE["topics"],
                "generator": _make_generator(ABBY_MATE),
            },
        },
    },
}


def check_answer(question, user_answer):
    if user_answer is None or str(user_answer).strip() == '':
        return False
    ua = str(user_answer).strip().lower()
    ca = str(question['answer']).strip().lower()
    if question.get('is_numeric'):
        try:
            return abs(float(ua) - float(ca)) < 0.01
        except ValueError:
            return False
    for a, b in [('í','i'),('á','a'),('é','e'),('ó','o'),('ú','u'),('ñ','n')]:
        ua = ua.replace(a, b)
        ca = ca.replace(a, b)
    ua = re.sub(r'[^\w\s,]', '', ua).strip()
    ca = re.sub(r'[^\w\s,]', '', ca).strip()
    if ua == ca:
        return True
    if ca in ua or ua in ca:
        return True
    palabras_ca = [w for w in ca.split() if len(w) > 3]
    if palabras_ca:
        palabras_ua = set(ua.split())
        coinciden = sum(1 for w in palabras_ca if w in palabras_ua)
        if coinciden >= max(1, len(palabras_ca) // 2):
            return True
    return False
