from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any, List
from enum import Enum


class LogLevel(str, Enum):
    """Log level enum."""
    DEBUG = "debug"
    INFO = "info"
    WARN = "warn"
    ERROR = "error"
    FATAL = "fatal"


class LogBase(BaseModel):
    """Base log schema."""
    
    level: LogLevel = Field(..., description="Log severity level")
    message: str = Field(..., min_length=1, max_length=10000, description="Log message")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional metadata")


class LogCreate(LogBase):
    """Schema for creating a log entry."""
    
    source: Optional[str] = Field(default=None, max_length=255, description="Log source identifier")
    timestamp: Optional[datetime] = Field(default=None, description="Log timestamp (defaults to now)")


class LogResponse(LogBase):
    """Schema for log response."""
    
    id: str = Field(..., description="Unique log identifier")
    source: Optional[str] = None
    timestamp: datetime
    created_at: datetime
    
    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "id": "log_abc123",
                "level": "info",
                "message": "User logged in successfully",
                "metadata": {"user_id": "usr_123", "ip": "192.168.1.1"},
                "source": "auth-service",
                "timestamp": "2024-01-15T10:30:00Z",
                "created_at": "2024-01-15T10:30:01Z",
            }
        }
    }


class PaginationMeta(BaseModel):
    """Pagination metadata."""
    
    page: int
    page_size: int
    total_items: int
    total_pages: int


class LogsListResponse(BaseModel):
    """Schema for paginated logs list response."""
    
    data: List[LogResponse]
    meta: PaginationMeta
