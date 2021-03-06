__all__ = [
    "User",
]
from app.db import Base
from app.types import RoleType
from sqlalchemy import Boolean, Column, Enum, String

from app.models.base import UUIDMixin


class User(Base, UUIDMixin):
    __tablename__ = "users"

    email = Column(String(120), nullable=False, unique=True)
    username = Column(String(120), nullable=False, unique=True)
    password = Column(String(120), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)
    is_banned = Column(Boolean, nullable=False, default=False)

    role = Column(Enum(RoleType))
