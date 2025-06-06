from pydantic import BaseModel, EmailStr
from typing import Optional

class EmailRequest(BaseModel):
    email: EmailStr

class QuestionnaireRequest(BaseModel):
    email: EmailStr
    stage: str
    gtm_known: bool
    gtm_description: Optional[str] = None
    launch_approach: Optional[str] = None
    audience: str
    growth: str
    pricing: str
    confidence: int
    first_customers_time: Optional[str] = None
    blockers: Optional[list[str]] = None

class FrameworkResponse(BaseModel):
    model: str
    rationale: str
    cta: str
