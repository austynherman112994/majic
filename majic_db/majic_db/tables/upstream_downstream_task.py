from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey

from majic_db.models.base import MajicBaseModel





upstream_downstream_task_table = Table(
    "upstream_downstream_task",
    MajicBaseModel.metadata,
    Column("upstream_task_id", ForeignKey("task.id"), primary_key=True),
    Column("downstream_task_id", ForeignKey("task.id"), primary_key=True),
)
