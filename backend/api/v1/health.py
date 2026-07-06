from fastapi import APIRouter

router = APIRouter(tags=["Health"])


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