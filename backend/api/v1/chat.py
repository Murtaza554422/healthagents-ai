from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["Chat"])


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    return {
        "reply": f"HealthAgents received: {request.message}"
    }