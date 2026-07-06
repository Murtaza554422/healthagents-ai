from fastapi import APIRouter

router = APIRouter(prefix="/report", tags=["Medical Reports"])


@router.get("/")
def report():

    return {
        "message": "Medical Report Agent Coming Soon"
    }