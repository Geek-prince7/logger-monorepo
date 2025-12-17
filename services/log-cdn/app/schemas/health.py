from pydantic import BaseModel
from enum import Enum
from typing import Dict


class HealthStatus(str, Enum):
    """Health status enum."""
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DEGRADED = "degraded"


class HealthResponse(BaseModel):
    """Health check response schema."""
    
    status: HealthStatus
    version: str
    service: str
    checks: Dict[str, str]
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "status": "healthy",
                "version": "1.0.0",
                "service": "Log CDN Service",
                "checks": {
                    "database": "healthy",
                    "redis": "healthy",
                }
            }
        }
    }
