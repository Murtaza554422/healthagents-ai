from fastapi import APIRouter

router = APIRouter()


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