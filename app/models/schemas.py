from pydantic import BaseModel


class CVComparisonResponse(BaseModel):
    match_percentage: float
    extracted_text: str
