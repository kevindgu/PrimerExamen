"""Datos de Español para Tyler — Tipos de textos, comprensión, analogías y puntuación."""
import random

# ============================================================
# GENERADORES DINÁMICOS
# ============================================================

_ANALOGIAS = [
    ("Chocolate", "cacao", "azúcar", "caña"),
    ("Cama", "habitación", "nevera", "cocina"),
    ("Audífono", "escuchar", "micrófono", "hablar"),
    ("Establo", "vaca", "pecera", "pez"),
    ("Patines", "patinador", "bicicleta", "ciclista"),
    ("Ala", "águila", "pata", "león"),
    ("Trigo", "pan", "leche", "vaca"),
    ("Guante", "mano", "gorro", "cabeza"),
    ("Árbitro", "silbato", "fotógrafo", "cámara"),
    ("Enfermera", "enfermería", "docente", "escuela"),
    ("Pincel", "pintor", "bisturí", "cirujano"),
    ("Libro", "biblioteca", "cuadro", "museo"),
    ("Pez", "agua", "pájaro", "aire"),
    ("Zapato", "pie", "guante", "mano"),
    ("Maestro", "escuela", "médico", "hospital"),
    ("Perro", "ladrar", "gato", "maullar"),
    ("Sol", "día", "luna", "noche"),
    ("Calor", "verano", "frío", "invierno"),
    ("Hambre", "comer", "sed", "beber"),
    ("Cuchillo", "cortar", "aguja", "coser"),
]

_PUNTUACION_EJERCICIOS = [
    ("María fue al mercado___ Compró frutas y verduras.", ".", "punto y seguido",
     "Se usa **punto y seguido** para separar oraciones del mismo párrafo."),
    ("Compré lápices___ cuadernos___ borradores y colores.", ",", "coma",
     "Se usa **coma** para separar elementos en una lista."),
    ("___Dónde está mi cuaderno___", "¿?", "signos de interrogación",
     "Se usan **signos de interrogación** para preguntas: ¿Dónde está mi cuaderno?"),
    ("___Qué sorpresa tan grande___", "¡!", "signos de admiración",
     "Se usan **signos de admiración** para emociones fuertes: ¡Qué sorpresa!"),
    ("Creo que olvidé algo importante___", "...", "puntos suspensivos",
     "Se usan **puntos suspensivos** para indicar suspenso o idea incompleta."),
    ("La maestra dijo: ___Estudien para el examen___.", '""', "comillas",
     "Se usan **comillas** para citar lo que alguien dice."),
    ("Fuimos al parque por la mañana___ regresamos antes de la lluvia.", ";", "punto y coma",
     "Se usa **punto y coma** para separar ideas relacionadas."),
]

_COMPLETAR_ORACIONES = [
    ("El ___ es el momento de mayor tensión en un texto narrativo.", "nudo",
     "El **nudo** es el momento de mayor tensión."),
    ("El texto ___ comunica datos y hechos concretos.", "informativo",
     "El texto **informativo** comunica datos y hechos."),
    ("El texto ___ cuenta historias sobre personajes.", "narrativo",
     "El texto **narrativo** cuenta historias."),
    ("Una ___ es un mensaje para participar en una actividad.", "invitación",
     "Una **invitación** es para participar en una actividad."),
    ("Un ___ es un mensaje breve que se deja a alguien que no está presente.", "recado",
     "Un **recado** es un mensaje breve."),
    ("Las ___ son ideas que sacamos del texto usando pistas.", "inferencias",
     "Las **inferencias** se deducen usando pistas del texto."),
    ("La ___ indica que las ideas estén bien conectadas.", "coherencia",
     "La **coherencia** conecta bien las ideas."),
    ("El ___ presenta los personajes, el lugar y el tiempo.", "inicio",
     "El **inicio** presenta personajes, lugar y tiempo."),
    ("El ___ resuelve los conflictos de la historia.", "desenlace",
     "El **desenlace** resuelve los conflictos."),
]

def _gen_analogia():
    a, b, c, d = random.choice(_ANALOGIAS)
    tipo = random.choice(['completar_d', 'identificar_relacion'])
    if tipo == 'completar_d':
        distractores = random.sample([x[3] for x in _ANALOGIAS if x[3] != d], 3)
        opciones = [d] + distractores
        random.shuffle(opciones)
        return {
            "q": f"{a} es a {b} como {c} es a ___",
            "answer": d,
            "opciones": opciones,
            "procedure": f"{a} → {b} (misma relación) → {c} → **{d}**",
            "tema": "Analogías"
        }
    # identificar relacion
    relaciones = [
        ("herramienta y quien la usa", [("Pincel","pintor"),("Bisturí","cirujano")]),
        ("animal y su hábitat", [("Pez","agua"),("Pájaro","aire")]),
        ("objeto y parte del cuerpo", [("Zapato","pie"),("Guante","mano")]),
    ]
    rel_nombre, ejemplos = random.choice(relaciones)
    ej = random.choice(ejemplos)
    distractores = ["opuesto", "sinónimo", "color y objeto"]
    opciones = [rel_nombre] + distractores
    random.shuffle(opciones)
    return {
        "q": f"¿Qué relación hay entre {ej[0]} y {ej[1]}?",
        "answer": rel_nombre,
        "opciones": opciones,
        "procedure": f"{ej[0]} y {ej[1]} tienen relación de **{rel_nombre}**",
        "tema": "Analogías"
    }


def _gen_puntuacion():
    ej = random.choice(_PUNTUACION_EJERCICIOS)
    oracion, signo, nombre, proc = ej
    distractores = [s[1] for s in _PUNTUACION_EJERCICIOS if s[1] != signo][:3]
    opciones = [signo] + distractores
    random.shuffle(opciones)
    return {
        "q": f"¿Qué signo de puntuación falta?\n\n{oracion}",
        "answer": signo,
        "opciones": opciones,
        "procedure": proc,
        "tema": "Signos de puntuación"
    }


def _gen_completar():
    elegida = random.choice(_COMPLETAR_ORACIONES)
    q_txt, answer, proc = elegida
    distractores = [a for _, a, _ in _COMPLETAR_ORACIONES if a != answer]
    random.shuffle(distractores)
    opciones = [answer] + distractores[:3]
    random.shuffle(opciones)
    return {
        "q": f"Completa la oración:\n\n{q_txt}",
        "answer": answer,
        "opciones": opciones,
        "procedure": proc,
        "tema": "Tipos de textos"
    }


def generate_dynamic(topic):
    if topic == "Analogías":
        return _gen_analogia()
    if topic == "Signos de puntuación":
        if random.random() < 0.5:
            return _gen_puntuacion()
    if topic == "Tipos de textos":
        if random.random() < 0.4:
            return _gen_completar()
    return None

DATA = {
    "topics": {
        "Tipos de textos": {
            "aprendizaje": "Identificar y diferenciar textos narrativos e informativos",
            "indicador": "Reconoce características de textos narrativos e informativos",
        },
        "Producción textual": {
            "aprendizaje": "Producir textos escritos con coherencia y estructura correcta",
            "indicador": "Aplica coherencia, ortografía y estructura en textos escritos",
        },
        "Comprensión e inferencias": {
            "aprendizaje": "Identificar información explícita e implícita en textos",
            "indicador": "Realiza inferencias a partir de pistas del texto",
        },
        "Analogías": {
            "aprendizaje": "Establecer relaciones entre palabras usando analogías",
            "indicador": "Completa analogías identificando la relación entre pares de palabras",
        },
        "Signos de puntuación": {
            "aprendizaje": "Usar correctamente los signos de puntuación",
            "indicador": "Identifica y usa punto, coma, signos de interrogación y admiración",
        },
    },

    "partes": [],

    "preguntas": [
        # ── TIPOS DE TEXTOS ──
        {"tema": "Tipos de textos", "q": "¿Qué tipo de texto cuenta historias reales o imaginarias sobre personajes?", "answer": "Narrativo", "opciones": ["Narrativo", "Informativo", "Descriptivo", "Argumentativo"], "procedure": "El texto **narrativo** cuenta historias sobre personajes."},
        {"tema": "Tipos de textos", "q": "¿Cuál es el propósito principal de un texto informativo?", "answer": "Comunicar datos, situaciones o hechos concretos", "opciones": ["Comunicar datos, situaciones o hechos concretos", "Contar una historia de ficción", "Expresar emociones del autor", "Entretener al lector"], "procedure": "El texto informativo busca **comunicar datos y hechos concretos**."},
        {"tema": "Tipos de textos", "q": "¿Cómo se llama la parte del texto narrativo donde se presentan los personajes y el lugar?", "answer": "Inicio", "opciones": ["Inicio", "Nudo", "Desenlace", "Clímax"], "procedure": "El **inicio** presenta personajes, lugar y tiempo."},
        {"tema": "Tipos de textos", "q": "¿Cómo se llama la parte del texto narrativo con mayor tensión y acciones importantes?", "answer": "Nudo", "opciones": ["Inicio", "Nudo", "Desenlace", "Introducción"], "procedure": "El **nudo** es el momento de mayor tensión."},
        {"tema": "Tipos de textos", "q": "¿Cómo se llama la parte donde se resuelven los conflictos del texto narrativo?", "answer": "Desenlace", "opciones": ["Inicio", "Nudo", "Desenlace", "Desarrollo"], "procedure": "El **desenlace** resuelve los conflictos."},
        {"tema": "Tipos de textos", "q": "¿Qué tipo de texto informativo es un mensaje breve que se deja a alguien que no está presente?", "answer": "Recado", "opciones": ["Recado", "Carta", "Noticia", "Invitación"], "procedure": "Un **recado** es un mensaje breve para alguien que no está presente."},
        {"tema": "Tipos de textos", "q": "¿Qué tipo de texto informativo es una información de actualidad que aparece en medios de comunicación?", "answer": "Noticia", "opciones": ["Noticia", "Carta", "Recado", "Invitación"], "procedure": "Una **noticia** es información de actualidad en medios de comunicación."},
        {"tema": "Tipos de textos", "q": "¿Qué tipo de texto informativo se envía en un sobre cerrado?", "answer": "Carta", "opciones": ["Carta", "Recado", "Noticia", "Invitación"], "procedure": "Una **carta** se envía en un sobre cerrado."},
        {"tema": "Tipos de textos", "q": "¿Qué tipo de texto informativo sirve para participar en una actividad como una fiesta?", "answer": "Invitación", "opciones": ["Invitación", "Carta", "Recado", "Noticia"], "procedure": "Una **invitación** es para participar en una actividad."},
        {"tema": "Tipos de textos", "q": "¿Cómo se llama el orden en que se organizan los hechos en un texto narrativo?", "answer": "Secuencia narrativa", "opciones": ["Secuencia narrativa", "Estructura informativa", "Orden alfabético", "Cronología"], "procedure": "Se llama **secuencia narrativa**."},

        # ── PRODUCCIÓN TEXTUAL ──
        {"tema": "Producción textual", "q": "¿Qué significa que un texto tenga coherencia?", "answer": "Que las ideas estén bien conectadas y tengan sentido", "opciones": ["Que las ideas estén bien conectadas y tengan sentido", "Que tenga muchas palabras difíciles", "Que sea muy largo", "Que tenga imágenes"], "procedure": "**Coherencia** = ideas bien conectadas con sentido."},
        {"tema": "Producción textual", "q": "¿Cuál es el primer paso para construir un texto informativo?", "answer": "Establecer con claridad la información que se va a comunicar", "opciones": ["Establecer con claridad la información que se va a comunicar", "Redactar la versión definitiva", "Hacer correcciones", "Identificar el medio"], "procedure": "El primer paso es **establecer la información** que se comunicará."},
        {"tema": "Producción textual", "q": "¿Qué debe incluir una invitación?", "answer": "Tipo de actividad, fecha, hora y lugar", "opciones": ["Tipo de actividad, fecha, hora y lugar", "Solo el nombre del invitado", "Solo la fecha", "Un cuento largo"], "procedure": "Una invitación debe incluir: **actividad, fecha, hora y lugar**."},
        {"tema": "Producción textual", "q": "¿Qué es la caligrafía en un texto?", "answer": "Letra clara y legible", "opciones": ["Letra clara y legible", "Usar muchos colores", "Escribir rápido", "Usar palabras difíciles"], "procedure": "La **caligrafía** es tener letra clara y legible."},

        # ── COMPRENSIÓN E INFERENCIAS ──
        {"tema": "Comprensión e inferencias", "q": "¿Qué es una inferencia?", "answer": "Una idea que sacamos del texto usando pistas, aunque no esté dicha directamente", "opciones": ["Una idea que sacamos del texto usando pistas, aunque no esté dicha directamente", "Copiar exactamente lo que dice el texto", "Inventar información nueva", "Resumir el texto"], "procedure": "Una **inferencia** es descubrir información usando pistas del texto."},
        {"tema": "Comprensión e inferencias", "q": "Pedro salió con botas, paraguas y abrigo. El cielo estaba gris. ¿Qué podemos inferir?", "answer": "Que iba a llover o estaba lloviendo", "opciones": ["Que iba a llover o estaba lloviendo", "Que iba a la playa", "Que hacía mucho calor", "Que era de noche"], "procedure": "Paraguas + botas + cielo gris → inferimos que **iba a llover**."},
        {"tema": "Comprensión e inferencias", "q": "Ana llegó a casa con los ojos rojos y la nariz hinchada. ¿Qué podemos inferir?", "answer": "Que había estado llorando", "opciones": ["Que había estado llorando", "Que tenía sueño", "Que había corrido", "Que estaba enojada"], "procedure": "Ojos rojos + nariz hinchada → inferimos que **había estado llorando**."},
        {"tema": "Comprensión e inferencias", "q": "¿Con qué se compara hacer inferencias en el texto?", "answer": "Con ser un detective que usa pistas", "opciones": ["Con ser un detective que usa pistas", "Con copiar el texto", "Con inventar historias", "Con memorizar palabras"], "procedure": "Hacer inferencias es como ser un **detective que usa pistas**."},

        # ── SIGNOS DE PUNTUACIÓN ──
        {"tema": "Signos de puntuación", "q": "¿Qué signo se usa para separar oraciones dentro de un mismo párrafo?", "answer": "Punto y seguido", "opciones": ["Punto y seguido", "Punto y aparte", "Coma", "Punto y coma"], "procedure": "El **punto y seguido** separa oraciones dentro del mismo párrafo."},
        {"tema": "Signos de puntuación", "q": "¿Qué signo se usa para separar párrafos cuando cambia la idea?", "answer": "Punto y aparte", "opciones": ["Punto y seguido", "Punto y aparte", "Coma", "Puntos suspensivos"], "procedure": "El **punto y aparte** separa párrafos con ideas diferentes."},
        {"tema": "Signos de puntuación", "q": "¿Qué signo indica una pausa breve dentro de la oración?", "answer": "Coma", "opciones": ["Coma", "Punto", "Punto y coma", "Puntos suspensivos"], "procedure": "La **coma** indica una pausa breve."},
        {"tema": "Signos de puntuación", "q": "¿Qué signo se usa para expresar emociones fuertes como alegría o sorpresa?", "answer": "Signos de admiración", "opciones": ["Signos de admiración", "Signos de interrogación", "Puntos suspensivos", "Comillas"], "procedure": "Los **signos de admiración** (¡!) expresan emociones fuertes."},
        {"tema": "Signos de puntuación", "q": "¿Qué signo se usa para hacer preguntas?", "answer": "Signos de interrogación", "opciones": ["Signos de admiración", "Signos de interrogación", "Puntos suspensivos", "Comillas"], "procedure": "Los **signos de interrogación** (¿?) se usan para preguntas."},
        {"tema": "Signos de puntuación", "q": "¿Qué signo indica que la idea queda incompleta o hay suspenso?", "answer": "Puntos suspensivos", "opciones": ["Puntos suspensivos", "Coma", "Punto final", "Comillas"], "procedure": "Los **puntos suspensivos** (...) indican idea incompleta o suspenso."},
        {"tema": "Signos de puntuación", "q": "¿Qué signo se usa para encerrar lo que alguien dice o citar frases?", "answer": "Comillas", "opciones": ["Comillas", "Paréntesis", "Puntos suspensivos", "Coma"], "procedure": "Las **comillas** (\"\") encierran citas o palabras especiales."},
        {"tema": "Signos de puntuación", "q": "En español, ¿cuántos signos de interrogación se escriben en una pregunta?", "answer": "Dos (uno al inicio y uno al final)", "opciones": ["Dos (uno al inicio y uno al final)", "Solo uno al final", "Tres", "Ninguno"], "procedure": "En español se escriben **dos**: ¿al inicio y ? al final."},
        {"tema": "Signos de puntuación", "q": "¿Qué signo indica que el texto ha terminado completamente?", "answer": "Punto final", "opciones": ["Punto final", "Punto y seguido", "Punto y aparte", "Coma"], "procedure": "El **punto final** indica que el texto terminó."},
    ],

    "verdadero_falso": [
        {"tema": "Tipos de textos", "afirmacion": "¿El texto narrativo tiene inicio, nudo y desenlace?", "correcto": True, "explicacion": "**Verdadero**. Esa es la secuencia narrativa."},
        {"tema": "Tipos de textos", "afirmacion": "¿El texto informativo expresa principalmente las emociones del autor?", "correcto": False, "explicacion": "**Falso**. El texto informativo comunica **datos y hechos**, no emociones."},
        {"tema": "Tipos de textos", "afirmacion": "¿Una noticia es un tipo de texto informativo?", "correcto": True, "explicacion": "**Verdadero**. La noticia informa sobre hechos de actualidad."},
        {"tema": "Comprensión e inferencias", "afirmacion": "¿Una inferencia es información que el texto dice directamente?", "correcto": False, "explicacion": "**Falso**. Una inferencia es información que **deducimos** usando pistas."},
        {"tema": "Signos de puntuación", "q": "¿La coma indica una pausa breve?", "afirmacion": "¿La coma indica una pausa breve?", "correcto": True, "explicacion": "**Verdadero**."},
        {"tema": "Signos de puntuación", "afirmacion": "¿En español solo se escribe un signo de interrogación al final?", "correcto": False, "explicacion": "**Falso**. En español se escriben **dos**: ¿al inicio y ? al final."},
        {"tema": "Producción textual", "afirmacion": "¿Un texto coherente tiene ideas bien conectadas?", "correcto": True, "explicacion": "**Verdadero**. Coherencia = ideas conectadas con sentido."},
    ],

    "secuencias": [
        {"tema": "Tipos de textos", "nombre": "la secuencia narrativa",
         "orden": ["Inicio", "Nudo", "Desenlace"]},
        {"tema": "Producción textual", "nombre": "los pasos para construir un texto informativo",
         "orden": ["Establecer la información", "Identificar el medio", "Redactar un borrador", "Revisar el mensaje", "Redactar la versión definitiva"]},
    ],

    "dynamic_generator": generate_dynamic,
}
