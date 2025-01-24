from sentence_transformers import SentenceTransformer, util

from app.utils.pdf_utils import extract_text_from_pdf

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")


def clean_text(text):
    keywords_to_remove = ["Teléfono", "Contacto", "Referencia", "Correo", "LinkedIn"]
    lines = text.split("\n")
    filtered_lines = [
        line for line in lines if not any(kw in line for kw in keywords_to_remove)
    ]
    return " ".join(filtered_lines)


async def compare_cv_with_job(cv_file, job_description):
    cv_text = extract_text_from_pdf(cv_file.file)

    if not cv_text:
        return {"error": "No se pudo extraer texto del PDF."}

    cv_text_cleaned = clean_text(cv_text)
    job_description_cleaned = clean_text(job_description)

    cv_embedding = model.encode(cv_text_cleaned, convert_to_tensor=True)
    job_embedding = model.encode(job_description_cleaned, convert_to_tensor=True)

    similarity_score = util.pytorch_cos_sim(cv_embedding, job_embedding).item()
    match_percentage = round(similarity_score * 100, 2)

    return {
        "cv_text_preview": cv_text_cleaned[:500],
        "job_description_preview": job_description_cleaned[:500],
        "match_percentage": match_percentage,
    }
