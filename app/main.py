from fastapi import FastAPI

from app.routers.users import router as users_router


app = FastAPI(
    title="Dummy User Service",
    version="1.0.0",
    description="A small FastAPI service used to validate endpoint ingestion from Git repositories.",
)


@app.get("/health", tags=["system"], summary="Health check")
async def health_check() -> dict[str, str]:
    """Return a simple service health response."""
    return {"status": "ok"}


app.include_router(users_router, prefix="")
