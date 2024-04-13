from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from majic_db.models.base import MajicBaseModel
from majic_db.models.data_types.status import TaskRunStatus

class TaskRun(MajicBaseModel):
    __tablename__ = "task_run"
    id: Mapped[int] = mapped_column(primary_key=True)
    attempt: Mapped[int]

    task_id: Mapped[int] = mapped_column(ForeignKey("task.id"))
    task: Mapped["Task"] = relationship(back_populates="task_runs")

    pipeline_run_id: Mapped[int] = mapped_column(ForeignKey("pipeline_run.id"))
    pipeline_run: Mapped["PipelineRun"] = relationship(back_populates="task_runs")

    status: Mapped[TaskRunStatus]

    def __repr__(self) -> str:
        return f"TaskRun(id={self.id!r})"
