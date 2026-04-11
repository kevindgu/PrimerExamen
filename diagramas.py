import random
import os

BASE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE, "imagenes")

# Mapeo de órganos/partes con sus imágenes y datos
SISTEMAS = {
    "digestivo": {
        "nombre": "Sistema digestivo",
        "imagen_completa": os.path.join(IMG_DIR, "digestivo", "sistemadigestivo.png"),
        "partes": [
            {"nombre": "boca", "imagen": os.path.join(IMG_DIR, "digestivo", "boca.jpg"),
             "funcion": "Aquí se mastica la comida y se mezcla con saliva"},
            {"nombre": "glándulas salivales", "imagen": os.path.join(IMG_DIR, "digestivo", "glandulas_salivales.png"),
             "funcion": "Producen saliva que ayuda a descomponer los alimentos"},
            {"nombre": "faringe", "imagen": os.path.join(IMG_DIR, "digestivo", "faringe.jpg"),
             "funcion": "Conecta la boca con el esófago, permite tragar"},
            {"nombre": "laringe", "imagen": os.path.join(IMG_DIR, "digestivo", "laringe.jpg"),
             "funcion": "Se encuentra cerca de la faringe, protege las vías respiratorias al tragar"},
            {"nombre": "esófago", "imagen": os.path.join(IMG_DIR, "digestivo", "esofago.png"),
             "funcion": "Tubo que lleva la comida de la boca al estómago"},
            {"nombre": "estómago", "imagen": os.path.join(IMG_DIR, "digestivo", "estamago.jpg"),
             "funcion": "Mezcla la comida con jugos gástricos para descomponerla"},
            {"nombre": "hígado", "imagen": os.path.join(IMG_DIR, "digestivo", "higado.jpg"),
             "funcion": "Produce bilis que ayuda a digerir las grasas"},
            {"nombre": "intestino delgado", "imagen": os.path.join(IMG_DIR, "digestivo", "intestinodelgado.jpg"),
             "funcion": "Absorbe los nutrientes de los alimentos hacia la sangre"},
            {"nombre": "intestino grueso", "imagen": os.path.join(IMG_DIR, "digestivo", "intestinogrueso.jpg"),
             "funcion": "Absorbe el agua y forma las heces"},
            {"nombre": "recto y ano", "imagen": os.path.join(IMG_DIR, "digestivo", "rectoyanojuntos.jpg"),
             "funcion": "El recto almacena las heces y el ano las expulsa del cuerpo"},
        ]
    },
    # Se pueden agregar más sistemas aquí cuando tengas las imágenes
    # "oseo": { ... },
    # "muscular": { ... },
}


def pregunta_con_imagen(sistema, dif="Normal"):
    if sistema not in SISTEMAS:
        return None

    info = SISTEMAS[sistema]
    partes = info["partes"]
    # Filtrar solo partes que tengan imagen existente
    partes_validas = [p for p in partes if os.path.exists(p["imagen"])]
    if not partes_validas:
        return None

    tipo = random.choice(["identificar", "funcion", "sistema_completo"])

    if tipo == "identificar":
        parte = random.choice(partes_validas)
        return {
            "question": f"🔬 Observa la imagen. ¿Qué órgano del {info['nombre'].lower()} es este?",
            "imagen": parte["imagen"],
            "answer": parte["nombre"],
            "is_numeric": False,
            "procedure": f"Este órgano es: **{parte['nombre']}**\n\nFunción: {parte['funcion']}",
            "topic": info["nombre"],
        }

    if tipo == "funcion":
        parte = random.choice(partes_validas)
        return {
            "question": f"🔬 Observa la imagen. ¿Cuál es la función de este órgano?",
            "imagen": parte["imagen"],
            "answer": parte["nombre"],
            "is_numeric": False,
            "procedure": f"Es el/la **{parte['nombre']}**.\n\nFunción: {parte['funcion']}",
            "topic": info["nombre"],
            # Para este tipo, aceptamos el nombre del órgano como respuesta
            "_hint": parte["funcion"],
        }

    # sistema_completo: mostrar el sistema entero
    if os.path.exists(info["imagen_completa"]):
        parte = random.choice(partes_validas)
        opciones = random.sample(partes_validas, min(3, len(partes_validas)))
        if parte not in opciones:
            opciones[0] = parte
        random.shuffle(opciones)
        opciones_txt = ", ".join(o["nombre"] for o in opciones)
        return {
            "question": f"🔬 Observa el {info['nombre']} completo.\n\n¿Cuál de estos órganos se encarga de: {parte['funcion'].lower()}?\n\nOpciones: {opciones_txt}",
            "imagen": info["imagen_completa"],
            "answer": parte["nombre"],
            "is_numeric": False,
            "procedure": f"La respuesta es **{parte['nombre']}**.\n\nFunción: {parte['funcion']}",
            "topic": info["nombre"],
        }

    # Fallback
    return pregunta_con_imagen(sistema, dif)
