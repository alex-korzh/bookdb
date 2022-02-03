from typing import Optional, cast

from app.config import settings
from app.models.user import User
from app.services.auth import AuthService, get_auth_service
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from jose import JWTError, jwt

security = HTTPBearer()


class AuthUtil:
    def __init__(
        self,
        credentials: HTTPBasicCredentials = Depends(security),
        auth_service: AuthService = Depends(get_auth_service),
    ) -> None:
        self._token = credentials.credentials  # type: ignore
        self._auth_service = auth_service
        self._credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credentials invalid"
        )

    async def authenticate(self) -> User:
        try:
            payload: dict = cast(
                dict,
                jwt.decode(
                    self._token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
                ),
            )
            email: Optional[str] = payload.get("sub")
            if not email:
                raise self._credentials_exception
        except JWTError:
            raise self._credentials_exception
        user = await self._auth_service.get_user_by_email(email)
        if not user:
            raise self._credentials_exception
        return user
