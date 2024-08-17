from __future__ import annotations

from dataclasses import dataclass
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sunstrike_db.models.base import BaseModel
from sunstrike_db.models.data_types.status import PipelineStatus


class Pipeline(BaseModel):
    __tablename__ = "pipeline"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128))
    pipeline_states = relationship("PipelineState", back_populates="pipeline")

    pipeline_runs = relationship("PipelineRun", back_populates="pipeline")

    status: Mapped[PipelineStatus]

    def to_dict(self):
        base_dict = {
            'id': self.id,
            'name': self.name,
            'status': self.status.name
        }
        return base_dict


    def __repr__(self) -> str:
        return f"""Pipeline(
            id={self.id!r},
            name={self.name!r},
            status={self.status!r},
        )"""

