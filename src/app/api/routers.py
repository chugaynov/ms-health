from fastapi import APIRouter

from app.api.health import endpoint as health

api_router = APIRouter()

api_router.include_router(health.router, include_in_schema=False)
