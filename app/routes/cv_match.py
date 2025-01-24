from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import JSONResponse

from app.models.schemas import CVComparisonResponse
from app.services.extract_job_desciption import extract_job_description
from app.services.generate import generate_match_analysis
from app.services.text_processing import compare_cv_with_job

router = APIRouter(prefix="/cv", tags=["CV Matching"])


@router.post("/compare/", response_model=CVComparisonResponse)
async def compare_cv(
    cv_file: UploadFile = File(...),
    job_description: str = Form(...),
):
    job_url = job_description
    description = ""

    if "linkedin" in job_url:
        description = await extract_job_description(job_url)
    else:
        description = job_url

    result = await compare_cv_with_job(cv_file, description)
    result2 = await generate_match_analysis(result, description)

    print(result2)

    if "error" in result:
        return JSONResponse(content=result, status_code=400)

    return JSONResponse(content=result, status_code=200)
