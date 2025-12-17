import redis.asyncio as redis
from typing import Optional
import json

from app.core.config import settings


class RedisClient:
    """Redis client wrapper for caching operations."""
    
    def __init__(self):
        self._client: Optional[redis.Redis] = None
    
    async def connect(self) -> None:
        """Initialize Redis connection."""
        self._client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            password=settings.REDIS_PASSWORD,
            db=settings.REDIS_DB,
            decode_responses=True,
        )
    
    async def disconnect(self) -> None:
        """Close Redis connection."""
        if self._client:
            await self._client.close()
            self._client = None
    
    @property
    def client(self) -> redis.Redis:
        """Get Redis client instance."""
        if self._client is None:
            raise RuntimeError("Redis client not initialized. Call connect() first.")
        return self._client
    
    async def get(self, key: str) -> Optional[str]:
        """Get value from cache."""
        return await self.client.get(key)
    
    async def get_json(self, key: str) -> Optional[dict]:
        """Get JSON value from cache."""
        value = await self.get(key)
        if value:
            return json.loads(value)
        return None
    
    async def set(
        self,
        key: str,
        value: str,
        ttl: Optional[int] = None
    ) -> bool:
        """Set value in cache with optional TTL."""
        ttl = ttl or settings.REDIS_CACHE_TTL
        return await self.client.setex(key, ttl, value)
    
    async def set_json(
        self,
        key: str,
        value: dict,
        ttl: Optional[int] = None
    ) -> bool:
        """Set JSON value in cache."""
        return await self.set(key, json.dumps(value), ttl)
    
    async def delete(self, key: str) -> int:
        """Delete key from cache."""
        return await self.client.delete(key)
    
    async def exists(self, key: str) -> bool:
        """Check if key exists in cache."""
        return bool(await self.client.exists(key))
    
    async def flush_pattern(self, pattern: str) -> int:
        """Delete all keys matching pattern."""
        keys = await self.client.keys(pattern)
        if keys:
            return await self.client.delete(*keys)
        return 0


# Global Redis client instance
redis_client = RedisClient()


async def get_redis() -> RedisClient:
    """
    Dependency that provides Redis client.
    
    Usage:
        @app.get("/items")
        async def get_items(cache: RedisClient = Depends(get_redis)):
            ...
    """
    return redis_client
