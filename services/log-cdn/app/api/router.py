from fastapi import APIRouter

from app.api.v1 import health, logs

# Main API router that includes all versioned routes
api_router = APIRouter()

# Include v1 routes
api_router.include_router(
    health.router,
    prefix="/v1",
    tags=["health"],
)

api_router.include_router(
    logs.router,
    prefix="/v1/logs",
    tags=["logs"],
)
