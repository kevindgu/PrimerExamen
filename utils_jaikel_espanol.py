import random

TOPICS_JAIKEL_ESPANOL = {
    "Fuentes de información": {
        "aprendizaje": "Identificar diferentes fuentes de información",
        "indicador": "Identifica libros, revistas, Internet, atlas, guía telefónica y su uso",
    },
    "Uso de textos informativos": {
        "aprendizaje": "Seleccionar la fuente adecuada según la situación",
        "indicador": "Relaciona necesidades de información con el tipo de texto correcto",
    },
    "Relación de conceptos": {
        "aprendizaje": "Asociar fuentes de información con sus características",
        "indicador": "Establece correspondencias correctamente",
    },
    "Comprensión lectora": {
        "aprendizaje": "Identificar información explícita en un texto",
        "indicador": "Responde preguntas sobre personajes, acciones y detalles",
    },
    "Valores y reflexión": {
        "aprendizaje": "Extraer enseñanzas de textos narrativos",
        "indicador": "Extrae enseñanzas y valores de un texto narrativo",
    },
    "Vocabulario": {
        "aprendizaje": "Completar oraciones con palabras adecuadas",
        "indicador": "Comprende el significado de palabras de uso cotidiano",
    },
}


def _q_fuentes_info(dif):
    preguntas = [
        ("¿En qué fuente de información puedes buscar el significado de una palabra?", "diccionario",
         "En el **diccionario** se buscan significados de palabras."),
        ("¿Qué fuente usarías para ver un mapa de Costa Rica?", "atlas",
         "Un **atlas** es un libro de mapas, ideal para buscar información geográfica."),
        ("¿Dónde puedes buscar el número de teléfono de un negocio?", "guia telefonica",
         "En la **guía telefónica** se buscan números de teléfono."),
        ("¿Qué fuente de información se actualiza constantemente y se accede con computadora?", "internet",
         "**Internet** se actualiza constantemente y se accede desde dispositivos electrónicos."),
        ("¿En qué fuente puedes leer noticias de lo que pasó ayer?", "periodico",
         "En el **periódico** se publican noticias recientes."),
        ("¿Las revistas son fuentes de información? (si o no)", "si",
         "**Sí**, las revistas son fuentes de información sobre temas variados."),
        ("¿Una enciclopedia tiene información sobre muchos temas o solo uno?", "muchos",
         "Una enciclopedia tiene información sobre **muchos** temas diferentes."),
        ("¿Qué fuente usarías para investigar sobre animales en peligro de extinción: atlas, diccionario o enciclopedia?", "enciclopedia",
         "La **enciclopedia** tiene información detallada sobre temas como animales."),
    ]
    q, a, p = random.choice(preguntas)
    return dict(question=q, answer=a, is_numeric=False, procedure=p)


def _q_uso_textos(dif):
    preguntas = [
        ("Si necesitas saber en qué año nació un personaje histórico, ¿qué usarías: diccionario, enciclopedia o atlas?", "enciclopedia",
         "La **enciclopedia** tiene información histórica sobre personajes."),
        ("Si quieres saber dónde queda un país, ¿qué usarías: atlas, periódico o guía telefónica?", "atlas",
         "El **atlas** tiene mapas para ubicar países y regiones."),
        ("Si no entiendes una palabra de tu tarea, ¿qué consultas?", "diccionario",
         "El **diccionario** te da el significado de las palabras."),
        ("Si quieres saber qué películas hay en el cine esta semana, ¿dónde buscas: atlas, periódico o diccionario?", "periodico",
         "El **periódico** tiene información actual como cartelera de cine."),
        ("Si necesitas el teléfono de una pizzería, ¿qué consultas?", "guia telefonica",
         "La **guía telefónica** tiene números de negocios y personas."),
        ("Para hacer una tarea sobre los volcanes de Costa Rica, ¿qué fuentes podrías usar: atlas e Internet, o guía telefónica?", "atlas e internet",
         "El **atlas** muestra ubicación y **Internet** tiene información actualizada sobre volcanes."),
        ("Si quieres leer sobre recetas de cocina, ¿qué fuente es mejor: revista, atlas o diccionario?", "revista",
         "Las **revistas** frecuentemente tienen secciones de recetas de cocina."),
    ]
    q, a, p = random.choice(preguntas)
    return dict(question=q, answer=a, is_numeric=False, procedure=p)


def _q_relacion_conceptos(dif):
    conceptos = [
        ("Libro con mapas de países y regiones", "atlas",
         "Un libro con mapas = **atlas**."),
        ("Libro que explica el significado de las palabras", "diccionario",
         "Significado de palabras = **diccionario**."),
        ("Publicación con noticias del día", "periodico",
         "Noticias del día = **periódico**."),
        ("Fuente digital con información de todo el mundo", "internet",
         "Fuente digital mundial = **Internet**."),
        ("Libro con información detallada sobre muchos temas", "enciclopedia",
         "Información de muchos temas = **enciclopedia**."),
        ("Lista de números de teléfono de personas y negocios", "guia telefonica",
         "Lista de teléfonos = **guía telefónica**."),
        ("Publicación periódica con artículos sobre temas variados", "revista",
         "Publicación periódica con artículos = **revista**."),
    ]
    q_text, a, p = random.choice(conceptos)
    return dict(question=f"¿Qué fuente de información es esta?\n«{q_text}»",
                answer=a, is_numeric=False, procedure=p)


# Mini textos para comprensión lectora
_TEXTOS = [
    {
        "texto": "María encontró un pajarito herido en el parque. Lo llevó a su casa, le dio agua y comida. Después de tres días, el pajarito ya podía volar. María lo llevó al parque y lo dejó libre. El pajarito cantó antes de irse volando.",
        "preguntas": [
            ("¿Dónde encontró María al pajarito?", "en el parque", "María encontró al pajarito **en el parque**."),
            ("¿Qué le dio María al pajarito?", "agua y comida", "María le dio **agua y comida** al pajarito."),
            ("¿Después de cuántos días pudo volar el pajarito?", 3, "Después de **3** días el pajarito pudo volar."),
            ("¿Qué hizo María cuando el pajarito se recuperó?", "lo dejo libre", "María **lo dejó libre** en el parque."),
        ],
        "ensenanza": "Debemos cuidar a los animales y ayudarlos cuando lo necesitan.",
        "valor": "bondad",
    },
    {
        "texto": "Pedro y Luis querían el mismo columpio. Pedro empujó a Luis para quitárselo. La maestra los vio y les pidió que hablaran. Pedro se disculpó y decidieron turnarse. Al final, jugaron juntos toda la tarde.",
        "preguntas": [
            ("¿Qué querían Pedro y Luis?", "el mismo columpio", "Querían **el mismo columpio**."),
            ("¿Qué hizo Pedro para quitarle el columpio a Luis?", "lo empujo", "Pedro **lo empujó** para quitárselo."),
            ("¿Quién los vio y les pidió que hablaran?", "la maestra", "**La maestra** los vio y les pidió que hablaran."),
            ("¿Cómo resolvieron el problema?", "turnarse", "Decidieron **turnarse** para usar el columpio."),
        ],
        "ensenanza": "Es mejor hablar y compartir que pelear por las cosas.",
        "valor": "respeto",
    },
    {
        "texto": "Ana tenía un examen de matemáticas. No había estudiado porque prefirió jugar videojuegos. El día del examen no supo responder. Se sintió triste y prometió que la próxima vez estudiaría primero y jugaría después.",
        "preguntas": [
            ("¿Qué examen tenía Ana?", "matematicas", "Ana tenía un examen de **matemáticas**."),
            ("¿Por qué no estudió Ana?", "prefirio jugar videojuegos", "Ana **prefirió jugar videojuegos** en vez de estudiar."),
            ("¿Cómo se sintió Ana después del examen?", "triste", "Ana se sintió **triste** porque no supo responder."),
            ("¿Qué prometió Ana?", "estudiar primero", "Prometió que **estudiaría primero** y jugaría después."),
        ],
        "ensenanza": "La responsabilidad es importante: primero el deber y luego el placer.",
        "valor": "responsabilidad",
    },
]


def _q_comprension_lectora(dif):
    historia = random.choice(_TEXTOS)
    q_text, a, p = random.choice(historia["preguntas"])
    texto_corto = historia["texto"]
    is_num = isinstance(a, int)
    return dict(
        question=f"Lee el texto y responde:\n\n«{texto_corto}»\n\n{q_text}",
        answer=a, is_numeric=is_num, procedure=p)


def _q_valores(dif):
    historia = random.choice(_TEXTOS)
    tipo = random.choice(['ensenanza', 'valor'])

    if tipo == 'ensenanza':
        return dict(
            question=f"Lee el texto y responde: ¿Cuál es la enseñanza?\n\n«{historia['texto']}»\n\n(Escribe: {historia['ensenanza'][:30]}...)",
            answer=historia['ensenanza'][:30].lower().strip(),
            is_numeric=False,
            procedure=f"La enseñanza es: **{historia['ensenanza']}**")

    return dict(
        question=f"Lee el texto:\n\n«{historia['texto']}»\n\n¿Qué valor se muestra en esta historia?",
        answer=historia['valor'], is_numeric=False,
        procedure=f"El valor principal es la **{historia['valor']}**.")


def _q_vocabulario(dif):
    if dif == "Fácil":
        ejercicios = [
            ("El perro ___ muy contento cuando vio a su dueño. (ladró / cocinó / leyó)", "ladro",
             "Los perros **ladran** cuando están contentos."),
            ("La maestra ___ la lección en la pizarra. (nadó / escribió / cocinó)", "escribio",
             "La maestra **escribió** la lección."),
            ("Los niños ___ en el recreo. (durmieron / jugaron / cocinaron)", "jugaron",
             "Los niños **jugaron** en el recreo."),
            ("Mi mamá ___ un pastel delicioso. (horneó / voló / nadó)", "horneo",
             "Mi mamá **horneó** un pastel."),
            ("El sol ___ muy fuerte hoy. (brilla / nada / corre)", "brilla",
             "El sol **brilla** fuerte."),
        ]
    elif dif == "Normal":
        ejercicios = [
            ("El explorador ___ la cueva con una linterna. (iluminó / sembró / tejió)", "ilumino",
             "**Iluminó** significa dar luz a un lugar oscuro."),
            ("La noticia ___ a todos en el pueblo. (sorprendió / regó / pintó)", "sorprendio",
             "**Sorprendió** significa causar asombro."),
            ("El río ___ por el valle hasta llegar al mar. (fluye / vuela / salta)", "fluye",
             "**Fluye** significa que el agua corre o se mueve."),
            ("Los bomberos ___ el incendio rápidamente. (apagaron / sembraron / leyeron)", "apagaron",
             "Los bomberos **apagaron** el incendio."),
            ("El científico ___ un nuevo insecto en la selva. (descubrió / cocinó / pintó)", "descubrio",
             "**Descubrió** significa encontrar algo nuevo."),
        ]
    else:
        ejercicios = [
            ("La ___ del volcán cubrió el cielo de ceniza. (erupción / canción / lección)", "erupcion",
             "Una **erupción** volcánica expulsa lava y ceniza."),
            ("El doctor le recetó un ___ para la fiebre. (medicamento / instrumento / alimento)", "medicamento",
             "Un **medicamento** es una medicina para curar enfermedades."),
            ("La ___ de los árboles produce oxígeno. (fotosíntesis / digestión / respiración)", "fotosintesis",
             "La **fotosíntesis** es el proceso por el cual las plantas producen oxígeno."),
            ("El ___ es un fenómeno natural que sacude la tierra. (terremoto / arcoíris / eclipse)", "terremoto",
             "Un **terremoto** es un movimiento fuerte de la tierra."),
            ("La ___ es la capacidad de ponerse en el lugar del otro. (empatía / apatía / simpatía)", "empatia",
             "La **empatía** es comprender los sentimientos de los demás."),
        ]

    q, a, p = random.choice(ejercicios)
    return dict(question=q, answer=a, is_numeric=False, procedure=p)


_GENERATORS = {
    "Fuentes de información": _q_fuentes_info,
    "Uso de textos informativos": _q_uso_textos,
    "Relación de conceptos": _q_relacion_conceptos,
    "Comprensión lectora": _q_comprension_lectora,
    "Valores y reflexión": _q_valores,
    "Vocabulario": _q_vocabulario,
}

def generate_question_jaikel_espanol(topic, dificultad="Normal"):
    q = _GENERATORS[topic](dificultad)
    q['topic'] = topic
    return q
