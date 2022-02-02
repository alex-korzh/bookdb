from typing import Optional

from app.models.user import User
from app.repositories.base import BaseRepository
from sqlalchemy import or_
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository(BaseRepository[User]):
    model = User

    async def get_by_email(self, email: str) -> Optional[User]:
        result = (
            await self.session.execute(
                self.select.filter_by(email=email)  # type: ignore
            )
        ).first()
        return result[0] if result else None

    async def check_user_by_email_username(self, email: str, username: str) -> bool:
        users = await self.session.execute(
            self.select_count.filter(  # type: ignore
                or_(User.email == email, User.username == username)
            )
        )
        return users.scalar_one() > 0


async def get_user_repository(session: AsyncSession) -> UserRepository:
    return UserRepository(session=session)
