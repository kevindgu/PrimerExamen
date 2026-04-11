"""Datos de Estudios Sociales para Jaikel — El Mapa y la Ubicación Geográfica."""

IMG = "socialesjaikel"

DATA = {
    "topics": {
        "Representación de la Tierra": {
            "aprendizaje": "Identificar qué es un mapa, sus tipos e importancia",
            "indicador": "Reconoce tipos de mapas y su utilidad",
        },
        "Elementos del mapa": {
            "aprendizaje": "Reconocer los elementos del mapa y su función",
            "indicador": "Identifica título, rosa de los vientos, simbología, escala y coordenadas",
        },
        "Escalas del mapa": {
            "aprendizaje": "Distinguir los tres tipos de escala del mapa",
            "indicador": "Diferencia escala numérica, cromática y gráfica",
        },
        "Paralelos y meridianos": {
            "aprendizaje": "Comprender paralelos, meridianos y coordenadas geográficas",
            "indicador": "Identifica paralelos, meridianos, latitud y longitud",
        },
        "Localización geográfica": {
            "aprendizaje": "Localizar lugares usando coordenadas geográficas",
            "indicador": "Usa intersección de coordenadas y cuadrantes para ubicar lugares",
        },
        "Batalla de Santa Rosa": {
            "aprendizaje": "Comprender la importancia histórica de la Batalla de Santa Rosa",
            "indicador": "Identifica causas, personajes y consecuencias de la Batalla de Santa Rosa",
        },
    },

    "tags": {
        "tipo_mapa": ["Físico", "Político", "Temático"],
        "tipo_escala": ["Numérica", "Cromática", "Gráfica"],
    },

    "partes": [
        # --- TIPOS DE MAPAS ---
        {"nombre": "Mapamundi", "img": f"{IMG}/mapamundi.jpeg",
         "funcion": "Muestra todo el planeta Tierra en una hoja plana", "grupo": "Representación de la Tierra"},
        {"nombre": "Mapa físico", "img": f"{IMG}/mapa_fisico.webp",
         "funcion": "Muestra formas del terreno como montañas, llanuras y ríos", "grupo": "Representación de la Tierra",
         "tags": {"tipo_mapa": "Físico"}},
        {"nombre": "Mapa político", "img": f"{IMG}/mapa_politico.jpeg",
         "funcion": "Muestra divisiones administrativas como provincias y fronteras", "grupo": "Representación de la Tierra",
         "tags": {"tipo_mapa": "Político"}},
        {"nombre": "Mapa temático", "img": f"{IMG}/mapa_tematico.jpeg",
         "funcion": "Muestra un tema específico como el clima o la población", "grupo": "Representación de la Tierra",
         "tags": {"tipo_mapa": "Temático"}},
        {"nombre": "Mapa de Costa Rica", "img": f"{IMG}/mapa_costa_rica.webp",
         "funcion": "Representa el territorio de Costa Rica con sus provincias y características", "grupo": "Representación de la Tierra"},

        # --- ELEMENTOS DEL MAPA ---
        {"nombre": "Rosa de los vientos", "img": f"{IMG}/rosa_de_los_vientos.webp",
         "funcion": "Símbolo en forma de estrella que señala los puntos cardinales", "grupo": "Elementos del mapa"},
        {"nombre": "Simbología", "img": f"{IMG}/simbologia_mapa.jpg",
         "funcion": "Representaciones gráficas que facilitan la comprensión del mapa", "grupo": "Elementos del mapa"},
        {"nombre": "Coordenadas geográficas", "img": f"{IMG}/coordenadas_geograficas.svg",
         "funcion": "Especifican la posición exacta de un lugar en el mapa", "grupo": "Elementos del mapa"},

        # --- ESCALAS ---
        {"nombre": "Escala numérica", "img": f"{IMG}/escala_numerica.png",
         "funcion": "Muestra la relación entre distancias del mapa y distancias reales con números (ej: 1:1 500 000)", "grupo": "Escalas del mapa",
         "tags": {"tipo_escala": "Numérica"}},
        {"nombre": "Escala cromática", "img": f"{IMG}/escala_cromatica.jpg",
         "funcion": "Usa colores para distinguir altitudes: verde para tierras bajas, marrón para elevadas", "grupo": "Escalas del mapa",
         "tags": {"tipo_escala": "Cromática"}},
        {"nombre": "Escala gráfica", "img": f"{IMG}/escala_grafica.jpg",
         "funcion": "Barra con divisiones que indica la escala usada para medir distancias en el mapa", "grupo": "Escalas del mapa",
         "tags": {"tipo_escala": "Gráfica"}},

        # --- PARALELOS Y MERIDIANOS ---
        {"nombre": "Paralelos", "img": f"{IMG}/paralelos.jpg",
         "funcion": "Líneas imaginarias que van de este a oeste y miden la latitud", "grupo": "Paralelos y meridianos"},
        {"nombre": "Meridianos", "img": f"{IMG}/meridianos.png",
         "funcion": "Líneas imaginarias que van de norte a sur y miden la longitud", "grupo": "Paralelos y meridianos"},
        {"nombre": "Ecuador", "img": f"{IMG}/ecuador.jpeg",
         "funcion": "Paralelo principal que divide la Tierra en Hemisferio Norte y Sur", "grupo": "Paralelos y meridianos"},
        {"nombre": "Meridiano de Greenwich", "img": f"{IMG}/meridiano_greenwich.jpg",
         "funcion": "Meridiano 0° que divide la Tierra en Hemisferio Oriental y Occidental", "grupo": "Paralelos y meridianos"},
        {"nombre": "Hemisferios", "img": f"{IMG}/hemisferios.jpg",
         "funcion": "Mitades de la Tierra divididas por el Ecuador (Norte/Sur) o Greenwich (Este/Oeste)", "grupo": "Paralelos y meridianos"},
        {"nombre": "Trópico de Cáncer", "img": f"{IMG}/tropico_cancer.jpg",
         "funcion": "Paralelo al norte del Ecuador que delimita la zona tropical norte", "grupo": "Paralelos y meridianos"},
        {"nombre": "Trópico de Capricornio", "img": f"{IMG}/tropico_capricornio.svg",
         "funcion": "Paralelo al sur del Ecuador que delimita la zona tropical sur", "grupo": "Paralelos y meridianos"},
        {"nombre": "Latitud y longitud", "img": f"{IMG}/latitud_longitud.png",
         "funcion": "Coordenadas que indican la posición exacta de un lugar en la Tierra", "grupo": "Paralelos y meridianos"},

        # --- LOCALIZACIÓN ---
        {"nombre": "Intersección de coordenadas", "img": f"{IMG}/interseccion_coordenadas.jpg",
         "funcion": "Método para ubicar un lugar usando el cruce de paralelo y meridiano", "grupo": "Localización geográfica"},
        {"nombre": "Cuadrantes del mapa", "img": f"{IMG}/cuadrantes_mapa.jpeg",
         "funcion": "Método para ubicar lugares dividiendo el mapa en secciones", "grupo": "Localización geográfica"},

        # --- BATALLA DE SANTA ROSA ---
        {"nombre": "Batalla de Santa Rosa", "img": f"{IMG}/batalla_santa_rosa.jpg",
         "funcion": "Victoria costarricense del 20 de marzo de 1856 contra los filibusteros", "grupo": "Batalla de Santa Rosa",
         "tipo_pregunta": "historia"},
        {"nombre": "William Walker", "img": f"{IMG}/william_walker.jpg",
         "funcion": "Líder filibustero de Tennessee que intentó anexar Centroamérica", "grupo": "Batalla de Santa Rosa",
         "tipo_pregunta": "historia"},
        {"nombre": "Campaña Nacional", "img": f"{IMG}/campana_nacional.png",
         "funcion": "Guerra de 1856-1857 en que Costa Rica defendió su soberanía", "grupo": "Batalla de Santa Rosa",
         "tipo_pregunta": "historia"},
        {"nombre": "Hacienda Santa Rosa", "img": f"{IMG}/hacienda_santa_rosa.jpg",
         "funcion": "Lugar donde se libró la Batalla de Santa Rosa en 1856", "grupo": "Batalla de Santa Rosa",
         "tipo_pregunta": "historia"},
    ],

    "preguntas": [
        # Representación de la Tierra
        {"tema": "Representación de la Tierra", "q": "¿Qué es un mapa?", "answer": "Dibujo que muestra la superficie de la Tierra en una hoja plana", "opciones": ["Dibujo que muestra la superficie de la Tierra en una hoja plana", "Una fotografía del planeta", "Un globo terráqueo", "Un libro de geografía"], "procedure": "Un mapa es un **dibujo plano** que representa la superficie terrestre."},
        {"tema": "Representación de la Tierra", "q": "¿Qué tipo de mapa muestra montañas, ríos y llanuras?", "answer": "Físico", "opciones": ["Físico", "Político", "Temático", "Histórico"], "procedure": "El mapa **físico** muestra el relieve: montañas, ríos y llanuras."},
        {"tema": "Representación de la Tierra", "q": "¿Qué tipo de mapa muestra provincias y fronteras?", "answer": "Político", "opciones": ["Físico", "Político", "Temático", "Climático"], "procedure": "El mapa **político** muestra divisiones administrativas."},
        {"tema": "Representación de la Tierra", "q": "¿Qué tipo de mapa muestra el clima de una región?", "answer": "Temático", "opciones": ["Físico", "Político", "Temático", "General"], "procedure": "El mapa **temático** muestra un tema específico como el clima."},
        {"tema": "Representación de la Tierra", "q": "¿Cómo se llama el mapa que muestra todo el planeta?", "answer": "Mapamundi", "opciones": ["Mapamundi", "Mapa físico", "Mapa político", "Atlas"], "procedure": "El **mapamundi** muestra todo el planeta Tierra."},

        # Elementos del mapa
        {"tema": "Elementos del mapa", "q": "¿Qué elemento del mapa señala los puntos cardinales?", "answer": "Rosa de los vientos", "opciones": ["Rosa de los vientos", "Simbología", "Escala", "Título"], "procedure": "La **rosa de los vientos** señala Norte, Sur, Este y Oeste."},
        {"tema": "Elementos del mapa", "q": "¿Qué elemento indica de qué trata el mapa?", "answer": "Título", "opciones": ["Título", "Escala", "Simbología", "Rosa de los vientos"], "procedure": "El **título** indica de qué trata el mapa y quién lo elaboró."},
        {"tema": "Elementos del mapa", "q": "¿Qué elemento del mapa explica el significado de los símbolos?", "answer": "Simbología", "opciones": ["Título", "Escala", "Simbología", "Coordenadas"], "procedure": "La **simbología** explica el significado de los símbolos del mapa."},
        {"tema": "Elementos del mapa", "q": "¿Cuántos puntos cardinales principales tiene la rosa de los vientos?", "answer": "4", "opciones": ["2", "4", "8", "16"], "procedure": "Los 4 puntos cardinales principales son: **Norte, Sur, Este y Oeste**."},
        {"tema": "Elementos del mapa", "q": "¿Qué elemento del mapa especifica la posición exacta de un lugar?", "answer": "Coordenadas geográficas", "opciones": ["Título", "Escala", "Simbología", "Coordenadas geográficas"], "procedure": "Las **coordenadas geográficas** especifican la posición exacta."},

        # Escalas
        {"tema": "Escalas del mapa", "q": "¿Qué tipo de escala usa colores para mostrar altitudes?", "answer": "Cromática", "opciones": ["Numérica", "Cromática", "Gráfica", "Física"], "procedure": "La escala **cromática** usa colores: verde para tierras bajas, marrón para elevadas."},
        {"tema": "Escalas del mapa", "q": "¿Qué tipo de escala usa números como 1:1 500 000?", "answer": "Numérica", "opciones": ["Numérica", "Cromática", "Gráfica", "Política"], "procedure": "La escala **numérica** usa números para indicar la proporción."},
        {"tema": "Escalas del mapa", "q": "¿Qué tipo de escala es una barra con divisiones?", "answer": "Gráfica", "opciones": ["Numérica", "Cromática", "Gráfica", "Temática"], "procedure": "La escala **gráfica** es una barra con divisiones para medir distancias."},
        {"tema": "Escalas del mapa", "q": "En la escala 1:1 500 000, ¿cuántos km reales representa 1 cm en el mapa?", "answer": "15 km", "opciones": ["1 km", "15 km", "150 km", "1500 km"], "procedure": "1 cm = 1 500 000 cm reales = **15 km** reales."},
        {"tema": "Escalas del mapa", "q": "¿Qué color representa las tierras bajas en la escala cromática?", "answer": "Verde", "opciones": ["Verde", "Marrón", "Azul", "Rojo"], "procedure": "En la escala cromática, el **verde** representa las tierras bajas (llanuras)."},

        # Paralelos y meridianos
        {"tema": "Paralelos y meridianos", "q": "¿En qué dirección van los paralelos?", "answer": "De este a oeste", "opciones": ["De norte a sur", "De este a oeste", "En diagonal", "De arriba a abajo"], "procedure": "Los paralelos van **de este a oeste** (horizontales)."},
        {"tema": "Paralelos y meridianos", "q": "¿En qué dirección van los meridianos?", "answer": "De norte a sur", "opciones": ["De norte a sur", "De este a oeste", "En diagonal", "De izquierda a derecha"], "procedure": "Los meridianos van **de norte a sur** (verticales)."},
        {"tema": "Paralelos y meridianos", "q": "¿Cómo se llama el paralelo más importante?", "answer": "Ecuador", "opciones": ["Ecuador", "Trópico de Cáncer", "Meridiano de Greenwich", "Trópico de Capricornio"], "procedure": "El paralelo más importante es el **Ecuador**."},
        {"tema": "Paralelos y meridianos", "q": "¿Qué mide la latitud?", "answer": "La distancia entre un punto y el Ecuador", "opciones": ["La distancia entre un punto y el Ecuador", "La distancia entre un punto y Greenwich", "La altura de las montañas", "El tamaño del país"], "procedure": "La **latitud** mide la distancia entre un punto y el Ecuador."},
        {"tema": "Paralelos y meridianos", "q": "¿Qué mide la longitud?", "answer": "La distancia entre un punto y el Meridiano de Greenwich", "opciones": ["La distancia entre un punto y el Ecuador", "La distancia entre un punto y el Meridiano de Greenwich", "La altura del terreno", "El ancho del país"], "procedure": "La **longitud** mide la distancia entre un punto y el Meridiano de Greenwich."},
        {"tema": "Paralelos y meridianos", "q": "¿En qué hemisferio está Costa Rica?", "answer": "Norte", "opciones": ["Norte", "Sur", "Este", "Oeste"], "procedure": "Costa Rica está en el **hemisferio norte**."},
        {"tema": "Paralelos y meridianos", "q": "¿Qué tipo de longitud usa Costa Rica?", "answer": "Longitud oeste", "opciones": ["Longitud este", "Longitud oeste", "Latitud norte", "Latitud sur"], "procedure": "Costa Rica usa **longitud oeste** por estar en el hemisferio occidental."},
        {"tema": "Paralelos y meridianos", "q": "¿Qué divide el Meridiano de Greenwich?", "answer": "Hemisferio Oriental y Occidental", "opciones": ["Hemisferio Norte y Sur", "Hemisferio Oriental y Occidental", "Trópico de Cáncer y Capricornio", "América y Europa"], "procedure": "El Meridiano de Greenwich divide la Tierra en **Hemisferio Oriental y Occidental**."},

        # Localización
        {"tema": "Localización geográfica", "q": "¿Cuáles son los dos métodos para localizar lugares en un mapa?", "answer": "Intersección de coordenadas y cuadrantes", "opciones": ["Intersección de coordenadas y cuadrantes", "Latitud y longitud", "Norte y sur", "Paralelos y meridianos"], "procedure": "Los dos métodos son: **intersección de coordenadas** y **cuadrantes**."},
        {"tema": "Localización geográfica", "q": "Al usar coordenadas, ¿qué se anota primero?", "answer": "El paralelo (latitud norte)", "opciones": ["El paralelo (latitud norte)", "El meridiano (longitud oeste)", "El nombre del país", "La escala"], "procedure": "Se anota primero el **paralelo (latitud norte)**, luego el meridiano."},
        {"tema": "Localización geográfica", "q": "¿Qué indica la latitud norte en Costa Rica?", "answer": "La distancia al norte del Ecuador", "opciones": ["La distancia al norte del Ecuador", "La distancia al sur del Ecuador", "La distancia a Greenwich", "La altura del terreno"], "procedure": "La **latitud norte** indica la distancia al norte del Ecuador."},

        # Batalla de Santa Rosa
        {"tema": "Batalla de Santa Rosa", "q": "¿Cuándo se conmemora la Batalla de Santa Rosa?", "answer": "20 de marzo", "opciones": ["15 de septiembre", "20 de marzo", "11 de abril", "25 de julio"], "procedure": "La Batalla de Santa Rosa se conmemora el **20 de marzo**."},
        {"tema": "Batalla de Santa Rosa", "q": "¿En qué año ocurrió la Batalla de Santa Rosa?", "answer": "1856", "opciones": ["1821", "1856", "1948", "1902"], "procedure": "La batalla ocurrió en **1856**."},
        {"tema": "Batalla de Santa Rosa", "q": "¿Quién lideraba el ejército filibustero?", "answer": "William Walker", "opciones": ["William Walker", "Juan Santamaría", "Braulio Carrillo", "José Figueres"], "procedure": "El ejército filibustero era liderado por **William Walker**."},
        {"tema": "Batalla de Santa Rosa", "q": "¿De dónde era originario William Walker?", "answer": "Tennessee, Estados Unidos", "opciones": ["Tennessee, Estados Unidos", "Nicaragua", "México", "Inglaterra"], "procedure": "William Walker era de **Tennessee, Estados Unidos**."},
        {"tema": "Batalla de Santa Rosa", "q": "¿Cómo se llama la guerra de la que fue parte la Batalla de Santa Rosa?", "answer": "Campaña Nacional", "opciones": ["Campaña Nacional", "Guerra de Independencia", "Revolución del 48", "Guerra Fría"], "procedure": "Fue parte de la **Campaña Nacional de 1856-1857**."},
        {"tema": "Batalla de Santa Rosa", "q": "¿Qué pretendía hacer William Walker con Centroamérica?", "answer": "Anexarla a una confederación de estados sureños", "opciones": ["Anexarla a una confederación de estados sureños", "Liberarla de España", "Crear un nuevo país", "Establecer comercio"], "procedure": "Walker quería **anexar Centroamérica** a una confederación de estados sureños de EE.UU."},
    ],

    "verdadero_falso": [
        {"tema": "Representación de la Tierra", "afirmacion": "¿Un mapa físico muestra las provincias de un país?", "correcto": False, "explicacion": "**Falso**. Las provincias las muestra el mapa **político**."},
        {"tema": "Representación de la Tierra", "afirmacion": "¿Los mapas sirven para planificar viajes?", "correcto": True, "explicacion": "**Verdadero**. Una de las utilidades del mapa es planificar viajes."},
        {"tema": "Elementos del mapa", "q": "¿La rosa de los vientos tiene 8 puntos en total?", "afirmacion": "¿La rosa de los vientos tiene 8 puntos en total?", "correcto": True, "explicacion": "**Verdadero**. Tiene 4 principales (N,S,E,O) y 4 intermedios (NE,NO,SE,SO)."},
        {"tema": "Escalas del mapa", "afirmacion": "¿La escala cromática usa colores para mostrar altitudes?", "correcto": True, "explicacion": "**Verdadero**. Verde = tierras bajas, marrón = tierras elevadas."},
        {"tema": "Escalas del mapa", "afirmacion": "¿La escala numérica 1:1 500 000 significa que 1 cm = 1 km real?", "correcto": False, "explicacion": "**Falso**. 1 cm = **15 km** reales."},
        {"tema": "Paralelos y meridianos", "afirmacion": "¿El Ecuador divide la Tierra en Hemisferio Norte y Sur?", "correcto": True, "explicacion": "**Verdadero**. El Ecuador es el paralelo que divide los hemisferios."},
        {"tema": "Paralelos y meridianos", "afirmacion": "¿Costa Rica está en el hemisferio sur?", "correcto": False, "explicacion": "**Falso**. Costa Rica está en el **hemisferio norte**."},
        {"tema": "Paralelos y meridianos", "afirmacion": "¿Los meridianos van de este a oeste?", "correcto": False, "explicacion": "**Falso**. Los meridianos van de **norte a sur**. Los que van de este a oeste son los paralelos."},
        {"tema": "Paralelos y meridianos", "afirmacion": "¿La latitud mide la distancia al Ecuador?", "correcto": True, "explicacion": "**Verdadero**."},
        {"tema": "Batalla de Santa Rosa", "afirmacion": "¿La Batalla de Santa Rosa ocurrió en 1856?", "correcto": True, "explicacion": "**Verdadero**. Fue el 20 de marzo de 1856."},
        {"tema": "Batalla de Santa Rosa", "afirmacion": "¿William Walker era costarricense?", "correcto": False, "explicacion": "**Falso**. Era de **Tennessee, Estados Unidos**."},
        {"tema": "Batalla de Santa Rosa", "afirmacion": "¿Costa Rica ganó la Batalla de Santa Rosa?", "correcto": True, "explicacion": "**Verdadero**. Costa Rica venció a los filibusteros."},
    ],

    "secuencias": [
        {"tema": "Localización geográfica", "nombre": "los pasos para localizar un lugar por coordenadas",
         "orden": ["Identificar el lugar", "Determinar el paralelo (latitud)", "Determinar el meridiano (longitud)", "Anotar latitud norte", "Anotar longitud oeste"]},
    ],
}
