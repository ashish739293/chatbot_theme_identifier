import pytesseract
from PIL import Image

def extract_text_with_ocr(path: str) -> list[str]:
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    return [para.strip() for para in text.split("\n\n") if para.strip()]
