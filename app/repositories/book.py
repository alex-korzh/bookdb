from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Book
from app.repositories.base import BaseRepository


class BookRepository(BaseRepository[Book]):
    model = Book


async def get_book_repository(session: AsyncSession) -> BookRepository:
    return BookRepository(session=session)
