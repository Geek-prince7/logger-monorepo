"""
API Dependencies.

Common dependencies used across API endpoints.
"""
from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from app.db import get_db
from app.cache import get_redis, RedisClient

# API Key header for authentication
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


async def verify_api_key(api_key: str = Depends(api_key_header)) -> str:
    """
    Verify API key from request header.
    
    Usage:
        @router.get("/protected")
        async def protected_route(api_key: str = Depends(verify_api_key)):
            ...
    """
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key required",
        )
    
    # TODO: Validate API key against database/cache
    # For now, accept any non-empty key
    
    return api_key


def get_pagination_params(
    page: int = 1,
    page_size: int = 50,
) -> dict:
    """
    Get pagination parameters.
    
    Returns offset and limit for database queries.
    """
    return {
        "offset": (page - 1) * page_size,
        "limit": page_size,
    }
