from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sunstrike_db.models.base import BaseModel


class Component(BaseModel):
    __tablename__ = "component"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128))

    # Todo add deployment schemes

    # tasks = relationship("Task", back_populates="component")

    def __repr__(self) -> str:
        return f"Component(id={self.id!r}, name={self.name!r}, tasks={self.tasks!r})"

