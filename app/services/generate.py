import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def generate_match_analysis(cv_text, job_description):
    prompt = f"""
    Eres un sistema ATS avanzado y experto en selección de talento. 
    Analiza y compara el siguiente currículum con la oferta de trabajo, 
    y devuelve una respuesta **en formato JSON válido** (sin texto adicional). 

    En la propiedad "recruiter_message", incluye consejos personalizados 
    para que el candidato optimice su CV y logre pasar con mayor éxito 
    los filtros de un ATS (por ejemplo, uso de palabras clave, 
    relevancia de la experiencia, estructura, etc.).

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
            "explicación": "Ejemplo: El candidato tiene más de 5 años de experiencia en frontend."
        }},
        "recruiter_message": "Aquí redacta consejos sobre cómo adaptar el CV para resaltar habilidades clave, cómo incluir palabras clave relevantes, y cualquier sugerencia adicional para optimizar la presentación según la oferta de trabajo."
    }}

    **IMPORTANTE:** Devuelve **exclusivamente** un JSON válido sin texto adicional.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un sistema que genera respuestas en JSON estricto.",
                },
                {"role": "user", "content": prompt},
            ],
            response_format={"type": "json_object"},
        )

        print("IAN", response)

        response_text = response.choices[0].message.content

        response_json = json.loads(response_text)

        return response_json

    except json.JSONDecodeError:
        return {
            "error": "La API de OpenAI no generó un JSON válido.",
            "raw_response": response_text,
        }
    except Exception as e:
        return {"error": str(e)}
