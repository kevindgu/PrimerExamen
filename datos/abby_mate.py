"""Matemáticas para Abby (1er grado) — Prueba martes 14 de abril 2025."""
import random
import os

_BASE_IMG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         "imagenes", "matemabby")

def _img(nombre):
    """Ruta completa a imagen en imagenes/matemabby/"""
    return os.path.join(_BASE_IMG, nombre)

def _img_ok(nombre):
    return os.path.exists(_img(nombre))

def _img_rel(nombre):
    """Ruta relativa que usa engine.py para construir la ruta final."""
    return f"matemabby/{nombre}"


# ════════════════════════════════════════════════════════════════
# TEMA 1 — Comparar tamaños
# ════════════════════════════════════════════════════════════════
_PARES_TAMANO = [
    ("un elefante", "una hormiga"),
    ("un árbol", "una flor"),
    ("una montaña", "una piedra pequeña"),
    ("un autobús", "un carro de juguete"),
    ("una casa", "una caja pequeña"),
    ("una ballena", "un pececito"),
    ("un camión grande", "una bicicleta"),
    ("un gigante", "un ratoncito"),
    ("un edificio", "una silla"),
    ("una jirafa", "un conejo"),
]

def _gen_comparar_tamano():
    tipo = random.choice(["grande_que", "pequeno_que", "igual", "completar"])

    if tipo == "igual":
        obj = random.choice([
            "dos manzanas del mismo tamaño",
            "dos pelotas iguales",
            "dos libros del mismo tamaño",
            "dos zapatos iguales",
        ])
        correcta = "tan grande como"
        opciones = [correcta, "más grande que", "más pequeño que", "mucho más grande"]
        random.shuffle(opciones)
        return {
            "q": f"Hay {obj}. ¿Cómo se comparan?",
            "answer": correcta,
            "opciones": opciones,
            "procedure": "Cuando dos cosas miden lo mismo decimos: uno es **tan grande como** el otro.",
        }

    if tipo == "completar":
        grande, pequeno = random.choice(_PARES_TAMANO)
        opciones = ["más grande que", "más pequeño que", "tan grande como", "igual a"]
        random.shuffle(opciones)
        return {
            "q": f"Completa: {grande.capitalize()} es _____ {pequeno}.",
            "answer": "más grande que",
            "opciones": opciones,
            "procedure": f"{grande.capitalize()} es **más grande que** {pequeno}.",
        }

    grande, pequeno = random.choice(_PARES_TAMANO)
    if tipo == "grande_que":
        correcta = "más grande que"
        q = f"¿Cómo es {grande} comparado con {pequeno}?"
        proc = f"{grande.capitalize()} es **más grande que** {pequeno}."
    else:
        correcta = "más pequeño que"
        q = f"¿Cómo es {pequeno} comparado con {grande}?"
        proc = f"{pequeno.capitalize()} es **más pequeño que** {grande}."

    distractores = [x for x in ["más grande que", "más pequeño que", "tan grande como", "igual que"] if x != correcta]
    opciones = [correcta] + random.sample(distractores, 3)
    random.shuffle(opciones)
    return {"q": q, "answer": correcta, "opciones": opciones, "procedure": proc}


# ════════════════════════════════════════════════════════════════
# TEMA 2 — Posición relativa
# ════════════════════════════════════════════════════════════════
_POSICIONES = {
    "arriba de":    ("arriba.png",     [("el pájaro", "el árbol"), ("la manzana", "la mesa"), ("el gato", "el sofá"), ("la nube", "la montaña")]),
    "abajo de":     ("abajo.png",      [("el perro", "la cama"), ("el zapato", "la silla"), ("la pelota", "la mesa"), ("el gato", "la silla")]),
    "dentro de":    ("dentro.png",     [("el juguete", "la caja"), ("el pez", "la pecera"), ("la ropa", "el closet"), ("la pelota", "la cesta")]),
    "fuera de":     ("fuera.png",      [("el gato", "la caja"), ("la pelota", "la canasta"), ("el niño", "la casa"), ("el perro", "la casita")]),
    "adelante de":  ("adelante.png",   [("María", "la pizarra"), ("el perro", "la casa"), ("el carro", "el semáforo"), ("Tomás", "la fila")]),
    "atrás de":     ("atras.png",      [("Juan", "la fila"), ("el gato", "la puerta"), ("la silla", "la pared"), ("Ana", "su amiga")]),
    "a la derecha de": ("derecha.png", [("el lápiz", "el cuaderno"), ("la lámpara", "la cama"), ("el vaso", "el plato"), ("el borrador", "el libro")]),
    "a la izquierda de": ("izquierda.png", [("el borrador", "el lápiz"), ("el vaso", "el plato"), ("la silla", "la mesa"), ("la flor", "la puerta")]),
    "junto a":      ("junto.png",      [("el perro", "el gato"), ("Ana", "su amiga"), ("el árbol", "la flor"), ("el libro", "el lápiz")]),
    "en medio de":  ("enmedio.png",    [("el niño", "sus dos amigos"), ("la flor", "los dos árboles"), ("la silla", "las dos mesas"), ("el gato", "los dos perros")]),
    "al lado de":   ("allado.png",     [("la mochila", "la silla"), ("el cuaderno", "el lápiz"), ("María", "Juan"), ("el árbol", "la casa")]),
}

def _gen_posicion():
    modo = random.choice(["identifica_pos", "completa_frase", "cual_posicion"])
    pos = random.choice(list(_POSICIONES.keys()))
    img_file, escenas = _POSICIONES[pos]
    objeto, lugar = random.choice(escenas)

    todas = list(_POSICIONES.keys())
    distractores = random.sample([p for p in todas if p != pos], 3)
    opciones = [pos] + distractores
    random.shuffle(opciones)

    if modo == "identifica_pos":
        q = f"{objeto.capitalize()} está {pos} {lugar}. ¿Qué posición describe esto?"
        proc = f"La posición correcta es **{pos}**."
    elif modo == "completa_frase":
        q = f"Completa: {objeto.capitalize()} está _____ {lugar}."
        proc = f"La respuesta es **{pos}**. {objeto.capitalize()} está {pos} {lugar}."
    else:
        q = f"Si {objeto} está {pos} {lugar}, ¿qué posición es esa?"
        proc = f"La posición es **{pos}**."

    result = {"q": q, "answer": pos, "opciones": opciones, "procedure": proc}
    if _img_ok(img_file):
        result["imagen"] = _img_rel(img_file)
    return result


# ════════════════════════════════════════════════════════════════
# TEMA 3 — Comparar cantidades
# ════════════════════════════════════════════════════════════════
_EMOJIS = ["🍎", "⭐", "🌸", "🐶", "🍌", "🎈", "🦋", "🍓", "🐱", "🌙", "🚗", "🌈"]

def _fila(emoji, n):
    return " ".join([emoji] * n)

def _gen_comparar_cantidades():
    tipo = random.choice(["mucho_poco", "mas_menos", "igual_cantidad",
                          "nociones_especiales", "tantos_como"])

    if tipo == "mucho_poco":
        e = random.choice(_EMOJIS)
        n_mucho = random.randint(7, 9)
        n_poco  = random.randint(1, 3)
        piden = random.choice(["mucho", "poco"])
        ga = f"Grupo A: {_fila(e, n_mucho)}"
        gb = f"Grupo B: {_fila(e, n_poco)}"
        if piden == "mucho":
            q = f"¿Cuál grupo tiene MUCHO?\n{ga}\n{gb}"
            correcta = f"Grupo A"
            distractores = ["Grupo B", "Los dos tienen mucho", "Ninguno tiene mucho"]
        else:
            q = f"¿Cuál grupo tiene POCO?\n{ga}\n{gb}"
            correcta = f"Grupo B"
            distractores = ["Grupo A", "Los dos tienen poco", "Ninguno tiene poco"]
        opciones = [correcta] + distractores
        random.shuffle(opciones)
        return {
            "q": q, "answer": correcta, "opciones": opciones,
            "procedure": f"Grupo A tiene {n_mucho} y Grupo B tiene {n_poco}.\n"
                         f"**Mucho** → el grupo con más objetos (Grupo A).\n**Poco** → el grupo con menos (Grupo B).",
        }

    if tipo == "mas_menos":
        e1, e2 = random.sample(_EMOJIS, 2)
        n1 = random.randint(2, 6)
        n2 = random.randint(2, 6)
        while n2 == n1:
            n2 = random.randint(2, 6)
        piden = random.choice(["más", "menos"])
        q = f"Grupo A: {_fila(e1, n1)}\nGrupo B: {_fila(e2, n2)}\n¿Cuál tiene {piden.upper()}?"
        if piden == "más":
            correcta = "Grupo A" if n1 > n2 else "Grupo B"
        else:
            correcta = "Grupo A" if n1 < n2 else "Grupo B"
        otra = "Grupo B" if correcta == "Grupo A" else "Grupo A"
        opciones = [correcta, otra, "Son iguales", "No se puede saber"]
        random.shuffle(opciones)
        return {
            "q": q, "answer": correcta, "opciones": opciones,
            "procedure": f"Grupo A tiene {n1} y Grupo B tiene {n2}.\n"
                         f"**Más** → {n1 if n1>n2 else n2} > {n2 if n1>n2 else n1} → {'Grupo A' if n1>n2 else 'Grupo B'}.\n"
                         f"**Menos** → {'Grupo A' if n1<n2 else 'Grupo B'}.",
        }

    if tipo == "igual_cantidad":
        e = random.choice(_EMOJIS)
        n = random.randint(2, 5)
        q = f"Grupo A: {_fila(e, n)}\nGrupo B: {_fila(e, n)}\n¿Cómo son los dos grupos?"
        correcta = "Igual cantidad"
        opciones = [correcta, "Grupo A tiene más", "Grupo B tiene más", "Son muy diferentes"]
        random.shuffle(opciones)
        return {
            "q": q, "answer": correcta, "opciones": opciones,
            "procedure": f"Ambos grupos tienen **{n}** objetos → **igual cantidad**.",
        }

    if tipo == "nociones_especiales":
        e = random.choice(_EMOJIS)
        subtipo = random.choice(["ninguno", "uno", "todos", "alguno"])
        if subtipo == "ninguno":
            q = f"La caja está vacía. ¿Cuántos {e} hay?"
            correcta = "Ninguno"
            opciones = ["Ninguno", "Uno", "Muchos", "Algunos"]
        elif subtipo == "uno":
            q = f"Hay un solo {e} en el plato. ¿Cuántos hay?"
            correcta = "Uno"
            opciones = ["Uno", "Ninguno", "Dos", "Muchos"]
        elif subtipo == "todos":
            n = random.randint(3, 5)
            q = f"Hay {n} {e} y se usan todos. ¿Cuántos quedan?"
            correcta = "Ninguno, se usaron todos"
            opciones = ["Ninguno, se usaron todos", "Queda uno", "Quedan dos", f"Quedan {n}"]
        else:
            n_total = random.randint(5, 8)
            n_tienen = random.randint(2, n_total - 1)
            q = f"Hay {n_total} niños. Solo {n_tienen} tienen {e}. ¿Cuántos tienen el objeto?"
            correcta = "Algunos sí tienen"
            opciones = ["Algunos sí tienen", "Todos tienen", "Ninguno tiene", "Uno tiene"]
        random.shuffle(opciones)
        return {"q": q, "answer": correcta, "opciones": opciones,
                "procedure": f"Respuesta: **{correcta}**."}

    # tantos_como
    e1, e2 = random.sample(_EMOJIS, 2)
    n = random.randint(2, 5)
    n2_op = random.choice([n + 1, n - 1 if n > 1 else n + 2])
    piden = random.choice(["tantos_a", "tantos_b"])
    if piden == "tantos_a":
        q = (f"Hay {n} {e1} y {n} {e2}.\n"
             f"¿Hay TANTOS {e1} COMO {e2}?")
        correcta = f"Sí, hay tantos como"
        opciones = [correcta, "No, hay más del primero", "No, hay más del segundo", "No se puede saber"]
    else:
        q = (f"Hay {n} {e1} y {n2_op} {e2}.\n"
             f"¿Hay TANTOS {e1} COMO {e2}?")
        correcta = "No, la cantidad es diferente"
        opciones = [correcta, "Sí, hay tantos como", "Son exactamente iguales", "No se puede contar"]
    random.shuffle(opciones)
    return {"q": q, "answer": correcta, "opciones": opciones,
            "procedure": f"Hay {n} de cada grupo → **{correcta}**."}


# ════════════════════════════════════════════════════════════════
# TEMA 4 — Correspondencia uno a uno
# ════════════════════════════════════════════════════════════════
_PARES_CORR = [
    ("perro 🐶", "hueso 🦴"),
    ("niño 👦", "globo 🎈"),
    ("flor 🌸", "mariposa 🦋"),
    ("vaso 🥛", "leche 🍼"),
    ("lápiz ✏️", "cuaderno 📓"),
    ("pájaro 🐦", "nido 🪺"),
    ("gato 🐱", "pelota 🎾"),
    ("niña 👧", "muñeca 🪆"),
]

def _gen_correspondencia():
    subtipo = random.choice(["misma_cantidad", "sobran_a", "falta_b", "hay_mas"])
    par = random.choice(_PARES_CORR)
    na_txt, nb_txt = par
    na_name = na_txt.split()[0]
    nb_name = nb_txt.split()[0]
    ea = na_txt.split()[-1]
    eb = nb_txt.split()[-1]

    na = random.randint(2, 5)

    if subtipo == "misma_cantidad":
        q = (f"Hay {na} {ea * na}\ny {na} {eb * na}.\n"
             f"¿Hay TANTOS {na_name} COMO {nb_name}?")
        correcta = f"Sí, hay tantos {na_name} como {nb_name}"
        opciones = [correcta, f"No, hay más {na_name}", f"No, hay más {nb_name}", "No se puede saber"]
        proc = f"Hay {na} de cada uno. **Uno a uno se emparejan todos** → hay tantos {na_name} como {nb_name}."
        random.shuffle(opciones)
        return {"q": q, "answer": correcta, "opciones": opciones, "procedure": proc}

    if subtipo == "sobran_a":
        nb = random.randint(1, na - 1)
        sobran = na - nb
        q = (f"Hay {na} {ea * na} y {nb} {eb * nb}.\n"
             f"¿Cuántos {na_name} se quedan sin {nb_name}?")
        correcta = str(sobran)
        todos_nums = [str(x) for x in range(1, 7) if str(x) != correcta]
        opciones = [correcta] + random.sample(todos_nums, 3)
        random.shuffle(opciones)
        proc = (f"Hay {na} {na_name} y solo {nb} {nb_name}.\n"
                f"Emparejamos uno a uno: {nb} quedan con pareja.\n"
                f"{na} - {nb} = **{sobran}** {na_name} sin pareja.")
        return {"q": q, "answer": correcta, "opciones": opciones, "procedure": proc}

    if subtipo == "falta_b":
        nb = random.randint(1, na - 1)
        q = (f"Hay {na} {ea * na} y {nb} {eb * nb}.\n"
             f"¿Hay suficientes {nb_name} para todos los {na_name}?")
        correcta = f"No, faltan {nb_name}"
        opciones = [correcta, "Sí, hay suficientes", "Hay de sobra", "Son iguales"]
        random.shuffle(opciones)
        proc = f"Hay {na} {na_name} pero solo {nb} {nb_name}. **No hay suficientes** {nb_name}."
        return {"q": q, "answer": correcta, "opciones": opciones, "procedure": proc}

    # hay_mas
    nb = na + random.randint(1, 2)
    q = (f"Hay {na} {ea * na} y {nb} {eb * nb}.\n"
         f"¿Quién tiene MÁS?")
    correcta = nb_name
    opciones = [correcta, na_name, "Son iguales", "Ninguno"]
    random.shuffle(opciones)
    proc = f"Hay {na} {na_name} y {nb} {nb_name}. **{nb_name}** tiene más."
    return {"q": q, "answer": correcta, "opciones": opciones, "procedure": proc}


# ════════════════════════════════════════════════════════════════
# TEMA 5 — Conteo y cardinalidades
# ════════════════════════════════════════════════════════════════
_EMOJIS_CONT = ["🍎", "⭐", "🌸", "🐶", "🎈", "🦋", "🍓", "🐱", "🚗", "🏠", "🎵", "🦁", "🌻", "🍕", "🐸"]

def _gen_conteo():
    tipo = random.choice(["cuantos_hay", "que_numero_es",
                          "cual_grupo_es_N", "antes_despues", "cero"])

    n = random.randint(1, 9)
    e = random.choice(_EMOJIS_CONT)

    if tipo == "cuantos_hay":
        q = f"¿Cuántos hay?\n{_fila(e, n)}"
        correcta = str(n)
        pool = [str(x) for x in range(1, 10) if x != n]
        opciones = [correcta] + random.sample(pool, 3)
        random.shuffle(opciones)
        conteo = " → ".join(str(i + 1) for i in range(n))
        return {
            "q": q, "answer": correcta, "opciones": opciones,
            "procedure": f"Contamos uno por uno: {conteo}\nHay **{n}** {e}.",
        }

    if tipo == "que_numero_es":
        q = f"¿Qué número representa este grupo?\n{_fila(e, n)}"
        correcta = str(n)
        pool = [str(x) for x in range(0, 10) if x != n]
        opciones = [correcta] + random.sample(pool, 3)
        random.shuffle(opciones)
        return {
            "q": q, "answer": correcta, "opciones": opciones,
            "procedure": f"Hay {n} objetos → el número es **{n}**.",
        }

    if tipo == "cual_grupo_es_N":
        n_target = random.randint(1, 7)
        alts = list({n_target + 1, n_target + 2, max(1, n_target - 1)})[:2]
        grupos_n = [n_target] + alts
        random.shuffle(grupos_n)
        letras = ["A", "B", "C"]
        e2 = random.choice(_EMOJIS_CONT)
        bloques = [f"Grupo {letras[i]}: {_fila(e2, grupos_n[i])}" for i in range(3)]
        idx_ok = grupos_n.index(n_target)
        correcta = f"Grupo {letras[idx_ok]}"
        q = f"¿Cuál grupo tiene exactamente {n_target}?\n" + "\n".join(bloques)
        distractores_op = [f"Grupo {letras[i]}" for i in range(3) if i != idx_ok]
        opciones = [correcta] + distractores_op + ["Ninguno"]
        opciones = list(dict.fromkeys(opciones))[:4]
        random.shuffle(opciones)
        return {
            "q": q, "answer": correcta, "opciones": opciones,
            "procedure": f"**{correcta}** tiene exactamente **{n_target}** objetos.",
        }

    if tipo == "cero":
        e3 = random.choice(_EMOJIS_CONT)
        q = f"La caja está vacía. ¿Cuántos {e3} hay?"
        correcta = "0"
        opciones = ["0", "1", "2", "3"]
        random.shuffle(opciones)
        return {
            "q": q, "answer": correcta, "opciones": opciones,
            "procedure": "Si está vacío, no hay ninguno. Eso se escribe **0** (cero).",
        }

    # antes_despues
    n_val = random.randint(1, 8)
    subtipo = random.choice(["antes", "despues"])
    if subtipo == "antes":
        correcta = str(n_val - 1)
        q = f"¿Qué número va ANTES del {n_val}?"
    else:
        correcta = str(n_val + 1)
        q = f"¿Qué número va DESPUÉS del {n_val}?"
    pool = [str(x) for x in range(0, 10) if str(x) != correcta]
    opciones = [correcta] + random.sample(pool, 3)
    random.shuffle(opciones)
    return {
        "q": q, "answer": correcta, "opciones": opciones,
        "procedure": (f"Los números en orden: …{n_val-1}, {n_val}, {n_val+1}…\n"
                      f"{'Antes' if subtipo == 'antes' else 'Después'} del {n_val} va el **{correcta}**."),
    }


# ════════════════════════════════════════════════════════════════
# TEMA 6 — Números del 0 al 9
# ════════════════════════════════════════════════════════════════
_NOMBRES = {
    0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro",
    5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve",
}

# Imágenes de los dígitos 0-9 (tarjetas de número)
_DIGIT_IMGS = {n: f"numero_{n}.png" for n in range(10)}

def _gen_numeros_0_9():
    tipo = random.choice(["nombre_a_numero", "numero_a_nombre",
                          "cual_es_mayor", "cual_es_menor",
                          "falta_en_serie", "tarjeta_numero"])

    if tipo == "nombre_a_numero":
        n = random.randint(0, 9)
        q = f"¿Cuál es el número {_NOMBRES[n].upper()}?"
        correcta = str(n)
        pool = [str(x) for x in range(0, 10) if x != n]
        opciones = [correcta] + random.sample(pool, 3)
        random.shuffle(opciones)
        return {
            "q": q, "answer": correcta, "opciones": opciones,
            "procedure": f"**{_NOMBRES[n].capitalize()}** se escribe con el dígito **{n}**.",
        }

    if tipo == "numero_a_nombre":
        n = random.randint(0, 9)
        q = f"¿Cómo se llama el número {n}?"
        correcta = _NOMBRES[n]
        pool = [_NOMBRES[x] for x in range(0, 10) if x != n]
        opciones = [correcta] + random.sample(pool, 3)
        random.shuffle(opciones)
        return {
            "q": q, "answer": correcta, "opciones": opciones,
            "procedure": f"El número **{n}** se llama **{_NOMBRES[n]}**.",
        }

    if tipo == "cual_es_mayor":
        a, b = random.sample(range(0, 10), 2)
        q = f"¿Cuál número es MAYOR: {a} o {b}?"
        correcta = str(max(a, b))
        menor = str(min(a, b))
        pool = [str(x) for x in range(0, 10) if str(x) not in [correcta, menor]]
        opciones = [correcta, menor] + random.sample(pool, 2)
        random.shuffle(opciones)
        return {
            "q": q, "answer": correcta, "opciones": opciones,
            "procedure": (f"{max(a,b)} es mayor porque viene después en la fila de números.\n"
                          f"**{max(a,b)} > {min(a,b)}**"),
        }

    if tipo == "cual_es_menor":
        a, b = random.sample(range(0, 10), 2)
        q = f"¿Cuál número es MENOR: {a} o {b}?"
        correcta = str(min(a, b))
        mayor = str(max(a, b))
        pool = [str(x) for x in range(0, 10) if str(x) not in [correcta, mayor]]
        opciones = [correcta, mayor] + random.sample(pool, 2)
        random.shuffle(opciones)
        return {
            "q": q, "answer": correcta, "opciones": opciones,
            "procedure": f"{min(a,b)} es menor porque viene antes.\n**{min(a,b)} < {max(a,b)}**",
        }

    if tipo == "falta_en_serie":
        inicio = random.randint(0, 6)
        serie = list(range(inicio, inicio + 4))
        oculto = random.randint(1, 2)
        correcta = str(serie[oculto])
        mostrar = [str(x) if i != oculto else "___" for i, x in enumerate(serie)]
        q = f"¿Qué número falta?\n{', '.join(mostrar)}"
        pool = [str(x) for x in range(0, 10) if str(x) != correcta]
        opciones = [correcta] + random.sample(pool, 3)
        random.shuffle(opciones)
        return {
            "q": q, "answer": correcta, "opciones": opciones,
            "procedure": f"Los números van en orden: {', '.join(str(x) for x in serie)}.\nFalta el **{correcta}**.",
        }

    # tarjeta_numero — muestra imagen de la tarjeta con el dígito
    n = random.randint(0, 9)
    img_file = _DIGIT_IMGS[n]
    q = f"¿Qué número está en la tarjeta?"
    correcta = str(n)
    pool = [str(x) for x in range(0, 10) if x != n]
    opciones = [correcta] + random.sample(pool, 3)
    random.shuffle(opciones)
    result = {
        "q": q, "answer": correcta, "opciones": opciones,
        "procedure": f"La tarjeta muestra el número **{n}** ({_NOMBRES[n]}).",
    }
    if _img_ok(img_file):
        result["imagen"] = _img_rel(img_file)
    return result


# ════════════════════════════════════════════════════════════════
# DESPACHADOR DINÁMICO
# ════════════════════════════════════════════════════════════════
_GENERATORS = {
    "Comparar tamaños":         _gen_comparar_tamano,
    "Posición relativa":        _gen_posicion,
    "Comparar cantidades":      _gen_comparar_cantidades,
    "Correspondencia uno a uno": _gen_correspondencia,
    "Conteo y cardinalidades":  _gen_conteo,
    "Números del 0 al 9":       _gen_numeros_0_9,
}


def generate_dynamic(topic):
    gen = _GENERATORS.get(topic)
    if not gen:
        return None
    preg = gen()
    preg["tema"] = topic
    return preg


# ════════════════════════════════════════════════════════════════
# DATA — estructura que consume engine.py / utils.py
# ════════════════════════════════════════════════════════════════
DATA = {
    "topics": {
        "Comparar tamaños": {
            "aprendizaje": "Comparar objetos del entorno según su tamaño",
            "indicador": "Usa: más grande que, más pequeño que, tan grande como, igual que",
        },
        "Posición relativa": {
            "aprendizaje": "Determinar la posición relativa entre objetos",
            "indicador": "Identifica: adelante, atrás, arriba, abajo, dentro, fuera, derecha, izquierda, junto a, en medio de, al lado de",
        },
        "Comparar cantidades": {
            "aprendizaje": "Comparar colecciones usando nociones de cantidad",
            "indicador": "Usa: mucho, poco, igual cantidad, uno, ninguno, todos, alguno, más que, menos que, tantos como",
        },
        "Correspondencia uno a uno": {
            "aprendizaje": "Establecer correspondencias uno a uno entre colecciones",
            "indicador": "Relaciona colecciones de objetos usando correspondencia uno a uno",
        },
        "Conteo y cardinalidades": {
            "aprendizaje": "Utilizar el conteo para asociar conjuntos con su cardinalidad",
            "indicador": "Cuenta objetos y asocia el conjunto con el número correcto (0–9)",
        },
        "Números del 0 al 9": {
            "aprendizaje": "Identificar los números del 0 al 9 en diferentes contextos",
            "indicador": "Reconoce, nombra y ordena los números del 0 al 9",
        },
    },

    "partes": [],          # sin imágenes de partes por ahora
    "preguntas": [],       # preguntas estáticas adicionales van aquí
    "verdadero_falso": [
        {
            "tema": "Comparar tamaños",
            "afirmacion": "Una hormiga es más grande que un elefante.",
            "correcto": False,
            "explicacion": "**Falso.** El elefante es **más grande que** la hormiga.",
        },
        {
            "tema": "Comparar tamaños",
            "afirmacion": "Un árbol es más grande que una flor.",
            "correcto": True,
            "explicacion": "**Verdadero.** El árbol es más grande que la flor.",
        },
        {
            "tema": "Posición relativa",
            "afirmacion": "Si la pelota está DENTRO de la caja, la pelota está fuera de la caja.",
            "correcto": False,
            "explicacion": "**Falso.** Si está dentro, no puede estar fuera al mismo tiempo.",
        },
        {
            "tema": "Posición relativa",
            "afirmacion": "Arriba es lo contrario de abajo.",
            "correcto": True,
            "explicacion": "**Verdadero.** Arriba y abajo son posiciones opuestas.",
        },
        {
            "tema": "Comparar cantidades",
            "afirmacion": "Ninguno significa que no hay ni uno.",
            "correcto": True,
            "explicacion": "**Verdadero.** Ninguno = cero = no hay nada.",
        },
        {
            "tema": "Conteo y cardinalidades",
            "afirmacion": "El número que representa este grupo 🍎🍎🍎 es 4.",
            "correcto": False,
            "explicacion": "**Falso.** Hay **3** manzanas, no 4.",
        },
        {
            "tema": "Números del 0 al 9",
            "afirmacion": "El número 7 va antes del número 5 en la fila de números.",
            "correcto": False,
            "explicacion": "**Falso.** El 5 va antes del 7. El orden es: 0, 1, 2, 3, 4, **5**, 6, **7**, 8, 9.",
        },
        {
            "tema": "Números del 0 al 9",
            "afirmacion": "El número cero significa que no hay ningún objeto.",
            "correcto": True,
            "explicacion": "**Verdadero.** El cero (0) representa ninguna cantidad.",
        },
    ],

    "secuencias": [],
    "dynamic_generator": generate_dynamic,
}
