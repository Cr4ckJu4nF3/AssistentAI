from fastapi import APIRouter

from app.core.config import (
    APP_NAME,
    APP_VERSION,
    ENVIRONMENT,
    LLM_ENABLED,
)
from app.schemas.info import InfoResponse


router = APIRouter(
    prefix="/api/v1/info",
    tags=["info"],
)


@router.get("", response_model=InfoResponse)
async def info() -> InfoResponse:
    return InfoResponse(
        name=APP_NAME,
        version=APP_VERSION,
        environment=ENVIRONMENT,
        llm_enabled=LLM_ENABLED,
    )
