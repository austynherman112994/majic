from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sunstrike_db.models.base import BaseModel

class Edge(BaseModel):
    __tablename__ = "edge"
    id: Mapped[int] = mapped_column(primary_key=True)

    pipeline_states = relationship(
        "PipelineState",
        secondary="pipeline_state_edge",
        back_populates='edges'
    )

    task_id: Mapped[int] = mapped_column(ForeignKey("task.id"))
    task = relationship(
        "Task", back_populates="downstream_edges", foreign_keys=[task_id],
        overlaps="downstream_edges"
        #primaryjoin="edge.task_id == task.id"
    )

    downstream_task_id: Mapped[int] = mapped_column(ForeignKey("task.id"))
    downstream_task = relationship(
        "Task", back_populates="upstream_edges", foreign_keys=[downstream_task_id],
        overlaps="upstream_edges"
        #primaryjoin="edge.downstream_task_id == task.id"
    )

    def __repr__(self) -> str:
        return f"""Edges(
            id={self.id!r}, pipeline_id={self.pipeline_id!r},
            task_id={self.task_id!r}, downstream_task_id={self.downstream_task_id!r}
        )"""
