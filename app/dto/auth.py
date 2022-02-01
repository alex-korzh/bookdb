from pydantic import BaseModel, SecretStr, validator


class LoginDto(BaseModel):
    email: str
    password: SecretStr


class RegistrationDto(LoginDto):
    username: str
    repeated_password: SecretStr

    @validator("repeated_password")
    def passwords_match(cls, v, values, **kwargs):
        if (
            "password" in values
            and v.get_secret_value() != values["password"].get_secret_value()
        ):
            raise ValueError("Passwords do not match")
        return v


class AccessTokenDto(BaseModel):
    access_token: str


class JwtCredentials(AccessTokenDto):
    id: str
    refresh_token: str