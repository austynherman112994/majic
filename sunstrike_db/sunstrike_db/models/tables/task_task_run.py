from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Table
from sunstrike_db.models.base import BaseModel

from sqlalchemy import Uuid

task_task_run_table = Table(
    "task_task_run",
    BaseModel.metadata,
    Column("task_id", Uuid, primary_key=True),
    Column("task_run_id", Uuid, primary_key=True),
)
