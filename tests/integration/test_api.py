import httpx
import pytest

from app.main import app


@pytest.fixture
async def client():
    """Cliente asíncrono que invoca la app directamente (sin servidor)."""
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(
        transport=transport, base_url="http://test"
    ) as c:
        yield c


async def test_health_returns_200(client):
    """T-02"""
    response = await client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


async def test_chat_valid_question_returns_200(client):
    """T-03"""
    response = await client.post(
        "/api/v1/chat", json={"question": "¿Qué es FastAPI?"}
    )

    assert response.status_code == 200
    body = response.json()
    assert set(body) == {"answer", "provider"}
    assert body["provider"] == "bootstrap-local"


async def test_chat_too_short_returns_422(client):
    """T-04"""
    response = await client.post("/api/v1/chat", json={"question": "ab"})

    assert response.status_code == 422


async def test_chat_too_long_returns_422(client):
    response = await client.post(
        "/api/v1/chat", json={"question": "a" * 2001}
    )

    assert response.status_code == 422


async def test_chat_missing_field_returns_422(client):
    response = await client.post("/api/v1/chat", json={})

    assert response.status_code == 422


async def test_info_returns_200_and_llm_disabled(client):
    """T-05"""
    response = await client.get("/api/v1/info")

    assert response.status_code == 200
    body = response.json()
    assert body["llm_enabled"] is False
    assert body["name"] == "AI Knowledge Assistant"
    assert body["version"] == "0.1.0"
    assert body["environment"] == "development"


async def test_docs_available(client):
    response = await client.get("/docs")

    assert response.status_code == 200
