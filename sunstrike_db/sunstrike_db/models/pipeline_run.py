from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sunstrike_db.models.base import BaseModel
from sunstrike_db.models.data_types.status import PipelineRunStatus


class PipelineRun(BaseModel):
    __tablename__ = "pipeline_run"
    id: Mapped[int] = mapped_column(primary_key=True)
    attempt: Mapped[int]
    status: Mapped[PipelineRunStatus]

    pipeline_id: Mapped[int] = mapped_column(ForeignKey("pipeline.id"))
    pipeline = relationship( "Pipeline", back_populates="pipeline_runs")

    task_runs = relationship("TaskRun", back_populates="pipeline_run")


    def __repr__(self) -> str:
        return f"""PipelineRun(
            id={self.id!r}, attempt={self.attempt!r},
            task_runs={self.task_runs!r}, status={self.status!r},
        )"""
