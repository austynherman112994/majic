from __future__ import annotations
import uuid
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import Uuid

from sunstrike_db.models.base import BaseModel


pipeline_pipeline_run_table = Table(
    "pipeline_pipeline_run",
    BaseModel.metadata,
    Column("pipeline_id", Uuid, primary_key=True),
    Column("pipeline_run_id", Uuid, primary_key=True),
)
