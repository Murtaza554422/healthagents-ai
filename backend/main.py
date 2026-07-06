from fastapi import FastAPI

from backend.api.routes import router
from backend.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
)

app.include_router(router)