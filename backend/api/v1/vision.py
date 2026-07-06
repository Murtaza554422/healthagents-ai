from fastapi import APIRouter

router = APIRouter(prefix="/vision", tags=["Medical Vision"])


@router.get("/")
def vision():

    return {
        "message": "Vision Agent Coming Soon"
    }