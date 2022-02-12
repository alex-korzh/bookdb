import uuid

from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID


class UUIDMixin:
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )


class IdentifiableMixin:
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False,
    )
