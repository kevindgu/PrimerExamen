"""Datos de Matemáticas para Jaikel (4to año)."""
import random

IMG = "matejaikel"

# --- Números en español ---
_UNITS = ['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']
_TEENS = {10:'diez',11:'once',12:'doce',13:'trece',14:'catorce',15:'quince',
          16:'dieciséis',17:'diecisiete',18:'dieciocho',19:'diecinueve'}
_TENS = ['','diez','veinte','treinta','cuarenta','cincuenta','sesenta','setenta','ochenta','noventa']
_HUNDREDS = {1:'ciento',2:'doscientos',3:'trescientos',4:'cuatrocientos',5:'quinientos',
             6:'seiscientos',7:'setecientos',8:'ochocientos',9:'novecientos'}

def _num_texto(n):
    if n < 10: return _UNITS[n]
    if n < 20: return _TEENS[n]
    if n < 30: return 'veinte' if n == 20 else 'veinti' + _UNITS[n % 10]
    if n < 100:
        t, u = divmod(n, 10)
        return _TENS[t] if u == 0 else f"{_TENS[t]} y {_UNITS[u]}"
    if n == 100: return 'cien'
    if n < 1000:
        h, rem = divmod(n, 100)
        return _HUNDREDS[h] if rem == 0 else f"{_HUNDREDS[h]} {_num_texto(rem)}"
    if n < 10000:
        mil, rem = divmod(n, 1000)
        prefix = 'mil' if mil == 1 else f"{_num_texto(mil)} mil"
        return prefix if rem == 0 else f"{prefix} {_num_texto(rem)}"
    if n < 100000:
        dm, rem = divmod(n, 10000)
        prefix = f"{_num_texto(dm * 10)} mil" if dm > 0 else ''
        resto = _num_texto(rem) if rem > 0 else ''
        return f"{prefix} {resto}".strip() if prefix else resto
    return str(n)

_ORDINALES = {
    1:'primero',2:'segundo',3:'tercero',4:'cuarto',5:'quinto',
    6:'sexto',7:'séptimo',8:'octavo',9:'noveno',10:'décimo',
    11:'décimo primero',12:'décimo segundo',13:'décimo tercero',
    14:'décimo cuarto',15:'décimo quinto',16:'décimo sexto',
    17:'décimo séptimo',18:'décimo octavo',19:'décimo noveno',20:'vigésimo',
}

# ============================================================
# GENERADORES DINÁMICOS
# ============================================================

def _gen_sucesiones():
    tipo = random.choice(['completar', 'patron', 'siguiente_dos', 'tipo_sucesion'])

    paso = random.choice([10, 100, 1000, 5, 50, 25, 200, 500])
    inicio = random.randint(1, 50) * paso
    largo = 6
    ascendente = random.choice([True, False])
    serie = [inicio + paso * i for i in range(largo)] if ascendente else [inicio - paso * i for i in range(largo)]
    serie = [x for x in serie if x >= 0]
    if len(serie) < 4:
        ascendente = True
        serie = [inicio + paso * i for i in range(largo)]

    if tipo == 'completar':
        oculto = random.randint(2, len(serie) - 2)
        mostrar = [str(x) if i != oculto else '___' for i, x in enumerate(serie)]
        correcto = serie[oculto]
        distractores = list(set([correcto + paso, correcto - paso, correcto + paso * 2]))
        opciones = list(set([str(correcto)] + [str(d) for d in distractores if d >= 0]))[:4]
        while len(opciones) < 4:
            opciones.append(str(correcto + random.randint(1, paso - 1)))
        opciones = list(set(opciones))[:4]
        random.shuffle(opciones)
        return {"q": f"¿Qué número falta?\n{', '.join(mostrar)}",
                "answer": str(correcto), "opciones": opciones,
                "procedure": f"La serie {'sube' if ascendente else 'baja'} de {paso} en {paso}:\n{', '.join(str(x) for x in serie)}\nFalta: **{correcto}**"}

    if tipo == 'patron':
        opciones = list(set([str(paso), str(paso + 10), str(paso - 5 if paso > 5 else paso + 5), str(paso * 2)]))[:4]
        while len(opciones) < 4:
            opciones.append(str(paso + random.randint(1, 20)))
        opciones = list(set(opciones))[:4]
        random.shuffle(opciones)
        return {"q": f"¿De cuánto en cuánto {'sube' if ascendente else 'baja'} esta serie?\n{', '.join(str(x) for x in serie[:5])}",
                "answer": str(paso), "opciones": opciones,
                "procedure": f"{serie[1]} - {serie[0]} = {paso} → avanza de **{paso}** en **{paso}**"}

    if tipo == 'siguiente_dos':
        mostrar = serie[:4]
        s1, s2 = serie[4], serie[5]
        resp = f"{s1},{s2}"
        opciones = [resp, f"{s1+1},{s2+1}", f"{s1-paso},{s2-paso}", f"{s1+paso},{s2+paso}"]
        opciones = list(set(opciones))[:4]
        random.shuffle(opciones)
        return {"q": f"¿Cuáles son los dos números que siguen? (separa con coma)\n{', '.join(str(x) for x in mostrar)}, ___, ___",
                "answer": resp, "opciones": opciones,
                "procedure": f"Avanza de {paso} en {paso}: {s1} y {s2} → **{resp}**"}

    # tipo_sucesion
    tipo_s = "ascendente" if ascendente else "descendente"
    otro = "descendente" if ascendente else "ascendente"
    opciones = [tipo_s, otro, "constante", "aleatoria"]
    random.shuffle(opciones)
    return {"q": f"¿Esta sucesión es ascendente o descendente?\n{', '.join(str(x) for x in serie[:5])}",
            "answer": tipo_s, "opciones": opciones,
            "procedure": f"Cada número es {'mayor' if ascendente else 'menor'} que el anterior → **{tipo_s}**"}


def _gen_angulos():
    tipo = random.choice(['clasificar_grados', 'elemento', 'imagen_tipo'])

    if tipo == 'clasificar_grados':
        grados = random.choice([
            random.randint(1, 89),
            90,
            random.randint(91, 179),
        ])
        if grados < 90: resp, proc = "Agudo", f"{grados}° < 90° → **agudo**"
        elif grados == 90: resp, proc = "Recto", f"{grados}° = 90° → **recto**"
        else: resp, proc = "Obtuso", f"{grados}° > 90° → **obtuso**"
        return {"q": f"Un ángulo de {grados}° es:", "answer": resp,
                "opciones": ["Agudo", "Recto", "Obtuso"], "procedure": proc}

    if tipo == 'elemento':
        preg = random.choice([
            ("¿Cómo se llama el punto donde se unen los lados de un ángulo?", "Vértice",
             ["Vértice", "Lado", "Base", "Arista"], "El punto de unión se llama **vértice**."),
            ("¿Cómo se llaman las líneas que forman un ángulo?", "Lados",
             ["Lados", "Vértices", "Bases", "Aristas"], "Las líneas que forman el ángulo son los **lados**."),
            ("¿Cuántos lados tiene un ángulo?", "2",
             ["1", "2", "3", "4"], "Un ángulo tiene **2 lados**."),
            ("Un ángulo recto mide exactamente:", "90°",
             ["45°", "90°", "180°", "60°"], "Un ángulo recto mide exactamente **90°**."),
            ("Un ángulo agudo mide:", "Menos de 90°",
             ["Menos de 90°", "Exactamente 90°", "Más de 90°", "180°"], "Un ángulo agudo mide **menos de 90°**."),
            ("Un ángulo obtuso mide:", "Más de 90° y menos de 180°",
             ["Menos de 90°", "Exactamente 90°", "Más de 90° y menos de 180°", "Exactamente 180°"],
             "Un ángulo obtuso mide **más de 90° y menos de 180°**."),
        ])
        q, a, opts, proc = preg
        return {"q": q, "answer": a, "opciones": opts, "procedure": proc}

    # imagen_tipo — usa imágenes reales
    angulos = [
        {"nombre": "agudo", "img": f"{IMG}/angulo_agudo44.4grados.png", "grados": "44.4°", "tipo": "Agudo"},
        {"nombre": "recto", "img": f"{IMG}/angulo_recto.png", "grados": "90°", "tipo": "Recto"},
        {"nombre": "obtuso", "img": f"{IMG}/angulo_obtuso120grados.jpeg", "grados": "120°", "tipo": "Obtuso"},
    ]
    ang = random.choice(angulos)
    return {"q": "Observa la imagen. ¿Qué tipo de ángulo es?",
            "answer": ang["tipo"], "opciones": ["Agudo", "Recto", "Obtuso"],
            "imagen": ang["img"],
            "procedure": f"El ángulo mide {ang['grados']} → **{ang['tipo']}**"}


def _gen_ordinales():
    tipo = random.choice(['num_a_palabra', 'palabra_a_num', 'posicion'])

    if tipo == 'num_a_palabra':
        n = random.randint(1, 20)
        correcto = _ORDINALES[n]
        otros = [_ORDINALES[x] for x in random.sample([i for i in range(1, 21) if i != n], 3)]
        opciones = [correcto] + otros
        random.shuffle(opciones)
        return {"q": f"¿Cómo se escribe el número ordinal {n}°?",
                "answer": correcto, "opciones": opciones,
                "procedure": f"{n}° = **{correcto}**"}

    if tipo == 'palabra_a_num':
        n = random.randint(1, 20)
        correcto = str(n)
        otros = [str(x) for x in random.sample([i for i in range(1, 21) if i != n], 3)]
        opciones = [correcto] + otros
        random.shuffle(opciones)
        return {"q": f"¿Qué número ordinal es «{_ORDINALES[n]}»?",
                "answer": correcto, "opciones": opciones,
                "procedure": f"«{_ORDINALES[n]}» = **{n}°**"}

    # posicion con emojis
    animales = ['🐶','🐱','🐰','🐸','🦁','🐯','🐮','🐷','🐵','🦊']
    cant = random.randint(5, 8)
    lista = animales[:cant]
    pos = random.randint(1, cant)
    correcto = lista[pos - 1]
    otros = [x for x in lista if x != correcto][:3]
    opciones = [correcto] + otros
    random.shuffle(opciones)
    return {"q": f"¿Qué animal está en la posición {_ORDINALES[pos]}?\n{' '.join(f'{i+1}.{a}' for i, a in enumerate(lista))}",
            "answer": correcto, "opciones": opciones,
            "procedure": f"Posición {_ORDINALES[pos]} ({pos}°) = **{correcto}**"}


def _gen_lectura_escritura():
    tipo = random.choice(['num_a_texto', 'texto_a_num'])

    n = random.randint(1000, 99999)
    txt = _num_texto(n)

    if tipo == 'num_a_texto':
        otros_n = random.sample([x for x in range(1000, 99999) if x != n], 3)
        otros_txt = [_num_texto(x) for x in otros_n]
        opciones = [txt] + otros_txt
        random.shuffle(opciones)
        return {"q": f"Escribe con letras el número {n:,}",
                "answer": txt, "opciones": opciones,
                "procedure": f"{n:,} = «**{txt}**»"}

    otros_n = random.sample([x for x in range(1000, 99999) if x != n], 3)
    opciones = [str(n)] + [str(x) for x in otros_n]
    random.shuffle(opciones)
    return {"q": f"Escribe en número: «{txt}»",
            "answer": str(n), "opciones": opciones,
            "procedure": f"«{txt}» = **{n:,}**"}


def _gen_comparacion():
    tipo = random.choice(['signo', 'mayor_menor', 'ordenar'])

    if tipo == 'signo':
        a = random.randint(1000, 99999)
        b = random.randint(1000, 99999)
        while a == b:
            b = random.randint(1000, 99999)
        signo = '>' if a > b else '<'
        return {"q": f"¿Qué signo va entre {a:,} ___ {b:,}?",
                "answer": signo, "opciones": ['>', '<', '='],
                "procedure": f"{a:,} es {'mayor' if a > b else 'menor'} que {b:,} → **{signo}**"}

    if tipo == 'mayor_menor':
        nums = random.sample(range(1000, 99999), 4)
        pedir = random.choice(['mayor', 'menor'])
        resp = max(nums) if pedir == 'mayor' else min(nums)
        opciones = [str(x) for x in nums]
        random.shuffle(opciones)
        return {"q": f"¿Cuál es el número {pedir}?\n{', '.join(f'{x:,}' for x in nums)}",
                "answer": str(resp), "opciones": opciones,
                "procedure": f"Ordenados: {', '.join(str(x) for x in sorted(nums))}\nEl {pedir} es **{resp:,}**"}

    # ordenar
    nums = random.sample(range(1000, 99999), 4)
    orden = random.choice(['menor a mayor', 'mayor a menor'])
    ordenados = sorted(nums) if orden == 'menor a mayor' else sorted(nums, reverse=True)
    resp = ','.join(str(x) for x in ordenados)
    alt1 = ','.join(str(x) for x in sorted(nums, reverse=(orden == 'menor a mayor')))
    alt2 = ','.join(str(x) for x in random.sample(nums, 4))
    alt3 = ','.join(str(x) for x in random.sample(nums, 4))
    opciones = list(set([resp, alt1, alt2, alt3]))[:4]
    while len(opciones) < 4:
        opciones.append(','.join(str(x) for x in random.sample(nums, 4)))
    opciones = list(set(opciones))[:4]
    random.shuffle(opciones)
    return {"q": f"Ordena de {orden} (separa con comas):\n{', '.join(f'{x:,}' for x in nums)}",
            "answer": resp, "opciones": opciones,
            "procedure": f"De {orden}: **{resp}**"}


def _gen_valor_posicional():
    tipo = random.choice(['digito', 'valor', 'armar', 'descomponer'])

    n = random.randint(1000, 99999)
    digits = str(n)
    largo = len(digits)

    posiciones = []
    if largo >= 1: posiciones.append(('unidades', largo - 1, 1))
    if largo >= 2: posiciones.append(('decenas', largo - 2, 10))
    if largo >= 3: posiciones.append(('centenas', largo - 3, 100))
    if largo >= 4: posiciones.append(('unidades de millar', largo - 4, 1000))
    if largo >= 5: posiciones.append(('decenas de millar', largo - 5, 10000))

    nombre, pos, mult = random.choice(posiciones)
    digito = int(digits[pos])
    valor = digito * mult

    if tipo == 'digito':
        opciones = list(set([str(digito), str(digito + 1), str(digito + 2), str((digito + 5) % 10)]))[:4]
        random.shuffle(opciones)
        return {"q": f"En el número {n:,}, ¿cuál es el dígito en las {nombre}?",
                "answer": str(digito), "opciones": opciones,
                "procedure": f"El dígito en {nombre} de {n:,} es **{digito}**"}

    if tipo == 'valor':
        opciones = list(set([str(valor), str(digito), str(valor * 10), str(valor + mult)]))[:4]
        while len(opciones) < 4:
            opciones.append(str(valor + random.randint(1, 9) * mult))
        opciones = list(set(opciones))[:4]
        random.shuffle(opciones)
        return {"q": f"En el número {n:,}, ¿cuál es el VALOR del dígito en las {nombre}?",
                "answer": str(valor), "opciones": opciones,
                "procedure": f"Dígito en {nombre}: {digito}\nValor = {digito} × {mult:,} = **{valor:,}**"}

    if tipo == 'armar':
        if largo == 4:
            um, c, d, u = int(digits[0]), int(digits[1]), int(digits[2]), int(digits[3])
            resp = str(n)
            opciones = [resp, str(um*1000+c*100+d*10+(u+1)), str(um*1000+c*100+(d+1)*10+u), str((um+1)*1000+c*100+d*10+u)]
        else:
            dm, um, c, d, u = int(digits[0]), int(digits[1]), int(digits[2]), int(digits[3]), int(digits[4])
            resp = str(n)
            opciones = [resp, str(n+1), str(n+10), str(n+100)]
        opciones = list(set(opciones))[:4]
        random.shuffle(opciones)
        return {"q": f"¿Qué número se forma con esta descomposición?\n{' + '.join(f'{int(digits[i])}×{10**(largo-1-i):,}' for i in range(largo) if int(digits[i]) > 0)}",
                "answer": resp, "opciones": opciones,
                "procedure": f"Sumando todos los valores = **{n:,}**"}

    # descomponer
    partes = []
    for i, d in enumerate(digits):
        if int(d) > 0:
            partes.append(f"{int(d)}×{10**(largo-1-i):,}")
    correcto = ' + '.join(partes)
    opciones = [correcto]
    for _ in range(3):
        alt_digits = list(digits)
        idx = random.randint(0, largo - 1)
        alt_digits[idx] = str((int(alt_digits[idx]) + random.randint(1, 3)) % 10)
        alt_n = int(''.join(alt_digits))
        alt_partes = []
        for i, d in enumerate(str(alt_n).zfill(largo)):
            if int(d) > 0:
                alt_partes.append(f"{int(d)}×{10**(largo-1-i):,}")
        opciones.append(' + '.join(alt_partes))
    opciones = list(set(opciones))[:4]
    random.shuffle(opciones)
    return {"q": f"¿Cómo se descompone el número {n:,}?",
            "answer": correcto, "opciones": opciones,
            "procedure": f"{n:,} = **{correcto}**"}


_GENERATORS = {
    "Sucesiones numéricas": _gen_sucesiones,
    "Ángulos": _gen_angulos,
    "Clasificación de ángulos": _gen_angulos,
    "Números ordinales": _gen_ordinales,
    "Lectura y escritura de números": _gen_lectura_escritura,
    "Comparación de números": _gen_comparacion,
    "Valor posicional": _gen_valor_posicional,
}

def generate_dynamic(topic):
    gen = _GENERATORS.get(topic)
    if not gen:
        return None
    preg = gen()
    preg["tema"] = topic
    return preg


DATA = {
    "topics": {
        "Sucesiones numéricas": {
            "aprendizaje": "Identificar patrones en sucesiones numéricas",
            "indicador": "Identifica patrones y completa series correctamente",
        },
        "Ángulos": {
            "aprendizaje": "Reconocer elementos de un ángulo y clasificarlos",
            "indicador": "Reconoce lado, vértice y clasifica ángulos como agudo, recto u obtuso",
        },
        "Números ordinales": {
            "aprendizaje": "Relacionar números ordinales con su escritura en palabras",
            "indicador": "Relaciona ordinales con palabras e identifica orden en secuencias",
        },
        "Lectura y escritura de números": {
            "aprendizaje": "Escribir números en letras y representar palabras como números",
            "indicador": "Escribe números en letras y los representa simbólicamente",
        },
        "Comparación de números": {
            "aprendizaje": "Utilizar símbolos <, >, = para comparar cantidades",
            "indicador": "Utiliza los símbolos correctamente y ordena números",
        },
        "Valor posicional": {
            "aprendizaje": "Identificar el valor posicional de un dígito",
            "indicador": "Reconoce unidades, decenas, centenas, millares y decenas de millar",
        },
        "Clasificación de ángulos": {
            "aprendizaje": "Clasificar ángulos según su medida",
            "indicador": "Clasifica ángulos en agudos, rectos u obtusos",
        },
    },

    "partes": [
        {"nombre": "Ángulo agudo", "img": f"{IMG}/angulo_agudo44.4grados.png",
         "funcion": "Mide más de 0° y menos de 90°", "grupo": "Ángulos"},
        {"nombre": "Ángulo recto", "img": f"{IMG}/angulo_recto.png",
         "funcion": "Mide exactamente 90°", "grupo": "Ángulos"},
        {"nombre": "Ángulo obtuso", "img": f"{IMG}/angulo_obtuso120grados.jpeg",
         "funcion": "Mide más de 90° y menos de 180°", "grupo": "Ángulos"},
        {"nombre": "Elementos del ángulo", "img": f"{IMG}/angulo_elementos.png",
         "funcion": "Un ángulo tiene dos lados y un vértice", "grupo": "Ángulos"},
        # Clasificación de ángulos (mismo grupo de imágenes)
        {"nombre": "Ángulo agudo", "img": f"{IMG}/angulo_agudo44.4grados.png",
         "funcion": "Mide más de 0° y menos de 90°", "grupo": "Clasificación de ángulos"},
        {"nombre": "Ángulo recto", "img": f"{IMG}/angulo_recto.png",
         "funcion": "Mide exactamente 90°", "grupo": "Clasificación de ángulos"},
        {"nombre": "Ángulo obtuso", "img": f"{IMG}/angulo_obtuso120grados.jpeg",
         "funcion": "Mide más de 90° y menos de 180°", "grupo": "Clasificación de ángulos"},
    ],

    "preguntas": [
        # Valor posicional
        {"tema": "Valor posicional", "q": "¿Cuántas unidades vale 1 decena?", "answer": "10", "opciones": ["1", "10", "100", "1000"], "procedure": "1 decena = **10** unidades."},
        {"tema": "Valor posicional", "q": "¿Cuántas unidades vale 1 centena?", "answer": "100", "opciones": ["10", "100", "1000", "10000"], "procedure": "1 centena = **100** unidades."},
        {"tema": "Valor posicional", "q": "¿Cuántas unidades vale 1 unidad de millar?", "answer": "1000", "opciones": ["100", "1000", "10000", "100000"], "procedure": "1 unidad de millar = **1 000** unidades."},
        {"tema": "Valor posicional", "q": "¿Cuántas unidades vale 1 decena de millar?", "answer": "10000", "opciones": ["1000", "10000", "100000", "1000000"], "procedure": "1 decena de millar = **10 000** unidades."},
        {"tema": "Valor posicional", "q": "¿En qué posición está el dígito de las unidades de millar?", "answer": "Cuarto lugar", "opciones": ["Primer lugar", "Segundo lugar", "Tercer lugar", "Cuarto lugar"], "procedure": "Las unidades de millar están en el **cuarto lugar** (de derecha a izquierda)."},
        # Comparación
        {"tema": "Comparación de números", "q": "¿Hacia dónde apunta la apertura del símbolo > o <?", "answer": "Hacia el número mayor", "opciones": ["Hacia el número mayor", "Hacia el número menor", "Hacia la derecha siempre", "Hacia la izquierda siempre"], "procedure": "La apertura siempre apunta **hacia el número mayor**."},
        {"tema": "Comparación de números", "q": "Si dos números tienen diferente cantidad de cifras, ¿cuál es mayor?", "answer": "El que tiene más cifras", "opciones": ["El que tiene más cifras", "El que tiene menos cifras", "El primero", "Depende"], "procedure": "El número con **más cifras** es el mayor."},
    ],

    "verdadero_falso": [
        {"tema": "Sucesiones numéricas", "afirmacion": "¿Una sucesión ascendente va de mayor a menor?", "correcto": False, "explicacion": "**Falso**. La ascendente va de **menor a mayor**."},
        {"tema": "Sucesiones numéricas", "afirmacion": "¿Una sucesión descendente va de mayor a menor?", "correcto": True, "explicacion": "**Verdadero**. La descendente va de mayor a menor."},
        {"tema": "Ángulos", "afirmacion": "¿Un ángulo recto mide exactamente 90°?", "correcto": True, "explicacion": "**Verdadero**."},
        {"tema": "Ángulos", "afirmacion": "¿Un ángulo de 120° es agudo?", "correcto": False, "explicacion": "**Falso**. 120° > 90° → es **obtuso**."},
        {"tema": "Ángulos", "afirmacion": "¿Un ángulo tiene dos lados y un vértice?", "correcto": True, "explicacion": "**Verdadero**. Todo ángulo tiene **2 lados** y **1 vértice**."},
        {"tema": "Comparación de números", "q": "¿5 432 > 5 342?", "afirmacion": "¿5 432 > 5 342?", "correcto": True, "explicacion": "**Verdadero**. En las centenas: 4 > 3, entonces 5 432 > 5 342."},
        {"tema": "Valor posicional", "afirmacion": "¿El dígito 3 en 3 500 vale 3 000?", "correcto": True, "explicacion": "**Verdadero**. 3 está en unidades de millar: 3 × 1 000 = **3 000**."},
    ],

    "secuencias": [],
    "dynamic_generator": generate_dynamic,
}
