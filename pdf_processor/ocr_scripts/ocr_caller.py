import json
import time
import random
from typing import Dict, List, Any

def process_pdf(pdf_path: str) -> Dict[str, Any]:
    processing_time = random.uniform(2.0, 5.0)
    time.sleep(processing_time)
    
    file_name = pdf_path.split('/')[-1] if '/' in pdf_path else pdf_path
    
    dummy_data = {
        "metadata": {
            "filename": file_name,
            "pages": random.randint(1, 10),
            "processing_time": round(processing_time, 2),
            "ocr_engine": "dummy_ocr_v1.0"
        },
        "pages": []
    }
    
    for page_num in range(1, dummy_data["metadata"]["pages"] + 1):
        page_data = {
            "page_number": page_num,
            "dimensions": {
                "width": random.randint(600, 1200),
                "height": random.randint(800, 1600)
            },
            "text_blocks": generate_dummy_text_blocks(page_num),
            "tables": generate_dummy_tables(page_num),
            "images": generate_dummy_images(page_num)
        }
        dummy_data["pages"].append(page_data)
    
    return dummy_data

def generate_dummy_text_blocks(page_num: int) -> List[Dict[str, Any]]:
    text_samples = [
        "azazazazazazazazazazazaz",
    ]
    
    blocks = []
    for i in range(random.randint(2, 6)):
        block = {
            "id": f"block_{page_num}_{i}",
            "text": random.choice(text_samples),
            "confidence": round(random.uniform(0.7, 0.99), 2),
            "bounding_box": {
                "x": random.randint(50, 200),
                "y": random.randint(100 + i * 150, 100 + (i + 1) * 150),
                "width": random.randint(300, 500),
                "height": random.randint(30, 80)
            },
            "font_size": random.choice([12, 14, 16, 18]),
            "font_family": random.choice(["Arial", "Times New Roman", "Helvetica"])
        }
        blocks.append(block)
    
    return blocks

def generate_dummy_tables(page_num: int) -> List[Dict[str, Any]]:
    if random.random() < 0.3:
        return []
    
    rows = random.randint(3, 6)
    cols = random.randint(2, 4)
    
    table_data = []
    for row in range(rows):
        row_data = []
        for col in range(cols):
            row_data.append(f"Ячейка {row+1}-{col+1}")
        table_data.append(row_data)
    
    return [{
        "id": f"table_{page_num}_1",
        "rows": rows,
        "columns": cols,
        "data": table_data,
        "bounding_box": {
            "x": random.randint(100, 300),
            "y": random.randint(400, 600),
            "width": random.randint(300, 400),
            "height": random.randint(150, 300)
        }
    }]

def generate_dummy_images(page_num: int) -> List[Dict[str, Any]]:
    if random.random() < 0.5:
        return []
    
    num_images = random.randint(1, 2)
    images = []
    
    for i in range(num_images):
        images.append({
            "id": f"image_{page_num}_{i}",
            "type": random.choice(["chart", "photo", "logo", "signature"]),
            "bounding_box": {
                "x": random.randint(400, 600),
                "y": random.randint(100, 300),
                "width": random.randint(150, 250),
                "height": random.randint(100, 200)
            },
            "confidence": round(random.uniform(0.8, 0.95), 2)
        })
    
    return images