# 📝 CV Matcher - Optimiza tu Currículum con IA 🤖  

¡Bienvenido a **CV Matcher**! 🚀  
Una herramienta inteligente que **analiza y compara tu currículum** con una oferta de trabajo utilizando **IA avanzada** para ayudarte a **superar los filtros ATS** y **mejorar tu postulación**. 🎯  

---

## 🚀 Características Principales  
✅ **Análisis de coincidencias**: Detecta qué habilidades del CV coinciden con la oferta.  
✅ **Optimización para ATS**: Te ayuda a mejorar tu CV para pasar los filtros de selección.  
✅ **Recomendaciones personalizadas**: Recibes sugerencias específicas para mejorar tu postulación.  
✅ **Formato JSON estructurado**: Los resultados se entregan en un formato procesable por otras aplicaciones.  
✅ **Basado en OpenAI**: Utiliza modelos avanzados de inteligencia artificial para el análisis.  

---

## 🛠️ Tecnologías Utilizadas  
🔹 **Python 3.11**  
🔹 **FastAPI** - Para una API rápida y eficiente.  
🔹 **OpenAI API** - Para análisis de texto y generación de recomendaciones.  
🔹 **Hugging Face API** - Para embeddings y comparación semántica.  
🔹 **Pydantic** - Para validación de datos.  
🔹 **Uvicorn** - Para ejecutar el servidor FastAPI.  

---

## 📂 Estructura del Proyecto  
```
app/
│   ├── __init__.py
│   ├── models/
│   │   └── schemas.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── cv_match.py
│   ├── services/
│   │   ├── extract_job_desciption.py
│   │   ├── generate.py
│   │   └── text_processing.py
│   └── utils/
│       └── pdf_utils.py
├── commitlint.config.js
├── main.py
├── package-lock.json
├── package.json
├── pyproject.toml
├── readme.md
├── requirements.txt
└── yarn.lock
```

---

## 🎯 Endpoints Disponibles  
### 📌 **`POST /cv/match`**  
📌 **Descripción:** Analiza el CV y lo compara con la oferta de trabajo.  

#### 👥 **Request Body:**  
```json
{
  "cv_text": "Desarrollador con experiencia en React y Python...",
  "job_description": "Buscamos un desarrollador con experiencia en React y TypeScript..."
}
```
#### 📤 **Response:**  
```json
{
  "skills_match": {
    "coincidencias": 2,
    "total_requeridas": 3,
    "habilidades_coincidentes": ["React", "JavaScript"]
  },
  "experience_level": {
    "cumple": true,
    "explicación": "El candidato tiene experiencia relevante en frontend."
  },
  "recruiter_message": "Incluye más detalles sobre TypeScript para mejorar la coincidencia."
}
```

---

## 📃 **Ejemplo de Uso con `cURL`**  
Puedes probar la API enviando una solicitud con `cURL`:
```bash
curl -X POST "http://127.0.0.1:8000/cv/match" \
     -H "Content-Type: application/json" \
     -d '{
           "cv_text": "Desarrollador con experiencia en React y Python...",
           "job_description": "Buscamos un desarrollador con experiencia en React y TypeScript..."
         }'
```

Si la API está corriendo correctamente, obtendrás un **JSON estructurado** con la evaluación de coincidencias y recomendaciones.

---

## 📦 Instalación y Configuración  
### 🔹 **1. Clonar el repositorio**  
```bash
git clone https://github.com/tu_usuario/cv-matcher.git
cd cv-matcher
```

### 🔹 **2. Crear un entorno virtual y activarlo**  
```bash
python -m venv env
source env/bin/activate  # MacOS/Linux
env\Scripts\activate  # Windows
```

### 🔹 **3. Instalar las dependencias**  
```bash
pip install -r requirements.txt
```

### 🔹 **4. Configurar variables de entorno**  
Crea un archivo `.env` en la raíz del proyecto y agrega:  
```
OPENAI_API_KEY=tu_clave_api
HF_API_KEY=tu_clave_de_huggingface
```

### 🔹 **5. Ejecutar el servidor**  
```bash
uvicorn app.main:app --reload
```
📌 La API estará disponible en `http://127.0.0.1:8000/docs` 📝  

---

## 🎯 Roadmap 🚀  
🔹 **Integración con LinkedIn** para extraer experiencia automáticamente.  
🔹 **Generación automática de cartas de presentación personalizadas.**  
🔹 **Soporte para múltiples idiomas.**  
🔹 **Visualización de datos y estadísticas de comparación.**  

---

## 📄 Licencia  
📝 Este proyecto está bajo la **MIT License**.  

---

## 🤝 Contribuciones  
¡Las contribuciones son bienvenidas! 🎉  
Si quieres mejorar el proyecto, **haz un fork y envía un PR**.  

📩 **Contacto:** [ianisaacmdz@gmail.com](mailto:ianisaacmdz@gmail.com)  

🌟 **Si te gusta el proyecto, dale una estrella en GitHub!** ⭐
