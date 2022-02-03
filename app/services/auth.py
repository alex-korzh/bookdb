from datetime import datetime, timedelta

from app.config import settings
from app.db import get_session
from app.dto.auth import JwtCredentials, LoginDto, RegistrationDto, RegistrationResponse
from app.models.user import User
from app.repositories.user import UserRepository, get_user_repository
from app.types import RoleType
from fastapi import Depends, HTTPException
from jose import jwt
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

    def _generate_token(self, email: str, expiration_delta: timedelta) -> str:
        expires = datetime.utcnow() + expiration_delta
        data = {
            "sub": email,
            "exp": expires,
        }
        return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    async def authenticate(self, data: LoginDto) -> JwtCredentials:
        user = await self._user_repository.get_by_email(data.email)
        if not user or not self._verify_password(
            data.password.get_secret_value(), user.password
        ):
            raise HTTPException(
                status_code=401, detail="User with this credentials was not found"
            )
        access_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_delta = timedelta(hours=settings.REFRESH_TOKEN_EXPIRE_HOURS)
        return JwtCredentials(
            access_token=self._generate_token(user.email, access_delta),
            refresh_token=self._generate_token(user.email, refresh_delta),
        )

    async def register(self, data: RegistrationDto) -> RegistrationResponse:
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
        return RegistrationResponse(
            email=db_user.email,
            username=db_user.username,
        )


async def get_auth_service(session: AsyncSession = Depends(get_session)) -> AuthService:
    user_repository = await get_user_repository(session)
    return AuthService(user_repository=user_repository)
