from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from majic_db.models.base import MajicBaseModel

class Component(MajicBaseModel):
    __tablename__ = "component"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128))

    # Todo add deployment schemes

    task: Mapped[List["Task"]] = relationship(back_populates="component")

    def __repr__(self) -> str:
        return f"Component(id={self.id!r})"
