import sys
import os
import fitz
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ullokevi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def extraer_pdf(ruta_pdf):
    if not os.path.exists(ruta_pdf):
        print(f"No se encontro: {ruta_pdf}")
        return
    doc = fitz.open(ruta_pdf)
    total = doc.page_count
    texto = ""
    for i in range(total):
        print(f"Procesando pagina {i+1}/{total}...")
        pagina = doc[i]
        # Intentar texto directo primero
        txt = pagina.get_text().strip()
        if txt:
            texto += f"\n{'='*50}\nPAGINA {i+1}\n{'='*50}\n{txt}\n"
        else:
            # OCR sobre imagen
            mat = fitz.Matrix(2, 2)  # zoom x2 para mejor calidad
            pix = pagina.get_pixmap(matrix=mat)
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            txt_ocr = pytesseract.image_to_string(img, lang="spa")
            texto += f"\n{'='*50}\nPAGINA {i+1} (OCR)\n{'='*50}\n{txt_ocr}\n"
    doc.close()
    ruta_txt = os.path.splitext(ruta_pdf)[0] + ".txt"
    with open(ruta_txt, "w", encoding="utf-8") as f:
        f.write(texto)
    print(f"Listo: {total} paginas -> {ruta_txt}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python leer_pdf.py archivo.pdf")
    else:
        extraer_pdf(sys.argv[1])
