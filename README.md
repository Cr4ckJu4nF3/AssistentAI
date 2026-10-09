# AI Knowledge Assistant — Bootstrap API (Módulo 0)

Primer incremento funcional: una API asíncrona con FastAPI, validada con
Pydantic y probada con pytest. **No integra ningún LLM** (el proveedor es
`bootstrap-local`).

## Requisitos

- Python 3.12 o superior
- Git

## Instalación

```bash
python -m venv .venv
```

Activar el entorno:

| Sistema | Comando |
|---|---|
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (CMD) | `.venv\Scripts\activate.bat` |
| Linux / macOS | `source .venv/bin/activate` |

Instalar dependencias (incluye las de desarrollo):

```bash
pip install -e ".[dev]"
```

## Ejecutar la API

```bash
uvicorn app.main:app --reload
```

- Documentación Swagger: http://127.0.0.1:8000/docs
- Health: http://127.0.0.1:8000/health

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/health` | Estado del servicio |
| POST | `/api/v1/chat` | Respuesta del asistente (bootstrap) |
| GET | `/api/v1/info` | Información del proyecto |

Ejemplo:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "¿Qué es FastAPI?"}'
```

```json
{"answer": "FastAPI es un framework de Python ...", "provider": "bootstrap-local"}
```

La pregunta debe tener entre 3 y 2000 caracteres; de lo contrario la API
responde `422 Unprocessable Entity` (validación de Pydantic).

## Pruebas

```bash
python -m pytest -q
```

## Scripts de demostración

```bash
python -m scripts.asyncio_demo   # secuencial vs concurrente con asyncio.gather
python -m scripts.httpx_demo     # httpx.AsyncClient contra la app (sin servidor)
```

## Estructura

```
app/
├── main.py            # creación de la app y registro de routers
├── core/config.py     # constantes (nombre, versión, provider)
├── api/routes/        # capa HTTP (health, chat, info)
├── schemas/           # modelos Pydantic
└── services/          # lógica del asistente (independiente del router)
scripts/               # demos AsyncIO / HTTPX
tests/unit/            # pruebas del servicio
tests/integration/     # pruebas de la API (sin servidor externo)
```

Flujo: `Cliente → FastAPI → Pydantic → Router → Servicio → Respuesta`.

## Flujo Git

Rama de trabajo `feat/bootstrap-api` → Pull Request hacia `main`.
