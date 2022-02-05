from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.repositories.book import BookRepository, get_book_repository


class BookService:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository


async def get_book_service(session: AsyncSession = Depends(get_session)) -> BookService:
    book_repository = await get_book_repository(session)
    return BookService(book_repository=book_repository)
