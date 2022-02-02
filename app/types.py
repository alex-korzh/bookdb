import enum


class RoleType(str, enum.Enum):
    USER = "user"
    MANAGER = "manager"
    MODERATOR = "moderator"
    ADMIN = "admin"
