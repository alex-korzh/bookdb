from typing import Optional

from app.db import get_session
from app.models.user import User
from app.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository(BaseRepository[User]):
    model = User

    async def get_by_email(self, email: str) -> Optional[User]:
        return await self.session.execute(
            self.select.filter_by(email=email)  # type: ignore
        )


async def get_user_repository(session: AsyncSession) -> UserRepository:
    return UserRepository(session=session)
