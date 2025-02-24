import pdfminer.high_level
import pytesseract
from pdf2image import convert_from_bytes


def extract_text_from_pdf(file):
    text = pdfminer.high_level.extract_text(file)
    if text.strip():
        return text.strip()

    images = convert_from_bytes(file.read())
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img) + "\n"

    return text.strip()
