import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine import _img_path
from datos.jaikel_ciencias import DATA as JC
from datos.tyler_ciencias import DATA as TC
from datos.tyler_sociales import DATA as TS

print("=== IMAGENES FALTANTES ===")
missing = []
for nombre, data in [("jaikel_ciencias", JC), ("tyler_ciencias", TC), ("tyler_sociales", TS)]:
    for p in data.get("partes", []):
        path = _img_path(p["img"])
        if not os.path.exists(path):
            missing.append(f"{nombre}: {p['img']}")

if missing:
    for m in missing:
        print("FALTA:", m)
else:
    print("Todas las imagenes existen OK")

print("\n=== GENERADORES ===")
from utils import ESTUDIANTES
errors = []
ok = 0
for nombre, info in ESTUDIANTES.items():
    for mat, minfo in info["materias"].items():
        for topic in minfo["topics"]:
            try:
                q = minfo["generator"](topic)
                if not q:
                    errors.append(f"{nombre}/{mat}/{topic}: retorno None")
                elif not q.get("opciones_btn") and not q.get("question"):
                    errors.append(f"{nombre}/{mat}/{topic}: sin pregunta ni botones")
                else:
                    ok += 1
            except Exception as e:
                errors.append(f"{nombre}/{mat}/{topic}: {e}")

print(f"OK: {ok} temas")
if errors:
    for e in errors:
        print("ERROR:", e)
else:
    print("Sin errores en generadores")

print("\n=== CHECK_ANSWER ===")
from utils import check_answer
tests = [
    ({"answer": "vagina", "is_numeric": False}, "vagina", True),
    ({"answer": "vagina", "is_numeric": False}, "VAGINA", True),
    ({"answer": "Canal donde se deposita el semen", "is_numeric": False}, "canal semen", True),
    ({"answer": "Intestino delgado", "is_numeric": False}, "intestino", True),
    ({"answer": "✅ Verdadero", "is_numeric": False}, "✅ Verdadero", True),
    ({"answer": "✅ Verdadero", "is_numeric": False}, "verdadero", True),
    ({"answer": "❌ Falso", "is_numeric": False}, "falso", True),
    ({"answer": "206", "is_numeric": True}, "206", True),
    ({"answer": "vagina", "is_numeric": False}, "pene", False),
]
for q, ua, expected in tests:
    result = check_answer(q, ua)
    status = "OK" if result == expected else "FAIL"
    print(f"{status}: '{ua}' vs '{q['answer']}' -> {result} (esperado {expected})")
