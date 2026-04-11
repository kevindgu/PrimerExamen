import random
import os

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "imagenes")

TOPICS_JAIKEL_CIENCIAS = {
    "Sistema óseo": {
        "aprendizaje": "Identificar funciones, articulaciones y cuidados del sistema óseo",
        "indicador": "Identifica funciones, tipos de articulaciones y medidas de cuidado",
    },
    "Sistema digestivo": {
        "aprendizaje": "Identificar órganos, funciones y proceso digestivo",
        "indicador": "Identifica órganos, recorrido del bolo alimenticio y medidas de salud",
    },
    "Sistema muscular": {
        "aprendizaje": "Identificar músculos y sus clasificaciones",
        "indicador": "Identifica músculos, clasificaciones y medidas de cuidado",
    },
}

# ============================================================
# DATOS DE PARTES CON IMÁGENES
# ============================================================
_DIGESTIVO = [
    {"nombre": "boca", "img": "digestivo/boca.jpg", "funcion": "Mastica la comida y la mezcla con saliva"},
    {"nombre": "glándulas salivales", "img": "digestivo/glandulas_salivales.png", "funcion": "Producen saliva para descomponer alimentos"},
    {"nombre": "faringe", "img": "digestivo/faringe.jpg", "funcion": "Conecta la boca con el esófago, permite tragar"},
    {"nombre": "laringe", "img": "digestivo/laringe.jpg", "funcion": "Protege las vías respiratorias al tragar"},
    {"nombre": "esófago", "img": "digestivo/esofago.png", "funcion": "Tubo que lleva la comida al estómago"},
    {"nombre": "estómago", "img": "digestivo/estamago.jpg", "funcion": "Mezcla la comida con jugos gástricos"},
    {"nombre": "hígado", "img": "digestivo/higado.jpg", "funcion": "Produce bilis para digerir las grasas"},
    {"nombre": "intestino delgado", "img": "digestivo/intestinodelgado.jpg", "funcion": "Absorbe los nutrientes hacia la sangre"},
    {"nombre": "intestino grueso", "img": "digestivo/intestinogrueso.jpg", "funcion": "Absorbe el agua y forma las heces"},
    {"nombre": "recto y ano", "img": "digestivo/rectoyanojuntos.jpg", "funcion": "Almacena y expulsa las heces del cuerpo"},
]

_OSEO = [
    {"nombre": "cráneo", "img": "osea/craneo.jpeg", "funcion": "Protege el cerebro"},
    {"nombre": "mandíbula", "img": "osea/mandibula.jpeg", "funcion": "Permite masticar y mover la boca"},
    {"nombre": "clavícula", "img": "osea/clavicula.jpeg", "funcion": "Conecta el hombro con el esternón"},
    {"nombre": "omóplato", "img": "osea/omoplato.jpg", "funcion": "Hueso plano de la espalda que conecta el brazo"},
    {"nombre": "costillas", "img": "osea/costillas.jpg", "funcion": "Protegen el corazón y los pulmones"},
    {"nombre": "pelvis", "img": "osea/pelvis.jpeg", "funcion": "Sostiene órganos del abdomen y conecta las piernas"},
    {"nombre": "fémur", "img": "osea/femur.jpeg", "funcion": "Hueso del muslo, el más largo del cuerpo"},
    {"nombre": "tibia", "img": "osea/tibia.jpg", "funcion": "Hueso principal de la parte inferior de la pierna"},
    {"nombre": "peroné", "img": "osea/perone.jpg", "funcion": "Hueso delgado al lado de la tibia"},
    {"nombre": "radio", "img": "osea/radio.jpg", "funcion": "Hueso del antebrazo del lado del pulgar"},
    {"nombre": "cúbito", "img": "osea/cubito.png", "funcion": "Hueso del antebrazo del lado del meñique"},
    {"nombre": "carpo", "img": "osea/carpo.webp", "funcion": "Huesos pequeños de la muñeca"},
    {"nombre": "metacarpo", "img": "osea/metacarpo.webp", "funcion": "Huesos de la palma de la mano"},
    {"nombre": "falanges", "img": "osea/falanges.jpg", "funcion": "Huesos de los dedos"},
    {"nombre": "tarso", "img": "osea/tarso.jpeg", "funcion": "Huesos del tobillo"},
    {"nombre": "metatarso", "img": "osea/metatorso.jpg", "funcion": "Huesos de la planta del pie"},
]

_MUSCULAR = [
    {"nombre": "frontal", "img": "muscular/frontal.jpeg", "funcion": "Músculo de la frente, levanta las cejas", "tipo": "voluntario"},
    {"nombre": "deltoides", "img": "muscular/deltoide.jpeg", "funcion": "Músculo del hombro, levanta el brazo", "tipo": "voluntario"},
    {"nombre": "pectorales", "img": "muscular/pectorales.png", "funcion": "Músculos del pecho, mueven los brazos", "tipo": "voluntario"},
    {"nombre": "bíceps", "img": "muscular/biceps.webp", "funcion": "Músculo frontal del brazo, flexiona el codo", "tipo": "voluntario"},
    {"nombre": "tríceps", "img": "muscular/triceps.jpg", "funcion": "Músculo trasero del brazo, extiende el codo", "tipo": "voluntario"},
    {"nombre": "abdominales", "img": "muscular/abdominales.jpg", "funcion": "Músculos del abdomen, protegen órganos", "tipo": "voluntario"},
    {"nombre": "cuádriceps", "img": "muscular/cuadriceps.webp", "funcion": "Músculo frontal del muslo, extiende la rodilla", "tipo": "voluntario"},
    {"nombre": "gemelos", "img": "muscular/gemelos.jpg", "funcion": "Músculos de la pantorrilla, permiten caminar y saltar", "tipo": "voluntario"},
    {"nombre": "glúteos", "img": "muscular/gluteos.jpg", "funcion": "Músculos de la cadera, los más grandes del cuerpo", "tipo": "voluntario"},
    {"nombre": "trapecio", "img": "muscular/trapecio.jpg", "funcion": "Músculo de la espalda superior, mueve los hombros", "tipo": "voluntario"},
    {"nombre": "dorsal", "img": "muscular/dorsal.webp", "funcion": "Músculo grande de la espalda, permite jalar", "tipo": "voluntario"},
]

_ARTICULACIONES = [
    {"nombre": "rodilla", "img": "articulaciones/rodilla.jpeg", "tipo": "móvil", "funcion": "Permite doblar y estirar la pierna"},
    {"nombre": "codo", "img": "articulaciones/codo.jpg", "tipo": "móvil", "funcion": "Permite doblar y estirar el brazo"},
    {"nombre": "hombro", "img": "articulaciones/hombro.jpeg", "tipo": "móvil", "funcion": "Permite mover el brazo en muchas direcciones"},
    {"nombre": "tobillo", "img": "articulaciones/tobillo.webp", "tipo": "móvil", "funcion": "Permite mover el pie"},
    {"nombre": "pelvis (cadera)", "img": "articulaciones/pelvis.jpeg", "tipo": "móvil", "funcion": "Permite mover las piernas y caminar"},
]

_ORDEN_DIGESTIVO = ["boca", "faringe", "esófago", "estómago", "intestino delgado", "intestino grueso", "recto y ano"]


def _img_path(relative):
    return os.path.join(IMG, relative)


def _validas(partes):
    return [p for p in partes if os.path.exists(_img_path(p["img"]))]


def _opciones_random(partes, correcta, n=4):
    """Genera lista de n opciones incluyendo la correcta."""
    otras = [p for p in partes if p["nombre"] != correcta["nombre"]]
    elegidas = random.sample(otras, min(n - 1, len(otras)))
    elegidas.append(correcta)
    random.shuffle(elegidas)
    return elegidas


# ============================================================
# TIPOS DE EJERCICIO GENÉRICOS
# ============================================================

def _comparar_imagenes(partes, sistema):
    """Muestra 2 imágenes lado a lado, pregunta cuál es X."""
    v = _validas(partes)
    if len(v) < 2:
        return None
    dos = random.sample(v, 2)
    correcta = random.choice(dos)
    return dict(
        question=f"¿Cuál de estas dos imágenes muestra: **{correcta['nombre']}**?",
        imagen=_img_path(dos[0]["img"]),
        imagen2=_img_path(dos[1]["img"]),
        imagen1_label=dos[0]["nombre"],
        imagen2_label=dos[1]["nombre"],
        opciones_btn=["Imagen 1", "Imagen 2"],
        answer="imagen 1" if dos[0]["nombre"] == correcta["nombre"] else "imagen 2",
        is_numeric=False,
        procedure=f"**{correcta['nombre']}**: {correcta['funcion']}\n\nImagen 1 era: {dos[0]['nombre']}\nImagen 2 era: {dos[1]['nombre']}",
        _tipo="comparar_imagenes")


def _seleccion_multiple_imagen(partes, sistema):
    """Muestra imagen, 4 botones para elegir el nombre."""
    v = _validas(partes)
    if not v:
        return None
    correcta = random.choice(v)
    opciones = _opciones_random(v, correcta)
    nombres = [op['nombre'] for op in opciones]
    return dict(
        question=f"¿Qué parte del {sistema} se muestra en la imagen?",
        imagen=_img_path(correcta["img"]),
        opciones_btn=nombres,
        answer=correcta["nombre"],
        is_numeric=False,
        procedure=f"La respuesta es **{correcta['nombre']}**\n\nFunción: {correcta['funcion']}",
        _tipo="seleccion_multiple")


def _seleccion_funcion_imagen(partes, sistema):
    """Muestra imagen, 4 botones de función para elegir."""
    v = _validas(partes)
    if not v:
        return None
    correcta = random.choice(v)
    opciones = _opciones_random(v, correcta)
    funciones = [op['funcion'] for op in opciones]
    return dict(
        question=f"Observa la imagen. ¿Cuál es la función de esta parte del {sistema}?",
        imagen=_img_path(correcta["img"]),
        opciones_btn=funciones,
        answer=correcta["funcion"],
        is_numeric=False,
        procedure=f"Es el/la **{correcta['nombre']}**\n\n{correcta['funcion']}",
        _tipo="seleccion_funcion")


def _verdadero_falso(partes, sistema):
    """Muestra imagen, dice una función, botones V o F."""
    v = _validas(partes)
    if len(v) < 2:
        return None
    parte = random.choice(v)
    es_verdadero = random.choice([True, False])
    if es_verdadero:
        afirmacion = parte['funcion']
        resp = "verdadero"
        expl = f"**Verdadero**. Es el/la {parte['nombre']}: {parte['funcion']}"
    else:
        otra = random.choice([p for p in v if p["nombre"] != parte["nombre"]])
        afirmacion = otra['funcion']
        resp = "falso"
        expl = f"**Falso**. Lo que ves es el/la **{parte['nombre']}**.\n\nSu función real es: {parte['funcion']}\n\nLa función mostrada era del/de la {otra['nombre']}."
    return dict(
        question=f"Observa la imagen. ¿Es correcta esta función?\n\n«{afirmacion}»",
        imagen=_img_path(parte["img"]),
        opciones_btn=["✅ Verdadero", "❌ Falso"],
        answer=resp,
        is_numeric=False,
        procedure=expl,
        _tipo="verdadero_falso")


def _completar(partes, sistema):
    """Completa la oración con botones."""
    v = _validas(partes)
    if not v:
        return None
    parte = random.choice(v)
    opciones = _opciones_random(v, parte, 4)
    nombres = [op['nombre'] for op in opciones]
    return dict(
        question=f"Completa la oración:\n\n«El/La _______ {parte['funcion'].lower()}»",
        opciones_btn=nombres,
        answer=parte["nombre"],
        is_numeric=False,
        procedure=f"**{parte['nombre']}**: {parte['funcion']}",
        _tipo="completar")


def _asociar_funcion(partes, sistema):
    """Muestra imagen + función, botones Sí/No."""
    v = _validas(partes)
    if len(v) < 2:
        return None
    parte = random.choice(v)
    coincide = random.choice([True, False])
    if coincide:
        funcion_mostrada = parte["funcion"]
        resp = "sí"
        expl = f"**Sí**, correcto. Es el/la {parte['nombre']}: {parte['funcion']}"
    else:
        otra = random.choice([p for p in v if p["nombre"] != parte["nombre"]])
        funcion_mostrada = otra["funcion"]
        resp = "no"
        expl = f"**No**. Lo que ves en la imagen es el/la **{parte['nombre']}**.\n\nSu función real es: {parte['funcion']}\n\nLa función mostrada era del/de la {otra['nombre']}."
    return dict(
        question=f"Observa la imagen. ¿La siguiente función corresponde a lo que ves?\n\n«{funcion_mostrada}»",
        imagen=_img_path(parte["img"]),
        opciones_btn=["👍 Sí", "👎 No"],
        answer=resp,
        is_numeric=False,
        procedure=expl,
        _tipo="asociar")


# ============================================================
# SISTEMA DIGESTIVO
# ============================================================
def _q_ordenar_digestivo():
    """Preguntas de orden del recorrido digestivo con botones."""
    idx1 = random.randint(0, len(_ORDEN_DIGESTIVO) - 2)
    organo1 = _ORDEN_DIGESTIVO[idx1]
    organo2 = _ORDEN_DIGESTIVO[idx1 + 1]
    if random.choice([True, False]):
        opciones = [organo1, organo2]
        random.shuffle(opciones)
        return dict(
            question="En el recorrido del alimento, ¿qué viene PRIMERO?",
            opciones_btn=opciones,
            answer=organo1,
            is_numeric=False,
            procedure=f"Orden: {' → '.join(_ORDEN_DIGESTIVO)}\n\n**{organo1}** viene antes que {organo2}",
            _tipo="ordenar")
    otras = [o for o in _ORDEN_DIGESTIVO if o != organo1 and o != organo2]
    distractores = random.sample(otras, min(2, len(otras)))
    opciones = distractores + [organo2]
    random.shuffle(opciones)
    return dict(
        question=f"En el recorrido del alimento, ¿qué viene DESPUÉS de **{organo1}**?",
        opciones_btn=opciones,
        answer=organo2,
        is_numeric=False,
        procedure=f"Orden: {' → '.join(_ORDEN_DIGESTIVO)}\n\nDespués de {organo1} viene **{organo2}**",
        _tipo="ordenar")


def _q_sistema_digestivo(dif):
    tipos_img = [
        lambda: _seleccion_multiple_imagen(_DIGESTIVO, "sistema digestivo"),
        lambda: _seleccion_funcion_imagen(_DIGESTIVO, "sistema digestivo"),
        lambda: _verdadero_falso(_DIGESTIVO, "sistema digestivo"),
        lambda: _completar(_DIGESTIVO, "sistema digestivo"),
        lambda: _asociar_funcion(_DIGESTIVO, "sistema digestivo"),
        lambda: _comparar_imagenes(_DIGESTIVO, "sistema digestivo"),
    ]
    tipos_texto = [
        lambda: _q_ordenar_digestivo(),
    ]

    # 60% imagen, 40% texto
    if random.random() < 0.6:
        gen = random.choice(tipos_img)
        q = gen()
        if q:
            return q

    # Texto
    if random.random() < 0.3:
        q = _q_ordenar_digestivo()
        if q:
            return q

    preguntas = [
        ("¿Por dónde entra la comida al sistema digestivo?", "Boca", ["Estómago", "Boca", "Intestino", "Esófago"],
         "**Boca**. La comida entra por la boca donde se mastica."),
        ("¿Qué tubo lleva la comida al estómago?", "Esófago", ["Intestino", "Faringe", "Esófago", "Tráquea"],
         "**Esófago**. Conecta la boca con el estómago."),
        ("¿Dónde se mezcla la comida con jugos gástricos?", "Estómago", ["Boca", "Intestino", "Hígado", "Estómago"],
         "**Estómago**. Ahí se mezcla con jugos gástricos."),
        ("¿Dónde se absorben los nutrientes?", "Intestino delgado", ["Estómago", "Intestino grueso", "Intestino delgado", "Boca"],
         "**Intestino delgado**. Absorbe nutrientes hacia la sangre."),
        ("¿Cómo se llama la comida masticada mezclada con saliva?", "Bolo alimenticio", ["Quimo", "Bolo alimenticio", "Quilo", "Bilis"],
         "**Bolo alimenticio**."),
        ("¿Qué órgano produce bilis?", "Hígado", ["Estómago", "Páncreas", "Hígado", "Intestino"],
         "**Hígado**. Produce bilis para digerir grasas."),
        ("¿Masticar bien ayuda a la digestión?", "✅ Verdadero", ["✅ Verdadero", "❌ Falso"],
         "**Verdadero**. Masticar bien facilita el trabajo del estómago."),
        ("¿Comer muy rápido es bueno para la digestión?", "❌ Falso", ["✅ Verdadero", "❌ Falso"],
         "**Falso**. Hay que comer despacio y masticar bien."),
        ("¿Las frutas y verduras ayudan al sistema digestivo?", "✅ Verdadero", ["✅ Verdadero", "❌ Falso"],
         "**Verdadero**. Tienen fibra que ayuda a la digestión."),
    ]
    if dif == "Fácil":
        q, a, opts, p = random.choice(preguntas[:5])
    elif dif == "Normal":
        q, a, opts, p = random.choice(preguntas[:7])
    else:
        q, a, opts, p = random.choice(preguntas)
    return dict(question=q, answer=a, opciones_btn=opts, is_numeric=False, procedure=p)


# ============================================================
# SISTEMA ÓSEO
# ============================================================
def _q_sistema_oseo(dif):
    tipos_img = [
        lambda: _seleccion_multiple_imagen(_OSEO, "sistema óseo"),
        lambda: _seleccion_multiple_imagen(_ARTICULACIONES, "cuerpo (articulaciones)"),
        lambda: _seleccion_funcion_imagen(_OSEO, "sistema óseo"),
        lambda: _verdadero_falso(_OSEO, "sistema óseo"),
        lambda: _completar(_OSEO, "sistema óseo"),
        lambda: _asociar_funcion(_OSEO, "sistema óseo"),
        lambda: _comparar_imagenes(_OSEO, "sistema óseo"),
    ]

    if random.random() < 0.6:
        gen = random.choice(tipos_img)
        q = gen()
        if q:
            return q

    preguntas = [
        ("¿Cuál es una función del sistema óseo?", "Dar soporte al cuerpo", ["Digerir alimentos", "Dar soporte al cuerpo", "Respirar", "Bombear sangre"],
         "**Dar soporte**. También protege órganos y permite movimiento."),
        ("¿Qué hueso protege el cerebro?", "Cráneo", ["Fémur", "Costillas", "Cráneo", "Pelvis"],
         "**Cráneo**."),
        ("¿Cuál es el hueso más largo del cuerpo?", "Fémur", ["Tibia", "Húmero", "Cráneo", "Fémur"],
         "**Fémur** (hueso del muslo)."),
        ("¿Qué huesos protegen corazón y pulmones?", "Costillas", ["Falanges", "Costillas", "Carpo", "Fémur"],
         "**Costillas**."),
        ("¿La rodilla es una articulación móvil o inmóvil?", "Móvil", ["Móvil", "Inmóvil"],
         "La rodilla es **móvil**, permite doblar la pierna."),
        ("¿Las articulaciones del cráneo son móviles o inmóviles?", "Inmóviles", ["Móviles", "Inmóviles"],
         "Son **inmóviles**, los huesos están fijos."),
        ("¿Qué nutriente fortalece los huesos?", "Calcio", ["Azúcar", "Grasa", "Calcio", "Sal"],
         "**Calcio**. Se encuentra en leche, queso y yogur."),
        ("¿El ejercicio ayuda a los huesos?", "✅ Verdadero", ["✅ Verdadero", "❌ Falso"],
         "**Verdadero**. El ejercicio fortalece huesos y articulaciones."),
        ("¿El sol ayuda a producir vitamina D para los huesos?", "✅ Verdadero", ["✅ Verdadero", "❌ Falso"],
         "**Verdadero**. La vitamina D ayuda a absorber calcio."),
        ("¿Los huesos de los dedos se llaman falanges?", "✅ Verdadero", ["✅ Verdadero", "❌ Falso"],
         "**Verdadero**. Las falanges son los huesos de los dedos."),
        ("¿La clavícula está en la pierna?", "❌ Falso", ["✅ Verdadero", "❌ Falso"],
         "**Falso**. La clavícula conecta el hombro con el esternón."),
    ]
    if dif == "Fácil":
        q, a, opts, p = random.choice(preguntas[:5])
    elif dif == "Normal":
        q, a, opts, p = random.choice(preguntas[:8])
    else:
        q, a, opts, p = random.choice(preguntas)
    return dict(question=q, answer=a, opciones_btn=opts, is_numeric=False, procedure=p)


# ============================================================
# SISTEMA MUSCULAR
# ============================================================
def _q_clasificar_musculo():
    """¿Este músculo es voluntario o involuntario? Con botones."""
    v = _validas(_MUSCULAR)
    if not v:
        return None
    parte = random.choice(v)
    es_vol = parte.get("tipo", "voluntario") == "voluntario"
    return dict(
        question=f"Observa la imagen. ¿Este músculo es voluntario o involuntario?",
        imagen=_img_path(parte["img"]),
        opciones_btn=["💪 Voluntario", "🫀 Involuntario"],
        answer="voluntario" if es_vol else "involuntario",
        is_numeric=False,
        procedure=f"El {parte['nombre']} es **{'voluntario' if es_vol else 'involuntario'}**.\n\n{'Lo movemos cuando queremos.' if es_vol else 'Trabaja solo, sin que lo decidamos.'}",
        _tipo="clasificar")


def _q_sistema_muscular(dif):
    tipos_img = [
        lambda: _seleccion_multiple_imagen(_MUSCULAR, "sistema muscular"),
        lambda: _seleccion_funcion_imagen(_MUSCULAR, "sistema muscular"),
        lambda: _verdadero_falso(_MUSCULAR, "sistema muscular"),
        lambda: _completar(_MUSCULAR, "sistema muscular"),
        lambda: _asociar_funcion(_MUSCULAR, "sistema muscular"),
        lambda: _q_clasificar_musculo(),
        lambda: _comparar_imagenes(_MUSCULAR, "sistema muscular"),
    ]

    if random.random() < 0.6:
        gen = random.choice(tipos_img)
        q = gen()
        if q:
            return q

    preguntas = [
        ("¿Cuál es el músculo más grande del cuerpo?", "Glúteos", ["Bíceps", "Glúteos", "Abdominales", "Tríceps"],
         "**Glúteos**."),
        ("¿El corazón es un músculo?", "✅ Verdadero", ["✅ Verdadero", "❌ Falso"],
         "**Verdadero**. Es un músculo involuntario que bombea sangre."),
        ("¿Los músculos del brazo son voluntarios o involuntarios?", "💪 Voluntarios", ["💪 Voluntarios", "🫀 Involuntarios"],
         "Son **voluntarios**: los movemos cuando queremos."),
        ("¿Los músculos del corazón son voluntarios o involuntarios?", "🫀 Involuntarios", ["💪 Voluntarios", "🫀 Involuntarios"],
         "Son **involuntarios**: trabajan solos."),
        ("¿Los músculos unidos a los huesos se llaman...?", "Esqueléticos", ["Cardíacos", "Lisos", "Esqueléticos", "Viscerales"],
         "**Esqueléticos**."),
        ("¿El músculo del corazón se llama músculo...?", "Cardíaco", ["Esquelético", "Liso", "Cardíaco", "Voluntario"],
         "**Cardíaco**."),
        ("¿Es importante calentar antes de hacer ejercicio?", "✅ Verdadero", ["✅ Verdadero", "❌ Falso"],
         "**Verdadero**. Calentar prepara los músculos y evita lesiones."),
        ("¿Estirar después del ejercicio ayuda a los músculos?", "✅ Verdadero", ["✅ Verdadero", "❌ Falso"],
         "**Verdadero**. Estirar relaja los músculos."),
        ("¿Dormir bien ayuda a recuperar los músculos?", "✅ Verdadero", ["✅ Verdadero", "❌ Falso"],
         "**Verdadero**. Durante el sueño los músculos se reparan."),
        ("¿El bíceps está en la pierna?", "❌ Falso", ["✅ Verdadero", "❌ Falso"],
         "**Falso**. El bíceps está en el brazo."),
        ("¿El trapecio está en la espalda?", "✅ Verdadero", ["✅ Verdadero", "❌ Falso"],
         "**Verdadero**. El trapecio está en la espalda superior."),
    ]
    if dif == "Fácil":
        q, a, opts, p = random.choice(preguntas[:5])
    elif dif == "Normal":
        q, a, opts, p = random.choice(preguntas[:8])
    else:
        q, a, opts, p = random.choice(preguntas)
    return dict(question=q, answer=a, opciones_btn=opts, is_numeric=False, procedure=p)


# ============================================================
# GENERADOR PRINCIPAL
# ============================================================
_GENERATORS = {
    "Sistema óseo": _q_sistema_oseo,
    "Sistema digestivo": _q_sistema_digestivo,
    "Sistema muscular": _q_sistema_muscular,
}

def generate_question_jaikel_ciencias(topic, dificultad="Normal"):
    q = _GENERATORS[topic](dificultad)
    q['topic'] = topic
    return q
