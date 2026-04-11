"""Datos de Estudios Sociales para Tyler (6to año) — Historia antigua de Costa Rica."""

DATA = {
    "topics": {
        "Periodos de la historia de Costa Rica": {
            "aprendizaje": "Identificar los periodos de la historia de Costa Rica y sus características",
            "indicador": "Ubica temporalmente los periodos históricos de Costa Rica",
        },
        "Fase cazadores y recolectores": {
            "aprendizaje": "Comprender las características de la fase cazadores-recolectores",
            "indicador": "Identifica características de los grupos nómadas y sus herramientas",
        },
        "Fase agricultores tempranos": {
            "aprendizaje": "Comprender el paso del nomadismo a la sedentarización",
            "indicador": "Identifica características de los agricultores tempranos y sus técnicas",
        },
        "Fase cacicazgos iniciales": {
            "aprendizaje": "Identificar la organización social de los cacicazgos",
            "indicador": "Reconoce roles del cacique, chamán, agricultores y artesanos",
        },
        "Fase sociedad cacical": {
            "aprendizaje": "Comprender la organización de la sociedad cacical",
            "indicador": "Identifica jerarquía social y características de aldeas principales y secundarias",
        },
        "Etnias de la Costa Rica antigua": {
            "aprendizaje": "Identificar las etnias antiguas de Costa Rica y sus regiones",
            "indicador": "Reconoce etnias por región arqueológica y sus características",
        },
        "Áreas culturales de América": {
            "aprendizaje": "Identificar las áreas culturales de América y sus características",
            "indicador": "Ubica y describe las áreas Mesoamericana, Intermedia y Andina",
        },
    },

    "tags": {
        "fase": ["Cazadores-recolectores", "Agricultores tempranos", "Cacicazgos iniciales", "Sociedad cacical"],
        "area_cultural": ["Mesoamericana", "Intermedia", "Andina"],
        "region_cr": ["Gran Nicoya", "Central", "Subregión Diquís"],
    },

    "partes": [
        # --- FASES HISTÓRICAS ---
        {"nombre": "Fase cazadores-recolectores", "img": "socialestyler/fasecazadoresyrecolectores.jpg",
         "funcion": "10 000 – 2000 a.C. Grupos nómadas que cazaban y recolectaban alimentos", "grupo": "Periodos de la historia de Costa Rica"},
        {"nombre": "Fase agricultores tempranos", "img": "socialestyler/Faseagricultorestempranos.jpg",
         "funcion": "2000 – 300 a.C. Inicio de la sedentarización y la agricultura", "grupo": "Periodos de la historia de Costa Rica"},
        {"nombre": "Fase cacicazgos iniciales", "img": "socialestyler/fasecacicazgosiniciales.jpg",
         "funcion": "300 a.C. – 800 d.C. Surgimiento de cacicazgos y organización social", "grupo": "Periodos de la historia de Costa Rica"},
        {"nombre": "Fase sociedad cacical", "img": "socialestyler/fasesociedadcacical.png",
         "funcion": "800 – 1502 d.C. Aldeas principales y secundarias, señoríos", "grupo": "Periodos de la historia de Costa Rica"},

        # --- CAZADORES Y RECOLECTORES ---
        {"nombre": "Nómadas", "img": "socialestyler/nomadas.jpg",
         "funcion": "Grupos que se trasladaban de un lugar a otro en busca de alimento", "grupo": "Fase cazadores y recolectores"},
        {"nombre": "Caza de animales", "img": "socialestyler/cazadeanimales.jpg",
         "funcion": "Los nómadas cazaban megafauna como mastodontes y perezosos gigantes", "grupo": "Fase cazadores y recolectores"},
        {"nombre": "Recolección de frutos", "img": "socialestyler/recolecciondefrutos.jpg",
         "funcion": "Los nómadas recolectaban frutos silvestres para alimentarse", "grupo": "Fase cazadores y recolectores"},
        {"nombre": "Pesca", "img": "socialestyler/pesca.png",
         "funcion": "La pesca era una actividad importante para la alimentación de los grupos nómadas", "grupo": "Fase cazadores y recolectores"},

        # --- AGRICULTORES TEMPRANOS ---
        {"nombre": "Sedentarios", "img": "socialestyler/sedentarios.jpg",
         "funcion": "Grupos que se establecieron en un lugar fijo gracias a la agricultura", "grupo": "Fase agricultores tempranos"},
        {"nombre": "Agricultura indígena", "img": "socialestyler/agriculturaindigena.webp",
         "funcion": "Los agricultores tempranos aprendieron a cultivar la tierra", "grupo": "Fase agricultores tempranos"},
        {"nombre": "Roza y quema", "img": "socialestyler/rozayquema.jpg",
         "funcion": "Técnica de cultivo que consistía en cortar árboles y quemarlos para fertilizar el suelo", "grupo": "Fase agricultores tempranos"},
        {"nombre": "Yuca, camote y papa", "img": "socialestyler/yucacamoteypapa.jpg",
         "funcion": "Tubérculos cultivados en la vegecultura (agricultura de raíces)", "grupo": "Fase agricultores tempranos"},
        {"nombre": "Las tribus", "img": "socialestyler/lastribus.jpg",
         "funcion": "Comunidades más grandes que los clanes, con relaciones igualitarias", "grupo": "Fase agricultores tempranos"},

        # --- CACICAZGOS INICIALES ---
        {"nombre": "El cacique", "img": "socialestyler/cacique.jpg",
         "funcion": "Líder que administraba cosechas, establecía relaciones políticas y comerciales", "grupo": "Fase cacicazgos iniciales"},
        {"nombre": "El chamán", "img": "socialestyler/chaman.jpg",
         "funcion": "Intermediario entre los dioses y los indígenas, poder hereditario", "grupo": "Fase cacicazgos iniciales"},
        {"nombre": "Los artesanos", "img": "socialestyler/artesanos.avif",
         "funcion": "Elaboraban objetos de cerámica y herramientas de piedra como metates", "grupo": "Fase cacicazgos iniciales"},
        {"nombre": "Maíz, frijoles y chile", "img": "socialestyler/maizfrijolesychile.jpg",
         "funcion": "Semillas cultivadas en la semicultura, principal actividad de los agricultores", "grupo": "Fase cacicazgos iniciales"},
        {"nombre": "Aldeas", "img": "socialestyler/aldeascostarica.webp",
         "funcion": "Pequeños pueblos donde se realizaban actividades religiosas, artesanales y comerciales", "grupo": "Fase cacicazgos iniciales"},

        # --- SOCIEDAD CACICAL ---
        {"nombre": "Jerarquía social", "img": "socialestyler/jerarquiasocial.jpg",
         "funcion": "Organización social: cacique y chamán, guerreros, artesanos y agricultores", "grupo": "Fase sociedad cacical"},
        {"nombre": "Guerreros indígenas", "img": "socialestyler/guerrerosindigenas.jpg",
         "funcion": "Clase social que surgió en el señorío para proteger y defender el territorio", "grupo": "Fase sociedad cacical"},
        {"nombre": "Calzadas de Guayabo", "img": "socialestyler/calzadas de guayabo zona arqueologica region central costa rica.jpg",
         "funcion": "Calzadas del monumento nacional Guayabo, similares a las culturas andinas y mesoamericanas", "grupo": "Fase sociedad cacical"},

        # --- ÁREAS CULTURALES ---
        {"nombre": "Área Mesoamericana", "img": "socialestyler/mesoamerica.png",
         "funcion": "Comprende México, Guatemala, Belice, El Salvador, Honduras, oeste de Nicaragua y noroeste de Costa Rica", "grupo": "Áreas culturales de América"},
        {"nombre": "Área Intermedia", "img": "socialestyler/areaintermedia.png",
         "funcion": "Abarca Costa Rica, Panamá, Colombia, Venezuela y las islas del Caribe", "grupo": "Áreas culturales de América"},
        {"nombre": "Área Andina", "img": "socialestyler/areaandina.png",
         "funcion": "Abarca Ecuador, Perú, Bolivia y parte de Chile y Argentina", "grupo": "Áreas culturales de América"},
        {"nombre": "Mapa áreas culturales", "img": "socialestyler/areasculturalesdeamericatraenumeros1mesoamerica2intermedia3andina.jpg",
         "funcion": "Las tres áreas culturales de América: 1-Mesoamericana, 2-Intermedia, 3-Andina", "grupo": "Áreas culturales de América"},
        {"nombre": "Cultivo en terrazas", "img": "socialestyler/cultivoenterraza.webp",
         "funcion": "Técnica andina de cultivo en estructuras tipo gradas rellenas con tierra fértil", "grupo": "Áreas culturales de América"},
        {"nombre": "Llama domesticada", "img": "socialestyler/llamadomesticada.jpg",
         "funcion": "Animal domesticado por los andinos para llevar carga", "grupo": "Áreas culturales de América"},
        {"nombre": "Cerámica polícroma", "img": "socialestyler/ceramicapolicroma.jpg",
         "funcion": "Cerámica de varios colores característica del área mesoamericana", "grupo": "Áreas culturales de América"},
        {"nombre": "Navegación área intermedia", "img": "socialestyler/navegacionantiguaareaintermedia.webp",
         "funcion": "La pesca impulsó el desarrollo de la navegación en el área intermedia", "grupo": "Áreas culturales de América"},

        # --- ETNIAS DE COSTA RICA ---
        {"nombre": "Región Gran Nicoya", "img": "socialestyler/ceramicagrannicoya.jpg",
         "funcion": "Región noroeste con influencia mesoamericana, etnias chorotega, nahua, corobicí", "grupo": "Etnias de la Costa Rica antigua"},
        {"nombre": "Región Central", "img": "socialestyler/rojo la gran nicoya verde la central y amarillo subregion diquis mapa tematico imagen.png",
         "funcion": "Región más extensa, influencia de las tres áreas culturales, etnias maleku y huetar", "grupo": "Etnias de la Costa Rica antigua"},
        {"nombre": "Subregión Diquís", "img": "socialestyler/suregion diquis imagen mapa tematico sale en color amerillo.png",
         "funcion": "Desde Quepos hasta Panamá, influencia andina, etnias cabécar, bribri y brunca", "grupo": "Etnias de la Costa Rica antigua"},
        {"nombre": "Esferas de piedra", "img": "socialestyler/esferasdepierdra subregion diquis.jpg",
         "funcion": "Objetos de piedra elaborados por los indígenas de la subregión Diquís", "grupo": "Etnias de la Costa Rica antigua"},
        {"nombre": "Ornamentos de jade Gran Nicoya", "img": "socialestyler/ornamentosjade gran nicoya.JPG",
         "funcion": "Objetos de jade encontrados en la región Gran Nicoya que simbolizaban rango social", "grupo": "Etnias de la Costa Rica antigua"},
    ],

    "preguntas": [
        # Periodos de la historia
        {"tema": "Periodos de la historia de Costa Rica", "q": "¿En qué año llegaron los primeros pobladores a Costa Rica?", "answer": "10 000 a.C.", "opciones": ["10 000 a.C.", "1502 d.C.", "2000 a.C.", "800 d.C."], "procedure": "Los primeros pobladores llegaron alrededor del **10 000 a.C.**"},
        {"tema": "Periodos de la historia de Costa Rica", "q": "¿Cuándo llegó Cristóbal Colón a Costa Rica?", "answer": "1502 d.C.", "opciones": ["1492 d.C.", "1502 d.C.", "1575 d.C.", "1821 d.C."], "procedure": "Cristóbal Colón llegó en **1502 d.C.**"},
        {"tema": "Periodos de la historia de Costa Rica", "q": "¿Cuántos periodos tiene la historia de Costa Rica?", "answer": "5", "opciones": ["3", "4", "5", "6"], "procedure": "La historia de Costa Rica se divide en **5 periodos**." },
        {"tema": "Periodos de la historia de Costa Rica", "q": "¿Cuál es el periodo más extenso de la historia de Costa Rica?", "answer": "Antiguo o Precolombino", "opciones": ["Conquista", "Colonial", "Antiguo o Precolombino", "Republicano"], "procedure": "El periodo **Antiguo o Precolombino** es el más extenso (10 000 a.C. – 1502 d.C.)."},
        {"tema": "Periodos de la historia de Costa Rica", "q": "¿En qué año se independizó Costa Rica de España?", "answer": "1821", "opciones": ["1502", "1575", "1821", "1948"], "procedure": "Costa Rica se independizó en **1821**."},
        {"tema": "Periodos de la historia de Costa Rica", "q": "¿Cuántas fases tiene el periodo Antiguo de Costa Rica?", "answer": "4", "opciones": ["2", "3", "4", "5"], "procedure": "El periodo Antiguo se subdivide en **4 fases**."},
        {"tema": "Periodos de la historia de Costa Rica", "q": "¿Cuál fue la primera fase del periodo Antiguo?", "answer": "Cazadores-recolectores", "opciones": ["Agricultores tempranos", "Cazadores-recolectores", "Cacicazgos iniciales", "Sociedad cacical"], "procedure": "La primera fase fue la de **cazadores-recolectores** (10 000 – 2000 a.C.)."},

        # Cazadores y recolectores
        {"tema": "Fase cazadores y recolectores", "q": "¿Cómo se llamaban los grupos que se trasladaban en busca de alimento?", "answer": "Nómadas", "opciones": ["Nómadas", "Sedentarios", "Caciques", "Artesanos"], "procedure": "Se llamaban **nómadas**."},
        {"tema": "Fase cazadores y recolectores", "q": "¿Cómo se llamaban los grupos de 20 a 30 individuos con lazos familiares?", "answer": "Clanes", "opciones": ["Tribus", "Clanes", "Cacicazgos", "Señoríos"], "procedure": "Se llamaban **clanes** o bandas."},
        {"tema": "Fase cazadores y recolectores", "q": "¿De qué materiales fabricaban herramientas los nómadas?", "answer": "Piedra, hueso y madera", "opciones": ["Piedra, hueso y madera", "Oro y plata", "Barro y arcilla", "Hierro y cobre"], "procedure": "Fabricaban herramientas de **piedra, hueso y madera**."},
        {"tema": "Fase cazadores y recolectores", "q": "¿Cómo se llamaban los animales grandes que cazaban los nómadas?", "answer": "Megafauna", "opciones": ["Megafauna", "Microfauna", "Fauna marina", "Fauna doméstica"], "procedure": "Se llamaba **megafauna** (mastodontes, perezosos gigantes)."},
        {"tema": "Fase cazadores y recolectores", "q": "¿Cuál era la base de la alimentación de los nómadas?", "answer": "Caza, pesca y recoleción", "opciones": ["Caza, pesca y recolección", "Agricultura y ganadería", "Comercio y artesanias", "Pesca y cerámica"], "procedure": "Su alimentación se basaba en **caza, pesca y recolección**."},

        # Agricultores tempranos
        {"tema": "Fase agricultores tempranos", "q": "¿Cómo se llama el proceso de establecerse en un lugar fijo?", "answer": "Sedentarización", "opciones": ["Sedentarización", "Nomadismo", "Migración", "Colonización"], "procedure": "El proceso se llama **sedentarización**."},
        {"tema": "Fase agricultores tempranos", "q": "¿Qué técnica de cultivo usaban los agricultores tempranos?", "answer": "Roza y quema", "opciones": ["Roza y quema", "Cultivo en terrazas", "Riego artificial", "Semicultura"], "procedure": "Usaban la técnica de **roza y quema**."},
        {"tema": "Fase agricultores tempranos", "q": "¿Cómo se llama la agricultura de tubérculos como yuca y camote?", "answer": "Vegecultura", "opciones": ["Vegecultura", "Semicultura", "Horticultura", "Agricultura extensiva"], "procedure": "Se llama **vegecultura**."},
        {"tema": "Fase agricultores tempranos", "q": "¿Qué tipo de comunidad surgió gracias a la agricultura?", "answer": "Tribus", "opciones": ["Tribus", "Clanes", "Cacicazgos", "Señoríos"], "procedure": "Surgieron las **tribus**, comunidades más grandes que los clanes."},
        {"tema": "Fase agricultores tempranos", "q": "¿Qué objetos de barro se elaboraron por primera vez en esta fase?", "answer": "Cerámica", "opciones": ["Cerámica", "Objetos de jade", "Herramientas de hierro", "Objetos de oro"], "procedure": "Se inició la elaboración de **cerámica**."},

        # Cacicazgos iniciales
        {"tema": "Fase cacicazgos iniciales", "q": "¿Quién administraba las cosechas y establecía relaciones políticas?", "answer": "El cacique", "opciones": ["El cacique", "El chamán", "El guerrero", "El artesano"], "procedure": "**El cacique** administraba las cosechas y relaciones políticas."},
        {"tema": "Fase cacicazgos iniciales", "q": "¿Quién era el intermediario entre los dioses y los indígenas?", "answer": "El chamán", "opciones": ["El cacique", "El chamán", "El guerrero", "El artesano"], "procedure": "**El chamán** era el intermediario espiritual."},
        {"tema": "Fase cacicazgos iniciales", "q": "¿Cómo se llama la agricultura de semillas como maíz y frijoles?", "answer": "Semicultura", "opciones": ["Vegecultura", "Semicultura", "Horticultura", "Roza y quema"], "procedure": "Se llama **semicultura**."},
        {"tema": "Fase cacicazgos iniciales", "q": "¿Cómo se llamaban los pequeños pueblos de los cacicazgos?", "answer": "Aldeas", "opciones": ["Aldeas", "Ciudades", "Tribus", "Clanes"], "procedure": "Se llamaban **aldeas**."},

        # Sociedad cacical
        {"tema": "Fase sociedad cacical", "q": "¿Cómo se llamaba el gobierno de un cacique principal sobre varios cacicazgos?", "answer": "Señorío", "opciones": ["Señorío", "Cacicazgo", "Tribu", "Clan"], "procedure": "Se llamaba **señorío**."},
        {"tema": "Fase sociedad cacical", "q": "¿Qué clase social surgió en el señorío para defender el territorio?", "answer": "Guerreros", "opciones": ["Guerreros", "Artesanos", "Agricultores", "Chamanes"], "procedure": "Surgieron los **guerreros**."},
        {"tema": "Fase sociedad cacical", "q": "¿Qué producto fue el más importante en la sociedad cacical?", "answer": "Maíz", "opciones": ["Maíz", "Yuca", "Cacao", "Frijol"], "procedure": "El **maíz** fue el producto más destacado."},
        {"tema": "Fase sociedad cacical", "q": "¿Dónde enterraban a sus familiares los indígenas?", "answer": "Tumbas de piedra en cerros o cerca de ríos", "opciones": ["Tumbas de piedra en cerros o cerca de ríos", "Bajo las casas", "En el mar", "En los bosques"], "procedure": "Los enterraban en **tumbas de piedra** en partes altas o cerca de ríos."},

        # Áreas culturales
        {"tema": "Áreas culturales de América", "q": "¿Cuántas áreas culturales principales tiene América?", "answer": "3", "opciones": ["2", "3", "4", "5"], "procedure": "Hay **3 áreas culturales**: Mesoamericana, Intermedia y Andina."},
        {"tema": "Áreas culturales de América", "q": "¿Qué área cultural comprende México, Guatemala y el noroeste de Costa Rica?", "answer": "Mesoamericana", "opciones": ["Mesoamericana", "Intermedia", "Andina", "Caribe"], "procedure": "El área **Mesoamericana**."},
        {"tema": "Áreas culturales de América", "q": "¿Qué área cultural abarca Perú, Bolivia y Ecuador?", "answer": "Andina", "opciones": ["Mesoamericana", "Intermedia", "Andina", "Caribe"], "procedure": "El área **Andina**."},
        {"tema": "Áreas culturales de América", "q": "¿En qué área cultural se ubica la mayor parte de Costa Rica?", "answer": "Intermedia", "opciones": ["Mesoamericana", "Intermedia", "Andina"], "procedure": "La mayor parte de Costa Rica está en el área **Intermedia**."},
        {"tema": "Áreas culturales de América", "q": "¿Qué técnica de cultivo usaban los andinos?", "answer": "Cultivo en terrazas", "opciones": ["Cultivo en terrazas", "Roza y quema", "Vegecultura", "Semicultura"], "procedure": "Los andinos usaban el **cultivo en terrazas**."},
        {"tema": "Áreas culturales de América", "q": "¿Qué animal domesticaron los andinos para llevar carga?", "answer": "Llama", "opciones": ["Llama", "Caballo", "Perro", "Jaguar"], "procedure": "Domesticaron la **llama**."},
        {"tema": "Áreas culturales de América", "q": "¿Qué etnias habitaron el área mesoamericana?", "answer": "Olmecas, aztecas y mayas", "opciones": ["Olmecas, aztecas y mayas", "Tainos y caribes", "Incas y mochicas", "Chorotegas y huetares"], "procedure": "**Olmecas, zapotecas, aztecas y mayas**."},
        {"tema": "Áreas culturales de América", "q": "¿Qué etnias habitaron el área andina?", "answer": "Incas y mochicas", "opciones": ["Olmecas y mayas", "Taínos y caribes", "Incas y mochicas", "Chorotegas y huetares"], "procedure": "**Mochica, nazca, incas y araucana**."},

        # Áreas culturales - países
        {"tema": "Áreas culturales de América", "q": "¿México pertenece al área cultural Mesoamericana?", "answer": "Sí", "opciones": ["Sí", "No"], "procedure": "**Sí**, México es parte del área Mesoamericana."},
        {"tema": "Áreas culturales de América", "q": "¿Guatemala pertenece al área cultural Mesoamericana?", "answer": "Sí", "opciones": ["Sí", "No"], "procedure": "**Sí**, Guatemala es parte del área Mesoamericana."},
        {"tema": "Áreas culturales de América", "q": "¿Perú pertenece al área cultural Andina?", "answer": "Sí", "opciones": ["Sí", "No"], "procedure": "**Sí**, Perú es parte del área Andina."},
        {"tema": "Áreas culturales de América", "q": "¿Panamá pertenece al área cultural Intermedia?", "answer": "Sí", "opciones": ["Sí", "No"], "procedure": "**Sí**, Panamá es parte del área Intermedia."},
        {"tema": "Áreas culturales de América", "q": "¿A qué área cultural pertenece México?", "answer": "Mesoamericana", "opciones": ["Mesoamericana", "Intermedia", "Andina"], "procedure": "México pertenece al área **Mesoamericana**."},
        {"tema": "Áreas culturales de América", "q": "¿A qué área cultural pertenece Perú?", "answer": "Andina", "opciones": ["Mesoamericana", "Intermedia", "Andina"], "procedure": "Perú pertenece al área **Andina**."},
        {"tema": "Áreas culturales de América", "q": "¿A qué área cultural pertenece Venezuela?", "answer": "Intermedia", "opciones": ["Mesoamericana", "Intermedia", "Andina"], "procedure": "Venezuela pertenece al área **Intermedia**."},
        {"tema": "Áreas culturales de América", "q": "¿A qué área cultural pertenece Bolivia?", "answer": "Andina", "opciones": ["Mesoamericana", "Intermedia", "Andina"], "procedure": "Bolivia pertenece al área **Andina**."},
        {"tema": "Áreas culturales de América", "q": "¿A qué área cultural pertenece Honduras?", "answer": "Mesoamericana", "opciones": ["Mesoamericana", "Intermedia", "Andina"], "procedure": "Honduras pertenece al área **Mesoamericana** (aunque su costa caribe es Intermedia)."},
        {"tema": "Áreas culturales de América", "q": "¿A qué área cultural pertenece Ecuador?", "answer": "Andina", "opciones": ["Mesoamericana", "Intermedia", "Andina"], "procedure": "Ecuador pertenece al área **Andina**."},
        {"tema": "Áreas culturales de América", "q": "¿A qué área cultural pertenece Colombia?", "answer": "Intermedia", "opciones": ["Mesoamericana", "Intermedia", "Andina"], "procedure": "Colombia (costa caribeña) pertenece al área **Intermedia**. El suroeste es Andina."},
        {"tema": "Áreas culturales de América", "q": "¿Qué países forman parte del área Mesoamericana?", "answer": "México, Guatemala, Belice, El Salvador, Honduras, oeste de Nicaragua y noroeste de Costa Rica", "opciones": ["México, Guatemala, Belice, El Salvador, Honduras, oeste de Nicaragua y noroeste de Costa Rica", "Perú, Bolivia, Ecuador y Chile", "Panamá, Colombia, Venezuela y las islas del Caribe", "Solo México y Guatemala"], "procedure": "El área Mesoamericana comprende: **México, Guatemala, Belice, El Salvador, Honduras, oeste de Nicaragua y noroeste de Costa Rica**."},
        {"tema": "Áreas culturales de América", "q": "¿Qué países forman parte del área Andina?", "answer": "Ecuador, Perú, Bolivia, parte de Chile y Argentina", "opciones": ["Ecuador, Perú, Bolivia, parte de Chile y Argentina", "México, Guatemala y Belice", "Panamá, Colombia y Venezuela", "Solo Perú y Bolivia"], "procedure": "El área Andina comprende: **Ecuador, Perú, Bolivia, parte de Chile y Argentina** (y el suroeste de Colombia)."},
        {"tema": "Áreas culturales de América", "q": "¿Qué países forman parte del área Intermedia?", "answer": "Costa Rica, Panamá, Colombia, Venezuela y las islas del Caribe", "opciones": ["Costa Rica, Panamá, Colombia, Venezuela y las islas del Caribe", "México, Guatemala y Belice", "Perú, Bolivia y Ecuador", "Solo Panamá y Colombia"], "procedure": "El área Intermedia comprende: **Costa Rica, Panamá, Colombia, Venezuela y las islas del Caribe** (y la costa caribeña de Honduras y Nicaragua)."},

        # Etnias de Costa Rica
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿En cuántas regiones arqueológicas se divide Costa Rica?", "answer": "3", "opciones": ["2", "3", "4", "5"], "procedure": "Se divide en **3 regiones**: Gran Nicoya, Central y Subregion Diquís."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Cuál es la etnia más antigua de Costa Rica?", "answer": "Chorotega", "opciones": ["Chorotega", "Huetar", "Bribri", "Maleku"], "procedure": "La etnia **chorotega** es la más antigua de Costa Rica."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Qué influencia cultural recibió la región Gran Nicoya?", "answer": "Mesoamericana", "opciones": ["Mesoamericana", "Andina", "Intermedia", "Caribe"], "procedure": "Recibió influencia **mesoamericana**."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Qué influencia cultural recibió la subregión Diquís?", "answer": "Andina", "opciones": ["Mesoamericana", "Andina", "Intermedia", "Caribe"], "procedure": "Recibió influencia **andina**."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Qué objetos famosos se encontraron en la subregión Diquís?", "answer": "Esferas de piedra", "opciones": ["Esferas de piedra", "Pirámides", "Momias", "Acueductos"], "procedure": "Se encontraron **esferas de piedra**."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Qué etnias habitaron la región Gran Nicoya?", "answer": "Chorotega y nahua", "opciones": ["Chorotega y nahua", "Maleku y huetar", "Bribri y cabécar", "Brunca y boruca"], "procedure": "**Chorotega, nahua, corobicí, nicarao y chondal**."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Qué etnias habitaron la subregión Diquís?", "answer": "Bribri y cabécar", "opciones": ["Chorotega y nahua", "Maleku y huetar", "Bribri y cabécar", "Nicarao y chondal"], "procedure": "**Cabécares, bribris y bruncas**."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Cuántos habitantes se estima que había en Costa Rica antes de 1502?", "answer": "400 000", "opciones": ["100 000", "200 000", "400 000", "1 000 000"], "procedure": "Se estima que había **400 000 habitantes** antes de 1502."},

        # Etnias - a qué región pertenecen
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Los **Chorotegas** pertenecen a qué región arqueológica?", "answer": "Gran Nicoya", "opciones": ["Gran Nicoya", "Región Central", "Subregión Diquís"], "procedure": "Los **chorotegas** pertenecen a la región **Gran Nicoya**."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Los **Bribris** pertenecen a qué región arqueológica?", "answer": "Subregión Diquís", "opciones": ["Gran Nicoya", "Región Central", "Subregión Diquís"], "procedure": "Los **bribris** pertenecen a la **subregión Diquís**."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Los **Malekus** pertenecen a qué región arqueológica?", "answer": "Región Central", "opciones": ["Gran Nicoya", "Región Central", "Subregión Diquís"], "procedure": "Los **malekus** pertenecen a la **región Central**."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Los **Huetares** pertenecen a qué región arqueológica?", "answer": "Región Central", "opciones": ["Gran Nicoya", "Región Central", "Subregión Diquís"], "procedure": "Los **huetares** pertenecen a la **región Central**."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Los **Cabécares** pertenecen a qué región arqueológica?", "answer": "Subregión Diquís", "opciones": ["Gran Nicoya", "Región Central", "Subregión Diquís"], "procedure": "Los **cabécares** pertenecen a la **subregión Diquís**."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Los **Nicaraos** pertenecen a qué región arqueológica?", "answer": "Gran Nicoya", "opciones": ["Gran Nicoya", "Región Central", "Subregión Diquís"], "procedure": "Los **nicaraos** pertenecen a la región **Gran Nicoya**."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Los **Bruncas** pertenecen a qué región arqueológica?", "answer": "Subregión Diquís", "opciones": ["Gran Nicoya", "Región Central", "Subregión Diquís"], "procedure": "Los **bruncas** pertenecen a la **subregión Diquís**."},

        # Etnias - influencia cultural
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Qué influencia cultural recibieron los **Chorotegas**?", "answer": "Mesoamericana", "opciones": ["Mesoamericana", "Andina", "Intermedia"], "procedure": "Los chorotegas recibieron influencia **mesoamericana** (idioma náhuatl, cerámica)."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Qué influencia cultural recibieron los **Bribris**?", "answer": "Andina", "opciones": ["Mesoamericana", "Andina", "Intermedia"], "procedure": "Los bribris recibieron influencia **andina** (trabajo en oro y piedra)."},
        {"tema": "Etnias de la Costa Rica antigua", "q": "¿Qué influencia cultural recibió la **Región Central**?", "answer": "Las tres áreas culturales", "opciones": ["Solo mesoamericana", "Solo andina", "Las tres áreas culturales"], "procedure": "La región Central recibió influencia de las **tres áreas culturales**."},
    ],

    "verdadero_falso": [
        {"tema": "Periodos de la historia de Costa Rica", "afirmacion": "¿El periodo Antiguo termina con la llegada de Cristóbal Colón en 1502?", "correcto": True, "explicacion": "**Verdadero**. El periodo Antiguo va de 10 000 a.C. a 1502 d.C."},
        {"tema": "Periodos de la historia de Costa Rica", "afirmacion": "¿El periodo Contemporáneo comenzó con la independencia de España?", "correcto": False, "explicacion": "**Falso**. El Contemporáneo comenzó en **1948** con la guerra civil."},
        {"tema": "Fase cazadores y recolectores", "afirmacion": "¿Los cazadores-recolectores eran nómadas?", "correcto": True, "explicacion": "**Verdadero**. Se trasladaban en busca de alimento."},
        {"tema": "Fase cazadores y recolectores", "afirmacion": "¿Los nómadas practicaban la agricultura?", "correcto": False, "explicacion": "**Falso**. La agricultura surgió en la fase de **agricultores tempranos**."},
        {"tema": "Fase agricultores tempranos", "afirmacion": "¿La roza y quema consiste en quemar árboles para fertilizar el suelo?", "correcto": True, "explicacion": "**Verdadero**. Las cenizas sirven como fertilizante."},
        {"tema": "Fase agricultores tempranos", "afirmacion": "¿Las tribus eran más pequeñas que los clanes?", "correcto": False, "explicacion": "**Falso**. Las tribus eran **más grandes** que los clanes."},
        {"tema": "Fase cacicazgos iniciales", "afirmacion": "¿El poder del chamán era hereditario?", "correcto": True, "explicacion": "**Verdadero**. El poder del chamán, al igual que el del cacique, era hereditario."},
        {"tema": "Fase cacicazgos iniciales", "afirmacion": "¿El cacique era el intermediario entre los dioses y los indígenas?", "correcto": False, "explicacion": "**Falso**. Ese era el rol del **chamán**."},
        {"tema": "Fase sociedad cacical", "afirmacion": "¿Los guerreros surgieron como clase social en el señorío?", "correcto": True, "explicacion": "**Verdadero**. Los guerreros surgieron en la fase de sociedad cacical."},
        {"tema": "Fase sociedad cacical", "afirmacion": "¿Las aldeas principales eran centros de poder y riqueza?", "correcto": True, "explicacion": "**Verdadero**. Contaban con calzadas, puentes, acueductos y templos."},
        {"tema": "Áreas culturales de América", "afirmacion": "¿Los mayas y aztecas pertenecen al área mesoamericana?", "correcto": True, "explicacion": "**Verdadero**. Son etnias del área mesoamericana."},
        {"tema": "Áreas culturales de América", "afirmacion": "¿Los incas pertenecen al área intermedia?", "correcto": False, "explicacion": "**Falso**. Los incas pertenecen al área **andina**."},
        {"tema": "Áreas culturales de América", "afirmacion": "¿El cultivo en terrazas fue desarrollado por los mesoamericanos?", "correcto": False, "explicacion": "**Falso**. Fue desarrollado por los **andinos**."},
        {"tema": "Etnias de la Costa Rica antigua", "afirmacion": "¿La región Central recibió influencia de las tres áreas culturales?", "correcto": True, "explicacion": "**Verdadero**. Es la región más extensa y recibió influencia de las tres áreas."},
        {"tema": "Etnias de la Costa Rica antigua", "afirmacion": "¿Los chorotegas son la etnia más antigua de Costa Rica?", "correcto": True, "explicacion": "**Verdadero**."},
        {"tema": "Etnias de la Costa Rica antigua", "afirmacion": "¿Las esferas de piedra se encontraron en la región Gran Nicoya?", "correcto": False, "explicacion": "**Falso**. Se encontraron en la **subregión Diquís**."},
        {"tema": "Etnias de la Costa Rica antigua", "afirmacion": "¿Los Bribris pertenecen a la subregión Diquís?", "correcto": True, "explicacion": "**Verdadero**. Los bribris habitan la subregión Diquís."},
        {"tema": "Etnias de la Costa Rica antigua", "afirmacion": "¿Los Chorotegas pertenecen a la región Central?", "correcto": False, "explicacion": "**Falso**. Los chorotegas pertenecen a la región **Gran Nicoya**."},
        {"tema": "Etnias de la Costa Rica antigua", "afirmacion": "¿Los Malekus pertenecen a la región Central?", "correcto": True, "explicacion": "**Verdadero**. Los malekus son de la región Central."},
        {"tema": "Etnias de la Costa Rica antigua", "afirmacion": "¿Los Cabécares recibieron influencia mesoamericana?", "correcto": False, "explicacion": "**Falso**. Recibieron influencia **andina**."},
    ],

    "secuencias": [
        {"tema": "Periodos de la historia de Costa Rica", "nombre": "los periodos de la historia de Costa Rica",
         "orden": ["Antiguo", "Conquista", "Colonial", "Republicano", "Contemporáneo"]},
        {"tema": "Periodos de la historia de Costa Rica", "nombre": "las fases del periodo Antiguo",
         "orden": ["Cazadores-recolectores", "Agricultores tempranos", "Cacicazgos iniciales", "Sociedad cacical"]},
    ],
}
