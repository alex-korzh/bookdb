from typing import cast

from app.db import get_session
from app.dto.auth import RegistrationDto, UserDto
from app.models.user import User
from app.repositories.user import UserRepository, get_user_repository
from app.types import RoleType
from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession


class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def _hash_password(self, password: str) -> str:
        return self._pwd_context.hash(password)

    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self._pwd_context.verify(plain_password, hashed_password)

    async def register(self, data: RegistrationDto) -> UserDto:
        if await self._user_repository.check_user_by_email_username(
            data.email, data.username
        ):
            raise HTTPException(
                status_code=409,
                detail="User with this email or username already exists",
            )
        new_user = User(
            email=data.email,
            username=data.username,
            password=self._hash_password(data.password.get_secret_value()),
            role=RoleType.USER,
        )
        await self._user_repository.update(new_user)
        db_user = await self._user_repository.get_by_email(data.email)
        if not db_user:
            raise HTTPException(status_code=500, detail="User creating unsuccessful")
        return UserDto(
            email=db_user.email,
            username=db_user.username,
            is_active=db_user.is_active,
            is_banned=db_user.is_banned,
            role=cast(RoleType, db_user.role),
        )


async def get_auth_service(session: AsyncSession = Depends(get_session)) -> AuthService:
    user_repository = await get_user_repository(session)
    return AuthService(user_repository=user_repository)
