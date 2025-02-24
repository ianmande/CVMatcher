from typing import Dict, List, Union

from pydantic import BaseModel


class SkillsMatch(BaseModel):
    coincidencias: int
    total_requeridas: int
    habilidades_coincidentes: List[str]


class ExperienceLevel(BaseModel):
    cumple: bool
    explicación: str


class CVComparisonResponse(BaseModel):
    skills_match: SkillsMatch
    experience_level: ExperienceLevel
    recruiter_message: str
