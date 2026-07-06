from fastapi import FastAPI
from backend.api.router import api_router
from backend.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
)

app.include_router(api_router)