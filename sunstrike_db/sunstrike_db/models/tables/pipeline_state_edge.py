from __future__ import annotations

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Table

from sunstrike_db.models.base import BaseModel


pipeline_state_edge_table = Table(
    "pipeline_state_edge",
    BaseModel.metadata,
    Column("pipeline_state_id", ForeignKey("pipeline_state.id"), primary_key=True),
    Column("edge_id", ForeignKey("edge.id"), primary_key=True),
)
