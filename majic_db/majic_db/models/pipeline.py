import uuid
from typing import List
from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from majic_db.models.base import MajicBaseModel
from majic_db.models.data_types.status import PipelineStatus


class Pipeline(MajicBaseModel):
    __tablename__ = "pipeline"
    id: Mapped[int] = mapped_column(primary_key=True)
    pipeline_id: Mapped[Uuid] = mapped_column(default=uuid.uuid4())
    version: Mapped[int] = mapped_column(default=0)
    name: Mapped[str] = mapped_column(String(128))
    tasks: Mapped[List["Task"]] = relationship(back_populates="pipeline")
    status: Mapped[PipelineStatus]

    def __repr__(self) -> str:
        return f"Pipeline(id={self.id!r})"

