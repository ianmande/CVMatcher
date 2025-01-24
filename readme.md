fastapi_sbert/
│── app/
│   │── __init__.py
│   │── main.py  # Punto de entrada de la API
│   │── config.py  # Configuración global de la API
│   │── models/  # Modelos de datos
│   │   │── __init__.py
│   │   │── schemas.py  # Definición de los schemas (Pydantic)
│   │── routes/  # Rutas y endpoints
│   │   │── __init__.py
│   │   │── cv_match.py  # Lógica del endpoint de comparación
│   │── services/  # Lógica de negocio
│   │   │── __init__.py
│   │   │── text_processing.py  # Funciones para extraer texto y procesar embeddings
│   │── utils/  # Funciones utilitarias
│   │   │── __init__.py
│   │   │── pdf_utils.py  # Funciones para manejar PDFs y OCR
│── data/  # Carpeta para almacenar PDFs subidos (opcional)
│── tests/  # Pruebas unitarias
│── .env  # Variables de entorno
│── requirements.txt  # Dependencias del proyecto
│── README.md  # Documentación del proyecto
│── run.sh  # Script para iniciar la API fácilmente