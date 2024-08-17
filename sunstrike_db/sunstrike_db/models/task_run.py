from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sunstrike_db.models.base import BaseModel
from sunstrike_db.models.data_types.status import TaskRunStatus


class TaskRun(BaseModel):
    __tablename__ = "task_run"
    id: Mapped[int] = mapped_column(primary_key=True)
    attempt: Mapped[int]

    task_id: Mapped[int] = mapped_column(ForeignKey("task.id"))
    task = relationship("Task", back_populates="task_runs")

    pipeline_run_id: Mapped[int] = mapped_column(ForeignKey("pipeline_run.id"))
    pipeline_run = relationship("PipelineRun", back_populates="task_runs")

    status: Mapped[TaskRunStatus]

    def __repr__(self) -> str:
        return f"""TaskRun(
            id={self.id!r}, attempt={self.attempt!r}, task_id={self.task_id!r}, task={self.task!r},
            pipeline_run_id={self.pipeline_run_id!r}, pipeline_run={self.pipeline_run!r}, status={self.status!r}
        )"""
