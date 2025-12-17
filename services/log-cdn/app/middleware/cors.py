from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings


def get_cors_middleware_params() -> dict:
    """
    Get CORS middleware configuration.
    
    Returns parameters to be passed to CORSMiddleware.
    """
    return {
        "allow_origins": settings.CORS_ORIGINS,
        "allow_credentials": True,
        "allow_methods": ["*"],
        "allow_headers": ["*"],
        "expose_headers": ["X-Request-ID", "X-Process-Time"],
    }
