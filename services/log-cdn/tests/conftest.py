"""
Pytest configuration and fixtures.
"""
import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, MagicMock

from app.main import app
from app.db import get_db
from app.cache import get_redis


@pytest.fixture
def client():
    """Create test client with mocked dependencies."""
    
    # Mock database session
    mock_db = MagicMock()
    
    # Mock Redis client
    mock_redis = AsyncMock()
    mock_redis.get.return_value = None
    mock_redis.set.return_value = True
    mock_redis.client = MagicMock()
    mock_redis.client.ping = AsyncMock(return_value=True)
    
    # Override dependencies
    app.dependency_overrides[get_db] = lambda: mock_db
    app.dependency_overrides[get_redis] = lambda: mock_redis
    
    with TestClient(app) as test_client:
        yield test_client
    
    # Clear overrides after test
    app.dependency_overrides.clear()


@pytest.fixture
def mock_db():
    """Provide a mock database session."""
    return MagicMock()


@pytest.fixture
def mock_redis():
    """Provide a mock Redis client."""
    mock = AsyncMock()
    mock.get.return_value = None
    mock.get_json.return_value = None
    mock.set.return_value = True
    mock.set_json.return_value = True
    mock.delete.return_value = 1
    mock.exists.return_value = False
    return mock
