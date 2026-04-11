import random

TOPICS_ABBY = {
    "Próximamente": {
        "aprendizaje": "Temas de Abby por definir",
        "indicador": "Pendiente",
    },
}

DIFICULTADES = ["Fácil", "Normal", "Difícil"]

def _q_placeholder(dif):
    return dict(
        question="🚧 Los temas de Abby están en construcción. ¡Pronto estarán listos!",
        answer="ok", is_numeric=False,
        procedure="Pendiente")

_GENERATORS_ABBY = {
    "Próximamente": _q_placeholder,
}

def generate_question_abby(topic, dificultad="Normal"):
    q = _GENERATORS_ABBY[topic](dificultad)
    q['topic'] = topic
    return q
