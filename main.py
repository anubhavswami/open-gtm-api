from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import QuestionnaireRequest, FrameworkResponse
from logic import suggest_framework

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Open GTM API"}

# Enable CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/suggest", response_model=FrameworkResponse)
def suggest(request: QuestionnaireRequest):
    framework = suggest_framework(request)
    return FrameworkResponse(framework=framework)
