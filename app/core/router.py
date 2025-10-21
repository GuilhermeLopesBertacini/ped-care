from fastapi import APIRouter
from app.routes import health, gemini

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health.router)
api_router.include_router(gemini.router)