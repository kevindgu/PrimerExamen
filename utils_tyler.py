import random
from math import gcd

TOPICS_TYLER = {
    "Números naturales": {
        "aprendizaje": "Contar, reconocer y escribir los números naturales",
        "indicador": "Reconoce números naturales en diferentes representaciones",
    },
    "Operaciones combinadas": {
        "aprendizaje": "Resolver problemas con suma, resta, multiplicación y división combinadas",
        "indicador": "Resuelve problemas que combinan suma, resta, multiplicación y división",
    },
    "Propiedad distributiva": {
        "aprendizaje": "Plantear y resolver problemas usando la propiedad distributiva",
        "indicador": "Aplica la propiedad distributiva de la multiplicación respecto a la suma",
    },
    "Múltiplos y pares/impares": {
        "aprendizaje": "Aplicar múltiplos, pares e impares en resolución de problemas",
        "indicador": "Aplica múltiplos y pares/impares en la resolución de problemas",
    },
}

DIFICULTADES = ["Fácil", "Normal", "Difícil"]

# --- Números en español (0-9999) ---
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


# ============================================================
# NÚMEROS NATURALES
# ============================================================
def _q_numeros_naturales(dif):
    if dif == "Fácil":
        tipos = ['siguiente', 'anterior', 'texto_a_num', 'comparar']
    elif dif == "Normal":
        tipos = ['siguiente', 'anterior', 'texto_a_num', 'num_a_texto', 'ordenar', 'comparar', 'valor_posicional']
    else:
        tipos = ['texto_a_num', 'num_a_texto', 'ordenar', 'valor_posicional', 'descomponer', 'serie']

    tipo = random.choice(tipos)

    if tipo == 'siguiente':
        rango = (0, 100) if dif == "Fácil" else (90, 1010)
        n = random.randint(*rango)
        return dict(question=f"¿Cuál es el número que sigue después de {n}?",
                    answer=n + 1, is_numeric=True,
                    procedure=f"{n} + 1 = **{n+1}**")

    if tipo == 'anterior':
        rango = (1, 100) if dif == "Fácil" else (99, 1011)
        n = random.randint(*rango)
        return dict(question=f"¿Cuál es el número anterior a {n}?",
                    answer=n - 1, is_numeric=True,
                    procedure=f"{n} − 1 = **{n-1}**")

    if tipo == 'texto_a_num':
        rango = (1, 99) if dif == "Fácil" else ((100, 999) if dif == "Normal" else (1000, 9999))
        n = random.randint(*rango)
        txt = num_a_texto(n)
        return dict(question=f"Escribe en número: «{txt}»",
                    answer=n, is_numeric=True,
                    procedure=f"«{txt}» = **{n}**")

    if tipo == 'num_a_texto':
        rango = (100, 999) if dif == "Normal" else (1000, 5000)
        n = random.randint(*rango)
        txt = num_a_texto(n)
        return dict(question=f"Escribe con letras el número {n} (minúsculas, sin acentos está bien)",
                    answer=txt, is_numeric=False,
                    procedure=f"{n} = «**{txt}**»")

    if tipo == 'ordenar':
        cant = 4 if dif == "Normal" else 5
        rango = (10, 999) if dif == "Normal" else (100, 9999)
        nums = random.sample(range(*rango), cant)
        orden = random.choice(['menor a mayor', 'mayor a menor'])
        ordenados = sorted(nums) if orden == 'menor a mayor' else sorted(nums, reverse=True)
        resp = ','.join(str(x) for x in ordenados)
        return dict(question=f"Ordena de {orden} (separa con comas sin espacios): {nums}",
                    answer=resp, is_numeric=False,
                    procedure=f"Ordenados de {orden}: **{resp}**")

    if tipo == 'comparar':
        rango = (1, 100) if dif == "Fácil" else ((100, 999) if dif == "Normal" else (1000, 9999))
        a, b = random.sample(range(*rango), 2)
        signo = '>' if a > b else '<'
        return dict(question=f"¿Qué signo va entre {a} ___ {b}? (escribe > o <)",
                    answer=signo, is_numeric=False,
                    procedure=f"{a} es {'mayor' if a > b else 'menor'} que {b} → {a} **{signo}** {b}")

    if tipo == 'valor_posicional':
        rango = (100, 999) if dif == "Normal" else (1000, 9999)
        n = random.randint(*rango)
        digits = str(n)
        if len(digits) == 3:
            opciones = [('centenas', 0), ('decenas', 1), ('unidades', 2)]
        else:
            opciones = [('unidades de millar', 0), ('centenas', 1), ('decenas', 2), ('unidades', 3)]
        nombre, pos = random.choice(opciones)
        valor = int(digits[pos])
        return dict(question=f"En el número {n}, ¿cuál es el dígito en las {nombre}?",
                    answer=valor, is_numeric=True,
                    procedure=f"{n} → dígito en {nombre} es **{valor}**")

    if tipo == 'descomponer':
        n = random.randint(1000, 9999)
        m, c, d, u = n // 1000, (n % 1000) // 100, (n % 100) // 10, n % 10
        resp = f"{m}x1000+{c}x100+{d}x10+{u}x1"
        return dict(
            question=f"Descompón {n} (formato: AxB+CxD+ExF+GxH, ejemplo: 3x1000+2x100+5x10+1x1)",
            answer=resp, is_numeric=False,
            procedure=f"{n} = {m}×1000 + {c}×100 + {d}×10 + {u}×1 = **{n}**")

    # serie
    paso = random.choice([3, 5, 7, 11, 25, 50])
    inicio = random.randint(10, 200)
    serie = [inicio + paso * i for i in range(6)]
    oculto = random.randint(3, 5)
    mostrar = [str(x) if i != oculto else '___' for i, x in enumerate(serie)]
    return dict(
        question=f"¿Qué número falta?\n{', '.join(mostrar)}",
        answer=serie[oculto], is_numeric=True,
        procedure=f"La serie avanza de {paso} en {paso}: {', '.join(str(x) for x in serie)}\nFalta: **{serie[oculto]}**")


# ============================================================
# OPERACIONES COMBINADAS
# ============================================================
def _q_operaciones_combinadas(dif):
    if dif == "Fácil":
        tipos = ['suma_resta', 'multi_simple', 'div_simple']
    elif dif == "Normal":
        tipos = ['expr_2ops', 'expr_div_sum', 'problema_1paso']
    else:
        tipos = ['expr_3ops', 'expr_parentesis', 'problema_2pasos', 'problema_3pasos']

    tipo = random.choice(tipos)

    if tipo == 'suma_resta':
        a, b = random.randint(5, 50), random.randint(5, 50)
        op = random.choice(['+', '−'])
        if op == '−' and a < b:
            a, b = b, a
        res = a + b if op == '+' else a - b
        return dict(question=f"Calcula: {a} {op} {b}",
                    answer=res, is_numeric=True,
                    procedure=f"{a} {op} {b} = **{res}**")

    if tipo == 'multi_simple':
        a, b = random.randint(2, 12), random.randint(2, 12)
        res = a * b
        return dict(question=f"Calcula: {a} × {b}",
                    answer=res, is_numeric=True,
                    procedure=f"{a} × {b} = **{res}**")

    if tipo == 'div_simple':
        b = random.randint(2, 10)
        a = b * random.randint(2, 10)
        res = a // b
        return dict(question=f"Calcula: {a} ÷ {b}",
                    answer=res, is_numeric=True,
                    procedure=f"{a} ÷ {b} = **{res}**")

    if tipo == 'expr_2ops':
        a, b, c = random.randint(5, 30), random.randint(2, 10), random.randint(2, 10)
        res = a + b * c
        return dict(question=f"Calcula: {a} + {b} × {c}",
                    answer=res, is_numeric=True,
                    procedure=f"1) {b} × {c} = {b*c}\n2) {a} + {b*c} = **{res}**")

    if tipo == 'expr_div_sum':
        b = random.randint(2, 8)
        a = b * random.randint(3, 10)
        d = random.randint(1, 15)
        res = a // b + d
        return dict(question=f"Calcula: {a} ÷ {b} + {d}",
                    answer=res, is_numeric=True,
                    procedure=f"1) {a} ÷ {b} = {a//b}\n2) {a//b} + {d} = **{res}**")

    if tipo == 'problema_1paso':
        ninos = random.randint(3, 8)
        dulces = random.randint(2, 6)
        total = ninos * dulces
        return dict(
            question=f"Hay {ninos} niños y a cada uno le dan {dulces} dulces. ¿Cuántos dulces se repartieron?",
            answer=total, is_numeric=True,
            procedure=f"{ninos} × {dulces} = **{total}**")

    if tipo == 'expr_3ops':
        a, b, c = random.randint(10, 50), random.randint(2, 10), random.randint(2, 8)
        d = random.randint(1, 15)
        res = a + b * c - d
        return dict(question=f"Calcula: {a} + {b} × {c} − {d}",
                    answer=res, is_numeric=True,
                    procedure=f"1) {b} × {c} = {b*c}\n2) {a} + {b*c} = {a+b*c}\n3) {a+b*c} − {d} = **{res}**")

    if tipo == 'expr_parentesis':
        a, b = random.randint(2, 12), random.randint(2, 12)
        c = random.randint(2, 8)
        res = (a + b) * c
        return dict(question=f"Calcula: ({a} + {b}) × {c}",
                    answer=res, is_numeric=True,
                    procedure=f"1) Paréntesis: {a} + {b} = {a+b}\n2) {a+b} × {c} = **{res}**")

    if tipo == 'problema_2pasos':
        cajas = random.randint(3, 6)
        por_caja = random.randint(4, 10)
        regalados = random.randint(2, 8)
        total = cajas * por_caja - regalados
        return dict(
            question=f"Llegan {cajas} cajas con {por_caja} juguetes cada una. Regalan {regalados}. ¿Cuántos quedan?",
            answer=total, is_numeric=True,
            procedure=f"1) {cajas} × {por_caja} = {cajas*por_caja}\n2) {cajas*por_caja} − {regalados} = **{total}**")

    # problema_3pasos
    equipos = random.randint(2, 5)
    jugadores = random.randint(4, 8)
    arbitros = random.randint(1, 3)
    botellas = random.randint(2, 3)
    total_p = equipos * jugadores + arbitros
    total_b = total_p * botellas
    return dict(
        question=f"Hay {equipos} equipos de {jugadores} jugadores y {arbitros} árbitros. Cada persona necesita {botellas} botellas de agua. ¿Cuántas botellas en total?",
        answer=total_b, is_numeric=True,
        procedure=f"1) Jugadores: {equipos} × {jugadores} = {equipos*jugadores}\n2) Personas: {equipos*jugadores} + {arbitros} = {total_p}\n3) Botellas: {total_p} × {botellas} = **{total_b}**")


# ============================================================
# PROPIEDAD DISTRIBUTIVA
# ============================================================
def _q_propiedad_distributiva(dif):
    if dif == "Fácil":
        tipos = ['calcular_simple', 'completar_simple']
    elif dif == "Normal":
        tipos = ['calcular', 'completar', 'problema1']
    else:
        tipos = ['calcular_grande', 'calcular_resta', 'igualdad', 'problema2']

    tipo = random.choice(tipos)

    if tipo == 'calcular_simple':
        m = random.randint(2, 5)
        a, b = random.randint(1, 10), random.randint(1, 10)
        res = m * (a + b)
        return dict(question=f"Calcula con la distributiva: {m} × ({a} + {b})",
                    answer=res, is_numeric=True,
                    procedure=f"{m}×{a} + {m}×{b} = {m*a} + {m*b} = **{res}**")

    if tipo == 'completar_simple':
        m = random.randint(2, 5)
        a, b = random.randint(1, 8), random.randint(1, 8)
        res = m * b
        return dict(question=f"{m} × ({a} + {b}) = {m} × {a} + {m} × ___\n¿Cuánto vale {m} × {b}?",
                    answer=res, is_numeric=True,
                    procedure=f"El espacio es {b}\n{m} × {b} = **{res}**")

    if tipo == 'calcular':
        m = random.randint(3, 12)
        a, b = random.randint(5, 20), random.randint(5, 20)
        res = m * (a + b)
        return dict(question=f"Usa la distributiva: {m} × ({a} + {b})",
                    answer=res, is_numeric=True,
                    procedure=f"{m}×{a} + {m}×{b} = {m*a} + {m*b} = **{res}**")

    if tipo == 'completar':
        m = random.randint(3, 10)
        a, b = random.randint(5, 15), random.randint(5, 15)
        res = m * a
        return dict(question=f"{m} × ({a} + {b}) = ___ + {m} × {b}\n¿Cuánto vale el espacio?",
                    answer=res, is_numeric=True,
                    procedure=f"Espacio = {m} × {a} = **{res}**")

    if tipo == 'problema1':
        paq = random.randint(3, 8)
        r, a = random.randint(3, 12), random.randint(3, 12)
        total = paq * (r + a)
        return dict(
            question=f"Hay {paq} bolsas con {r} canicas rojas y {a} azules cada una. ¿Cuántas canicas en total?",
            answer=total, is_numeric=True,
            procedure=f"{paq} × ({r} + {a}) = {paq}×{r} + {paq}×{a} = {paq*r} + {paq*a} = **{total}**")

    if tipo == 'calcular_grande':
        m = random.randint(5, 15)
        a, b = random.randint(10, 30), random.randint(10, 30)
        res = m * (a + b)
        return dict(question=f"Distributiva: {m} × ({a} + {b})",
                    answer=res, is_numeric=True,
                    procedure=f"{m}×{a} + {m}×{b} = {m*a} + {m*b} = **{res}**")

    if tipo == 'calcular_resta':
        m = random.randint(3, 12)
        a = random.randint(15, 40)
        b = random.randint(1, a - 1)
        res = m * (a - b)
        return dict(question=f"Distributiva: {m} × ({a} − {b})",
                    answer=res, is_numeric=True,
                    procedure=f"{m}×{a} − {m}×{b} = {m*a} − {m*b} = **{res}**")

    if tipo == 'igualdad':
        m = random.randint(3, 10)
        a, b = random.randint(5, 20), random.randint(5, 20)
        ma, mb = m * a, m * b
        res = ma + mb
        return dict(question=f"Si {m}×{a}={ma} y {m}×{b}={mb}, ¿cuánto vale {m} × ({a}+{b})?",
                    answer=res, is_numeric=True,
                    procedure=f"{m}×({a}+{b}) = {ma} + {mb} = **{res}**")

    # problema2
    salones = random.randint(4, 10)
    ninos, ninas = random.randint(8, 20), random.randint(8, 20)
    total = salones * (ninos + ninas)
    return dict(
        question=f"Una escuela tiene {salones} salones con {ninos} niños y {ninas} niñas cada uno. ¿Cuántos alumnos hay?",
        answer=total, is_numeric=True,
        procedure=f"{salones}×({ninos}+{ninas}) = {salones}×{ninos} + {salones}×{ninas} = {salones*ninos} + {salones*ninas} = **{total}**")


# ============================================================
# MÚLTIPLOS Y PARES/IMPARES
# ============================================================
def _q_multiplos_pares(dif):
    if dif == "Fácil":
        tipos = ['paridad', 'multiplo_simple', 'listar_multiplos']
    elif dif == "Normal":
        tipos = ['paridad', 'multiplo', 'listar_multiplos', 'problema_par', 'problema_multiplo']
    else:
        tipos = ['multiplo', 'problema_par', 'problema_multiplo', 'mcm', 'suma_pares', 'patron']

    tipo = random.choice(tipos)

    if tipo == 'paridad':
        rango = (1, 100) if dif == "Fácil" else (50, 9999)
        n = random.randint(*rango)
        resp = 'par' if n % 2 == 0 else 'impar'
        return dict(question=f"¿{n} es par o impar?",
                    answer=resp, is_numeric=False,
                    procedure=f"Último dígito: {n%10} → **{resp}**")

    if tipo == 'multiplo_simple':
        n = random.randint(1, 50)
        k = random.randint(2, 5)
        resp = 'si' if n % k == 0 else 'no'
        return dict(question=f"¿Es {n} múltiplo de {k}? (si o no)",
                    answer=resp, is_numeric=False,
                    procedure=f"{n} ÷ {k} = {n//k} residuo {n%k} → **{resp}**")

    if tipo == 'multiplo':
        n = random.randint(10, 200)
        k = random.randint(3, 12)
        resp = 'si' if n % k == 0 else 'no'
        return dict(question=f"¿Es {n} múltiplo de {k}? (si o no)",
                    answer=resp, is_numeric=False,
                    procedure=f"{n} ÷ {k} = {n//k} residuo {n%k} → **{resp}**")

    if tipo == 'listar_multiplos':
        k = random.randint(2, 9) if dif == "Fácil" else random.randint(3, 12)
        n = random.randint(3, 4) if dif == "Fácil" else random.randint(4, 6)
        multiplos = [k * i for i in range(1, n + 1)]
        resp = ','.join(str(x) for x in multiplos)
        return dict(question=f"Escribe los primeros {n} múltiplos de {k} (comas sin espacios)",
                    answer=resp, is_numeric=False,
                    procedure=', '.join(f"{k}×{i}={k*i}" for i in range(1, n+1)) + f" → **{resp}**")

    if tipo == 'problema_par':
        a = random.randint(1, 30)
        b = a + random.randint(10, 40)
        pares = len([x for x in range(a, b + 1) if x % 2 == 0])
        return dict(question=f"¿Cuántos números pares hay del {a} al {b}?",
                    answer=pares, is_numeric=True,
                    procedure=f"Pares: {', '.join(str(x) for x in range(a+(a%2), b+1, 2))}\nTotal: **{pares}**")

    if tipo == 'problema_multiplo':
        k = random.randint(3, 9)
        limite = random.randint(20, 80) if dif == "Normal" else random.randint(50, 150)
        mults = list(range(k, limite + 1, k))
        return dict(question=f"¿Cuántos múltiplos de {k} hay del 1 al {limite}?",
                    answer=len(mults), is_numeric=True,
                    procedure=f"Múltiplos: {', '.join(str(x) for x in mults)}\nTotal: **{len(mults)}**")

    if tipo == 'mcm':
        a, b = random.sample([2, 3, 4, 5, 6, 7, 8, 9, 10, 12], 2)
        mcm = a * b // gcd(a, b)
        return dict(question=f"¿Cuál es el mínimo común múltiplo (MCM) de {a} y {b}?",
                    answer=mcm, is_numeric=True,
                    procedure=f"Múltiplos de {a}: {', '.join(str(a*i) for i in range(1, mcm//a+3))}...\nMúltiplos de {b}: {', '.join(str(b*i) for i in range(1, mcm//b+3))}...\nMCM = **{mcm}**")

    if tipo == 'suma_pares':
        n = random.randint(3, 8)
        pares = [2 * i for i in range(1, n + 1)]
        total = sum(pares)
        return dict(question=f"¿Cuánto suman los primeros {n} números pares?",
                    answer=total, is_numeric=True,
                    procedure=f"{' + '.join(str(x) for x in pares)} = **{total}**")

    # patron
    n = random.randint(10, 50)
    n = n if n % 2 == 0 else n + 1
    pares = random.choice([True, False])
    if not pares:
        n += 1
    s1, s2 = n + 2, n + 4
    return dict(question=f"Serie de {'pares' if pares else 'impares'}: ..., {n-4}, {n-2}, {n}, ___, ___\n¿Qué sigue? (coma sin espacio)",
                answer=f"{s1},{s2}", is_numeric=False,
                procedure=f"Avanza de 2 en 2: {n}, {s1}, {s2} → **{s1},{s2}**")


# ============================================================
# GENERADOR PRINCIPAL
# ============================================================
_GENERATORS = {
    "Números naturales": _q_numeros_naturales,
    "Operaciones combinadas": _q_operaciones_combinadas,
    "Propiedad distributiva": _q_propiedad_distributiva,
    "Múltiplos y pares/impares": _q_multiplos_pares,
}

def generate_question_tyler(topic, dificultad="Normal"):
    q = _GENERATORS[topic](dificultad)
    q['topic'] = topic
    return q

