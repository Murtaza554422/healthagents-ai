from fastapi import APIRouter
from pydantic import BaseModel
from backend.agents.rag_agent import rag_agent
from backend.agents.router_agent import router_agent
from backend.agents.symptom_agent import symptom_agent
from backend.agents.report_agent import report_agent
from backend.agents.vision_agent import vision_agent

router = APIRouter(tags=["Chat"])


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    route = router_agent.route(request.message)

    if route == "symptom":
        return symptom_agent.process(request.message)

    elif route == "report":
        return report_agent.process(request.message)

    elif route == "vision":
        return vision_agent.process(request.message)

    else:
        return rag_agent.process(request.message)