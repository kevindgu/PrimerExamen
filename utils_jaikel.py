import random

TOPICS_JAIKEL = {
    "Sucesiones numéricas": {
        "aprendizaje": "Identificar patrones en sucesiones numéricas",
        "indicador": "Identifica patrones y completa series de números correctamente",
    },
    "Ángulos": {
        "aprendizaje": "Reconocer elementos y clasificar ángulos",
        "indicador": "Reconoce lado, vértice y clasifica ángulos como agudo, recto u obtuso",
    },
    "Números ordinales": {
        "aprendizaje": "Relacionar números ordinales con su escritura",
        "indicador": "Relaciona ordinales con palabras e identifica orden en secuencias",
    },
    "Lectura y escritura de números": {
        "aprendizaje": "Escribir números en letras y representar palabras como números",
        "indicador": "Escribe números en letras y representa palabras de forma simbólica",
    },
    "Comparación de números": {
        "aprendizaje": "Utilizar símbolos <, >, = para comparar cantidades",
        "indicador": "Utiliza los símbolos <, >, = correctamente",
    },
    "Valor posicional": {
        "aprendizaje": "Identificar el valor posicional de un dígito",
        "indicador": "Reconoce unidades, decenas, centenas y millares",
    },
    "Clasificación de ángulos": {
        "aprendizaje": "Clasificar ángulos según su medida",
        "indicador": "Clasifica ángulos en agudos, rectos u obtusos",
    },
}

DIFICULTADES = ["Fácil", "Normal", "Difícil"]

# --- Números en español (reutilizado) ---
_UNITS = ['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']
_TEENS = {10:'diez',11:'once',12:'doce',13:'trece',14:'catorce',15:'quince',
           16:'dieciséis',17:'diecisiete',18:'dieciocho',19:'diecinueve'}
_TENS = ['','diez','veinte','treinta','cuarenta','cincuenta','sesenta','setenta','ochenta','noventa']
_HUNDREDS = {1:'ciento',2:'doscientos',3:'trescientos',4:'cuatrocientos',5:'quinientos',
             6:'seiscientos',7:'setecientos',8:'ochocientos',9:'novecientos'}

def num_a_texto(n):
    if n < 10: return _UNITS[n]
    if n < 20: return _TEENS[n]
    if n < 30:
        return 'veinte' if n == 20 else 'veinti' + _UNITS[n % 10]
    if n < 100:
        t, u = divmod(n, 10)
        return _TENS[t] if u == 0 else f"{_TENS[t]} y {_UNITS[u]}"
    if n == 100: return 'cien'
    if n < 1000:
        h, rem = divmod(n, 100)
        return _HUNDREDS[h] if rem == 0 else f"{_HUNDREDS[h]} {num_a_texto(rem)}"
    if n < 10000:
        mil, rem = divmod(n, 1000)
        prefix = 'mil' if mil == 1 else f"{num_a_texto(mil)} mil"
        return prefix if rem == 0 else f"{prefix} {num_a_texto(rem)}"
    return str(n)

# --- Ordinales ---
_ORDINALES = {
    1: 'primero', 2: 'segundo', 3: 'tercero', 4: 'cuarto', 5: 'quinto',
    6: 'sexto', 7: 'séptimo', 8: 'octavo', 9: 'noveno', 10: 'décimo',
    11: 'undécimo', 12: 'duodécimo', 13: 'decimotercero', 14: 'decimocuarto',
    15: 'decimoquinto', 16: 'decimosexto', 17: 'decimoséptimo',
    18: 'decimoctavo', 19: 'decimonoveno', 20: 'vigésimo',
}

# ============================================================
# SUCESIONES NUMÉRICAS
# ============================================================
def _q_sucesiones(dif):
    if dif == "Fácil":
        paso = random.choice([2, 3, 5, 10])
        inicio = random.randint(1, 20)
        largo = 5
    elif dif == "Normal":
        paso = random.choice([3, 4, 6, 7, 8, 9, 11])
        inicio = random.randint(5, 50)
        largo = 6
    else:
        paso = random.choice([7, 9, 11, 13, 15, 25])
        inicio = random.randint(10, 100)
        largo = 7

    tipo = random.choice(['completar', 'patron', 'siguiente'])

    serie = [inicio + paso * i for i in range(largo)]

    if tipo == 'completar':
        oculto = random.randint(2, largo - 2)
        mostrar = [str(x) if i != oculto else '___' for i, x in enumerate(serie)]
        return dict(
            question=f"¿Qué número falta en la serie?\n{', '.join(mostrar)}",
            answer=serie[oculto], is_numeric=True,
            procedure=f"La serie avanza de {paso} en {paso}:\n{', '.join(str(x) for x in serie)}\nEl número faltante es **{serie[oculto]}**")

    if tipo == 'patron':
        return dict(
            question=f"¿De cuánto en cuánto avanza esta serie?\n{', '.join(str(x) for x in serie[:5])}",
            answer=paso, is_numeric=True,
            procedure=f"{serie[1]} − {serie[0]} = {paso}\nLa serie avanza de **{paso}** en **{paso}**")

    # siguiente
    mostrados = serie[:-1]
    return dict(
        question=f"¿Cuál es el siguiente número?\n{', '.join(str(x) for x in mostrados)}, ___",
        answer=serie[-1], is_numeric=True,
        procedure=f"Avanza de {paso} en {paso}:\n{mostrados[-1]} + {paso} = **{serie[-1]}**")


# ============================================================
# ÁNGULOS (elementos)
# ============================================================
def _q_angulos(dif):
    tipo = random.choice(['elemento', 'clasificar_desc', 'grados_tipo'])

    if tipo == 'elemento':
        pregunta = random.choice([
            ("¿Cómo se llama el punto donde se unen los dos lados de un ángulo?", "vertice",
             "El punto donde se unen los lados se llama **vértice**"),
            ("¿Cómo se llaman las líneas que forman un ángulo?", "lados",
             "Las líneas que forman un ángulo se llaman **lados**"),
            ("¿Cuántos lados tiene un ángulo?", 2,
             "Un ángulo tiene **2** lados"),
        ])
        q, a, p = pregunta
        return dict(question=q, answer=a, is_numeric=isinstance(a, int), procedure=p)

    if tipo == 'clasificar_desc':
        opciones = [
            ("Un ángulo que mide exactamente 90° es un ángulo...", "recto",
             "Un ángulo de 90° es un ángulo **recto**"),
            ("Un ángulo que mide menos de 90° es un ángulo...", "agudo",
             "Menos de 90° = ángulo **agudo**"),
            ("Un ángulo que mide más de 90° pero menos de 180° es un ángulo...", "obtuso",
             "Entre 90° y 180° = ángulo **obtuso**"),
        ]
        q, a, p = random.choice(opciones)
        return dict(question=q, answer=a, is_numeric=False, procedure=p)

    # grados_tipo
    grados = random.choice([
        random.randint(1, 89),
        90,
        random.randint(91, 179),
    ])
    if grados < 90:
        resp = "agudo"
    elif grados == 90:
        resp = "recto"
    else:
        resp = "obtuso"
    return dict(
        question=f"Un ángulo de {grados}° es: ¿agudo, recto u obtuso?",
        answer=resp, is_numeric=False,
        procedure=f"{grados}° {'< 90°' if grados < 90 else ('= 90°' if grados == 90 else '> 90°')} → ángulo **{resp}**")


# ============================================================
# NÚMEROS ORDINALES
# ============================================================
def _q_ordinales(dif):
    if dif == "Fácil":
        rango = range(1, 11)
    elif dif == "Normal":
        rango = range(1, 16)
    else:
        rango = range(1, 21)

    tipo = random.choice(['num_a_palabra', 'palabra_a_num', 'posicion'])

    if tipo == 'num_a_palabra':
        n = random.choice(list(rango))
        sufijo = '°' if n != 3 else 'er'
        return dict(
            question=f"Escribe con letras el número ordinal {n}°",
            answer=_ORDINALES[n], is_numeric=False,
            procedure=f"{n}° = **{_ORDINALES[n]}**")

    if tipo == 'palabra_a_num':
        n = random.choice(list(rango))
        return dict(
            question=f"¿Qué número ordinal es «{_ORDINALES[n]}»? (escribe solo el número)",
            answer=n, is_numeric=True,
            procedure=f"«{_ORDINALES[n]}» = **{n}°**")

    # posicion
    objetos = random.choice([
        ['🐶','🐱','🐰','🐸','🦁','🐯','🐮','🐷','🐵','🦊'],
        ['🍎','🍊','🍋','🍇','🍓','🍌','🍉','🍒','🥝','🍑'],
        ['⚽','🏀','🎾','🏐','🎱','🏈','⚾','🥎','🏓','🎳'],
    ])
    cant = min(len(list(rango)), len(objetos))
    seleccion = objetos[:cant]
    pos = random.randint(1, cant)
    return dict(
        question=f"¿Qué objeto está en la posición {_ORDINALES[pos]}?\n{' '.join(f'{i+1}.{o}' for i, o in enumerate(seleccion))}",
        answer=seleccion[pos - 1], is_numeric=False,
        procedure=f"Posición {_ORDINALES[pos]} ({pos}°) = **{seleccion[pos-1]}**")


# ============================================================
# LECTURA Y ESCRITURA DE NÚMEROS
# ============================================================
def _q_lectura_escritura(dif):
    if dif == "Fácil":
        n = random.randint(1, 99)
    elif dif == "Normal":
        n = random.randint(100, 999)
    else:
        n = random.randint(1000, 9999)

    tipo = random.choice(['num_a_texto', 'texto_a_num'])
    txt = num_a_texto(n)

    if tipo == 'num_a_texto':
        return dict(
            question=f"Escribe con letras el número {n} (minúsculas, sin acentos está bien)",
            answer=txt, is_numeric=False,
            procedure=f"{n} = «**{txt}**»")

    return dict(
        question=f"Escribe en número: «{txt}»",
        answer=n, is_numeric=True,
        procedure=f"«{txt}» = **{n}**")


# ============================================================
# COMPARACIÓN DE NÚMEROS
# ============================================================
def _q_comparacion(dif):
    if dif == "Fácil":
        a, b = random.randint(1, 50), random.randint(1, 50)
    elif dif == "Normal":
        a, b = random.randint(10, 999), random.randint(10, 999)
    else:
        a, b = random.randint(100, 9999), random.randint(100, 9999)

    tipo = random.choice(['signo', 'verdadero_falso', 'mayor_menor'])

    if tipo == 'signo':
        if a == b:
            b = a + random.choice([-1, 1])
        signo = '>' if a > b else '<'
        return dict(
            question=f"¿Qué signo va entre {a} ___ {b}? (escribe > o <)",
            answer=signo, is_numeric=False,
            procedure=f"{a} es {'mayor' if a > b else 'menor'} que {b} → {a} **{signo}** {b}")

    if tipo == 'verdadero_falso':
        if a == b:
            a += 1
        correcto = random.choice([True, False])
        if correcto:
            signo = '>' if a > b else '<'
        else:
            signo = '<' if a > b else '>'
        resp = 'si' if correcto else 'no'
        return dict(
            question=f"¿Es correcto? {a} {signo} {b} (responde si o no)",
            answer=resp, is_numeric=False,
            procedure=f"{a} es {'mayor' if a > b else 'menor'} que {b}, entonces {a} {signo} {b} es **{'correcto' if correcto else 'incorrecto'}** → **{resp}**")

    # mayor_menor
    nums = random.sample(range(max(1, a-50), a+50), random.randint(3, 5))
    pedir = random.choice(['mayor', 'menor'])
    resp = max(nums) if pedir == 'mayor' else min(nums)
    return dict(
        question=f"¿Cuál es el número {pedir} de estos?\n{', '.join(str(x) for x in nums)}",
        answer=resp, is_numeric=True,
        procedure=f"Ordenados: {', '.join(str(x) for x in sorted(nums))}\nEl {pedir} es **{resp}**")


# ============================================================
# VALOR POSICIONAL
# ============================================================
def _q_valor_posicional(dif):
    if dif == "Fácil":
        n = random.randint(10, 99)
        digits = str(n)
        opciones = [('decenas', 0), ('unidades', 1)]
    elif dif == "Normal":
        n = random.randint(100, 999)
        digits = str(n)
        opciones = [('centenas', 0), ('decenas', 1), ('unidades', 2)]
    else:
        n = random.randint(1000, 9999)
        digits = str(n)
        opciones = [('unidades de millar', 0), ('centenas', 1), ('decenas', 2), ('unidades', 3)]

    tipo = random.choice(['digito', 'valor', 'armar'])

    if tipo == 'digito':
        nombre, pos = random.choice(opciones)
        valor = int(digits[pos])
        return dict(
            question=f"En el número {n}, ¿cuál es el dígito en las {nombre}?",
            answer=valor, is_numeric=True,
            procedure=f"{n} → dígito en {nombre} es **{valor}**")

    if tipo == 'valor':
        nombre, pos = random.choice(opciones)
        digito = int(digits[pos])
        multiplicadores = {'unidades de millar': 1000, 'centenas': 100, 'decenas': 10, 'unidades': 1}
        valor_real = digito * multiplicadores[nombre]
        return dict(
            question=f"En el número {n}, ¿cuál es el VALOR del dígito en las {nombre}?",
            answer=valor_real, is_numeric=True,
            procedure=f"Dígito en {nombre}: {digito}\nValor: {digito} × {multiplicadores[nombre]} = **{valor_real}**")

    # armar
    if dif == "Fácil":
        d, u = random.randint(1, 9), random.randint(0, 9)
        resp = d * 10 + u
        return dict(
            question=f"¿Qué número se forma con {d} decenas y {u} unidades?",
            answer=resp, is_numeric=True,
            procedure=f"{d} × 10 + {u} × 1 = {d*10} + {u} = **{resp}**")
    elif dif == "Normal":
        c, d, u = random.randint(1, 9), random.randint(0, 9), random.randint(0, 9)
        resp = c * 100 + d * 10 + u
        return dict(
            question=f"¿Qué número se forma con {c} centenas, {d} decenas y {u} unidades?",
            answer=resp, is_numeric=True,
            procedure=f"{c}×100 + {d}×10 + {u}×1 = {c*100} + {d*10} + {u} = **{resp}**")
    else:
        m, c, d, u = random.randint(1, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)
        resp = m * 1000 + c * 100 + d * 10 + u
        return dict(
            question=f"¿Qué número se forma con {m} millares, {c} centenas, {d} decenas y {u} unidades?",
            answer=resp, is_numeric=True,
            procedure=f"{m}×1000 + {c}×100 + {d}×10 + {u}×1 = **{resp}**")


# ============================================================
# CLASIFICACIÓN DE ÁNGULOS
# ============================================================
def _q_clasificacion_angulos(dif):
    if dif == "Fácil":
        grados = random.choice([
            random.randint(10, 80),
            90,
            random.randint(100, 170),
        ])
    elif dif == "Normal":
        grados = random.choice([
            random.randint(1, 89),
            90,
            random.randint(91, 179),
        ])
    else:
        grados = random.randint(1, 179)

    tipo = random.choice(['clasificar', 'rango', 'ejemplo'])

    if grados < 90:
        resp = "agudo"
        rango = "menos de 90°"
    elif grados == 90:
        resp = "recto"
        rango = "exactamente 90°"
    else:
        resp = "obtuso"
        rango = "más de 90° y menos de 180°"

    if tipo == 'clasificar':
        return dict(
            question=f"Clasifica el ángulo de {grados}°: ¿agudo, recto u obtuso?",
            answer=resp, is_numeric=False,
            procedure=f"{grados}° → {rango} → ángulo **{resp}**")

    if tipo == 'rango':
        preg_tipo = random.choice(['agudo', 'recto', 'obtuso'])
        rangos = {'agudo': 'menos de 90°', 'recto': 'exactamente 90°', 'obtuso': 'más de 90° y menos de 180°'}
        ejemplos = {'agudo': random.randint(1, 89), 'recto': 90, 'obtuso': random.randint(91, 179)}
        return dict(
            question=f"¿Cuánto puede medir un ángulo {preg_tipo}? Da un ejemplo en grados (solo el número)",
            answer=ejemplos[preg_tipo], is_numeric=True,
            procedure=f"Un ángulo {preg_tipo} mide {rangos[preg_tipo]}.\nEjemplo: **{ejemplos[preg_tipo]}°**")

    # ejemplo: dar grados y preguntar si es mayor/menor que 90
    return dict(
        question=f"¿El ángulo de {grados}° es mayor, menor o igual a 90°? (escribe mayor, menor o igual)",
        answer='menor' if grados < 90 else ('igual' if grados == 90 else 'mayor'),
        is_numeric=False,
        procedure=f"{grados}° {'<' if grados < 90 else ('=' if grados == 90 else '>')} 90° → **{'menor' if grados < 90 else ('igual' if grados == 90 else 'mayor')}**")


# ============================================================
# GENERADOR PRINCIPAL JAIKEL
# ============================================================
_GENERATORS_JAIKEL = {
    "Sucesiones numéricas": _q_sucesiones,
    "Ángulos": _q_angulos,
    "Números ordinales": _q_ordinales,
    "Lectura y escritura de números": _q_lectura_escritura,
    "Comparación de números": _q_comparacion,
    "Valor posicional": _q_valor_posicional,
    "Clasificación de ángulos": _q_clasificacion_angulos,
}

def generate_question_jaikel(topic, dificultad="Normal"):
    gen = _GENERATORS_JAIKEL[topic]
    # Ángulos y Clasificación de ángulos no usan dificultad tan diferenciada
    try:
        q = gen(dificultad)
    except TypeError:
        q = gen("Normal")
    q['topic'] = topic
    return q
