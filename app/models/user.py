from app.db import Base
from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import IdentifiableMixin


class User(Base, IdentifiableMixin):
    __tablename__ = "users"

    email = Column(String(120), nullable=False)
    password = Column(String(120), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)
    is_banned = Column(Boolean, nullable=False, default=False)

    role_id = Column(UUID(as_uuid=True), ForeignKey("role.id"))


class Role(Base, IdentifiableMixin):
    __tablename__ = "roles"

    name = Column(String(120), nullable=False)

    users = relationship("User", backref="role")
