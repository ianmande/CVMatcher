import json

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "EleutherAI/gpt-j-6B"
tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype=torch.float16, device_map="auto"
)


def generate_match_analysis(cv_text, job_description):
    prompt = f"""
    Eres un asistente experto en selección de talento. Compara el siguiente currículum con la oferta de trabajo y devuelve una respuesta **en formato JSON válido**.

    📄 **Currículum del Candidato:**
    {cv_text}

    📌 **Descripción del Trabajo:**
    {job_description}

    **📊 Respuesta en formato JSON:**  
    {{
        "skills_match": {{
            "coincidencias": [Número de habilidades coincidentes],
            "total_requeridas": [Total de habilidades requeridas],
            "habilidades_coincidentes": ["React", "React Native", "TypeScript"]
        }},
        "experience_level": {{
            "cumple": [true/false],
            "explicación": "El candidato tiene más de 5 años de experiencia en frontend."
        }},
        "recruiter_message": "Hola [Nombre], me emociona postularme para esta vacante..."
    }}
    
    **IMPORTANTE:** Devuelve **exclusivamente** un JSON válido sin texto adicional.
    """

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output = model.generate(**inputs, max_length=800)

    response_text = tokenizer.decode(output[0], skip_special_tokens=True)

    try:
        response_json = json.loads(response_text)
    except json.JSONDecodeError:
        return {
            "error": "LLaMA 2 no generó un JSON válido.",
            "raw_response": response_text,
        }

    return response_json
