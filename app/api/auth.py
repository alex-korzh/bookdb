__all__ = [
    "auth_router",
    "register",
    "login",
    "refresh_token",
]
from app.dto.auth import JwtCredentials, LoginDto, RegistrationDto, RegistrationResponse
from app.services.auth import AuthService, get_auth_service
from app.utils.auth import AuthUtil
from fastapi import APIRouter, Depends

auth_router = APIRouter()


@auth_router.post("/register/", response_model=RegistrationResponse)
async def register(
    data: RegistrationDto, auth_service: AuthService = Depends(get_auth_service)
) -> RegistrationResponse:
    return await auth_service.register(data)


@auth_router.post("/login/", response_model=JwtCredentials)
async def login(
    data: LoginDto, auth_service: AuthService = Depends(get_auth_service)
) -> JwtCredentials:
    return await auth_service.authenticate(data)


@auth_router.post("/refresh/", response_model=JwtCredentials)
async def refresh_token(
    auth_service: AuthService = Depends(get_auth_service),
    auth_util: AuthUtil = Depends(),
) -> JwtCredentials:
    auth_user = await auth_util.authenticate()
    return await auth_service.refresh(auth_user)
