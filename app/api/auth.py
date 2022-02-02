from app.api.router import router
from app.dto.auth import (
    AccessTokenDto,
    JwtCredentials,
    LoginDto,
    RegistrationDto,
    UserDto,
)
from app.services.auth import AuthService, get_auth_service
from fastapi import Depends, HTTPException


@router.post("/register/", response_model=UserDto)
async def register(
    data: RegistrationDto, auth_service: AuthService = Depends(get_auth_service)
) -> UserDto:
    return await auth_service.register(data)


@router.post("/login/", response_model=JwtCredentials)
async def login(data: LoginDto) -> JwtCredentials:
    pass


@router.post("/token/")
async def refresh_token() -> AccessTokenDto:
    pass
