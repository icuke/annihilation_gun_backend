import fitz
import easyocr
from PIL import Image
import numpy as np

reader = easyocr.Reader(['ru', 'en'])

def process_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    output = {"pages": []}

    for i, page in enumerate(doc, start=1):
        zoom = 300 / 72
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)

        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img_np = np.array(img)

        result = reader.readtext(img_np)

        blocks = []
        for bbox, text, conf in result:
            (x1, y1), (_, _), (x2, y2), (_, _) = bbox
            blocks.append({
                "text": text,
                "confidence": conf,
                "bounding_box": {
                    "x": int(x1),
                    "y": int(y1),
                    "width": int(x2 - x1),
                    "height": int(y2 - y1),
                }
            })

        output["pages"].append({
            "page_number": i,
            "text_blocks": blocks
        })

    doc.close()
    return output
