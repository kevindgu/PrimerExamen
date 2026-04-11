"""Datos de Español para Jaikel — Fuentes de información, comprensión lectora y vocabulario."""
import random

# ============================================================
# GENERADOR DINÁMICO DE SÍLABAS — preguntas para escribir
# ============================================================

_SILABAS = {
    "PL": ["pluma", "plato", "plano", "playa", "pliego", "placa", "plaza", "planta"],
    "CL": ["claro", "cloro", "clima", "clavel", "cliente", "club", "clon", "clase"],
    "FL": ["flores", "flan", "flaco", "flotar", "flujo", "fleco", "flete", "florero"],
    "TL": ["atlas", "atleta", "Atl\u00e1ntico", "decatl\u00f3n"],
    "GL": ["igl\u00fa", "glot\u00f3n", "iglesia", "regla", "gladiador", "glaciar"],
    "PR": ["prueba", "pr\u00e1ctica", "princesa", "prado", "precio", "premio", "profesor", "compra"],
    "CR": ["crayones", "cruz", "cristal", "cr\u00e1neo", "cr\u00e1ter", "crucero", "croquis"],
    "FR": ["fr\u00edo", "frase", "frijoles", "fruta", "frente", "Francia", "frontal"],
    "TR": ["tren", "triste", "trucha", "trampa", "trigo", "trabajo", "tractor", "tractor"],
    "GR": ["grande", "gr\u00faa", "gris", "gritar", "negro", "grifo", "cangrejo"],
}

def _gen_vocabulario_escribir():
    tipo = random.choice(["completar_silaba", "completar_palabra", "escribir_ejemplo"])

    silaba = random.choice(list(_SILABAS.keys()))
    palabras = _SILABAS[silaba]
    palabra = random.choice(palabras)

    if tipo == "completar_silaba":
        # Mostrar la palabra con la sílaba oculta, escribir la sílaba
        resto = palabra[len(silaba.lower()):] if palabra.lower().startswith(silaba.lower()) else palabra
        # Buscar dónde está la sílaba en la palabra
        idx = palabra.lower().find(silaba.lower())
        if idx >= 0:
            oculta = "___" + palabra[idx + len(silaba):]
            prefix = palabra[:idx] if idx > 0 else ""
            mostrar = prefix + oculta
        else:
            mostrar = "___" + palabra[2:]
        return {
            "q": f"Completa la sílaba que falta:\n\n**{mostrar}**\n\n(Escribe solo la sílaba, ej: PL)",
            "answer": silaba,
            "procedure": f"La sílaba es **{silaba}** → {silaba.lower()}{palabra[len(silaba):]}",
            "tema": "Vocabulario"
        }

    if tipo == "completar_palabra":
        # Dar la sílaba y el resto, escribir la palabra completa
        resto = palabra[len(silaba):] if palabra.lower().startswith(silaba.lower()) else palabra[2:]
        return {
            "q": f"Completa la palabra usando la sílaba **{silaba}**:\n\n{silaba}**{resto}**\n\n(Escribe la palabra completa)",
            "answer": palabra,
            "procedure": f"**{silaba}** + {resto} = **{palabra}**",
            "tema": "Vocabulario"
        }

    # escribir_ejemplo
    return {
        "q": f"Escribe una palabra que contenga la sílaba **{silaba}**\n\n(Ejemplos válidos: {', '.join(palabras[:3])}...)",
        "answer": palabras[0],
        "procedure": f"Palabras con **{silaba}**: {', '.join(palabras)}",
        "tema": "Vocabulario"
    }

def generate_dynamic(topic):
    return None

DATA = {
    "topics": {
        "Fuentes de información": {
            "aprendizaje": "Identificar diferentes fuentes de información y su uso",
            "indicador": "Identifica libros, revistas, internet, atlas, guía telefónica y su uso",
        },
        "Uso de textos informativos": {
            "aprendizaje": "Seleccionar la fuente adecuada según la situación",
            "indicador": "Relaciona necesidades de información con el tipo de texto correcto",
        },
        "Relación de conceptos": {
            "aprendizaje": "Asociar fuentes de información con sus características",
            "indicador": "Establece correspondencias correctamente entre fuentes y descripciones",
        },
        "Comprensión lectora": {
            "aprendizaje": "Identificar información explícita en un texto",
            "indicador": "Responde preguntas sobre personajes, acciones y detalles del texto",
        },
        "Valores y reflexión": {
            "aprendizaje": "Extraer enseñanzas de un texto narrativo",
            "indicador": "Extrae enseñanzas y valores de textos narrativos",
        },
        "Vocabulario": {
            "aprendizaje": "Completar oraciones con palabras adecuadas según el contexto",
            "indicador": "Comprende el significado de palabras de uso cotidiano",
        },
    },

    "partes": [],

    "preguntas": [
        # ── FUENTES DE INFORMACIÓN ──
        {"tema": "Fuentes de información", "q": "¿Qué fuente usarías para buscar información rápidamente sobre cualquier tema?", "answer": "Internet", "opciones": ["Internet", "Atlas", "Guía telefónica", "Testimonio"], "procedure": "**Internet** permite buscar casi cualquier tipo de información rápidamente."},
        {"tema": "Fuentes de información", "q": "¿Qué fuente contiene mapas de países, ciudades y ríos?", "answer": "Atlas", "opciones": ["Atlas", "Enciclopedia", "Revista", "Internet"], "procedure": "El **atlas** es un libro lleno de mapas."},
        {"tema": "Fuentes de información", "q": "¿Qué fuente usarías para encontrar el número de teléfono de un negocio?", "answer": "Guía telefónica", "opciones": ["Guía telefónica", "Atlas", "Enciclopedia", "Revista"], "procedure": "La **guía telefónica** contiene números de teléfono de personas y negocios."},
        {"tema": "Fuentes de información", "q": "¿Qué fuente tiene información organizada por temas con explicaciones claras?", "answer": "Enciclopedia", "opciones": ["Enciclopedia", "Revista", "Testimonio", "Atlas"], "procedure": "La **enciclopedia** organiza información por temas con explicaciones claras."},
        {"tema": "Fuentes de información", "q": "¿Qué fuente son relatos de personas que cuentan lo que vivieron?", "answer": "Testimonios", "opciones": ["Testimonios", "Revistas", "Atlas", "Enciclopedia"], "procedure": "Los **testimonios** son relatos de experiencias reales y personales."},
        {"tema": "Fuentes de información", "q": "¿Qué tipo de revista sería 'Golazo! Los Mejores Momentos del Deporte'?", "answer": "Deportes", "opciones": ["Deportes", "Tecnología", "Moda", "Ciencia"], "procedure": "Es una revista de **deportes**."},
        {"tema": "Fuentes de información", "q": "¿Qué tipo de revista sería 'Futuro Digital: Las Innovaciones del Mañana'?", "answer": "Tecnología", "opciones": ["Deportes", "Tecnología", "Moda", "Entretenimiento"], "procedure": "Es una revista de **tecnología**."},
        {"tema": "Fuentes de información", "q": "¿Qué fuente usarías para saber dónde está el río Amazonas?", "answer": "Atlas", "opciones": ["Atlas", "Guía telefónica", "Testimonio", "Revista"], "procedure": "El **atlas** tiene mapas que muestran ríos, países y ciudades."},

        # ── USO DE TEXTOS INFORMATIVOS ──
        {"tema": "Uso de textos informativos", "q": "Quieres saber qué come un animal desconocido. ¿Qué fuente usas?", "answer": "Internet", "opciones": ["Internet", "Guía telefónica", "Testimonio", "Atlas"], "procedure": "**Internet** permite buscar información sobre animales rápidamente."},
        {"tema": "Uso de textos informativos", "q": "Necesitas el número de un taller de bicicletas. ¿Qué fuente usas?", "answer": "Guía telefónica", "opciones": ["Guía telefónica", "Atlas", "Enciclopedia", "Revista"], "procedure": "La **guía telefónica** tiene números de negocios."},
        {"tema": "Uso de textos informativos", "q": "Quieres saber los resultados de un torneo de fútbol local. ¿Qué fuente usas?", "answer": "Diario (periódico)", "opciones": ["Diario (periódico)", "Atlas", "Enciclopedia", "Testimonio"], "procedure": "El **diario o periódico** publica noticias y resultados deportivos locales."},
        {"tema": "Uso de textos informativos", "q": "Escribes una historia sobre cómo los abuelos llegaron a la ciudad. ¿Qué fuente usas?", "answer": "Testimonio", "opciones": ["Testimonio", "Atlas", "Guía telefónica", "Revista de moda"], "procedure": "Un **testimonio** aporta detalles reales y personales de experiencias vividas."},
        {"tema": "Uso de textos informativos", "q": "Quieres investigar cómo funciona un volcán. ¿Qué fuente usas?", "answer": "Internet", "opciones": ["Internet", "Guía telefónica", "Testimonio", "Revista de moda"], "procedure": "**Internet** tiene información científica sobre volcanes."},
        {"tema": "Uso de textos informativos", "q": "Quieres contactar a un doctor cercano. ¿Qué fuente usas?", "answer": "Internet", "opciones": ["Internet", "Atlas", "Enciclopedia", "Testimonio"], "procedure": "**Internet** permite buscar médicos y sus contactos."},

        # ── RELACIÓN DE CONCEPTOS ──
        {"tema": "Relación de conceptos", "q": "«Ver la ubicación de locales en tiempo real» corresponde a:", "answer": "Internet", "opciones": ["Internet", "Diario", "Guía telefónica", "Atlas"], "procedure": "**Internet** permite ver ubicaciones en tiempo real (Google Maps, etc.)."},
        {"tema": "Relación de conceptos", "q": "«¿Cómo puedo contactar a un veterinario?» corresponde a:", "answer": "Guía telefónica", "opciones": ["Guía telefónica", "Atlas", "Enciclopedia", "Revista"], "procedure": "La **guía telefónica** tiene números de contacto de profesionales."},
        {"tema": "Relación de conceptos", "q": "«Historia de América Central» corresponde a:", "answer": "Libro", "opciones": ["Libro", "Guía telefónica", "Internet", "Testimonio"], "procedure": "Un **libro** de historia contiene información detallada sobre temas históricos."},
        {"tema": "Relación de conceptos", "q": "¿Cuál es el primer paso para investigar sobre un tema?", "answer": "Definir el tema", "opciones": ["Definir el tema", "Buscar palabras clave", "Anotar lo importante", "Crear un escrito"], "procedure": "El primer paso es **definir el tema** que se va a investigar."},
        {"tema": "Relación de conceptos", "q": "¿Cuál es el último paso al investigar un tema?", "answer": "Crear un escrito a partir de lo encontrado", "opciones": ["Definir el tema", "Buscar palabras clave", "Anotar lo importante", "Crear un escrito a partir de lo encontrado"], "procedure": "El último paso es **crear un escrito** con la información recopilada."},
        {"tema": "Relación de conceptos", "q": "¿Qué paso va después de buscar palabras clave?", "answer": "Organizar la información recopilada", "opciones": ["Definir el tema", "Organizar la información recopilada", "Crear un escrito", "Anotar lo importante"], "procedure": "Después de buscar, se **organiza la información** recopilada."},

        # ── COMPRENSIÓN LECTORA — La Liebre y la Tortuga ──
        {"tema": "Comprensión lectora", "q": "En la fábula, ¿qué hizo la liebre al inicio de la carrera?", "answer": "Se burló de la tortuga y presumió de su velocidad", "opciones": ["Se burló de la tortuga y presumió de su velocidad", "Corrió sin parar hasta el final", "Ayudó a la tortuga", "Se rindió antes de empezar"], "procedure": "La liebre **se burló de la tortuga y presumió** de su velocidad."},
        {"tema": "Comprensión lectora", "q": "¿Qué hizo la tortuga cuando la liebre se burló de ella?", "answer": "Aceptó el reto y decidió competir", "opciones": ["Aceptó el reto y decidió competir", "Se fue a casa", "También se burló", "Pidió ayuda"], "procedure": "La tortuga **aceptó el reto** y decidió competir."},
        {"tema": "Comprensión lectora", "q": "¿Por qué perdió la liebre la carrera?", "answer": "Se detuvo a descansar y se quedó dormida", "opciones": ["Se detuvo a descansar y se quedó dormida", "Se lastimó una pata", "La tortuga hizo trampa", "Llegaron al mismo tiempo"], "procedure": "La liebre **se detuvo a descansar y se quedó dormida**."},
        {"tema": "Comprensión lectora", "q": "¿Cómo caminó la tortuga durante toda la carrera?", "answer": "Despacio pero sin rendirse", "opciones": ["Despacio pero sin rendirse", "Muy rápido", "Con ayuda de otros", "Corriendo y descansando"], "procedure": "La tortuga caminó **despacio pero sin rendirse**."},
        {"tema": "Comprensión lectora", "q": "¿Cuál fue la actitud de la tortuga durante la carrera?", "answer": "Positiva", "opciones": ["Positiva", "Negativa", "Indiferente", "Agresiva"], "procedure": "La actitud de la tortuga fue **positiva**: constante y sin rendirse."},
        {"tema": "Comprensión lectora", "q": "¿Cuál fue la actitud de la liebre durante la carrera?", "answer": "Negativa", "opciones": ["Positiva", "Negativa", "Indiferente", "Ejemplar"], "procedure": "La actitud de la liebre fue **negativa**: presumida y descuidada."},

        # ── VALORES Y REFLEXIÓN ──
        {"tema": "Valores y reflexión", "q": "¿Qué enseñanza principal nos deja la fábula de la liebre y la tortuga?", "answer": "La constancia y el esfuerzo son más importantes que la velocidad", "opciones": ["La constancia y el esfuerzo son más importantes que la velocidad", "Los rápidos siempre ganan", "No hay que competir", "Dormir es importante"], "procedure": "La enseñanza es que **la constancia y el esfuerzo** valen más que el talento o la velocidad."},
        {"tema": "Valores y reflexión", "q": "¿Por qué la actitud de la tortuga fue importante para ganar?", "answer": "Nunca paró y siguió caminando sin rendirse", "opciones": ["Nunca paró y siguió caminando sin rendirse", "Corrió muy rápido al final", "La liebre le dejó ganar", "Tomó un atajo"], "procedure": "La tortuga ganó porque **nunca paró y siguió sin rendirse**."},
        {"tema": "Valores y reflexión", "q": "¿Qué valor negativo demostró la liebre?", "answer": "La soberbia y la pereza", "opciones": ["La soberbia y la pereza", "La humildad", "La constancia", "El esfuerzo"], "procedure": "La liebre demostró **soberbia** (presumir) y **pereza** (dormirse)."},
        {"tema": "Valores y reflexión", "q": "¿Qué valor positivo demostró la tortuga?", "answer": "La constancia y la perseverancia", "opciones": ["La constancia y la perseverancia", "La velocidad", "La soberbia", "La pereza"], "procedure": "La tortuga demostró **constancia y perseverancia**."},
        {"tema": "Valores y reflexión", "q": "¿Tomó buenas decisiones la liebre durante la carrera?", "answer": "No", "opciones": ["No", "Sí", "A veces", "Solo al inicio"], "procedure": "**No**, la liebre tomó malas decisiones: se paró a dormir y presumió."},

        # ── VOCABULARIO — Sílabas compuestas ──
        {"tema": "Vocabulario", "q": "¿Qué sílaba compuesta tiene la palabra 'pluma'?", "answer": "PL", "opciones": ["PL", "CL", "FL", "GL"], "procedure": "**PL**uma → sílaba PL (consonante P + L + vocal)."},
        {"tema": "Vocabulario", "q": "¿Qué sílaba compuesta tiene la palabra 'claro'?", "answer": "CL", "opciones": ["PL", "CL", "FL", "GL"], "procedure": "**CL**aro → sílaba CL."},
        {"tema": "Vocabulario", "q": "¿Qué sílaba compuesta tiene la palabra 'flores'?", "answer": "FL", "opciones": ["PL", "CL", "FL", "TL"], "procedure": "**FL**ores → sílaba FL."},
        {"tema": "Vocabulario", "q": "¿Qué sílaba compuesta tiene la palabra 'iglú'?", "answer": "GL", "opciones": ["PL", "CL", "FL", "GL"], "procedure": "i**GL**ú → sílaba GL."},
        {"tema": "Vocabulario", "q": "¿Qué sílaba compuesta tiene la palabra 'prueba'?", "answer": "PR", "opciones": ["PR", "CR", "FR", "TR"], "procedure": "**PR**ueba → sílaba PR."},
        {"tema": "Vocabulario", "q": "¿Qué sílaba compuesta tiene la palabra 'crayones'?", "answer": "CR", "opciones": ["PR", "CR", "FR", "GR"], "procedure": "**CR**ayones → sílaba CR."},
        {"tema": "Vocabulario", "q": "¿Qué sílaba compuesta tiene la palabra 'frío'?", "answer": "FR", "opciones": ["PR", "CR", "FR", "TR"], "procedure": "**FR**ío → sílaba FR."},
        {"tema": "Vocabulario", "q": "¿Qué sílaba compuesta tiene la palabra 'tren'?", "answer": "TR", "opciones": ["PR", "CR", "FR", "TR"], "procedure": "**TR**en → sílaba TR."},
        {"tema": "Vocabulario", "q": "¿Qué sílaba compuesta tiene la palabra 'grande'?", "answer": "GR", "opciones": ["PR", "CR", "FR", "GR"], "procedure": "**GR**ande → sílaba GR."},
        {"tema": "Vocabulario", "q": "¿Cuál de estas palabras tiene sílaba con L compuesta?", "answer": "plato", "opciones": ["plato", "casa", "mesa", "libro"], "procedure": "**PL**ato → tiene la sílaba compuesta PL."},
        {"tema": "Vocabulario", "q": "¿Cuál de estas palabras tiene sílaba con R compuesta?", "answer": "princesa", "opciones": ["princesa", "paloma", "flor", "globo"], "procedure": "**PR**incesa → tiene la sílaba compuesta PR."},
        {"tema": "Vocabulario", "q": "La palabra 'atlas' tiene la sílaba compuesta:", "answer": "TL", "opciones": ["TL", "TR", "PL", "CL"], "procedure": "a**TL**as → sílaba TL."},
    ],

    "verdadero_falso": [
        {"tema": "Fuentes de información", "afirmacion": "¿El atlas es un libro lleno de mapas?", "correcto": True, "explicacion": "**Verdadero**. El atlas contiene mapas de países, ciudades y ríos."},
        {"tema": "Fuentes de información", "afirmacion": "¿Todo lo que se encuentra en internet es verdadero?", "correcto": False, "explicacion": "**Falso**. No todo en internet es verdadero; hay que buscar páginas confiables."},
        {"tema": "Fuentes de información", "afirmacion": "¿Los testimonios son relatos de experiencias reales?", "correcto": True, "explicacion": "**Verdadero**. Los testimonios son relatos de personas que cuentan lo que vivieron."},
        {"tema": "Uso de textos informativos", "afirmacion": "¿La guía telefónica es la mejor fuente para investigar sobre volcanes?", "correcto": False, "explicacion": "**Falso**. Para investigar volcanes se usa **internet** o enciclopedias."},
        {"tema": "Comprensión lectora", "afirmacion": "¿La tortuga ganó la carrera porque corrió más rápido que la liebre?", "correcto": False, "explicacion": "**Falso**. La tortuga ganó porque fue **constante** y no se detuvo."},
        {"tema": "Comprensión lectora", "afirmacion": "¿La liebre se quedó dormida durante la carrera?", "correcto": True, "explicacion": "**Verdadero**. La liebre se detuvo a descansar y se quedó dormida."},
        {"tema": "Valores y reflexión", "afirmacion": "¿La fábula enseña que la velocidad es lo más importante?", "correcto": False, "explicacion": "**Falso**. Enseña que la **constancia y el esfuerzo** son más importantes."},
        {"tema": "Vocabulario", "afirmacion": "¿La palabra 'claro' tiene una sílaba compuesta con L?", "correcto": True, "explicacion": "**Verdadero**. **CL**aro → sílaba CL (consonante + L + vocal)."},
        {"tema": "Vocabulario", "afirmacion": "¿La palabra 'casa' tiene una sílaba compuesta?", "correcto": False, "explicacion": "**Falso**. 'Casa' tiene sílabas simples: ca-sa."},
    ],

    "secuencias": [
        {"tema": "Relación de conceptos", "nombre": "los pasos para investigar un tema",
         "orden": ["Definir el tema", "Buscar palabras clave", "Organizar la información recopilada", "Anotar lo más importante", "Crear un escrito a partir de lo encontrado"]},
    ],
    "dynamic_generator": generate_dynamic,
}
