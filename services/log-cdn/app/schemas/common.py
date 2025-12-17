from pydantic import BaseModel
from typing import Optional, Any


class ErrorResponse(BaseModel):
    """Standard error response schema."""
    
    error: str
    message: str
    request_id: Optional[str] = None
    details: Optional[Any] = None
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "error": "ValidationError",
                "message": "Invalid request data",
                "request_id": "req_abc123",
                "details": {"field": "email", "issue": "invalid format"}
            }
        }
    }


class SuccessResponse(BaseModel):
    """Standard success response schema."""
    
    success: bool = True
    message: str
    data: Optional[Any] = None
