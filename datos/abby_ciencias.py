"""Datos de Ciencias para Abby (1er grado) — todo visual con botones simples."""

IMG = "cienciasabby"

DATA = {
    "topics": {
        "Partes del cuerpo": {
            "aprendizaje": "Identificar las partes del cuerpo humano",
            "indicador": "Identifica partes del cuerpo humano",
        },
        "Los sentidos": {
            "aprendizaje": "Reconocer los cinco sentidos y sus órganos",
            "indicador": "Reconoce los sentidos del ser humano",
        },
        "Hábitos de salud": {
            "aprendizaje": "Reconocer hábitos de higiene, alimentación y ejercicio",
            "indicador": "Reconoce hábitos para el cuidado de la salud",
        },
        "Prevención de accidentes": {
            "aprendizaje": "Identificar situaciones de riesgo y cómo prevenirlas",
            "indicador": "Identifica situaciones que pueden afectar el bienestar",
        },
        "Violencia": {
            "aprendizaje": "Reconocer tipos de violencia y cómo pedir ayuda",
            "indicador": "Identifica tipos de violencia y sabe a quién acudir",
        },
    },

    "tags": {
        "sentido": ["Vista", "Oído", "Olfato", "Gusto", "Tacto"],
        "extremidad": ["Superior (brazo)", "Inferior (pierna)"],
    },

    "partes": [
        # --- CUERPO COMPLETO ---
        {"nombre": "cuerpo completo", "img": f"{IMG}/cuerpo_completo.webp",
         "funcion": "El cuerpo tiene cabeza, tronco, abdomen y extremidades", "grupo": "Partes del cuerpo"},

        # --- CABEZA Y CARA ---
        {"nombre": "cabeza", "img": f"{IMG}/cabeza.webp",
         "funcion": "Parte superior del cuerpo donde está el cráneo y la cara", "grupo": "Partes del cuerpo"},
        {"nombre": "cráneo", "img": f"{IMG}/craneo.jpg",
         "funcion": "Hueso duro que protege el cerebro", "grupo": "Partes del cuerpo"},
        {"nombre": "frente", "img": f"{IMG}/frente.webp",
         "funcion": "Parte superior de la cara", "grupo": "Partes del cuerpo"},
        {"nombre": "ojos", "img": f"{IMG}/ojos.jpg",
         "funcion": "Sirven para ver", "grupo": "Partes del cuerpo"},
        {"nombre": "cejas", "img": f"{IMG}/cejas.jpg",
         "funcion": "Pelos sobre los ojos que protegen de la lluvia y el sudor", "grupo": "Partes del cuerpo"},
        {"nombre": "pestañas", "img": f"{IMG}/pestanas.jpeg",
         "funcion": "Pelos en los párpados que protegen los ojos", "grupo": "Partes del cuerpo"},
        {"nombre": "nariz", "img": f"{IMG}/nariz.avif",
         "funcion": "Sirve para oler y respirar", "grupo": "Partes del cuerpo"},
        {"nombre": "orejas", "img": f"{IMG}/orejas.jpeg",
         "funcion": "Sirven para escuchar", "grupo": "Partes del cuerpo"},
        {"nombre": "boca", "img": f"{IMG}/boca.webp",
         "funcion": "Sirve para comer, hablar y saborear", "grupo": "Partes del cuerpo"},
        {"nombre": "mejillas", "img": f"{IMG}/mejillas.jpg",
         "funcion": "Partes laterales de la cara", "grupo": "Partes del cuerpo"},
        {"nombre": "barbilla", "img": f"{IMG}/barbilla.webp",
         "funcion": "Parte inferior de la cara, debajo de la boca", "grupo": "Partes del cuerpo"},

        # --- TRONCO ---
        {"nombre": "tronco", "img": f"{IMG}/tronco.webp",
         "funcion": "Parte central del cuerpo donde están los órganos importantes", "grupo": "Partes del cuerpo"},
        {"nombre": "tórax", "img": f"{IMG}/torax.jpeg",
         "funcion": "Parte superior del tronco donde están el corazón y los pulmones", "grupo": "Partes del cuerpo"},
        {"nombre": "abdomen", "img": f"{IMG}/abdomen.png",
         "funcion": "Parte del tronco donde están el estómago y los intestinos", "grupo": "Partes del cuerpo"},
        {"nombre": "glúteos", "img": f"{IMG}/gluteos.webp",
         "funcion": "Parte trasera del tronco", "grupo": "Partes del cuerpo"},

        # --- EXTREMIDADES SUPERIORES ---
        {"nombre": "extremidades superiores", "img": f"{IMG}/extremidades superiores.jpg",
         "funcion": "Los brazos: sirven para agarrar, cargar y hacer actividades", "grupo": "Partes del cuerpo",
         "tags": {"extremidad": "Superior (brazo)"}},
        {"nombre": "hombro", "img": f"{IMG}/hombro.jpg",
         "funcion": "Une el brazo con el tronco", "grupo": "Partes del cuerpo"},
        {"nombre": "codo", "img": f"{IMG}/codo.webp",
         "funcion": "Articulación en el medio del brazo que permite doblarlo", "grupo": "Partes del cuerpo"},
        {"nombre": "antebrazo", "img": f"{IMG}/antebrazo.jpg",
         "funcion": "Parte del brazo entre el codo y la muñeca", "grupo": "Partes del cuerpo"},
        {"nombre": "muñeca", "img": f"{IMG}/muneca.jpg",
         "funcion": "Une el antebrazo con la mano", "grupo": "Partes del cuerpo"},
        {"nombre": "mano", "img": f"{IMG}/mano.webp",
         "funcion": "Tiene cinco dedos y sirve para agarrar cosas", "grupo": "Partes del cuerpo"},
        {"nombre": "dedos de la mano", "img": f"{IMG}/dedos_mano.jpg",
         "funcion": "Cinco dedos en cada mano para agarrar y tocar", "grupo": "Partes del cuerpo"},

        # --- EXTREMIDADES INFERIORES ---
        {"nombre": "extremidades inferiores", "img": f"{IMG}/extremidades inferiores.jpeg",
         "funcion": "Las piernas: sirven para caminar, correr y saltar", "grupo": "Partes del cuerpo",
         "tags": {"extremidad": "Inferior (pierna)"}},
        {"nombre": "muslo", "img": f"{IMG}/muslo.webp",
         "funcion": "Parte superior de la pierna", "grupo": "Partes del cuerpo"},
        {"nombre": "rodilla", "img": f"{IMG}/rodilla.webp",
         "funcion": "Articulación en el medio de la pierna que permite doblarla", "grupo": "Partes del cuerpo"},
        {"nombre": "pierna", "img": f"{IMG}/pierna.webp",
         "funcion": "Parte entre la rodilla y el tobillo", "grupo": "Partes del cuerpo"},
        {"nombre": "tobillo", "img": f"{IMG}/tobillo.webp",
         "funcion": "Une la pierna con el pie", "grupo": "Partes del cuerpo"},
        {"nombre": "talón", "img": f"{IMG}/talon.jpg",
         "funcion": "Parte trasera del pie", "grupo": "Partes del cuerpo"},
        {"nombre": "pie", "img": f"{IMG}/pie.avif",
         "funcion": "Tiene cinco dedos y sirve para caminar", "grupo": "Partes del cuerpo"},
        {"nombre": "dedos del pie", "img": f"{IMG}/dedos_pie.jpeg",
         "funcion": "Cinco dedos en cada pie", "grupo": "Partes del cuerpo"},

        # --- SENTIDOS ---
        {"nombre": "vista", "img": f"{IMG}/vista.jpeg",
         "funcion": "Sentido que nos permite ver con los ojos", "grupo": "Los sentidos",
         "tags": {"sentido": "Vista"}},
        {"nombre": "oído", "img": f"{IMG}/oido.webp",
         "funcion": "Sentido que nos permite escuchar con las orejas", "grupo": "Los sentidos",
         "tags": {"sentido": "Oído"}},
        {"nombre": "olfato", "img": f"{IMG}/olfato.webp",
         "funcion": "Sentido que nos permite oler con la nariz", "grupo": "Los sentidos",
         "tags": {"sentido": "Olfato"}},
        {"nombre": "gusto", "img": f"{IMG}/gusto.avif",
         "funcion": "Sentido que nos permite saborear con la boca y la lengua", "grupo": "Los sentidos",
         "tags": {"sentido": "Gusto"}},
        {"nombre": "tacto", "img": f"{IMG}/tacto.jpg",
         "funcion": "Sentido que nos permite tocar y sentir con la piel y las manos", "grupo": "Los sentidos",
         "tags": {"sentido": "Tacto"}},

        # --- HÁBITOS ---
        {"nombre": "cepillar los dientes", "img": f"{IMG}/cepillar_dientes.webp",
         "funcion": "Hábito de higiene para tener dientes limpios y sanos", "grupo": "Hábitos de salud"},
        {"nombre": "bañarse", "img": f"{IMG}/banarse.webp",
         "funcion": "Hábito de higiene para estar limpio y saludable", "grupo": "Hábitos de salud"},
        {"nombre": "lavar las manos", "img": f"{IMG}/lavar_manos.jpg",
         "funcion": "Hábito de higiene para prevenir enfermedades", "grupo": "Hábitos de salud"},
        {"nombre": "comer saludable", "img": f"{IMG}/comer_saludable.avif",
         "funcion": "Hábito alimenticio para crecer sano y fuerte", "grupo": "Hábitos de salud"},
        {"nombre": "hacer ejercicio", "img": f"{IMG}/hacer_ejercicio.jpg",
         "funcion": "Actividad que mejora los pulmones, músculos y el corazón", "grupo": "Hábitos de salud"},

        # --- PREVENCIÓN ---
        {"nombre": "no tocar enchufes", "img": f"{IMG}/no_tocar_enchufes.avif",
         "funcion": "Los enchufes pueden causar quemaduras, nunca los toques", "grupo": "Prevención de accidentes",
         "tipo_pregunta": "enfermedad"},
        {"nombre": "no jugar con fuego", "img": f"{IMG}/no_jugar_fuego.webp",
         "funcion": "El fuego puede quemarte, nunca juegues con él", "grupo": "Prevención de accidentes",
         "tipo_pregunta": "enfermedad"},
        {"nombre": "cruzar la calle con un adulto", "img": f"{IMG}/cruzar_calle.webp",
         "funcion": "Camina en compañía de un adulto para estar seguro", "grupo": "Prevención de accidentes",
         "tipo_pregunta": "enfermedad"},

        # --- VIOLENCIA ---
        {"nombre": "decir no", "img": f"{IMG}/decir_no.webp",
         "funcion": "Tienes derecho a decir NO si alguien te hace sentir mal", "grupo": "Violencia",
         "tipo_pregunta": "enfermedad"},
        {"nombre": "contar a un adulto", "img": f"{IMG}/contar_adulto.webp",
         "funcion": "Si alguien te hace daño, cuéntaselo a un adulto de confianza", "grupo": "Violencia",
         "tipo_pregunta": "enfermedad"},
    ],

    "preguntas": [
        # Partes del cuerpo
        {"tema": "Partes del cuerpo", "q": "¿Cuáles son las partes principales del cuerpo?", "answer": "Cabeza, tronco, abdomen y extremidades", "opciones": ["Cabeza, tronco, abdomen y extremidades", "Solo la cabeza y los pies", "Brazos y piernas", "Ojos y nariz"], "procedure": "Las partes principales son: **cabeza, tronco, abdomen y extremidades**."},
        {"tema": "Partes del cuerpo", "q": "¿Cómo se llaman los brazos?", "answer": "Extremidades superiores", "opciones": ["Extremidades superiores", "Extremidades inferiores", "Tronco", "Abdomen"], "procedure": "Los brazos se llaman **extremidades superiores**."},
        {"tema": "Partes del cuerpo", "q": "¿Cómo se llaman las piernas?", "answer": "Extremidades inferiores", "opciones": ["Extremidades superiores", "Extremidades inferiores", "Tronco", "Cabeza"], "procedure": "Las piernas se llaman **extremidades inferiores**."},
        {"tema": "Partes del cuerpo", "q": "¿Qué protege el cráneo?", "answer": "El cerebro", "opciones": ["El cerebro", "El corazón", "Los pulmones", "El estómago"], "procedure": "El cráneo protege **el cerebro**."},
        {"tema": "Partes del cuerpo", "q": "¿Cuántos dedos tiene cada mano?", "answer": "5", "opciones": ["3", "4", "5", "6"], "procedure": "Cada mano tiene **5 dedos**."},
        {"tema": "Partes del cuerpo", "q": "¿Cuántos dedos tiene cada pie?", "answer": "5", "opciones": ["3", "4", "5", "6"], "procedure": "Cada pie tiene **5 dedos**."},
        {"tema": "Partes del cuerpo", "q": "¿Dónde están el corazón y los pulmones?", "answer": "En el tórax", "opciones": ["En el tórax", "En el abdomen", "En la cabeza", "En los brazos"], "procedure": "El corazón y los pulmones están en el **tórax**."},

        # Sentidos
        {"tema": "Los sentidos", "q": "¿Cuántos sentidos tiene el ser humano?", "answer": "5", "opciones": ["3", "4", "5", "6"], "procedure": "El ser humano tiene **5 sentidos**."},
        {"tema": "Los sentidos", "q": "¿Con qué órgano vemos?", "answer": "Ojos", "opciones": ["Ojos", "Orejas", "Nariz", "Manos"], "procedure": "Vemos con los **ojos**."},
        {"tema": "Los sentidos", "q": "¿Con qué órgano escuchamos?", "answer": "Orejas", "opciones": ["Ojos", "Orejas", "Nariz", "Boca"], "procedure": "Escuchamos con las **orejas**."},
        {"tema": "Los sentidos", "q": "¿Con qué órgano olemos?", "answer": "Nariz", "opciones": ["Ojos", "Orejas", "Nariz", "Manos"], "procedure": "Olemos con la **nariz**."},
        {"tema": "Los sentidos", "q": "¿Con qué órgano saboreamos?", "answer": "Boca y lengua", "opciones": ["Ojos", "Orejas", "Nariz", "Boca y lengua"], "procedure": "Saboreamos con la **boca y la lengua**."},
        {"tema": "Los sentidos", "q": "¿Con qué sentimos al tocar?", "answer": "Piel y manos", "opciones": ["Ojos", "Orejas", "Nariz", "Piel y manos"], "procedure": "Tocamos con la **piel y las manos**."},
        {"tema": "Los sentidos", "q": "¿Qué sentido nos avisa si hay humo cerca?", "answer": "Olfato", "opciones": ["Vista", "Oído", "Olfato", "Tacto"], "procedure": "El **olfato** nos avisa si hay humo cerca."},

        # Hábitos
        {"tema": "Hábitos de salud", "q": "¿Qué hábito ayuda a prevenir enfermedades lavándose?", "answer": "Lavar las manos", "opciones": ["Lavar las manos", "Comer dulces", "Ver televisión", "Correr"], "procedure": "**Lavar las manos** previene enfermedades."},
        {"tema": "Hábitos de salud", "q": "¿Qué hábito cuida tus dientes?", "answer": "Cepillar los dientes", "opciones": ["Cepillar los dientes", "Comer dulces", "Bañarse", "Dormir"], "procedure": "**Cepillar los dientes** los mantiene limpios y sanos."},
        {"tema": "Hábitos de salud", "q": "¿Qué beneficio tiene hacer ejercicio?", "answer": "Mejora los pulmones, músculos y el corazón", "opciones": ["Mejora los pulmones, músculos y el corazón", "Da sueño", "Hace daño", "No tiene beneficios"], "procedure": "El ejercicio **mejora pulmones, músculos y corazón**."},
        {"tema": "Hábitos de salud", "q": "¿Qué debes beber para mantenerte sano?", "answer": "Agua potable", "opciones": ["Agua potable", "Refresco", "Jugo con azúcar", "Café"], "procedure": "Debes beber **agua potable**."},

        # Prevención
        {"tema": "Prevención de accidentes", "q": "¿Qué puedes sufrir si tocas un enchufe?", "answer": "Quemaduras", "opciones": ["Quemaduras", "Frío", "Sueño", "Hambre"], "procedure": "Los enchufes pueden causarte **quemaduras**."},
        {"tema": "Prevención de accidentes", "q": "¿Con quién debes cruzar la calle?", "answer": "Con un adulto", "opciones": ["Con un adulto", "Solo", "Con tu mascota", "Corriendo"], "procedure": "Debes cruzar la calle **con un adulto**."},
        {"tema": "Prevención de accidentes", "q": "¿Qué puede pasar si corres por las escaleras?", "answer": "Puedes caerte y golpearte", "opciones": ["Puedes caerte y golpearte", "Nada malo", "Llegas más rápido", "Te pones fuerte"], "procedure": "Corriendo en escaleras **puedes caerte y golpearte**."},
        {"tema": "Prevención de accidentes", "q": "¿Qué debes hacer si ves un objeto desconocido?", "answer": "No tocarlo ni jugar con él", "opciones": ["No tocarlo ni jugar con él", "Meterlo a la boca", "Jugar con él", "Tirarlo al agua"], "procedure": "**No toques ni juegues** con objetos desconocidos."},

        # Violencia
        {"tema": "Violencia", "q": "¿Qué tipo de violencia es cuando alguien te golpea?", "answer": "Violencia física", "opciones": ["Violencia física", "Violencia psicológica", "Violencia sexual", "No es violencia"], "procedure": "Golpear es **violencia física**."},
        {"tema": "Violencia", "q": "¿Qué tipo de violencia es cuando alguien se burla de ti?", "answer": "Violencia psicológica", "opciones": ["Violencia física", "Violencia psicológica", "Violencia sexual", "No es violencia"], "procedure": "Burlarse es **violencia psicológica**."},
        {"tema": "Violencia", "q": "Si alguien te hace daño, ¿qué debes hacer?", "answer": "Contárselo a un adulto de confianza", "opciones": ["Contárselo a un adulto de confianza", "Quedarte callado", "Esconderte", "Llorar solo"], "procedure": "Debes **contárselo a un adulto de confianza**."},
        {"tema": "Violencia", "q": "¿Qué derecho tienen todos los niños?", "answer": "Vivir en un ambiente de paz y amor", "opciones": ["Vivir en un ambiente de paz y amor", "Trabajar", "No ir a la escuela", "Estar solos"], "procedure": "Los niños tienen derecho a vivir en **paz y amor**."},
    ],

    "verdadero_falso": [
        {"tema": "Partes del cuerpo", "afirmacion": "¿Los brazos se llaman extremidades superiores?", "correcto": True, "explicacion": "**Verdadero**. Los brazos son las extremidades superiores."},
        {"tema": "Partes del cuerpo", "afirmacion": "¿El cráneo protege el corazón?", "correcto": False, "explicacion": "**Falso**. El cráneo protege el **cerebro**."},
        {"tema": "Los sentidos", "afirmacion": "¿Tenemos 5 sentidos?", "correcto": True, "explicacion": "**Verdadero**. Vista, oído, olfato, gusto y tacto."},
        {"tema": "Los sentidos", "afirmacion": "¿Olemos con los ojos?", "correcto": False, "explicacion": "**Falso**. Olemos con la **nariz**."},
        {"tema": "Hábitos de salud", "afirmacion": "¿Lavar las manos ayuda a prevenir enfermedades?", "correcto": True, "explicacion": "**Verdadero**."},
        {"tema": "Hábitos de salud", "afirmacion": "¿Comer muchos dulces es un hábito saludable?", "correcto": False, "explicacion": "**Falso**. Debemos comer alimentos **nutritivos**."},
        {"tema": "Prevención de accidentes", "afirmacion": "¿Puedes tocar los enchufes sin peligro?", "correcto": False, "explicacion": "**Falso**. Los enchufes pueden causarte **quemaduras**."},
        {"tema": "Violencia", "afirmacion": "¿Debes contarle a un adulto si alguien te hace daño?", "correcto": True, "explicacion": "**Verdadero**. Siempre cuéntaselo a un adulto de confianza."},
    ],

    "secuencias": [],
}
