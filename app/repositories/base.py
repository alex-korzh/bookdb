import uuid
from statistics import mode
from typing import Any, Generic, List, Optional, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql.expression import Select

TModel = TypeVar("TModel")


class BaseRepository(Generic[TModel]):
    model: Type[TModel]

    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        super().__init__()

    @property
    def select(self) -> Select:
        return select(self.model)

    async def get_by_id(self, id: uuid.UUID) -> Optional[TModel]:
        return await self.session.get(self.model, id)

    async def get_all(self) -> List[TModel]:
        return await self.session.execute(self.select)

    async def update(self, obj: TModel) -> None:
        self.session.add(obj)
        await self.session.flush([obj])

    async def delete(self, obj: TModel) -> None:
        await self.session.delete(obj)
        await self.session.flush([obj])
