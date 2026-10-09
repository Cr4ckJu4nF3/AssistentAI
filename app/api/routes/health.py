from fastapi import APIRouter

from app.core.config import APP_VERSION
from app.schemas.health import HealthResponse


router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(
        service="ai-knowledge-assistant",
        version=APP_VERSION,
    )
