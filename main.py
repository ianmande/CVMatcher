from dotenv import load_dotenv
from fastapi import FastAPI

from app.routes.cv_match import router as cv_router

load_dotenv()

app = FastAPI(title="CV Matching API")

app.include_router(cv_router)


@app.get("/")
def root():
    return {"message": "API de comparación de CVs con SBERT funcionando!"}
