from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import EmailRequest, QuestionnaireRequest, FrameworkResponse
from logic import suggest_framework
from typing import Dict, List
import json

app = FastAPI()

# Simple in-memory database for MVP
email_db: List[str] = []
answers_db: Dict[str, dict] = {}

@app.get("/")
def read_root():
    return {"message": "Hello from Open GTM API"}

# Enable CORS for local dev and Docker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://frontend:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/start")
def start(request: EmailRequest):
    """
    Capture email and store in DB
    """
    email = request.email
    if email not in email_db:
        email_db.append(email)
    return {"success": True, "message": "Email captured successfully"}

@app.post("/api/submit_answers", response_model=FrameworkResponse)
def submit_answers(request: QuestionnaireRequest):
    """
    Validate payload, process questionnaire and return GTM model recommendation
    """
    # Store answers in DB
    answers_db[request.email] = request.dict()

    # Process through logic engine
    result = suggest_framework(request)

    return FrameworkResponse(**result)

# Keep the original endpoint for backward compatibility
@app.post("/suggest", response_model=FrameworkResponse)
def suggest(request: QuestionnaireRequest):
    result = suggest_framework(request)
    return FrameworkResponse(**result)
