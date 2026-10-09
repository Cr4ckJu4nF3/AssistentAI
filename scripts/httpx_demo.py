"""Demo de HTTPX asíncrono contra la propia app (sin servidor externo).

Ejecutar desde la raíz del proyecto:
    python -m scripts.httpx_demo
"""
import asyncio
import time

import httpx

from app.main import app

QUESTIONS = [
    "¿Qué es FastAPI?",
    "¿Qué es Pydantic?",
    "¿Qué es AsyncIO?",
    "¿Qué es HTTPX?",
]


async def ask(client: httpx.AsyncClient, question: str) -> str:
    response = await client.post(
        "/api/v1/chat", json={"question": question}
    )
    response.raise_for_status()
    return response.json()["answer"]


async def main() -> None:
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(
        transport=transport, base_url="http://demo"
    ) as client:
        health = await client.get("/health")
        print("health:", health.json())

        start = time.perf_counter()
        answers = await asyncio.gather(
            *(ask(client, q) for q in QUESTIONS)
        )
        elapsed = time.perf_counter() - start

        for question, answer in zip(QUESTIONS, answers):
            print(f"\n> {question}\n{answer}")
        print(f"\n{len(QUESTIONS)} peticiones concurrentes en {elapsed:.3f}s")


if __name__ == "__main__":
    asyncio.run(main())
