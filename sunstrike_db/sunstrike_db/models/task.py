from __future__ import annotations

import uuid
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sunstrike_db.models.base import BaseModel


class Task(BaseModel):
    __tablename__ = "task"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    concurrency: Mapped[int] = mapped_column(default=10)

    pipeline_states = relationship(
        "PipelineState",
        secondary="pipeline_state_task",
        back_populates='tasks'
    )

    upstream_edges = relationship("Edge", foreign_keys="Edge.downstream_task_id")
    downstream_edges = relationship("Edge", foreign_keys="Edge.task_id")

    task_runs = relationship('TaskRun',  back_populates="task")


    # component_id: Mapped[int] = mapped_column(ForeignKey("component.id"))
    # component = relationship("Component", back_populates="tasks")


    # upstream_tasks: Mapped[List["Task"]] = relationship(
    #     secondary=upstream_downstream_task_table,
    #     primaryjoin=upstream_downstream_task_table.c.downstream_task_id == id,
    #     secondaryjoin=upstream_downstream_task_table.c.upstream_task_id == id,
    #     backref="downstream_tasks")
    # downstream_tasks: Mapped[List["Task"]] = relationship(
    #     secondary=upstream_downstream_task_table,
    #     primaryjoin=upstream_downstream_task_table.c.upstream_task_id == id,
    #     secondaryjoin=upstream_downstream_task_table.c.downstream_task_id == id,
    #     backref="upstream_tasks")

    # config_id: Mapped[int] = mapped_column(ForeignKey("config.id"))
    # config: Mapped["Config"] = relationship(back_populates="tasks")
    def __repr__(self) -> str:
        return f"""Task(
            id={self.id!r}, name={self.name!r}, concurrency={self.concurrency!r},
            pipeline_id={self.pipeline_id!r},
        )"""
