from app.db import get_session
from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    model = User


async def get_user_repository() -> UserRepository:
    session = await get_session()
    return UserRepository(session=session)
