from __future__ import annotations

import uuid
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sunstrike_db.models.base import BaseModel
from sunstrike_db.models.data_types.status import PipelineStateStatus


class PipelineState(BaseModel):
    __tablename__ = "pipeline_state"
    id: Mapped[int] = mapped_column(primary_key=True)
    version: Mapped[str] = mapped_column(default=0)
    status: Mapped[PipelineStateStatus]

    pipeline_id: Mapped[int] = mapped_column(ForeignKey("pipeline.id"))
    pipeline = relationship("Pipeline", back_populates="pipeline_states")
    tasks = relationship("Task", secondary="pipeline_state_task", back_populates="pipeline_states")
    edges = relationship("Edge", secondary="pipeline_state_edge", back_populates="pipeline_states")


    def __repr__(self) -> str:
        return f"""PipelineState(
            id={self.id!r},
            pipeline_id={self.pipeline_id!r},
            version={self.version!r},
            status={self.status!r}
        )"""

