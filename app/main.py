from fastapi import FastAPI

from app.api.routes.chat import router as chat_router
from app.api.routes.health import router as health_router
from app.api.routes.info import router as info_router
from app.core.config import APP_NAME, APP_VERSION


app = FastAPI(
    title=APP_NAME,
    description=(
        "API evolutiva para el curso "
        "de Ingeniería de Sistemas de IA."
    ),
    version=APP_VERSION,
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(info_router)
