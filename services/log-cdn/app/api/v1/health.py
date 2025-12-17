from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db import get_db
from app.cache import redis_client
from app.core.config import settings
from app.schemas.health import HealthResponse, HealthStatus

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check(db: Session = Depends(get_db)) -> HealthResponse:
    """
    Health check endpoint for load balancers and monitoring.
    
    Checks:
    - Database connectivity
    - Redis connectivity
    - Application status
    """
    status = HealthStatus.HEALTHY
    checks = {}
    
    # Check database
    try:
        db.execute(text("SELECT 1"))
        checks["database"] = "healthy"
    except Exception as e:
        checks["database"] = f"unhealthy: {str(e)}"
        status = HealthStatus.UNHEALTHY
    
    # Check Redis
    try:
        await redis_client.client.ping()
        checks["redis"] = "healthy"
    except Exception as e:
        checks["redis"] = f"unhealthy: {str(e)}"
        status = HealthStatus.UNHEALTHY
    
    return HealthResponse(
        status=status,
        version=settings.APP_VERSION,
        service=settings.APP_NAME,
        checks=checks,
    )


@router.get("/ready")
async def readiness_check():
    """
    Readiness probe for Kubernetes.
    
    Returns 200 if the service is ready to accept traffic.
    """
    return {"status": "ready"}


@router.get("/live")
async def liveness_check():
    """
    Liveness probe for Kubernetes.
    
    Returns 200 if the service is alive.
    """
    return {"status": "alive"}
