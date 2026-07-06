from fastapi import APIRouter

from backend.api.v1.health import router as health_router
from backend.api.v1.chat import router as chat_router
from backend.api.v1.report import router as report_router
from backend.api.v1.vision import router as vision_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(chat_router)
api_router.include_router(report_router)
api_router.include_router(vision_router)