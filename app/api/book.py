__all__ = [
    "book_router",
]
from fastapi import APIRouter

book_router = APIRouter(prefix="/book")
