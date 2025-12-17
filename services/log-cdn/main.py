"""
Log CDN Service - Entry Point

This file re-exports the app from the modular structure.
Run with: uvicorn main:app --reload
Or: uvicorn app.main:app --reload
"""
from app.main import app

__all__ = ["app"]