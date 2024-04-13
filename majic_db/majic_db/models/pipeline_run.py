from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from majic_db.models.base import MajicBaseModel
from majic_db.models.data_types.status import PipelineRunStatus

class PipelineRun(MajicBaseModel):
    __tablename__ = "pipeline_run"
    id: Mapped[int] = mapped_column(primary_key=True)
    attempt: Mapped[int]
    pipeline_id: Mapped[int] = mapped_column(ForeignKey("pipeline.id"))
    pipeline: Mapped["Pipeline"] = relationship(back_populates="pipeline_runs")

    task_runs: Mapped[List["TaskRun"]] = relationship(back_populates="pipeline_run")
    status: Mapped[PipelineRunStatus]

    def __repr__(self) -> str:
        return f"PipelineRun(id={self.id!r})"
