import os

import numpy as np
import requests

from app.utils.pdf_utils import extract_text_from_pdf

HF_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-mpnet-base-v2"


def clean_text(text):
    keywords_to_remove = ["Teléfono", "Contacto", "Referencia", "Correo", "LinkedIn"]
    lines = text.split("\n")
    filtered_lines = [
        line for line in lines if not any(kw in line for kw in keywords_to_remove)
    ]
    return " ".join(filtered_lines)


def get_similarity_score(text1, text2):
    if not HF_API_KEY:
        raise ValueError("La variable de entorno HF_API_KEY no está definida.")

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"inputs": {"source_sentence": text1, "sentences": [text2]}}

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise ValueError(
            f"Error en la API de Hugging Face: {response.status_code} - {response.json()}"
        )

    data = response.json()

    if isinstance(data, list) and len(data) > 0:
        return round(float(data[0]) * 100, 2)

    raise ValueError(f"Formato de respuesta no esperado: {data}")


async def compare_cv_with_job(cv_file, job_description):
    cv_text = extract_text_from_pdf(cv_file.file)
    if not cv_text:
        return {"error": "No se pudo extraer texto del PDF."}

    cv_text_cleaned = clean_text(cv_text)
    job_description_cleaned = clean_text(job_description)

    match_percentage = get_similarity_score(cv_text_cleaned, job_description_cleaned)

    return {
        "cv_text_preview": cv_text_cleaned,
        "job_description_preview": job_description_cleaned,
        "match_percentage": match_percentage,
    }
