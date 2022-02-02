from app.db import get_session
from app.dto.auth import RegistrationDto, UserDto
from app.models.user import User
from app.repositories.user import UserRepository, get_user_repository
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    async def register(self, data: RegistrationDto) -> UserDto:
        new_user = User(email=data.email, password=data.password.get_secret_value())
        # TODO add role (consider adding it to the migration as it is part of the app. Also add migrations itself)
        await self._user_repository.update(new_user)
        db_user = await self._user_repository.get_by_email(data.email)
        if not db_user:
            # TODO system of exceptions
            raise Exception()
        return UserDto(
            email=db_user.email,
            is_active=db_user.is_active,
            is_banned=db_user.is_banned,
            role=db_user.role.name,
        )


async def get_auth_service(session: AsyncSession = Depends(get_session)) -> AuthService:
    user_repository = await get_user_repository(session)
    return AuthService(user_repository=user_repository)
