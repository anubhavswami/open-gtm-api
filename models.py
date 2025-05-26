from pydantic import BaseModel

class QuestionnaireRequest(BaseModel):
    audience: str
    growth: str
    pricing: str

class FrameworkResponse(BaseModel):
    framework: str
