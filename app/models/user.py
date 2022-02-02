from app.db import Base
from app.types import RoleType
from sqlalchemy import Boolean, Column, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import IdentifiableMixin


class User(Base, IdentifiableMixin):
    __tablename__ = "users"

    email = Column(String(120), nullable=False, unique=True)
    username = Column(String(120), nullable=False, unique=True)
    password = Column(String(120), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)
    is_banned = Column(Boolean, nullable=False, default=False)

    role = Column(Enum(RoleType))
