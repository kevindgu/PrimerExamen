"""Datos de Matemáticas para Tyler (6to año) — basado en material escolar."""
import random
from math import gcd


# ============================================================
# GENERADORES DINÁMICOS
# ============================================================

def _gen_numeros_naturales():
    tipo = random.choice(['valor_posicional', 'descomponer', 'comparar', 'siguiente', 'anterior', 'ordenar'])

    if tipo == 'valor_posicional':
        n = random.randint(1000, 9999999)
        digits = str(n)
        posiciones = {
            1: ('unidades', 1),
            2: ('decenas', 10),
            3: ('centenas', 100),
            4: ('unidades de millar', 1000),
            5: ('decenas de millar', 10000),
            6: ('centenas de millar', 100000),
            7: ('unidades de millón', 1000000),
        }
        largo = len(digits)
        pos_idx = random.randint(1, min(largo, 7))
        nombre, mult = posiciones[pos_idx]
        digito = int(digits[largo - pos_idx])
        valor = digito * mult
        opciones = list(set([valor, digito, valor * 10, valor // 10 if valor >= 10 else valor + mult]))[:4]
        while len(opciones) < 4:
            opciones.append(valor + random.randint(1, 9) * mult)
        opciones = list(set(opciones))[:4]
        random.shuffle(opciones)
        return {"q": f"En el número {n:,}, ¿cuál es el VALOR del dígito en las {nombre}?",
                "answer": str(valor), "opciones": [str(o) for o in opciones],
                "procedure": f"El dígito en {nombre} de {n:,} es {digito}. Valor = {digito} × {mult:,} = **{valor:,}**"}

    if tipo == 'descomponer':
        n = random.randint(1000, 999999)
        partes = []
        temp = n
        for mult, nombre in [(100000,'centenas de millar'),(10000,'decenas de millar'),(1000,'unidades de millar'),(100,'centenas'),(10,'decenas'),(1,'unidades')]:
            d = temp // mult
            if d > 0:
                partes.append(f"{d}×{mult:,}")
            temp %= mult
        correcto = ' + '.join(partes)
        # Generar distractores cambiando un valor
        def distractor():
            p2 = partes.copy()
            if p2:
                idx = random.randint(0, len(p2)-1)
                num, mul = p2[idx].split('×')
                p2[idx] = f"{int(num)+random.choice([-1,1,2])}×{mul}"
            return ' + '.join(p2)
        opciones = list(set([correcto, distractor(), distractor(), distractor()]))[:4]
        while len(opciones) < 4:
            opciones.append(distractor())
        opciones = list(set(opciones))[:4]
        random.shuffle(opciones)
        return {"q": f"¿Cómo se descompone el número {n:,}?",
                "answer": correcto, "opciones": opciones,
                "procedure": f"{n:,} = **{correcto}**"}

    if tipo == 'comparar':
        a = random.randint(10000, 9999999)
        b = random.randint(10000, 9999999)
        while a == b:
            b = random.randint(10000, 9999999)
        signo = '>' if a > b else '<'
        return {"q": f"¿Qué signo va entre {a:,} ___ {b:,}?",
                "answer": signo, "opciones": ['>', '<', '='],
                "procedure": f"{a:,} es {'mayor' if a > b else 'menor'} que {b:,} → **{signo}**"}

    if tipo == 'siguiente':
        n = random.choice([random.randint(9990, 10010), random.randint(99990, 100010), random.randint(999990, 1000010)])
        opciones = list(set([n+1, n+2, n-1, n+10]))[:4]
        random.shuffle(opciones)
        return {"q": f"¿Cuál es el número que sigue después de {n:,}?",
                "answer": str(n+1), "opciones": [str(o) for o in opciones],
                "procedure": f"{n:,} + 1 = **{n+1:,}**"}

    if tipo == 'anterior':
        n = random.choice([random.randint(10000, 10010), random.randint(100000, 100010)])
        opciones = list(set([n-1, n-2, n+1, n-10]))[:4]
        random.shuffle(opciones)
        return {"q": f"¿Cuál es el número anterior a {n:,}?",
                "answer": str(n-1), "opciones": [str(o) for o in opciones],
                "procedure": f"{n:,} − 1 = **{n-1:,}**"}

    # ordenar
    nums = random.sample(range(10000, 999999), 4)
    orden = random.choice(['menor a mayor', 'mayor a menor'])
    ordenados = sorted(nums) if orden == 'menor a mayor' else sorted(nums, reverse=True)
    resp = ','.join(str(x) for x in ordenados)
    opciones = [resp]
    for _ in range(3):
        alt = ordenados.copy()
        i, j = random.sample(range(4), 2)
        alt[i], alt[j] = alt[j], alt[i]
        opciones.append(','.join(str(x) for x in alt))
    opciones = list(set(opciones))[:4]
    random.shuffle(opciones)
    return {"q": f"Ordena de {orden} (separa con comas): {nums}",
            "answer": resp, "opciones": opciones,
            "procedure": f"Ordenados de {orden}: **{resp}**"}


def _gen_operaciones_combinadas():
    tipo = random.choice(['sin_parentesis', 'con_parentesis', 'estimacion', 'mental'])

    if tipo == 'sin_parentesis':
        variante = random.choice(['mul_div_sum', 'div_mul_res'])
        if variante == 'mul_div_sum':
            a, b, c = random.randint(2, 15), random.randint(2, 12), random.randint(10, 50)
            res = a * b + c
            expr = f"{a} × {b} + {c}"
            proc = f"Primero ×: {a}×{b}={a*b}, luego +: {a*b}+{c}=**{res}**"
        else:
            b = random.randint(2, 8)
            a = b * random.randint(3, 10)
            c = random.randint(2, 8)
            d = random.randint(5, 30)
            res = a // b * c - d
            expr = f"{a} ÷ {b} × {c} − {d}"
            proc = f"÷ y × de izq a der: {a}÷{b}={a//b}, {a//b}×{c}={a//b*c}, luego −: {a//b*c}−{d}=**{res}**"
        opciones = list(set([res, res+random.randint(1,5), res-random.randint(1,5), res+random.randint(6,15)]))[:4]
        random.shuffle(opciones)
        return {"q": f"Calcula (sin paréntesis, respeta jerarquía): {expr}",
                "answer": str(res), "opciones": [str(o) for o in opciones], "procedure": proc}

    if tipo == 'con_parentesis':
        a = random.randint(50, 200)
        b = random.randint(5, 20)
        c = random.randint(5, 20)
        d = random.randint(2, 8)
        res = a - (b + c) * d
        expr = f"{a} − ({b} + {c}) × {d}"
        proc = f"Paréntesis: {b}+{c}={b+c}, luego ×: {b+c}×{d}={b+c*d if False else (b+c)*d}, luego −: {a}−{(b+c)*d}=**{res}**"
        opciones = list(set([res, a-(b+c)*d+random.randint(1,10), a-b+c*d, a-(b*c+d)]))[:4]
        opciones = [o for o in opciones if isinstance(o, int)][:4]
        while len(opciones) < 4:
            opciones.append(res + random.randint(-20, 20))
        opciones = list(set(opciones))[:4]
        random.shuffle(opciones)
        return {"q": f"Calcula (con paréntesis): {expr}",
                "answer": str(res), "opciones": [str(o) for o in opciones], "procedure": proc}

    if tipo == 'estimacion':
        a = random.randint(1000000, 9000000)
        b = random.randint(1000000, 9000000)
        # Redondear a millón más cercano
        ar = round(a / 1000000) * 1000000
        br = round(b / 1000000) * 1000000
        op = random.choice(['+', '-'])
        res = ar + br if op == '+' else abs(ar - br)
        return {"q": f"Estima redondeando al millón más cercano: {a:,} {op} {b:,}",
                "answer": str(res), "opciones": [str(res), str(res+1000000), str(res-1000000), str(res+2000000)],
                "procedure": f"{a:,} ≈ {ar:,} y {b:,} ≈ {br:,}\n{ar:,} {op} {br:,} = **{res:,}**"}

    # mental - descomposición
    a = random.randint(100, 999)
    b = random.choice([10, 100, 1000, 200, 300, 500])
    res = a * b
    a1 = (a // 100) * 100
    a2 = a % 100
    return {"q": f"Calcula mentalmente: {a} × {b}",
            "answer": str(res), "opciones": [str(res), str(res+b), str(res-b), str(res+a)],
            "procedure": f"Descomponer: {a} = {a1} + {a2}\n({a1}+{a2})×{b} = {a1*b} + {a2*b} = **{res:,}**"}


def _gen_distributiva():
    tipo = random.choice(['calcular', 'verificar', 'completar', 'con_resta'])

    if tipo == 'calcular':
        a = random.randint(3, 20)
        b = random.randint(5, 30)
        c = random.randint(5, 30)
        res = a * (b + c)
        opciones = list(set([res, a*b+c, a+b*c, res+a]))[:4]
        while len(opciones) < 4:
            opciones.append(res + random.randint(1, 20))
        opciones = list(set(opciones))[:4]
        random.shuffle(opciones)
        return {"q": f"Usa la propiedad distributiva: {a} × ({b} + {c})",
                "answer": str(res), "opciones": [str(o) for o in opciones],
                "procedure": f"{a}×{b} + {a}×{c} = {a*b} + {a*c} = **{res}**"}

    if tipo == 'verificar':
        a = random.randint(3, 15)
        b = random.randint(5, 20)
        c = random.randint(5, 20)
        lado_izq = a * (b + c)
        lado_der_correcto = a * b + a * c
        lado_der_incorrecto = a * b + c
        correcto = random.choice([True, False])
        lado_der = lado_der_correcto if correcto else lado_der_incorrecto
        resp = "Verdadero" if correcto else "Falso"
        return {"q": f"¿Es correcta esta aplicación de la distributiva?\n{a} × ({b} + {c}) = {lado_der}",
                "answer": resp, "opciones": ["Verdadero", "Falso"],
                "procedure": f"{a}×({b}+{c}) = {a}×{b} + {a}×{c} = {a*b} + {a*c} = **{lado_izq}**\n{'Correcto' if correcto else f'Incorrecto, el resultado es {lado_izq}'}"}

    if tipo == 'completar':
        a = random.randint(3, 15)
        b = random.randint(5, 20)
        c = random.randint(5, 20)
        res_b = a * b
        opciones = list(set([res_b, a+b, a*c, res_b+a]))[:4]
        while len(opciones) < 4:
            opciones.append(res_b + random.randint(1, 10))
        opciones = list(set(opciones))[:4]
        random.shuffle(opciones)
        return {"q": f"Completa: {a} × ({b} + {c}) = ___ + {a} × {c}",
                "answer": str(res_b), "opciones": [str(o) for o in opciones],
                "procedure": f"Por la distributiva: {a}×{b} + {a}×{c}\nEl espacio = {a}×{b} = **{res_b}**"}

    # con_resta
    a = random.randint(3, 15)
    b = random.randint(15, 40)
    c = random.randint(1, b-1)
    res = a * (b - c)
    opciones = list(set([res, a*b-c, a*b+a*c, res+a]))[:4]
    while len(opciones) < 4:
        opciones.append(res + random.randint(1, 15))
    opciones = list(set(opciones))[:4]
    random.shuffle(opciones)
    return {"q": f"Distributiva con resta: {a} × ({b} − {c})",
            "answer": str(res), "opciones": [str(o) for o in opciones],
            "procedure": f"{a}×{b} − {a}×{c} = {a*b} − {a*c} = **{res}**"}


def _gen_multiplos_pares():
    tipo = random.choice(['paridad', 'multiplo', 'divisor', 'divisibilidad', 'listar', 'mcm'])

    if tipo == 'paridad':
        n = random.randint(100, 999999)
        resp = "Par" if n % 2 == 0 else "Impar"
        ultimo = n % 10
        return {"q": f"¿El número {n:,} es par o impar?",
                "answer": resp, "opciones": ["Par", "Impar"],
                "procedure": f"Último dígito: {ultimo} → {'par (0,2,4,6,8)' if n%2==0 else 'impar (1,3,5,7,9)'} → **{resp}**"}

    if tipo == 'multiplo':
        k = random.randint(2, 12)
        n = random.randint(2, 20) * k
        resp = "Sí"
        return {"q": f"¿Es {n} múltiplo de {k}?",
                "answer": resp, "opciones": ["Sí", "No"],
                "procedure": f"{n} ÷ {k} = {n//k} residuo 0 → **Sí**, es múltiplo"}

    if tipo == 'divisor':
        k = random.randint(2, 10)
        n = random.randint(2, 15) * k
        resp = "Sí"
        return {"q": f"¿Es {k} divisor de {n}?",
                "answer": resp, "opciones": ["Sí", "No"],
                "procedure": f"{n} ÷ {k} = {n//k} residuo 0 → **Sí**, {k} es divisor de {n}"}

    if tipo == 'divisibilidad':
        regla = random.choice([2, 3, 5, 10])
        if regla == 2:
            n = random.choice([random.randint(100,999)*2, random.randint(100,999)*2+1])
            resp = "Sí" if n % 2 == 0 else "No"
            proc = f"Termina en {n%10} → {'par → divisible' if n%2==0 else 'impar → no divisible'} por 2"
        elif regla == 3:
            n = random.randint(100, 9999)
            suma = sum(int(d) for d in str(n))
            resp = "Sí" if n % 3 == 0 else "No"
            proc = f"Suma de dígitos: {'+'.join(list(str(n)))} = {suma} → {'múltiplo de 3' if suma%3==0 else 'no múltiplo de 3'} → **{resp}**"
        elif regla == 5:
            n = random.choice([random.randint(10,999)*5, random.randint(10,999)*5+random.randint(1,4)])
            resp = "Sí" if n % 5 == 0 else "No"
            proc = f"Termina en {n%10} → {'0 o 5 → divisible' if n%5==0 else 'no termina en 0 ni 5 → no divisible'} por 5"
        else:
            n = random.choice([random.randint(10,999)*10, random.randint(10,999)*10+random.randint(1,9)])
            resp = "Sí" if n % 10 == 0 else "No"
            proc = f"Termina en {n%10} → {'0 → divisible' if n%10==0 else 'no termina en 0 → no divisible'} por 10"
        return {"q": f"¿Es {n} divisible por {regla}?",
                "answer": resp, "opciones": ["Sí", "No"], "procedure": proc}

    if tipo == 'listar':
        k = random.randint(2, 9)
        n = random.randint(3, 6)
        multiplos = [k * i for i in range(1, n+1)]
        resp = ','.join(str(x) for x in multiplos)
        alt1 = ','.join(str(k*i+1) for i in range(1, n+1))
        alt2 = ','.join(str(k*i-1) for i in range(1, n+1))
        alt3 = ','.join(str(k*(i+1)) for i in range(1, n+1))
        opciones = list(set([resp, alt1, alt2, alt3]))[:4]
        random.shuffle(opciones)
        return {"q": f"Escribe los primeros {n} múltiplos de {k} (comas sin espacios)",
                "answer": resp, "opciones": opciones,
                "procedure": ', '.join(f"{k}×{i}={k*i}" for i in range(1, n+1)) + f" → **{resp}**"}

    # mcm
    a, b = random.sample([2, 3, 4, 5, 6, 7, 8, 9, 10, 12], 2)
    mcm = a * b // gcd(a, b)
    opciones = list(set([mcm, a*b, mcm+a, mcm-b if mcm > b else mcm+b]))[:4]
    while len(opciones) < 4:
        opciones.append(mcm + random.randint(1, 10))
    opciones = list(set(opciones))[:4]
    random.shuffle(opciones)
    return {"q": f"¿Cuál es el mínimo común múltiplo (MCM) de {a} y {b}?",
            "answer": str(mcm), "opciones": [str(o) for o in opciones],
            "procedure": f"Múltiplos de {a}: {', '.join(str(a*i) for i in range(1, mcm//a+2))}...\nMúltiplos de {b}: {', '.join(str(b*i) for i in range(1, mcm//b+2))}...\nMCM = **{mcm}**"}


_GENERATORS = {
    "Números naturales": _gen_numeros_naturales,
    "Operaciones combinadas": _gen_operaciones_combinadas,
    "Propiedad distributiva": _gen_distributiva,
    "Múltiplos y pares/impares": _gen_multiplos_pares,
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
        "Números naturales": {
            "aprendizaje": "Reconocer y escribir números naturales en diferentes representaciones",
            "indicador": "Identifica valor posicional, descompone y compara números naturales",
        },
        "Operaciones combinadas": {
            "aprendizaje": "Resolver combinación de operaciones: suma, resta, multiplicación y división",
            "indicador": "Aplica jerarquía de operaciones con y sin paréntesis",
        },
        "Propiedad distributiva": {
            "aprendizaje": "Aplicar la propiedad distributiva de la multiplicación respecto a la suma",
            "indicador": "Usa a×(b+c) = a×b + a×c correctamente",
        },
        "Múltiplos y pares/impares": {
            "aprendizaje": "Aplicar múltiplos, divisores, pares e impares",
            "indicador": "Identifica múltiplos, divisores y aplica reglas de divisibilidad",
        },
    },

    "partes": [],

    "preguntas": [
        # Jerarquía de operaciones
        {"tema": "Operaciones combinadas", "q": "¿Qué operaciones se resuelven primero cuando no hay paréntesis?", "answer": "Multiplicación y división", "opciones": ["Suma y resta", "Multiplicación y división", "De izquierda a derecha", "Las más difíciles"], "procedure": "Sin paréntesis: primero **multiplicación y división**, luego suma y resta."},
        {"tema": "Operaciones combinadas", "q": "¿Qué se resuelve primero cuando hay paréntesis?", "answer": "Lo que está dentro del paréntesis", "opciones": ["Lo que está fuera", "Lo que está dentro del paréntesis", "Las multiplicaciones", "Las sumas"], "procedure": "Con paréntesis: primero **lo que está dentro**, luego lo de afuera."},
        {"tema": "Operaciones combinadas", "q": "¿Cómo se llama el resultado de una multiplicación?", "answer": "Producto", "opciones": ["Suma", "Diferencia", "Producto", "Cociente"], "procedure": "El resultado de multiplicar se llama **producto**."},
        {"tema": "Operaciones combinadas", "q": "¿Cómo se llama el resultado de una división?", "answer": "Cociente", "opciones": ["Suma", "Diferencia", "Producto", "Cociente"], "procedure": "El resultado de dividir se llama **cociente**."},
        {"tema": "Operaciones combinadas", "q": "¿Cómo se llama la cantidad que sobra en una división?", "answer": "Residuo", "opciones": ["Cociente", "Divisor", "Residuo", "Dividendo"], "procedure": "La cantidad que sobra se llama **residuo**."},
        # Propiedad distributiva
        {"tema": "Propiedad distributiva", "q": "¿Cuál es la fórmula de la propiedad distributiva?", "answer": "a × (b + c) = a × b + a × c", "opciones": ["a × (b + c) = a × b + a × c", "a × (b + c) = a + b × c", "a × b + c = (a + b) × c", "a × (b + c) = a × b × c"], "procedure": "La propiedad distributiva: **a × (b + c) = a × b + a × c**"},
        # Múltiplos
        {"tema": "Múltiplos y pares/impares", "q": "¿Cuál es la cifra de las unidades de un número par?", "answer": "0, 2, 4, 6 u 8", "opciones": ["0, 2, 4, 6 u 8", "1, 3, 5, 7 o 9", "0 o 5", "Cualquier cifra"], "procedure": "Los números pares terminan en **0, 2, 4, 6 u 8**."},
        {"tema": "Múltiplos y pares/impares", "q": "¿Cuántos múltiplos tiene un número natural?", "answer": "Infinitos", "opciones": ["10", "100", "Infinitos", "Depende del número"], "procedure": "Un número tiene **infinitos** múltiplos."},
        {"tema": "Múltiplos y pares/impares", "q": "¿Cuándo es un número divisible por 10?", "answer": "Cuando termina en 0", "opciones": ["Cuando termina en 0", "Cuando termina en 5", "Cuando es par", "Cuando sus dígitos suman 10"], "procedure": "Divisible por 10: cuando **termina en 0**."},
        {"tema": "Múltiplos y pares/impares", "q": "¿Cuándo es un número divisible por 5?", "answer": "Cuando termina en 0 o 5", "opciones": ["Cuando termina en 0 o 5", "Cuando termina en 5", "Cuando es impar", "Cuando sus dígitos suman 5"], "procedure": "Divisible por 5: cuando **termina en 0 o 5**."},
        {"tema": "Múltiplos y pares/impares", "q": "¿Cuándo es un número divisible por 3?", "answer": "Cuando la suma de sus dígitos es múltiplo de 3", "opciones": ["Cuando la suma de sus dígitos es múltiplo de 3", "Cuando termina en 3", "Cuando es impar", "Cuando termina en 0"], "procedure": "Divisible por 3: cuando la **suma de sus dígitos es múltiplo de 3**."},
    ],

    "verdadero_falso": [
        {"tema": "Operaciones combinadas", "afirmacion": "¿En 5 + 3 × 2, primero se resuelve la multiplicación?", "correcto": True, "explicacion": "**Verdadero**. Sin paréntesis, la multiplicación va primero: 3×2=6, luego 5+6=11."},
        {"tema": "Operaciones combinadas", "afirmacion": "¿En (5 + 3) × 2, primero se resuelve la suma?", "correcto": True, "explicacion": "**Verdadero**. Con paréntesis, primero lo de adentro: 5+3=8, luego 8×2=16."},
        {"tema": "Propiedad distributiva", "afirmacion": "¿5 × (3 + 4) = 5 × 3 + 5 × 4?", "correcto": True, "explicacion": "**Verdadero**. 5×7=35 y 15+20=35. ✓"},
        {"tema": "Propiedad distributiva", "afirmacion": "¿3 × (2 + 6) = 3 × 2 + 6?", "correcto": False, "explicacion": "**Falso**. Debe ser 3×2 + 3×6 = 6+18 = 24, no 3×2+6=12."},
        {"tema": "Múltiplos y pares/impares", "afirmacion": "¿El número 0 es par?", "correcto": True, "explicacion": "**Verdadero**. 0 ÷ 2 = 0 con residuo 0, por lo tanto es par."},
        {"tema": "Múltiplos y pares/impares", "afirmacion": "¿Todo múltiplo de 10 también es múltiplo de 5?", "correcto": True, "explicacion": "**Verdadero**. Si termina en 0, también termina en 0 o 5."},
        {"tema": "Números naturales", "afirmacion": "¿El valor del dígito 3 en 3,500 es 3,000?", "correcto": True, "explicacion": "**Verdadero**. El 3 está en unidades de millar: 3 × 1,000 = 3,000."},
    ],

    "secuencias": [],
    "dynamic_generator": generate_dynamic,
}
