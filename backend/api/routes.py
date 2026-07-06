from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.get("/")
def home():
    return {
        "message": "Welcome to HealthAgents API 🚀",
        "status": "Running"
    }


@router.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@router.post("/chat")
def chat(request: ChatRequest):
    return {
        "reply": f"HealthAgents received: {request.message}"
    }