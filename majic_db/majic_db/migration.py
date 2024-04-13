from majic_db.engine import create_majic_db_engine

from majic_db.models.base import MajicBaseModel
from majic_db.models.component import Component
from  majic_db.models.pipeline import Pipeline
from majic_db.models.pipeline_run import PipelineRun
from majic_db.models.task import Task
from majic_db.models.task_run import TaskRun

from majic_db.tables.upstream_downstream_task import upstream_downstream_task_table


engine = create_majic_db_engine()

MajicBaseModel.metadata.create_all(engine)
