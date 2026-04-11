"""
Motor universal de preguntas.

Formato de datos que espera:

MATERIA = {
    "topics": {
        "Nombre del tema": {
            "aprendizaje": "...",
            "indicador": "...",
        }
    },
    # Para materias con imágenes (ciencias):
    "partes": [
        {"nombre": "x", "img": "ruta/img.jpg", "funcion": "...", "grupo": "tema", "tags": {"tipo": "voluntario"}},
    ],
    # Para materias de texto (mate, sociales, español):
    "preguntas": [
        {"tema": "Nombre del tema", "q": "pregunta", "answer": "respuesta", "opciones": ["a","b","c","d"], "procedure": "..."},
    ],
    # Para V/F:
    "verdadero_falso": [
        {"tema": "Nombre del tema", "afirmacion": "...", "correcto": True, "explicacion": "..."},
    ],
}
"""
import random
import os

BASE = os.path.dirname(os.path.abspath(__file__))


def _img_path(relative):
    return os.path.join(BASE, "imagenes", relative)


def _img_exists(relative):
    return os.path.exists(_img_path(relative))


def _pick_distractors(pool, correcta, n=3):
    """Elige n distractores del pool excluyendo la correcta."""
    otros = [p for p in pool if p["nombre"] != correcta["nombre"]]
    return random.sample(otros, min(n, len(otros)))


# ============================================================
# GENERADORES DE PREGUNTAS CON BOTONES
# ============================================================

def _gen_seleccion_multiple(partes):
    """Imagen → ¿Qué parte/enfermedad es? [4 botones]"""
    validas = [p for p in partes if _img_exists(p["img"])]
    if len(validas) < 2:
        return None
    correcta = random.choice(validas)
    distractores = _pick_distractors(validas, correcta)
    opciones = [d["nombre"] for d in distractores] + [correcta["nombre"]]
    random.shuffle(opciones)
    tipo = correcta.get("tipo_pregunta", "funcion")
    pregunta = "¿Qué enfermedad se muestra en la imagen?" if tipo == "enfermedad" else "¿Qué se muestra en la imagen?"
    return dict(
        question=pregunta,
        imagen=_img_path(correcta["img"]),
        opciones_btn=opciones,
        answer=correcta["nombre"],
        is_numeric=False,
        procedure=f"**{correcta['nombre']}**: {correcta['funcion']}")


def _gen_seleccion_funcion(partes):
    """Imagen → ¿Cuál es su función/descripción? [4 botones]"""
    validas = [p for p in partes if _img_exists(p["img"])]
    if len(validas) < 2:
        return None
    correcta = random.choice(validas)
    distractores = _pick_distractors(validas, correcta)
    opciones = [d["funcion"] for d in distractores] + [correcta["funcion"]]
    random.shuffle(opciones)
    # Usar pregunta apropiada según tipo
    tipo = correcta.get("tipo_pregunta", "funcion")
    if tipo == "enfermedad":
        pregunta = f"¿Qué es la/el **{correcta['nombre']}**?"
    else:
        pregunta = "Observa la imagen. ¿Cuál es su función?"
    return dict(
        question=pregunta,
        imagen=_img_path(correcta["img"]),
        opciones_btn=opciones,
        answer=correcta["funcion"],
        is_numeric=False,
        procedure=f"**{correcta['nombre']}**: {correcta['funcion']}")


def _gen_verdadero_falso_img(partes):
    """Imagen + función → ¿V o F?"""
    validas = [p for p in partes if _img_exists(p["img"])]
    if len(validas) < 2:
        return None
    parte = random.choice(validas)
    es_v = random.choice([True, False])
    if es_v:
        func = parte["funcion"]
        answer = "✅ Verdadero"
        proc = f"**Verdadero**. Es: {parte['nombre']} — {parte['funcion']}"
    else:
        otra = random.choice([p for p in validas if p["nombre"] != parte["nombre"]])
        func = otra["funcion"]
        answer = "❌ Falso"
        proc = f"**Falso**. Es: {parte['nombre']} — {parte['funcion']}\n\nLa función mostrada era de: {otra['nombre']}"
    return dict(
        question="Observa la imagen. ¿La descripción es verdadera o falsa?",
        texto_comparar=f"📋 {func}",
        imagen=_img_path(parte["img"]),
        opciones_btn=["✅ Verdadero", "❌ Falso"],
        answer=answer,
        is_numeric=False,
        procedure=proc)


def _gen_asociar(partes):
    """Imagen + función → ¿Sí o No?"""
    validas = [p for p in partes if _img_exists(p["img"])]
    if len(validas) < 2:
        return None
    parte = random.choice(validas)
    coincide = random.choice([True, False])
    if coincide:
        func = parte["funcion"]
        answer = "👍 Sí"
        proc = f"**Sí**. Es: {parte['nombre']} — {parte['funcion']}"
    else:
        otra = random.choice([p for p in validas if p["nombre"] != parte["nombre"]])
        func = otra["funcion"]
        answer = "👎 No"
        proc = f"**No**. Es: {parte['nombre']} — {parte['funcion']}\n\nLa función mostrada era de: {otra['nombre']}"
    return dict(
        question="Observa la imagen. ¿La descripción corresponde a lo que ves?",
        texto_comparar=f"📋 {func}",
        imagen=_img_path(parte["img"]),
        opciones_btn=["👍 Sí", "👎 No"],
        answer=answer,
        is_numeric=False,
        procedure=proc)


def _gen_completar(partes):
    """Completa la oración. Solo usa partes con función corta (menos de 45 chars)."""
    validas = [p for p in partes if _img_exists(p["img"]) and len(p.get("funcion", "")) < 45]
    if len(validas) < 2:
        return None
    correcta = random.choice(validas)
    distractores = _pick_distractors(validas, correcta)
    opciones = [d["nombre"] for d in distractores] + [correcta["nombre"]]
    random.shuffle(opciones)
    return dict(
        question=f"Completa:\n\n«El/La _______ {correcta['funcion'].lower()}»",
        opciones_btn=opciones,
        answer=correcta["nombre"],
        is_numeric=False,
        procedure=f"**{correcta['nombre']}**: {correcta['funcion']}")


def _gen_comparar_imagenes(partes):
    """2 imágenes lado a lado → ¿Cuál es X?"""
    validas = [p for p in partes if _img_exists(p["img"])]
    if len(validas) < 2:
        return None
    dos = random.sample(validas, 2)
    correcta = random.choice(dos)
    return dict(
        question=f"¿Cuál de estas imágenes muestra: **{correcta['nombre']}**?",
        imagen=_img_path(dos[0]["img"]),
        imagen2=_img_path(dos[1]["img"]),
        opciones_btn=["Imagen 1", "Imagen 2"],
        answer="Imagen 1" if dos[0]["nombre"] == correcta["nombre"] else "Imagen 2",
        is_numeric=False,
        procedure=f"**{correcta['nombre']}**: {correcta['funcion']}\n\nImagen 1: {dos[0]['nombre']}\nImagen 2: {dos[1]['nombre']}")


def _gen_clasificar_tag(partes, tag_key, opciones_tag):
    """Imagen → ¿Es [tag_valor1] o [tag_valor2]?"""
    validas = [p for p in partes if _img_exists(p["img"]) and tag_key in p.get("tags", {})]
    if not validas:
        return None
    parte = random.choice(validas)
    answer = parte["tags"][tag_key]
    return dict(
        question=f"Observa la imagen. ¿Cómo se clasifica? ({' o '.join(opciones_tag)})",
        imagen=_img_path(parte["img"]),
        opciones_btn=opciones_tag,
        answer=answer,
        is_numeric=False,
        procedure=f"**{parte['nombre']}** es **{answer}**")


def _gen_desde_pregunta_texto(preg):
    """Convierte pregunta de texto con opciones a formato botones."""
    q = dict(
        question=preg["q"],
        answer=preg["answer"],
        opciones_btn=preg["opciones"],
        is_numeric=False,
        procedure=preg.get("procedure", f"Respuesta: **{preg['answer']}**"))
    if preg.get("imagen"):
        q["imagen"] = _img_path(preg["imagen"])
    return q


def _gen_desde_vf(vf):
    """Convierte V/F a formato botones."""
    answer = "✅ Verdadero" if vf["correcto"] else "❌ Falso"
    return dict(
        question=vf["afirmacion"],
        opciones_btn=["✅ Verdadero", "❌ Falso"],
        answer=answer,
        is_numeric=False,
        procedure=vf["explicacion"])


def _gen_orden(secuencia, nombre_secuencia):
    """Genera pregunta de orden: ¿qué viene primero/después?"""
    if len(secuencia) < 2:
        return None
    idx = random.randint(0, len(secuencia) - 2)
    a, b = secuencia[idx], secuencia[idx + 1]
    if random.choice([True, False]):
        opciones = [a, b]
        random.shuffle(opciones)
        return dict(
            question=f"En {nombre_secuencia}, ¿qué viene PRIMERO?",
            opciones_btn=opciones,
            answer=a,
            is_numeric=False,
            procedure=f"Orden: {' → '.join(secuencia)}\n\n**{a}** viene antes que {b}")
    otras = [x for x in secuencia if x != a and x != b]
    distractores = random.sample(otras, min(2, len(otras)))
    opciones = distractores + [b]
    random.shuffle(opciones)
    return dict(
        question=f"En {nombre_secuencia}, ¿qué viene DESPUÉS de **{a}**?",
        opciones_btn=opciones,
        answer=b,
        is_numeric=False,
        procedure=f"Orden: {' → '.join(secuencia)}\n\nDespués de {a} viene **{b}**")


# ============================================================
# GENERADOR PRINCIPAL
# ============================================================

def generate_question(materia_data, topic, dificultad="Normal"):
    """
    Genera una pregunta aleatoria para el tema dado.
    materia_data: dict con keys 'topics', y opcionalmente 'partes', 'preguntas', 'verdadero_falso', 'secuencias', 'tags'
    """
    img_generators = []   # generadores que usan imágenes
    txt_generators = []   # generadores de texto puro

    # Preguntas con imágenes (partes)
    partes_tema = [p for p in materia_data.get("partes", []) if p.get("grupo") == topic]
    if len(partes_tema) >= 2:
        img_generators.extend([
            lambda pt=partes_tema: _gen_seleccion_multiple(pt),
            lambda pt=partes_tema: _gen_seleccion_funcion(pt),
            lambda pt=partes_tema: _gen_verdadero_falso_img(pt),
            lambda pt=partes_tema: _gen_asociar(pt),
            lambda pt=partes_tema: _gen_comparar_imagenes(pt),
        ])
        txt_generators.append(lambda pt=partes_tema: _gen_completar(pt))
        # Tags (voluntario/involuntario, móvil/inmóvil, etc.)
        for tag_key, tag_opciones in materia_data.get("tags", {}).items():
            tagged = [p for p in partes_tema if tag_key in p.get("tags", {})]
            if tagged:
                img_generators.append(lambda tk=tag_key, to=tag_opciones, pt=partes_tema: _gen_clasificar_tag(pt, tk, to))

    # Preguntas de texto con opciones
    preguntas_tema = [p for p in materia_data.get("preguntas", []) if p.get("tema") == topic]
    for preg in preguntas_tema:
        txt_generators.append(lambda p=preg: _gen_desde_pregunta_texto(p))

    # Preguntas trampa (solo en Super/Mega Difícil)
    if dificultad in ("💀 Super Difícil", "☠️ Mega Difícil"):
        trampa_tema = [p for p in materia_data.get("preguntas_trampa", []) if p.get("tema") == topic]
        for preg in trampa_tema:
            txt_generators.append(lambda p=preg: _gen_desde_pregunta_texto(p))

    # Verdadero/Falso
    vf_tema = [v for v in materia_data.get("verdadero_falso", []) if v.get("tema") == topic]
    for vf in vf_tema:
        txt_generators.append(lambda v=vf: _gen_desde_vf(v))

    # Secuencias (ordenar)
    for seq in materia_data.get("secuencias", []):
        if seq.get("tema") == topic:
            txt_generators.append(lambda s=seq: _gen_orden(s["orden"], s["nombre"]))

    # Preguntas dinámicas (mate, etc.)
    dyn = materia_data.get("dynamic_generator")
    if dyn:
        def _dyn_gen(d=dyn):
            preg = d(topic)
            # Solo convertir si tiene opciones (botones); ignorar preguntas de escribir
            if preg and preg.get("opciones"):
                return _gen_desde_pregunta_texto(preg)
            return None
        txt_generators.append(_dyn_gen)

    # Intercalar img y txt para dar ~50% de probabilidad a cada categoría
    # independientemente de cuántos haya en cada grupo
    random.shuffle(img_generators)
    random.shuffle(txt_generators)

    if img_generators and txt_generators:
        # Alternar: img, txt, img, txt… empezando por la categoría aleatoria
        a, b = (img_generators, txt_generators) if random.random() < 0.5 else (txt_generators, img_generators)
        generators = [x for pair in zip(a, b) for x in pair]
        # Añadir los que sobran (si una lista es más larga)
        generators += a[len(b):] + b[len(a):]
    else:
        generators = img_generators + txt_generators

    if not generators:
        return dict(question="🚧 No hay preguntas disponibles para este tema", answer="ok",
                    opciones_btn=["OK"], is_numeric=False, procedure="", topic=topic)

    for gen in generators:
        q = gen()
        if q:
            q['topic'] = topic
            q = _aplicar_dificultad(q, dificultad, materia_data.get("partes", []))
            return q

    return dict(question="🚧 No se pudo generar pregunta", answer="ok",
                opciones_btn=["OK"], is_numeric=False, procedure="", topic=topic)


def _aplicar_dificultad(q, dificultad, all_partes):
    """Modifica la pregunta para Super/Mega Difícil: distractores trampa y texto libre."""
    if dificultad not in ("💀 Super Difícil", "☠️ Mega Difícil"):
        return q

    opciones = q.get("opciones_btn")
    correct = q.get("answer", "")

    # Solo modificar preguntas con 4 opciones donde la respuesta esté en las opciones
    if opciones and len(opciones) >= 4 and correct in opciones:
        # Determinar si la respuesta es un nombre de parte o una función
        nombres_pool = [p["nombre"] for p in all_partes if p["nombre"] != correct]
        funciones_pool = [p["funcion"] for p in all_partes if p["funcion"] != correct]

        all_nombres = {p["nombre"] for p in all_partes}
        all_funciones = {p["funcion"] for p in all_partes}

        if correct in all_nombres and len(nombres_pool) >= 3:
            # Reemplazar distractores con nombres de OTRAS partes del cuerpo (confusores)
            nuevos = random.sample(nombres_pool, 3)
            nuevas_opciones = nuevos + [correct]
            random.shuffle(nuevas_opciones)
            q["opciones_btn"] = nuevas_opciones

        elif correct in all_funciones and len(funciones_pool) >= 3:
            # Reemplazar distractores con funciones de otras partes (muy confuso)
            nuevos = random.sample(funciones_pool, 3)
            nuevas_opciones = nuevos + [correct]
            random.shuffle(nuevas_opciones)
            q["opciones_btn"] = nuevas_opciones

    # Prefijo visual
    if dificultad == "💀 Super Difícil" and not q["question"].startswith("💀"):
        q["question"] = "💀 " + q["question"]
    elif dificultad == "☠️ Mega Difícil" and not q["question"].startswith("☠️"):
        q["question"] = "☠️ " + q["question"]

    return q
