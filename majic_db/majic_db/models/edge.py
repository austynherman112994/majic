from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from majic_db.models.base import MajicBaseModel

class Edges(MajicBaseModel):
    __tablename__ = "edges"
    id: Mapped[int] = mapped_column(primary_key=True)

    pipeline_id: Mapped[int] = mapped_column(ForeignKey("pipeline.id"))
    pipeline: Mapped["Pipeline"] = relationship(back_populates="edges")

    task_id: Mapped[int] = mapped_column(ForeignKey("task.id"))
    task: Mapped["Task"] = relationship(back_populates="edge")

    downstream_task_id: Mapped[int] = mapped_column(ForeignKey("task.id"))
    downstream_task: Mapped["Task"] = relationship(back_populates="tasks")


    def __repr__(self) -> str:
        return f"Edges(id={self.id!r})"
