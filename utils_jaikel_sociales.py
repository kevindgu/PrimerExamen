import random

TOPICS_JAIKEL_SOCIALES = {
    "Representación de la Tierra": {
        "aprendizaje": "Identificar diferentes formas de representar la Tierra",
        "indicador": "Identifica mapa, croquis, globo terráqueo y sus características",
    },
    "Tipos de mapas": {
        "aprendizaje": "Distinguir entre mapa físico, político y temático",
        "indicador": "Identifica el uso de cada tipo de mapa según su información",
    },
    "Elementos del mapa": {
        "aprendizaje": "Reconocer elementos del mapa y su función",
        "indicador": "Reconoce título, escala, simbología, orientación y su función",
    },
    "Ubicación geográfica": {
        "aprendizaje": "Interpretar información en mapas de Costa Rica",
        "indicador": "Identifica elementos señalados en un mapa de Costa Rica",
    },
    "Coordenadas geográficas": {
        "aprendizaje": "Comprender el uso de meridianos y paralelos",
        "indicador": "Interpreta información básica de coordenadas geográficas",
    },
}


def _q_representacion_tierra(dif):
    preguntas = [
        # Identificar representaciones
        ("¿Cuál es la representación más parecida a la forma real de la Tierra?", "globo terraqueo",
         "El **globo terráqueo** es esférico como la Tierra, por eso es la representación más fiel."),
        ("¿Cómo se llama el dibujo sencillo que muestra cómo llegar a un lugar, sin ser exacto?", "croquis",
         "Un **croquis** es un dibujo simple, hecho a mano, que muestra rutas o ubicaciones sin medidas exactas."),
        ("¿Cómo se llama la representación plana de la Tierra o parte de ella?", "mapa",
         "Un **mapa** es una representación plana (en 2D) de la superficie terrestre."),
        # Características
        ("¿El globo terráqueo es plano o esférico?", "esferico",
         "El globo terráqueo es **esférico**, igual que la forma de la Tierra."),
        ("¿Un croquis tiene medidas exactas? (si o no)", "no",
         "**No**, un croquis es un dibujo aproximado, sin escala ni medidas exactas."),
        ("¿Un mapa puede mostrar todo el mundo o solo una parte? (responde: ambos)", "ambos",
         "Un mapa puede mostrar **ambos**: todo el mundo (planisferio) o solo una parte (mapa regional)."),
        # Relación
        ("Si quieres ver cómo se ve la Tierra desde el espacio, ¿qué usarías: mapa, croquis o globo terráqueo?", "globo terraqueo",
         "El **globo terráqueo** muestra la Tierra como se ve desde el espacio."),
        ("Si necesitas explicarle a un amigo cómo llegar a tu casa, ¿qué harías: mapa, croquis o globo terráqueo?", "croquis",
         "Un **croquis** es ideal para dibujar rápidamente una ruta sencilla."),
        ("Para estudiar los países del mundo en detalle, ¿qué usarías: mapa, croquis o globo terráqueo?", "mapa",
         "Un **mapa** permite ver detalles como fronteras, ciudades y ríos con más precisión."),
    ]
    if dif == "Fácil":
        q, a, p = random.choice(preguntas[:6])
    else:
        q, a, p = random.choice(preguntas)
    return dict(question=q, answer=a, is_numeric=False, procedure=p)


def _q_tipos_mapas(dif):
    preguntas = [
        ("¿Qué tipo de mapa muestra montañas, ríos y volcanes?", "fisico",
         "El mapa **físico** muestra el relieve: montañas, ríos, volcanes, llanuras."),
        ("¿Qué tipo de mapa muestra países, capitales y fronteras?", "politico",
         "El mapa **político** muestra divisiones: países, provincias, capitales y fronteras."),
        ("¿Qué tipo de mapa muestra información específica como clima, población o cultivos?", "tematico",
         "El mapa **temático** muestra un tema específico: clima, población, recursos, etc."),
        ("Si quieres saber dónde están los volcanes de Costa Rica, ¿qué mapa usas: físico, político o temático?", "fisico",
         "Los volcanes son parte del relieve → mapa **físico**."),
        ("Si quieres saber cuáles son las provincias de Costa Rica, ¿qué mapa usas?", "politico",
         "Las provincias son divisiones administrativas → mapa **político**."),
        ("Si quieres saber qué cultivos se producen en cada zona, ¿qué mapa usas?", "tematico",
         "Los cultivos son un tema específico → mapa **temático**."),
        ("¿Un mapa que muestra las temperaturas de un país es físico, político o temático?", "tematico",
         "La temperatura es un tema específico → mapa **temático**."),
        ("¿Un mapa que muestra la cordillera de Talamanca es físico, político o temático?", "fisico",
         "Una cordillera es relieve → mapa **físico**."),
        ("¿Por qué son importantes los mapas? Porque nos ayudan a... (responde: ubicarnos)", "ubicarnos",
         "Los mapas son importantes porque nos ayudan a **ubicarnos** y conocer el mundo."),
    ]
    q, a, p = random.choice(preguntas)
    return dict(question=q, answer=a, is_numeric=False, procedure=p)


def _q_elementos_mapa(dif):
    preguntas = [
        ("¿Qué elemento del mapa indica qué representa el mapa?", "titulo",
         "El **título** nos dice qué zona o tema representa el mapa."),
        ("¿Qué elemento del mapa nos dice qué significan los colores y símbolos?", "simbologia",
         "La **simbología** (o leyenda) explica qué significa cada color y símbolo."),
        ("¿Qué elemento del mapa indica dónde está el norte?", "rosa de los vientos",
         "La **rosa de los vientos** (u orientación) indica dónde está el norte, sur, este y oeste."),
        ("¿Qué elemento del mapa nos ayuda a saber las distancias reales?", "escala",
         "La **escala** nos permite calcular distancias reales a partir del mapa."),
        ("¿Cuáles son los 4 puntos cardinales?", "norte sur este oeste",
         "Los 4 puntos cardinales son: **Norte, Sur, Este y Oeste**."),
        # Función
        ("Si en un mapa ves un cuadrito azul y en la leyenda dice 'lago', ¿qué elemento consultaste?", "simbologia",
         "Consultaste la **simbología** (leyenda) para saber qué significa el símbolo."),
        ("Si quieres saber si el mapa es de Costa Rica o de todo Centroamérica, ¿qué elemento revisas?", "titulo",
         "Revisas el **título** del mapa para saber qué zona representa."),
    ]
    if dif == "Fácil":
        q, a, p = random.choice(preguntas[:4])
    else:
        q, a, p = random.choice(preguntas)
    return dict(question=q, answer=a, is_numeric=False, procedure=p)


def _q_ubicacion_geografica(dif):
    provincias = ['San José', 'Alajuela', 'Cartago', 'Heredia', 'Guanacaste', 'Puntarenas', 'Limón']

    preguntas = [
        ("¿Cuál es la capital de Costa Rica?", "san jose",
         "La capital de Costa Rica es **San José**."),
        ("¿Cuántas provincias tiene Costa Rica?", 7,
         "Costa Rica tiene **7** provincias."),
        ("¿En qué continente está Costa Rica?", "america",
         "Costa Rica está en **América** (América Central)."),
        ("¿Qué océano está al este de Costa Rica?", "atlantico",
         "Al este (Caribe) está el océano **Atlántico**."),
        ("¿Qué océano está al oeste de Costa Rica?", "pacifico",
         "Al oeste está el océano **Pacífico**."),
        ("¿Qué país está al norte de Costa Rica?", "nicaragua",
         "Al norte de Costa Rica está **Nicaragua**."),
        ("¿Qué país está al sur de Costa Rica?", "panama",
         "Al sur de Costa Rica está **Panamá**."),
        ("¿En qué provincia está el volcán Arenal?", "alajuela",
         "El volcán Arenal está en la provincia de **Alajuela**."),
        ("¿Cuál es la provincia más grande de Costa Rica?", "guanacaste",
         "La provincia más grande es **Guanacaste**."),
    ]

    if dif == "Fácil":
        q, a, p = random.choice(preguntas[:5])
    else:
        q, a, p = random.choice(preguntas)
    is_num = isinstance(a, int)
    return dict(question=q, answer=a, is_numeric=is_num, procedure=p)


def _q_coordenadas(dif):
    preguntas = [
        ("¿Cómo se llaman las líneas imaginarias que van de norte a sur en el globo terráqueo?", "meridianos",
         "Los **meridianos** son líneas verticales que van de polo norte a polo sur."),
        ("¿Cómo se llaman las líneas imaginarias que van de este a oeste?", "paralelos",
         "Los **paralelos** son líneas horizontales que rodean la Tierra de este a oeste."),
        ("¿Cómo se llama el paralelo más importante, que divide la Tierra en hemisferio norte y sur?", "ecuador",
         "La línea del **Ecuador** divide la Tierra en hemisferio norte y hemisferio sur."),
        ("¿Cómo se llama el meridiano principal que pasa por Greenwich?", "meridiano de greenwich",
         "El **meridiano de Greenwich** (meridiano 0°) divide la Tierra en hemisferio este y oeste."),
        ("¿En qué hemisferio está Costa Rica: norte o sur?", "norte",
         "Costa Rica está en el hemisferio **norte**, cerca del Ecuador."),
        ("¿Las coordenadas geográficas usan dos valores: latitud y...?", "longitud",
         "Las coordenadas usan **latitud** (norte-sur) y **longitud** (este-oeste)."),
        ("¿La latitud se mide con paralelos o meridianos?", "paralelos",
         "La latitud se mide con **paralelos** (líneas horizontales)."),
        ("¿La longitud se mide con paralelos o meridianos?", "meridianos",
         "La longitud se mide con **meridianos** (líneas verticales)."),
        ("¿Para qué sirven las coordenadas geográficas? Para... (responde: ubicar lugares)", "ubicar lugares",
         "Las coordenadas sirven para **ubicar lugares** exactos en la Tierra."),
    ]
    if dif == "Fácil":
        q, a, p = random.choice(preguntas[:5])
    else:
        q, a, p = random.choice(preguntas)
    return dict(question=q, answer=a, is_numeric=False, procedure=p)


_GENERATORS = {
    "Representación de la Tierra": _q_representacion_tierra,
    "Tipos de mapas": _q_tipos_mapas,
    "Elementos del mapa": _q_elementos_mapa,
    "Ubicación geográfica": _q_ubicacion_geografica,
    "Coordenadas geográficas": _q_coordenadas,
}

def generate_question_jaikel_sociales(topic, dificultad="Normal"):
    q = _GENERATORS[topic](dificultad)
    q['topic'] = topic
    return q
