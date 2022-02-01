from app.api.router import router
from app.dto.auth import AccessTokenDto, JwtCredentials, LoginDto, RegistrationDto
from fastapi import HTTPException


@router.post("/register/", response_model=JwtCredentials)
async def register(data: RegistrationDto) -> JwtCredentials:
    pass


@router.post("/login/", response_model=JwtCredentials)
async def login(data: LoginDto) -> JwtCredentials:
    pass


@router.post("/token/")
async def refresh_token() -> AccessTokenDto:
    pass
