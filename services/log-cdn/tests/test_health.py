"""
Tests for health check endpoints.
"""
import pytest
from unittest.mock import MagicMock, AsyncMock, patch
from sqlalchemy import text


def test_liveness_check(client):
    """Test liveness probe returns 200."""
    response = client.get("/api/v1/live")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}


def test_readiness_check(client):
    """Test readiness probe returns 200."""
    response = client.get("/api/v1/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_root_endpoint(client):
    """Test root endpoint returns service info."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "service" in data
    assert "version" in data
