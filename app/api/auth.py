from app.dto.auth import (
    AccessTokenDto,
    JwtCredentials,
    LoginDto,
    RegistrationDto,
    RegistrationResponse,
)
from app.services.auth import AuthService, get_auth_service
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.post("/register/", response_model=RegistrationResponse)
async def register(
    data: RegistrationDto, auth_service: AuthService = Depends(get_auth_service)
) -> RegistrationResponse:
    return await auth_service.register(data)


@router.post("/login/", response_model=JwtCredentials)
async def login(
    data: LoginDto, auth_service: AuthService = Depends(get_auth_service)
) -> JwtCredentials:
    return await auth_service.authenticate(data)


@router.post("/token/")
async def refresh_token() -> AccessTokenDto:
    pass
