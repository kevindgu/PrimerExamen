"""Datos de Ciencias para Tyler (5to/6to año) — Reproducción humana y sistema urinario."""

IMG = "cienciastyler"

DATA = {
    "topics": {
        "Caracteres sexuales": {
            "aprendizaje": "Identificar los caracteres sexuales primarios y secundarios",
            "indicador": "Reconoce los principales cambios de la madurez sexual en hombres y mujeres",
        },
        "Sistema reproductor masculino": {
            "aprendizaje": "Identificar los órganos del sistema reproductor masculino y sus funciones",
            "indicador": "Determina la función de los órganos del sistema reproductor masculino",
        },
        "Sistema reproductor femenino": {
            "aprendizaje": "Identificar los órganos del sistema reproductor femenino y sus funciones",
            "indicador": "Determina la función de los órganos del sistema reproductor femenino",
        },
        "Enfermedades del sistema reproductor": {
            "aprendizaje": "Identificar enfermedades del sistema reproductor y sus causas",
            "indicador": "Aplica conocimientos sobre enfermedades y medidas preventivas",
        },
        "Sexo, género y sexualidad": {
            "aprendizaje": "Explicar la relación entre sexo, género y sexualidad",
            "indicador": "Explica la relación entre sexo, género y sexualidad humana",
        },
        "Sistema urinario": {
            "aprendizaje": "Identificar los órganos del sistema urinario y su función en la excreción",
            "indicador": "Reconoce las estructuras del sistema renal y su funcionamiento",
        },
        "Enfermedades del sistema urinario": {
            "aprendizaje": "Identificar enfermedades del sistema urinario y sus causas",
            "indicador": "Reconoce enfermedades del sistema urinario y medidas preventivas",
        },
    },

    "tags": {
        "sistema": ["Masculino", "Femenino"],
    },

    "partes": [
        # --- SISTEMA REPRODUCTOR MASCULINO ---
        {"nombre": "testículos", "img": f"{IMG}/testiculos.webp",
         "funcion": "Producen espermatozoides y la hormona testosterona", "grupo": "Sistema reproductor masculino"},
        {"nombre": "pene", "img": f"{IMG}/pene.jpg",
         "funcion": "Deposita el semen en el sistema reproductor femenino", "grupo": "Sistema reproductor masculino"},
        {"nombre": "próstata", "img": f"{IMG}/prostata.jpg",
         "funcion": "Produce secreción que facilita la movilidad de los espermatozoides", "grupo": "Sistema reproductor masculino"},
        {"nombre": "escroto", "img": f"{IMG}/escroto.webp",
         "funcion": "Bolsa de piel que mantiene los testículos a temperatura adecuada", "grupo": "Sistema reproductor masculino"},
        {"nombre": "vesículas seminales", "img": f"{IMG}/vesículas seminales.jpg",
         "funcion": "Producen gran parte del líquido llamado semen", "grupo": "Sistema reproductor masculino"},
        {"nombre": "conductos deferentes", "img": f"{IMG}/conductodeferentemarcadoenverde.jpeg",
         "funcion": "Llevan los espermatozoides desde los testículos hasta la uretra", "grupo": "Sistema reproductor masculino"},
        {"nombre": "espermatozoide", "img": f"{IMG}/espermatozoide.jpeg",
         "funcion": "Célula sexual masculina que fecunda al óvulo", "grupo": "Sistema reproductor masculino"},

        # --- SISTEMA REPRODUCTOR FEMENINO ---
        {"nombre": "ovarios", "img": f"{IMG}/ovarios.jpg",
         "funcion": "Producen óvulos y las hormonas progesterona y estrógenos", "grupo": "Sistema reproductor femenino"},
        {"nombre": "útero", "img": f"{IMG}/útero.jpg",
         "funcion": "Órgano musculoso que alberga al bebé durante el embarazo", "grupo": "Sistema reproductor femenino"},
        {"nombre": "vagina", "img": f"{IMG}/vagina.webp",
         "funcion": "Canal donde se deposita el semen y por donde sale el bebé en el parto", "grupo": "Sistema reproductor femenino"},
        {"nombre": "trompas de Falopio", "img": f"{IMG}/trompas de falopio.png",
         "funcion": "Transportan los óvulos desde los ovarios hasta el útero; lugar de fecundación", "grupo": "Sistema reproductor femenino"},
        {"nombre": "vulva", "img": f"{IMG}/vulva.webp",
         "funcion": "Estructura externa que cubre y protege la entrada de la vagina", "grupo": "Sistema reproductor femenino"},
        {"nombre": "óvulo", "img": f"{IMG}/óvulo.webp",
         "funcion": "Célula sexual femenina que puede ser fecundada por un espermatozoide", "grupo": "Sistema reproductor femenino"},

        # --- SISTEMA URINARIO ---
        {"nombre": "riñones", "img": f"{IMG}/riñones.jpg",
         "funcion": "Filtran la sangre y forman la orina", "grupo": "Sistema urinario"},
        {"nombre": "vejiga urinaria", "img": f"{IMG}/vejiga urinaria.webp",
         "funcion": "Almacena la orina hasta el momento de su expulsión", "grupo": "Sistema urinario"},
        {"nombre": "uréteres", "img": f"{IMG}/uréteres.webp",
         "funcion": "Transportan la orina desde los riñones hasta la vejiga", "grupo": "Sistema urinario"},
        {"nombre": "uretra", "img": f"{IMG}/uretra.jpeg",
         "funcion": "Conduce la orina desde la vejiga hacia el exterior del cuerpo", "grupo": "Sistema urinario"},

        # --- ENFERMEDADES REPRODUCTOR ---
        {"nombre": "balanitis", "img": f"{IMG}/balantis.png",
         "funcion": "Inflamación del prepucio y del glande por mala higiene", "grupo": "Enfermedades del sistema reproductor", "tipo_pregunta": "enfermedad"},
        {"nombre": "fimosis", "img": f"{IMG}/fimosis.webp",
         "funcion": "Estrechez del prepucio que dificulta descubrir el glande", "grupo": "Enfermedades del sistema reproductor", "tipo_pregunta": "enfermedad"},
        {"nombre": "criptorquidia", "img": f"{IMG}/criptorquidia.gif",
         "funcion": "Ausencia de uno o ambos testículos en el escroto", "grupo": "Enfermedades del sistema reproductor", "tipo_pregunta": "enfermedad"},
        {"nombre": "vulvovaginitis", "img": f"{IMG}/vulvovaginitisnoimagenrealsolomujertapandoselaspartescomocondolor.jpg",
         "funcion": "Infección de la vulva y la vagina por higiene inadecuada", "grupo": "Enfermedades del sistema reproductor", "tipo_pregunta": "enfermedad"},
        {"nombre": "síndrome de ovarios poliquísticos", "img": f"{IMG}/síndrome de ovarios poliquísticos.jpg",
         "funcion": "Formación de quistes alrededor de los ovarios", "grupo": "Enfermedades del sistema reproductor", "tipo_pregunta": "enfermedad"},
        {"nombre": "dismenorrea", "img": f"{IMG}/dismenorrea.png",
         "funcion": "Dolor intenso en el abdomen durante la menstruación", "grupo": "Enfermedades del sistema reproductor", "tipo_pregunta": "enfermedad"},
        {"nombre": "gonorrea", "img": f"{IMG}/gonorrea.jpg",
         "funcion": "ITS causada por bacteria que provoca pus en la uretra e infertilidad", "grupo": "Enfermedades del sistema reproductor", "tipo_pregunta": "enfermedad"},
        {"nombre": "papiloma humano", "img": f"{IMG}/papiloma humano.png",
         "funcion": "ITS que causa verrugas en los genitales", "grupo": "Enfermedades del sistema reproductor", "tipo_pregunta": "enfermedad"},

        # --- ENFERMEDADES URINARIO ---
        {"nombre": "cistitis", "img": f"{IMG}/cistitis.webp",
         "funcion": "Inflamación del interior de la vejiga, causa ardor al orinar", "grupo": "Enfermedades del sistema urinario", "tipo_pregunta": "enfermedad"},
        {"nombre": "nefritis", "img": f"{IMG}/nefritis.webp",
         "funcion": "Inflamación de uno o ambos riñones", "grupo": "Enfermedades del sistema urinario", "tipo_pregunta": "enfermedad"},
        {"nombre": "cálculos renales", "img": f"{IMG}/cálculos renales.jpg",
         "funcion": "Cristales de sales en la orina que obstruyen el paso y causan dolor", "grupo": "Enfermedades del sistema urinario", "tipo_pregunta": "enfermedad"},
        {"nombre": "uremia", "img": f"{IMG}/uremia.jpeg",
         "funcion": "Acumulación de sustancias tóxicas en la sangre por fallo renal", "grupo": "Enfermedades del sistema urinario", "tipo_pregunta": "enfermedad"},

        # --- CARACTERES SEXUALES ---
        {"nombre": "caracteres sexuales secundarios femeninos", "img": f"{IMG}/caracteres sexuales secundarios femeninos.jpeg",
         "funcion": "Desarrollo de senos, caderas, menstruación", "grupo": "Caracteres sexuales"},
        {"nombre": "caracteres sexuales secundarios masculinos", "img": f"{IMG}/caracteres sexuales secundarios masculinos.jpeg",
         "funcion": "Cambio de voz, barba, ensanchamiento de hombros, primera eyaculación", "grupo": "Caracteres sexuales"},
        {"nombre": "cromosomas XX y XY", "img": f"{IMG}/cromosomas XX y XY.webp",
         "funcion": "Determinan el sexo biológico: XX femenino, XY masculino", "grupo": "Sexo, género y sexualidad"},
        {"nombre": "menstruación", "img": f"{IMG}/menstruación.jpg",
         "funcion": "Expulsión mensual de sangre y óvulo sin fecundar a través de la vagina", "grupo": "Caracteres sexuales"},
    ],

    "preguntas": [
        # Caracteres sexuales
        {"tema": "Caracteres sexuales", "q": "¿Cómo se llaman las características corporales que diferencian hombres de mujeres?", "answer": "Caracteres sexuales", "opciones": ["Caracteres sexuales", "Hormonas", "Gametos", "Cromosomas"], "procedure": "Se llaman **caracteres sexuales**."},
        {"tema": "Caracteres sexuales", "q": "¿Cuáles son los caracteres sexuales que se manifiestan desde antes de nacer?", "answer": "Primarios", "opciones": ["Primarios", "Secundarios", "Hormonales", "Genéticos"], "procedure": "Los **primarios** son los órganos sexuales presentes desde el nacimiento."},
        {"tema": "Caracteres sexuales", "q": "¿Dónde se producen las hormonas sexuales femeninas?", "answer": "Ovarios", "opciones": ["Ovarios", "Útero", "Vagina", "Trompas"], "procedure": "Se producen en los **ovarios**."},
        {"tema": "Caracteres sexuales", "q": "¿Dónde se producen las hormonas sexuales masculinas?", "answer": "Testículos", "opciones": ["Testículos", "Pene", "Próstata", "Escroto"], "procedure": "Se producen en los **testículos**."},
        {"tema": "Caracteres sexuales", "q": "¿Cómo se llama la primera menstruación?", "answer": "Menarquia", "opciones": ["Menarquia", "Menopausia", "Ovulación", "Fecundación"], "procedure": "La primera menstruación se llama **menarquia**."},
        {"tema": "Caracteres sexuales", "q": "¿Entre qué edades suele ocurrir la primera menstruación?", "answer": "10 y 14 años", "opciones": ["10 y 14 años", "5 y 8 años", "16 y 20 años", "20 y 25 años"], "procedure": "Ocurre entre los **10 y 14 años**."},

        # Sistema reproductor masculino
        {"tema": "Sistema reproductor masculino", "q": "¿Cómo se llaman las células sexuales masculinas?", "answer": "Espermatozoides", "opciones": ["Espermatozoides", "Óvulos", "Gametos", "Cigotos"], "procedure": "Se llaman **espermatozoides**."},
        {"tema": "Sistema reproductor masculino", "q": "¿Cómo se llama la hormona sexual masculina?", "answer": "Testosterona", "opciones": ["Testosterona", "Estrógeno", "Progesterona", "Adrenalina"], "procedure": "Se llama **testosterona**."},
        {"tema": "Sistema reproductor masculino", "q": "¿Cómo se llama el líquido que contiene los espermatozoides?", "answer": "Semen", "opciones": ["Semen", "Orina", "Plasma", "Bilis"], "procedure": "Se llama **semen**."},

        # Sistema reproductor femenino
        {"tema": "Sistema reproductor femenino", "q": "¿Cómo se llaman las células sexuales femeninas?", "answer": "Óvulos", "opciones": ["Óvulos", "Espermatozoides", "Cigotos", "Gametos"], "procedure": "Se llaman **óvulos**."},
        {"tema": "Sistema reproductor femenino", "q": "¿Cómo se llaman las hormonas sexuales femeninas?", "answer": "Estrógenos y progesterona", "opciones": ["Estrógenos y progesterona", "Testosterona y adrenalina", "Insulina y glucagón", "Cortisol y melatonina"], "procedure": "Se llaman **estrógenos y progesterona**."},
        {"tema": "Sistema reproductor femenino", "q": "¿Dónde ocurre la fecundación?", "answer": "Trompas de Falopio", "opciones": ["Trompas de Falopio", "Útero", "Vagina", "Ovarios"], "procedure": "Ocurre en las **trompas de Falopio**."},
        {"tema": "Sistema reproductor femenino", "q": "¿Cómo se llama la célula que se forma cuando se unen el óvulo y el espermatozoide?", "answer": "Cigoto", "opciones": ["Cigoto", "Embrión", "Gameto", "Feto"], "procedure": "Se llama **cigoto**."},
        {"tema": "Sistema reproductor femenino", "q": "¿Cómo se llama la unión del óvulo y el espermatozoide?", "answer": "Fecundación", "opciones": ["Fecundación", "Ovulación", "Menstruación", "Gestación"], "procedure": "Se llama **fecundación**."},

        # Sexo, género y sexualidad
        {"tema": "Sexo, género y sexualidad", "q": "¿Qué cromosomas tienen las mujeres?", "answer": "XX", "opciones": ["XX", "XY", "YY", "XO"], "procedure": "Las mujeres tienen cromosomas **XX**."},
        {"tema": "Sexo, género y sexualidad", "q": "¿Qué cromosomas tienen los hombres?", "answer": "XY", "opciones": ["XX", "XY", "YY", "XO"], "procedure": "Los hombres tienen cromosomas **XY**."},
        {"tema": "Sexo, género y sexualidad", "q": "¿Qué determina el sexo biológico de una persona?", "answer": "Los cromosomas sexuales", "opciones": ["Los cromosomas sexuales", "La cultura", "La ropa", "La familia"], "procedure": "El sexo lo determinan los **cromosomas sexuales**."},
        {"tema": "Sexo, género y sexualidad", "q": "¿Cómo se llaman los comportamientos que la sociedad espera según el sexo?", "answer": "Roles de género", "opciones": ["Roles de género", "Caracteres sexuales", "Hormonas", "Cromosomas"], "procedure": "Se llaman **roles de género**."},

        # Sistema urinario
        {"tema": "Sistema urinario", "q": "¿Cuál es la función principal del sistema urinario?", "answer": "Eliminar desechos del cuerpo mediante la orina", "opciones": ["Eliminar desechos del cuerpo mediante la orina", "Bombear sangre", "Digerir alimentos", "Producir hormonas"], "procedure": "Su función es **eliminar desechos** mediante la orina."},
        {"tema": "Sistema urinario", "q": "¿Cómo se llama la acción de orinar?", "answer": "Micción", "opciones": ["Micción", "Excreción", "Filtración", "Absorción"], "procedure": "Se llama **micción**."},
        {"tema": "Sistema urinario", "q": "¿Qué sustancia tóxica contiene la orina?", "answer": "Urea", "opciones": ["Urea", "Glucosa", "Calcio", "Proteínas"], "procedure": "La orina contiene **urea**."},
        {"tema": "Sistema urinario", "q": "¿Cuántos riñones tiene el cuerpo humano?", "answer": "2", "opciones": ["1", "2", "3", "4"], "procedure": "El cuerpo tiene **2 riñones**."},

        # Enfermedades reproductor
        {"tema": "Enfermedades del sistema reproductor", "q": "¿Qué es la balanitis?", "answer": "Inflamación del prepucio y del glande", "opciones": ["Inflamación del prepucio y del glande", "Ausencia de testículos", "Estrechez del prepucio", "Infección de la vagina"], "procedure": "La **balanitis** es inflamación del prepucio y glande."},
        {"tema": "Enfermedades del sistema reproductor", "q": "¿Qué es la criptorquidia?", "answer": "Ausencia de uno o ambos testículos en el escroto", "opciones": ["Ausencia de uno o ambos testículos en el escroto", "Inflamación del pene", "Estrechez del prepucio", "Infección de la próstata"], "procedure": "La **criptorquidia** es la ausencia de testículos en el escroto."},
        {"tema": "Enfermedades del sistema reproductor", "q": "¿Cómo se llaman las enfermedades que se transmiten por relaciones sexuales?", "answer": "ITS", "opciones": ["ITS", "IRS", "ETS", "VIH"], "procedure": "Se llaman **ITS** (Infecciones de Transmisión Sexual)."},

        # Enfermedades urinario
        {"tema": "Enfermedades del sistema urinario", "q": "¿Qué son los cálculos renales?", "answer": "Cristales de sales en la orina que obstruyen el paso", "opciones": ["Cristales de sales en la orina que obstruyen el paso", "Inflamación de los riñones", "Infección de la vejiga", "Acumulación de toxinas en la sangre"], "procedure": "Los **cálculos renales** son cristales de sales en la orina."},
        {"tema": "Enfermedades del sistema urinario", "q": "¿Qué es la uremia?", "answer": "Acumulación de toxinas en la sangre por fallo renal", "opciones": ["Acumulación de toxinas en la sangre por fallo renal", "Inflamación de la vejiga", "Piedras en el riñón", "Infección urinaria"], "procedure": "La **uremia** es acumulación de toxinas por fallo renal."},
        {"tema": "Enfermedades del sistema urinario", "q": "¿Qué hábito ayuda a prevenir los cálculos renales?", "answer": "Tomar suficiente agua", "opciones": ["Tomar suficiente agua", "Comer mucha sal", "No hacer ejercicio", "Tomar refrescos"], "procedure": "**Tomar suficiente agua** previene los cálculos renales."},
    ],

    "verdadero_falso": [
        # Caracteres sexuales
        {"tema": "Caracteres sexuales", "afirmacion": "¿Los caracteres sexuales primarios son los órganos sexuales presentes desde el nacimiento?", "correcto": True, "explicacion": "**Verdadero**. Los primarios están desde antes de nacer."},
        {"tema": "Caracteres sexuales", "afirmacion": "¿La barba es un carácter sexual primario?", "correcto": False, "explicacion": "**Falso**. La barba es un carácter sexual **secundario**."},
        {"tema": "Caracteres sexuales", "afirmacion": "¿Las hormonas sexuales se producen en las glándulas sexuales?", "correcto": True, "explicacion": "**Verdadero**. En ovarios (mujeres) y testículos (hombres)."},
        # Reproductor masculino
        {"tema": "Sistema reproductor masculino", "afirmacion": "¿Los testículos producen espermatozoides y testosterona?", "correcto": True, "explicacion": "**Verdadero**."},
        {"tema": "Sistema reproductor masculino", "afirmacion": "¿El escroto produce espermatozoides?", "correcto": False, "explicacion": "**Falso**. El escroto **mantiene la temperatura** adecuada para los testículos."},
        # Reproductor femenino
        {"tema": "Sistema reproductor femenino", "afirmacion": "¿La fecundación ocurre en el útero?", "correcto": False, "explicacion": "**Falso**. Ocurre en las **trompas de Falopio**."},
        {"tema": "Sistema reproductor femenino", "afirmacion": "¿Los ovarios producen óvulos y estrógenos?", "correcto": True, "explicacion": "**Verdadero**."},
        {"tema": "Sistema reproductor femenino", "afirmacion": "¿El cigoto se forma cuando se unen el óvulo y el espermatozoide?", "correcto": True, "explicacion": "**Verdadero**. La fusión de gametos forma el **cigoto**."},
        # Sexo y género
        {"tema": "Sexo, género y sexualidad", "afirmacion": "¿Las mujeres tienen cromosomas XY?", "correcto": False, "explicacion": "**Falso**. Las mujeres tienen **XX**, los hombres **XY**."},
        {"tema": "Sexo, género y sexualidad", "afirmacion": "¿El sexo biológico está determinado por los cromosomas?", "correcto": True, "explicacion": "**Verdadero**."},
        {"tema": "Sexo, género y sexualidad", "afirmacion": "¿Los roles de género son iguales en todas las culturas?", "correcto": False, "explicacion": "**Falso**. Los roles de género **varían** entre culturas y épocas."},
        # Sistema urinario
        {"tema": "Sistema urinario", "afirmacion": "¿Los riñones filtran la sangre y forman la orina?", "correcto": True, "explicacion": "**Verdadero**."},
        {"tema": "Sistema urinario", "afirmacion": "¿La uretra transporta la orina de los riñones a la vejiga?", "correcto": False, "explicacion": "**Falso**. Eso lo hacen los **uréteres**. La uretra expulsa la orina al exterior."},
        {"tema": "Sistema urinario", "afirmacion": "¿La vejiga almacena la orina?", "correcto": True, "explicacion": "**Verdadero**."},
        # Enfermedades
        {"tema": "Enfermedades del sistema urinario", "afirmacion": "¿La cistitis es una inflamación de los riñones?", "correcto": False, "explicacion": "**Falso**. La cistitis es inflamación de la **vejiga**. La inflamación de riñones es nefritis."},
        {"tema": "Enfermedades del sistema urinario", "afirmacion": "¿Beber poca agua puede causar cálculos renales?", "correcto": True, "explicacion": "**Verdadero**. Beber poca agua favorece la formación de cálculos."},
        {"tema": "Enfermedades del sistema reproductor", "afirmacion": "¿La vulvovaginitis puede ser causada por higiene inadecuada?", "correcto": True, "explicacion": "**Verdadero**."},
        {"tema": "Enfermedades del sistema reproductor", "afirmacion": "¿Todas las ITS tienen cura?", "correcto": False, "explicacion": "**Falso**. Algunas como el herpes genital y el sida **aún no tienen cura**."},
    ],

    "secuencias": [
        {"tema": "Sistema urinario", "nombre": "el recorrido de la orina",
         "orden": ["riñones", "uréteres", "vejiga urinaria", "uretra"]},
        {"tema": "Sistema reproductor femenino", "nombre": "el recorrido del óvulo",
         "orden": ["ovarios", "trompas de Falopio", "útero", "vagina"]},
    ],
}
