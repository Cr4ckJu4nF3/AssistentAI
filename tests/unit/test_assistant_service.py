from app.core.config import PROVIDER_NAME
from app.services.assistant_service import BootstrapAssistantService


async def test_service_answers_known_question():
    """T-01: el servicio responde a una pregunta conocida."""
    service = BootstrapAssistantService()

    response = await service.answer("¿Qué es FastAPI?")

    assert "FastAPI" in response.answer
    assert response.provider == PROVIDER_NAME


async def test_service_returns_default_for_unknown_question():
    service = BootstrapAssistantService()

    response = await service.answer("Pregunta sin tema conocido")

    assert "operativa" in response.answer
    assert response.provider == PROVIDER_NAME
