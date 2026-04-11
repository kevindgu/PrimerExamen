"""Datos de Ciencias para Jaikel — solo datos, cero lógica."""

DATA = {
    "topics": {
        "Sistema digestivo": {
            "aprendizaje": "Identificar órganos, funciones y proceso digestivo",
            "indicador": "Identifica órganos, recorrido del bolo alimenticio y medidas de salud",
        },
        "Sistema óseo": {
            "aprendizaje": "Identificar funciones y estructuras del sistema óseo",
            "indicador": "Identifica huesos, funciones y medidas de cuidado",
        },
        "Articulaciones": {
            "aprendizaje": "Reconocer tipos de articulaciones",
            "indicador": "Reconoce articulaciones móviles e inmóviles",
        },
        "Sistema muscular": {
            "aprendizaje": "Identificar músculos y sus clasificaciones",
            "indicador": "Identifica músculos, clasificaciones y medidas de cuidado",
        },
    },

    "tags": {
        "tipo": ["💪 Voluntario", "🫀 Involuntario"],
        "articulacion": ["Móvil", "Inmóvil"],
    },

    "partes": [
        # --- DIGESTIVO ---
        {"nombre": "boca", "img": "digestivo/boca.jpg", "funcion": "Mastica la comida y la mezcla con saliva", "grupo": "Sistema digestivo"},
        {"nombre": "glándulas salivales", "img": "digestivo/glandulas_salivales.png", "funcion": "Producen saliva para descomponer alimentos", "grupo": "Sistema digestivo"},
        {"nombre": "faringe", "img": "digestivo/faringe.jpg", "funcion": "Conecta la boca con el esófago, permite tragar", "grupo": "Sistema digestivo"},
        {"nombre": "laringe", "img": "digestivo/laringe.jpg", "funcion": "Protege las vías respiratorias al tragar", "grupo": "Sistema digestivo"},
        {"nombre": "esófago", "img": "digestivo/esofago.png", "funcion": "Tubo que lleva la comida al estómago", "grupo": "Sistema digestivo"},
        {"nombre": "estómago", "img": "digestivo/estamago.jpg", "funcion": "Mezcla la comida con jugos gástricos", "grupo": "Sistema digestivo"},
        {"nombre": "hígado", "img": "digestivo/higado.jpg", "funcion": "Produce bilis para digerir las grasas", "grupo": "Sistema digestivo"},
        {"nombre": "intestino delgado", "img": "digestivo/intestinodelgado.jpg", "funcion": "Absorbe los nutrientes hacia la sangre", "grupo": "Sistema digestivo"},
        {"nombre": "intestino grueso", "img": "digestivo/intestinogrueso.jpg", "funcion": "Absorbe el agua y forma las heces", "grupo": "Sistema digestivo"},
        {"nombre": "recto y ano", "img": "digestivo/rectoyanojuntos.jpg", "funcion": "Almacena y expulsa las heces del cuerpo", "grupo": "Sistema digestivo"},

        # --- ÓSEO ---
        {"nombre": "cráneo", "img": "osea/craneo.jpeg", "funcion": "Protege el cerebro", "grupo": "Sistema óseo"},
        {"nombre": "mandíbula", "img": "osea/mandibula.jpeg", "funcion": "Permite masticar y mover la boca", "grupo": "Sistema óseo"},
        {"nombre": "clavícula", "img": "osea/clavicula.jpeg", "funcion": "Conecta el hombro con el esternón", "grupo": "Sistema óseo"},
        {"nombre": "omóplato", "img": "osea/omoplato.jpg", "funcion": "Hueso plano de la espalda que conecta el brazo", "grupo": "Sistema óseo"},
        {"nombre": "costillas", "img": "osea/costillas.jpg", "funcion": "Protegen el corazón y los pulmones", "grupo": "Sistema óseo"},
        {"nombre": "pelvis", "img": "osea/pelvis.jpeg", "funcion": "Sostiene órganos del abdomen y conecta las piernas", "grupo": "Sistema óseo"},
        {"nombre": "fémur", "img": "osea/femur.jpeg", "funcion": "Hueso del muslo, el más largo del cuerpo", "grupo": "Sistema óseo"},
        {"nombre": "tibia", "img": "osea/tibia.jpg", "funcion": "Hueso principal de la parte inferior de la pierna", "grupo": "Sistema óseo"},
        {"nombre": "peroné", "img": "osea/perone.jpg", "funcion": "Hueso delgado al lado de la tibia", "grupo": "Sistema óseo"},
        {"nombre": "radio", "img": "osea/radio.jpg", "funcion": "Hueso del antebrazo del lado del pulgar", "grupo": "Sistema óseo"},
        {"nombre": "cúbito", "img": "osea/cubito.png", "funcion": "Hueso del antebrazo del lado del meñique", "grupo": "Sistema óseo"},
        {"nombre": "carpo", "img": "osea/carpo.webp", "funcion": "Huesos pequeños de la muñeca", "grupo": "Sistema óseo"},
        {"nombre": "metacarpo", "img": "osea/metacarpo.webp", "funcion": "Huesos de la palma de la mano", "grupo": "Sistema óseo"},
        {"nombre": "falanges", "img": "osea/falanges.jpg", "funcion": "Huesos de los dedos", "grupo": "Sistema óseo"},
        {"nombre": "tarso", "img": "osea/tarso.jpeg", "funcion": "Huesos del tobillo", "grupo": "Sistema óseo"},
        {"nombre": "metatarso", "img": "osea/metatorso.jpg", "funcion": "Huesos de la planta del pie", "grupo": "Sistema óseo"},

        # --- ARTICULACIONES (tema propio) ---
        {"nombre": "rodilla", "img": "articulaciones/rodilla.jpeg", "funcion": "Permite doblar y estirar la pierna", "grupo": "Articulaciones", "tags": {"articulacion": "Móvil"}},
        {"nombre": "codo", "img": "articulaciones/codo.jpg", "funcion": "Permite doblar y estirar el brazo", "grupo": "Articulaciones", "tags": {"articulacion": "Móvil"}},
        {"nombre": "hombro", "img": "articulaciones/hombro.jpeg", "funcion": "Permite mover el brazo en muchas direcciones", "grupo": "Articulaciones", "tags": {"articulacion": "Móvil"}},
        {"nombre": "tobillo", "img": "articulaciones/tobillo.webp", "funcion": "Permite mover el pie", "grupo": "Articulaciones", "tags": {"articulacion": "Móvil"}},
        {"nombre": "pelvis (cadera)", "img": "articulaciones/pelvis.jpeg", "funcion": "Permite mover las piernas y caminar", "grupo": "Articulaciones", "tags": {"articulacion": "Móvil"}},

        # --- MUSCULAR ---
        {"nombre": "frontal", "img": "muscular/frontal.jpeg", "funcion": "Músculo de la frente, levanta las cejas", "grupo": "Sistema muscular", "tags": {"tipo": "💪 Voluntario"}},
        {"nombre": "deltoides", "img": "muscular/deltoide.jpeg", "funcion": "Músculo del hombro, levanta el brazo", "grupo": "Sistema muscular", "tags": {"tipo": "💪 Voluntario"}},
        {"nombre": "pectorales", "img": "muscular/pectorales.png", "funcion": "Músculos del pecho, mueven los brazos", "grupo": "Sistema muscular", "tags": {"tipo": "💪 Voluntario"}},
        {"nombre": "bíceps", "img": "muscular/biceps.webp", "funcion": "Músculo frontal del brazo, flexiona el codo", "grupo": "Sistema muscular", "tags": {"tipo": "💪 Voluntario"}},
        {"nombre": "tríceps", "img": "muscular/triceps.jpg", "funcion": "Músculo trasero del brazo, extiende el codo", "grupo": "Sistema muscular", "tags": {"tipo": "💪 Voluntario"}},
        {"nombre": "abdominales", "img": "muscular/abdominales.jpg", "funcion": "Músculos del abdomen, protegen órganos", "grupo": "Sistema muscular", "tags": {"tipo": "💪 Voluntario"}},
        {"nombre": "cuádriceps", "img": "muscular/cuadriceps.webp", "funcion": "Músculo frontal del muslo, extiende la rodilla", "grupo": "Sistema muscular", "tags": {"tipo": "💪 Voluntario"}},
        {"nombre": "gemelos", "img": "muscular/gemelos.jpg", "funcion": "Músculos de la pantorrilla, permiten caminar y saltar", "grupo": "Sistema muscular", "tags": {"tipo": "💪 Voluntario"}},
        {"nombre": "glúteos", "img": "muscular/gluteos.jpg", "funcion": "Músculos de la cadera, los más grandes del cuerpo", "grupo": "Sistema muscular", "tags": {"tipo": "💪 Voluntario"}},
        {"nombre": "trapecio", "img": "muscular/trapecio.jpg", "funcion": "Músculo de la espalda superior, mueve los hombros", "grupo": "Sistema muscular", "tags": {"tipo": "💪 Voluntario"}},
        {"nombre": "dorsal", "img": "muscular/dorsal.webp", "funcion": "Músculo grande de la espalda, permite jalar", "grupo": "Sistema muscular", "tags": {"tipo": "💪 Voluntario"}},
    ],

    "preguntas": [
        # Digestivo
        {"tema": "Sistema digestivo", "q": "¿Por dónde entra la comida al sistema digestivo?", "answer": "Boca", "opciones": ["Estómago", "Boca", "Intestino", "Esófago"], "procedure": "La comida entra por la **boca**."},
        {"tema": "Sistema digestivo", "q": "¿Qué tubo lleva la comida al estómago?", "answer": "Esófago", "opciones": ["Intestino", "Faringe", "Esófago", "Tráquea"], "procedure": "El **esófago** conecta la boca con el estómago."},
        {"tema": "Sistema digestivo", "q": "¿Dónde se mezcla la comida con jugos gástricos?", "answer": "Estómago", "opciones": ["Boca", "Intestino", "Hígado", "Estómago"], "procedure": "En el **estómago**."},
        {"tema": "Sistema digestivo", "q": "¿Dónde se absorben los nutrientes?", "answer": "Intestino delgado", "opciones": ["Estómago", "Intestino grueso", "Intestino delgado", "Boca"], "procedure": "En el **intestino delgado**."},
        {"tema": "Sistema digestivo", "q": "¿Cómo se llama la comida masticada con saliva?", "answer": "Bolo alimenticio", "opciones": ["Quimo", "Bolo alimenticio", "Quilo", "Bilis"], "procedure": "Se llama **bolo alimenticio**."},
        {"tema": "Sistema digestivo", "q": "¿Qué órgano produce bilis?", "answer": "Hígado", "opciones": ["Estómago", "Páncreas", "Hígado", "Intestino"], "procedure": "El **hígado** produce bilis."},
        # Óseo
        {"tema": "Sistema óseo", "q": "¿Cuál es una función del sistema óseo?", "answer": "Dar soporte al cuerpo", "opciones": ["Digerir alimentos", "Dar soporte al cuerpo", "Respirar", "Bombear sangre"], "procedure": "**Dar soporte**, proteger órganos y permitir movimiento."},
        {"tema": "Sistema óseo", "q": "¿Qué hueso protege el cerebro?", "answer": "Cráneo", "opciones": ["Fémur", "Costillas", "Cráneo", "Pelvis"], "procedure": "El **cráneo**."},
        {"tema": "Sistema óseo", "q": "¿Cuál es el hueso más largo del cuerpo?", "answer": "Fémur", "opciones": ["Tibia", "Húmero", "Cráneo", "Fémur"], "procedure": "El **fémur** (muslo)."},
        {"tema": "Sistema óseo", "q": "¿Qué huesos protegen corazón y pulmones?", "answer": "Costillas", "opciones": ["Falanges", "Costillas", "Carpo", "Fémur"], "procedure": "Las **costillas**."},
        {"tema": "Sistema óseo", "q": "¿Qué nutriente fortalece los huesos?", "answer": "Calcio", "opciones": ["Azúcar", "Grasa", "Calcio", "Sal"], "procedure": "El **calcio** (leche, queso, yogur)."},
        # Muscular
        {"tema": "Sistema muscular", "q": "¿Cuál es el músculo más grande del cuerpo?", "answer": "Glúteos", "opciones": ["Bíceps", "Glúteos", "Abdominales", "Tríceps"], "procedure": "Los **glúteos**."},
        {"tema": "Sistema muscular", "q": "¿Los músculos unidos a los huesos se llaman...?", "answer": "Esqueléticos", "opciones": ["Cardíacos", "Lisos", "Esqueléticos", "Viscerales"], "procedure": "**Esqueléticos**."},
        {"tema": "Sistema muscular", "q": "¿El músculo del corazón se llama músculo...?", "answer": "Cardíaco", "opciones": ["Esquelético", "Liso", "Cardíaco", "Voluntario"], "procedure": "**Cardíaco**."},

        # Articulaciones
        {"tema": "Articulaciones", "q": "¿Cómo se llama la unión entre dos huesos?", "answer": "Articulación", "opciones": ["Articulación", "Ligamento", "Tendón", "Músculo"], "procedure": "La **articulación** es donde se unen dos huesos."},
        {"tema": "Articulaciones", "q": "¿Las articulaciones del cráneo son móviles o inmóviles?", "answer": "Inmóviles", "opciones": ["Móviles", "Inmóviles"], "procedure": "Son **inmóviles**, los huesos están fijos."},
        {"tema": "Articulaciones", "q": "¿La rodilla es una articulación móvil o inmóvil?", "answer": "Móvil", "opciones": ["Móvil", "Inmóvil"], "procedure": "La rodilla es **móvil**."},
        {"tema": "Articulaciones", "q": "¿Qué articulación permite mover el brazo en muchas direcciones?", "answer": "Hombro", "opciones": ["Hombro", "Codo", "Rodilla", "Tobillo"], "procedure": "El **hombro**."},
        {"tema": "Articulaciones", "q": "¿Qué tipo de articulación tiene el codo?", "answer": "Móvil", "opciones": ["Móvil", "Inmóvil", "Semimóvil"], "procedure": "El codo es **móvil**."},

        # Cuidado del sistema digestivo
        {"tema": "Sistema digestivo", "q": "¿Qué hábito ayuda a cuidar el sistema digestivo?", "answer": "Comer frutas y verduras", "opciones": ["Comer frutas y verduras", "Comer solo dulces", "Saltarse comidas", "Comer muy rápido"], "procedure": "Las **frutas y verduras** tienen fibra que ayuda a la digestión."},
        {"tema": "Sistema digestivo", "q": "¿Por qué es importante tomar agua?", "answer": "Ayuda a la digestión", "opciones": ["Ayuda a la digestión", "Da más hambre", "No es importante", "Solo quita la sed"], "procedure": "El agua **ayuda a la digestión** y absorción de nutrientes."},
        {"tema": "Sistema digestivo", "q": "¿Qué pasa si comes muy rápido?", "answer": "Dificulta la digestión", "opciones": ["Dificulta la digestión", "Mejora la digestión", "No pasa nada", "Da más energía"], "procedure": "Comer rápido **dificulta la digestión**."},

        # Cuidado del sistema óseo
        {"tema": "Sistema óseo", "q": "¿Qué alimento fortalece los huesos?", "answer": "Leche", "opciones": ["Leche", "Refresco", "Papas fritas", "Dulces"], "procedure": "La **leche** tiene calcio que fortalece los huesos."},
        {"tema": "Sistema óseo", "q": "¿Qué vitamina ayuda a absorber el calcio?", "answer": "Vitamina D", "opciones": ["Vitamina D", "Vitamina C", "Vitamina A", "Vitamina B"], "procedure": "La **vitamina D** (del sol) ayuda a absorber calcio."},
        {"tema": "Sistema óseo", "q": "¿Cómo puedes cuidar tus huesos?", "answer": "Hacer ejercicio y comer calcio", "opciones": ["Hacer ejercicio y comer calcio", "No moverse", "Comer solo dulces", "Dormir todo el día"], "procedure": "**Ejercicio + calcio** fortalecen los huesos."},

        # Cuidado del sistema muscular
        {"tema": "Sistema muscular", "q": "¿Qué debes hacer antes de hacer ejercicio?", "answer": "Calentar", "opciones": ["Calentar", "Comer mucho", "Dormir", "Nada"], "procedure": "**Calentar** prepara los músculos y evita lesiones."},
        {"tema": "Sistema muscular", "q": "¿Qué debes hacer después de hacer ejercicio?", "answer": "Estirar", "opciones": ["Estirar", "Comer dulces", "Correr más", "Nada"], "procedure": "**Estirar** relaja los músculos y evita dolor."},
        {"tema": "Sistema muscular", "q": "¿Qué ayuda a recuperar los músculos?", "answer": "Dormir bien", "opciones": ["Dormir bien", "No dormir", "Comer dulces", "Ver televisión"], "procedure": "**Dormir bien** permite que los músculos se reparen."},

        # Cuidado de articulaciones
        {"tema": "Articulaciones", "q": "¿Cómo puedes cuidar tus articulaciones?", "answer": "Hacer ejercicio moderado", "opciones": ["Hacer ejercicio moderado", "No moverse nunca", "Cargar cosas muy pesadas", "Saltar desde alturas"], "procedure": "El **ejercicio moderado** mantiene las articulaciones sanas."},

        # Sistema óseo - tipos de huesos
        {"tema": "Sistema óseo", "q": "¿Cómo se clasifica el fémur según su forma?", "answer": "Hueso largo", "opciones": ["Hueso largo", "Hueso corto", "Hueso plano", "Hueso curvo"], "procedure": "El fémur es un **hueso largo**."},
        {"tema": "Sistema óseo", "q": "¿Cómo se clasifican las falanges según su forma?", "answer": "Huesos cortos", "opciones": ["Huesos largos", "Huesos cortos", "Huesos planos", "Huesos curvos"], "procedure": "Las falanges son **huesos cortos**."},
        {"tema": "Sistema óseo", "q": "¿Cómo se clasifica el omóplato según su forma?", "answer": "Hueso plano", "opciones": ["Hueso largo", "Hueso corto", "Hueso plano", "Hueso curvo"], "procedure": "El omóplato es un **hueso plano**."},
        {"tema": "Sistema óseo", "q": "¿Cómo se clasifican las costillas según su forma?", "answer": "Huesos curvos", "opciones": ["Huesos largos", "Huesos cortos", "Huesos planos", "Huesos curvos"], "procedure": "Las costillas son **huesos curvos**."},
        {"tema": "Sistema óseo", "q": "¿Cuántos huesos tiene el cuerpo humano aproximadamente?", "answer": "206", "opciones": ["106", "206", "306", "406"], "procedure": "El cuerpo humano tiene aproximadamente **206 huesos**."},
        {"tema": "Sistema óseo", "q": "¿Cómo se llama el conjunto de todos los huesos?", "answer": "Esqueleto", "opciones": ["Esqueleto", "Músculo", "Articulación", "Ligamento"], "procedure": "El conjunto de todos los huesos se llama **esqueleto**."},
        {"tema": "Sistema óseo", "q": "¿Qué sustancias almacenan los huesos?", "answer": "Calcio y fósforo", "opciones": ["Calcio y fósforo", "Azúcar y sal", "Agua y grasa", "Hierro y zinc"], "procedure": "Los huesos almacenan **calcio y fósforo**."},

        # Sistema óseo - enfermedades
        {"tema": "Sistema óseo", "q": "¿Cómo se llama cuando se rompe un hueso?", "answer": "Fractura", "opciones": ["Fractura", "Artritis", "Osteoporosis", "Luxación"], "procedure": "Cuando se rompe un hueso se llama **fractura**."},
        {"tema": "Sistema óseo", "q": "¿Qué enfermedad debilita los huesos por falta de calcio?", "answer": "Osteoporosis", "opciones": ["Artritis", "Fractura", "Luxación", "Osteoporosis"], "procedure": "La **osteoporosis** debilita los huesos."},
        {"tema": "Sistema óseo", "q": "¿Cómo se llama la inflamación de las articulaciones?", "answer": "Artritis", "opciones": ["Artritis", "Fractura", "Osteoporosis", "Luxación"], "procedure": "La **artritis** es la inflamación de las articulaciones."},
        {"tema": "Sistema óseo", "q": "¿Qué es una luxación?", "answer": "Cuando un hueso se sale de su articulación", "opciones": ["Cuando un hueso se sale de su articulación", "Cuando un hueso se rompe", "Cuando un músculo se desgarra", "Cuando hay inflamación"], "procedure": "Una **luxación** es cuando un hueso se sale de su articulación."},

        # Articulaciones - tipos
        {"tema": "Articulaciones", "q": "¿Qué tipo de articulación NO permite movimiento?", "answer": "Fija", "opciones": ["Fija", "Semímóvil", "Móvil"], "procedure": "Las articulaciones **fijas** no permiten movimiento (ej: cráneo)."},
        {"tema": "Articulaciones", "q": "¿Qué tipo de articulación permite movimiento restringido?", "answer": "Semímóvil", "opciones": ["Fija", "Semímóvil", "Móvil"], "procedure": "Las articulaciones **semímóviles** permiten movimiento limitado (ej: pelvis, columna)."},
        {"tema": "Articulaciones", "q": "¿Qué une los huesos en las articulaciones?", "answer": "Ligamentos", "opciones": ["Ligamentos", "Tendones", "Músculos", "Nervios"], "procedure": "Los **ligamentos** unen los huesos en las articulaciones."},
        {"tema": "Articulaciones", "q": "¿Las articulaciones de la columna son fijas, semímóviles o móviles?", "answer": "Semímóviles", "opciones": ["Fijas", "Semímóviles", "Móviles"], "procedure": "La columna tiene articulaciones **semímóviles**."},

        # Sistema muscular - funciones y lesiones
        {"tema": "Sistema muscular", "q": "¿Cuántos músculos tiene el cuerpo humano aproximadamente?", "answer": "Más de 600", "opciones": ["Más de 100", "Más de 300", "Más de 600", "Más de 1000"], "procedure": "El cuerpo tiene **más de 600 músculos**."},
        {"tema": "Sistema muscular", "q": "¿Qué une los músculos a los huesos?", "answer": "Tendones", "opciones": ["Tendones", "Ligamentos", "Nervios", "Venas"], "procedure": "Los **tendones** unen los músculos a los huesos."},
        {"tema": "Sistema muscular", "q": "¿Cómo se llama la lesión cuando un músculo se rompe con hemorragia?", "answer": "Desgarro", "opciones": ["Esguince", "Atrofia", "Desgarro", "Fractura"], "procedure": "Se llama **desgarro**."},
        {"tema": "Sistema muscular", "q": "¿Qué es la atrofia muscular?", "answer": "Pérdida de masa muscular", "opciones": ["Pérdida de masa muscular", "Inflamación muscular", "Ruptura muscular", "Calambres"], "procedure": "La **atrofia muscular** es la pérdida de masa muscular."},
        {"tema": "Sistema muscular", "q": "¿Qué es un esguince?", "answer": "Cuando una articulación se tuerce", "opciones": ["Cuando una articulación se tuerce", "Cuando un hueso se rompe", "Cuando un músculo crece", "Cuando hay fiebre"], "procedure": "Un **esguince** ocurre cuando una articulación se tuerce."},
        {"tema": "Sistema muscular", "q": "¿Qué función tienen los músculos además de mover el cuerpo?", "answer": "Regular la temperatura", "opciones": ["Regular la temperatura", "Producir saliva", "Filtrar la sangre", "Producir huesos"], "procedure": "Los músculos también **regulan la temperatura** del cuerpo."},

        # Sistema digestivo - proceso y órganos adicionales
        {"tema": "Sistema digestivo", "q": "¿Qué produce el páncreas?", "answer": "Jugo pancreático", "opciones": ["Bilis", "Saliva", "Jugo pancreático", "Quimo"], "procedure": "El **páncreas** produce jugo pancreático."},
        {"tema": "Sistema digestivo", "q": "¿Cómo se llama la sustancia semílíquida que forma el estómago?", "answer": "Quimo", "opciones": ["Quilo", "Bolo alimenticio", "Bilis", "Quimo"], "procedure": "Se llama **quimo**."},
        {"tema": "Sistema digestivo", "q": "¿Cómo se llama la sustancia líquida que se forma en el intestino delgado?", "answer": "Quilo", "opciones": ["Quimo", "Bolo alimenticio", "Bilis", "Quilo"], "procedure": "Se llama **quilo**."},
        {"tema": "Sistema digestivo", "q": "¿Cuál es la primera etapa del proceso digestivo?", "answer": "Ingestión", "opciones": ["Ingestión", "Digestión", "Absorción", "Defecación"], "procedure": "La primera etapa es la **ingestión** (entrada de alimentos)."},
        {"tema": "Sistema digestivo", "q": "¿En qué etapa se absorben los nutrientes hacia la sangre?", "answer": "Absorción", "opciones": ["Ingestión", "Digestión", "Absorción", "Defecación"], "procedure": "En la etapa de **absorción** (intestino delgado)."},
        {"tema": "Sistema digestivo", "q": "¿Qué hace el hígado además de producir bilis?", "answer": "Elimina toxinas", "opciones": ["Elimina toxinas", "Produce saliva", "Absorbe agua", "Produce quimo"], "procedure": "El hígado **elimina toxinas** y almacena nutrientes."},
    ],

    "verdadero_falso": [
        # Digestivo
        {"tema": "Sistema digestivo", "afirmacion": "¿Masticar bien ayuda a la digestión?", "correcto": True, "explicacion": "**Verdadero**. Facilita el trabajo del estómago."},
        {"tema": "Sistema digestivo", "afirmacion": "¿Comer muy rápido es bueno para la digestión?", "correcto": False, "explicacion": "**Falso**. Hay que comer despacio."},
        {"tema": "Sistema digestivo", "afirmacion": "¿Las frutas y verduras ayudan al sistema digestivo?", "correcto": True, "explicacion": "**Verdadero**. Tienen fibra."},
        # Óseo
        {"tema": "Sistema óseo", "afirmacion": "¿El ejercicio ayuda a los huesos?", "correcto": True, "explicacion": "**Verdadero**. Fortalece huesos y articulaciones."},
        {"tema": "Sistema óseo", "afirmacion": "¿El sol ayuda a producir vitamina D?", "correcto": True, "explicacion": "**Verdadero**. La vitamina D ayuda a absorber calcio."},
        {"tema": "Sistema óseo", "afirmacion": "¿Los huesos de los dedos se llaman falanges?", "correcto": True, "explicacion": "**Verdadero**."},
        {"tema": "Sistema óseo", "afirmacion": "¿La clavícula está en la pierna?", "correcto": False, "explicacion": "**Falso**. Conecta el hombro con el esternón."},
        # Muscular
        {"tema": "Sistema muscular", "afirmacion": "¿El corazón es un músculo?", "correcto": True, "explicacion": "**Verdadero**. Es involuntario."},
        {"tema": "Sistema muscular", "afirmacion": "¿Es importante calentar antes de hacer ejercicio?", "correcto": True, "explicacion": "**Verdadero**. Evita lesiones."},
        {"tema": "Sistema muscular", "afirmacion": "¿El bíceps está en la pierna?", "correcto": False, "explicacion": "**Falso**. Está en el brazo."},
        {"tema": "Sistema muscular", "afirmacion": "¿El trapecio está en la espalda?", "correcto": True, "explicacion": "**Verdadero**. Espalda superior."},
        {"tema": "Sistema muscular", "afirmacion": "¿Dormir bien ayuda a recuperar los músculos?", "correcto": True, "explicacion": "**Verdadero**. Se reparan durante el sueño."},
        # Articulaciones
        {"tema": "Articulaciones", "afirmacion": "¿La rodilla es una articulación móvil?", "correcto": True, "explicacion": "**Verdadero**. Permite doblar la pierna."},
        {"tema": "Articulaciones", "afirmacion": "¿Las articulaciones del cráneo son móviles?", "correcto": False, "explicacion": "**Falso**. Son inmóviles."},
        {"tema": "Articulaciones", "afirmacion": "¿El ejercicio moderado ayuda a las articulaciones?", "correcto": True, "explicacion": "**Verdadero**. Las mantiene sanas."},
        # Cuidados
        {"tema": "Sistema digestivo", "afirmacion": "¿Lavarse las manos antes de comer ayuda al sistema digestivo?", "correcto": True, "explicacion": "**Verdadero**. Evita que entren bacterias."},
        {"tema": "Sistema óseo", "afirmacion": "¿Tomar refresco fortalece los huesos?", "correcto": False, "explicacion": "**Falso**. El refresco no tiene calcio. Mejor tomar leche."},
        {"tema": "Sistema muscular", "afirmacion": "¿Hacer ejercicio sin calentar es seguro?", "correcto": False, "explicacion": "**Falso**. Puede causar lesiones."},

        # Tipos de huesos
        {"tema": "Sistema óseo", "afirmacion": "¿El fémur es un hueso corto?", "correcto": False, "explicacion": "**Falso**. Es un hueso **largo**, el más largo del cuerpo."},
        {"tema": "Sistema óseo", "afirmacion": "¿Las costillas son huesos curvos?", "correcto": True, "explicacion": "**Verdadero**. Las costillas son huesos curvos."},
        {"tema": "Sistema óseo", "afirmacion": "¿El cuerpo humano tiene 206 huesos?", "correcto": True, "explicacion": "**Verdadero**. Aproximadamente 206 huesos."},
        {"tema": "Sistema óseo", "afirmacion": "¿La osteoporosis fortalece los huesos?", "correcto": False, "explicacion": "**Falso**. La osteoporosis **debilita** los huesos por falta de calcio."},
        {"tema": "Sistema óseo", "afirmacion": "¿Una fractura es cuando un hueso se rompe?", "correcto": True, "explicacion": "**Verdadero**."},

        # Articulaciones
        {"tema": "Articulaciones", "afirmacion": "¿Las articulaciones semímóviles permiten movimiento total?", "correcto": False, "explicacion": "**Falso**. Permiten movimiento **restringido**."},
        {"tema": "Articulaciones", "afirmacion": "¿Los ligamentos unen los huesos en las articulaciones?", "correcto": True, "explicacion": "**Verdadero**. Los ligamentos conectan huesos."},

        # Músculos
        {"tema": "Sistema muscular", "afirmacion": "¿Los tendones unen los músculos a los huesos?", "correcto": True, "explicacion": "**Verdadero**. Los tendones conectan músculos con huesos."},
        {"tema": "Sistema muscular", "afirmacion": "¿Los músculos involuntarios los controlamos conscientemente?", "correcto": False, "explicacion": "**Falso**. Se mueven solos, como el corazón."},
        {"tema": "Sistema muscular", "afirmacion": "¿El cuerpo tiene más de 600 músculos?", "correcto": True, "explicacion": "**Verdadero**. Más de 600 músculos."},

        # Digestivo
        {"tema": "Sistema digestivo", "afirmacion": "¿El intestino grueso absorbe los nutrientes?", "correcto": False, "explicacion": "**Falso**. Los nutrientes se absorben en el **intestino delgado**. El grueso absorbe agua."},
        {"tema": "Sistema digestivo", "afirmacion": "¿El páncreas produce jugo pancreático?", "correcto": True, "explicacion": "**Verdadero**."},
        {"tema": "Sistema digestivo", "afirmacion": "¿El quimo se forma en el estómago?", "correcto": True, "explicacion": "**Verdadero**. El estómago mezcla el bolo con jugos gástricos formando el quimo."},

        # ── TRAMPAS: afirmaciones que parecen verdaderas pero son falsas ──
        {"tema": "Sistema digestivo", "afirmacion": "¿El esófago digiere la comida con ácidos?", "correcto": False, "explicacion": "**Falso**. El esófago solo **transporta** la comida al estómago. Los ácidos están en el estómago."},
        {"tema": "Sistema digestivo", "afirmacion": "¿La faringe forma el bolo alimenticio?", "correcto": False, "explicacion": "**Falso**. El bolo se forma en la **boca** al masticar con saliva. La faringe solo permite tragar."},
        {"tema": "Sistema digestivo", "afirmacion": "¿El intestino grueso absorbe los nutrientes hacia la sangre?", "correcto": False, "explicacion": "**Falso**. Eso lo hace el **intestino DELGADO**. El grueso solo absorbe agua."},
        {"tema": "Sistema digestivo", "afirmacion": "¿El quilo se forma en el estómago?", "correcto": False, "explicacion": "**Falso**. El quilo se forma en el **intestino delgado**. El quimo se forma en el estómago."},
        {"tema": "Sistema óseo", "afirmacion": "¿Los ligamentos unen los músculos a los huesos?", "correcto": False, "explicacion": "**Falso**. Los ligamentos unen **huesos con huesos**. Los **tendones** unen músculos con huesos."},
        {"tema": "Sistema óseo", "afirmacion": "¿El radio está en la pierna?", "correcto": False, "explicacion": "**Falso**. El radio está en el **antebrazo** (del lado del pulgar). En la pierna están la tibia y el peroné."},
        {"tema": "Sistema óseo", "afirmacion": "¿El peroné es el hueso principal de la parte inferior de la pierna?", "correcto": False, "explicacion": "**Falso**. El hueso principal es la **tibia**. El peroné es el hueso delgado que acompaña a la tibia."},
        {"tema": "Sistema óseo", "afirmacion": "¿El carpo está en el pie?", "correcto": False, "explicacion": "**Falso**. El carpo está en la **muñeca**. En el pie está el **tarso**."},
        {"tema": "Sistema óseo", "afirmacion": "¿El metacarpo está en la palma de la mano?", "correcto": True, "explicacion": "**Verdadero**. El metacarpo son los huesos de la palma. El metatarso es el equivalente en el pie."},
        {"tema": "Articulaciones", "afirmacion": "¿Los tendones unen los huesos en las articulaciones?", "correcto": False, "explicacion": "**Falso**. Los **ligamentos** unen huesos. Los tendones unen músculos con huesos."},
        {"tema": "Sistema muscular", "afirmacion": "¿Los ligamentos unen los músculos a los huesos?", "correcto": False, "explicacion": "**Falso**. Los **tendones** unen músculos con huesos. Los ligamentos unen huesos con huesos."},
        {"tema": "Sistema muscular", "afirmacion": "¿El músculo cardíaco es voluntario?", "correcto": False, "explicacion": "**Falso**. El corazón es músculo **involuntario**. Late sin que lo pensemos."},
        {"tema": "Sistema muscular", "afirmacion": "¿El bíceps extiende el codo?", "correcto": False, "explicacion": "**Falso**. El bíceps **flexiona** el codo (dobla el brazo). El **tríceps** es el que lo extiende."},
        {"tema": "Sistema muscular", "afirmacion": "¿El tríceps flexiona el codo?", "correcto": False, "explicacion": "**Falso**. El tríceps **extiende** el codo (estira el brazo). El **bíceps** es el que lo flexiona."},
        {"tema": "Articulaciones", "afirmacion": "¿La columna vertebral tiene articulaciones fijas?", "correcto": False, "explicacion": "**Falso**. La columna tiene articulaciones **semímóviles** que permiten movimiento limitado."},
    ],

    # ── PREGUNTAS TRAMPA ── (opciones muy similares para confundir)
    "preguntas_trampa": [
        # Digestivo: Quimo vs Quilo
        {"tema": "Sistema digestivo", "q": "¿Cuál es la diferencia correcta entre Quimo y Quilo?\n\n*¡Cuidado! Son muy parecidos.*",
         "answer": "Quimo = estómago / Quilo = intestino delgado",
         "opciones": ["Quimo = intestino delgado / Quilo = estómago", "Quimo = estómago / Quilo = intestino delgado", "Son lo mismo, solo cambia el nombre", "Quimo = hígado / Quilo = estómago"],
         "procedure": "**Quimo** se forma en el estómago (mezcla con jugos gástricos).\n**Quilo** se forma en el intestino delgado (después de absorber nutrientes)."},

        {"tema": "Sistema digestivo", "q": "¿Cuál NO es una función del intestino DELGADO?\n\n*¡Una es trampa!*",
         "answer": "Absorber el agua",
         "opciones": ["Absorber los nutrientes", "Absorber el agua", "Formar el quilo", "Pasar nutrientes a la sangre"],
         "procedure": "El intestino delgado **absorbe nutrientes** y forma el quilo.\nAbsorber el **agua** es función del intestino **GRUESO**. ¡Esa era la trampa!"},

        {"tema": "Sistema digestivo", "q": "¿En qué orden correcto pasa la comida?\n\n*¡Todas suenan bien!*",
         "answer": "Boca → Faringe → Esófago → Estómago",
         "opciones": ["Boca → Esófago → Faringe → Estómago", "Boca → Laringe → Esófago → Estómago", "Boca → Faringe → Esófago → Estómago", "Boca → Faringe → Laringe → Estómago"],
         "procedure": "El orden correcto es: Boca → **Faringe** → **Esófago** → Estómago.\nLa laringe protege las vías respiratorias pero la comida NO pasa por ella."},

        # Óseo: pares confusos
        {"tema": "Sistema óseo", "q": "¿Cuál es la diferencia entre el RADIO y el CÚBITO?\n\n*¡Son muy parecidos!*",
         "answer": "Radio = lado del pulgar / Cúbito = lado del meñique",
         "opciones": ["Radio = lado del meñique / Cúbito = lado del pulgar", "Radio = lado del pulgar / Cúbito = lado del meñique", "Radio está en la pierna / Cúbito está en el brazo", "Son el mismo hueso con distintos nombres"],
         "procedure": "**Radio** → lado del pulgar (puedes girar la muñeca con él).\n**Cúbito** → lado del meñique (forma el codo)."},

        {"tema": "Sistema óseo", "q": "¿Cuál es la diferencia entre el CARPO y el TARSO?\n\n*¡No te confundas!*",
         "answer": "Carpo = muñeca / Tarso = tobillo",
         "opciones": ["Carpo = tobillo / Tarso = muñeca", "Carpo = muñeca / Tarso = tobillo", "Carpo = rodilla / Tarso = codo", "Carpo = palma / Tarso = planta"],
         "procedure": "**Carpo** → muñeca (mano)\n**Tarso** → tobillo (pie)\nSon equivalentes: el carpo está en la mano y el tarso en el pie."},

        {"tema": "Sistema óseo", "q": "¿Cuál NO es un hueso del ANTEBRAZO?\n\n*¡Uno es trampa!*",
         "answer": "Fémur",
         "opciones": ["Radio", "Cúbito", "Fémur", "Húmero"],
         "procedure": "El **fémur** está en el MUSLO, no en el antebrazo. Los huesos del antebrazo son el **radio** y el **cúbito**. El húmero es el hueso del brazo superior."},

        {"tema": "Sistema óseo", "q": "¿Cuál NO es un hueso de la PIERNA?\n\n*¡Cuidado con las trampas!*",
         "answer": "Peroné... espera, SÍ está en la pierna. La respuesta es: Cúbito",
         "opciones": ["Tibia", "Fémur", "Peroné", "Cúbito"],
         "procedure": "El **cúbito** está en el **antebrazo** (brazo), no en la pierna.\nEn la pierna están: **fémur** (muslo), **tibia** y **peroné** (pierna inferior)."},

        # Muscular: ligamento vs tendón
        {"tema": "Sistema muscular", "q": "¿Qué estructura une el músculo al hueso?\n\n*¡El más confundido de ciencias!*",
         "answer": "Tendón",
         "opciones": ["Ligamento", "Tendón", "Cartílago", "Nervio"],
         "procedure": "**Tendón** → une MÚSCULO con HUESO\n**Ligamento** → une HUESO con HUESO\n¡Este par confunde a todos!"},

        {"tema": "Sistema muscular", "q": "¿Qué estructura une un HUESO con otro HUESO?\n\n*¡No te confundas con el tendón!*",
         "answer": "Ligamento",
         "opciones": ["Tendón", "Ligamento", "Músculo", "Cartílago"],
         "procedure": "**Ligamento** → une HUESO con HUESO (en las articulaciones)\n**Tendón** → une MÚSCULO con HUESO\n¡Grábatelos: ten-dón = músculo-hue**so**!"},

        {"tema": "Sistema muscular", "q": "¿Cuál NO es un músculo VOLUNTARIO?\n\n*¡Uno está escondido!*",
         "answer": "Corazón (cardíaco)",
         "opciones": ["Bíceps", "Cuádriceps", "Corazón (cardíaco)", "Deltoides"],
         "procedure": "El **corazón** es músculo **involuntario** (no lo controlamos conscientemente).\nBíceps, cuádriceps y deltoides son todos voluntarios."},

        {"tema": "Sistema muscular", "q": "El bíceps FLEXIONA el codo. ¿Qué hace el TRÍCEPS?\n\n*¡Son contrarios!*",
         "answer": "Extiende el codo",
         "opciones": ["Flexiona el codo también", "Extiende el codo", "Levanta el hombro", "Mueve los dedos"],
         "procedure": "**Bíceps** → FLEXIONA (dobla) el codo\n**Tríceps** → EXTIENDE (estira) el codo\nSon músculos antagonistas: uno hace lo contrario del otro."},

        # Articulaciones: tipos
        {"tema": "Articulaciones", "q": "¿Qué tipo de articulación tiene la COLUMNA VERTEBRAL?\n\n*¡No es ni fija ni móvil del todo!*",
         "answer": "Semímóvil",
         "opciones": ["Fija", "Móvil", "Semímóvil", "Rígida"],
         "procedure": "La columna tiene articulaciones **semímóviles**: permiten movimiento limitado pero no libre como la rodilla."},

        {"tema": "Articulaciones", "q": "¿Cuál de estas articulaciones permite movimiento en TODAS DIRECCIONES?\n\n*¡Solo una puede!*",
         "answer": "Hombro",
         "opciones": ["Rodilla", "Codo", "Hombro", "Tobillo"],
         "procedure": "El **hombro** es una articulación esférica que permite movimiento en todas direcciones.\nLa rodilla y el codo solo permiten doblar/estirar (bisagra)."},
    ],

    "secuencias": [
        {"tema": "Sistema digestivo", "nombre": "el recorrido del alimento", "orden": ["boca", "faringe", "esófago", "estómago", "intestino delgado", "intestino grueso", "recto y ano"]},
    ],
}
