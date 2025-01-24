from fastapi import FastAPI

from app.routes.cv_match import router as cv_router

app = FastAPI(title="CV Matching API")

# Incluir las rutas
app.include_router(cv_router)


@app.get("/")
def root():
    return {"message": "API de comparación de CVs con SBERT funcionando!"}
