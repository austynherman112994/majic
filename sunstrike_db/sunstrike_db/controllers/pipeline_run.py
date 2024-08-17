from sqlalchemy import select
from sqlalchemy.orm import Session

from sunstrike_db.controllers.controller import BaseController
from sunstrike_db.models import PipelineRun




class PipelineRunController(BaseController):
    def __init__(self, engine):
        super().__init__(engine)


    def create(self, primary_id, attempt, pipeline_id):
        with Session(self.engine) as session:
            pipeline_run = PipelineRun(
                id=primary_id,
                attempt=attempt,
                pipeline_id=pipeline_id
            )

            session.add(pipeline_run)
            session.commit()

    def read(self):
        pass

    def update(self):
        pass

    def delete(self, pipeline_run_id):
        pass


# id: Mapped[int] = mapped_column(primary_key=True)
# attempt: Mapped[int]
# status: Mapped[PipelineRunStatus]
# pipeline_id: Mapped[int] = mapped_column("pipeline.pipeline_id")
# pipeline = relationship(
#     "Pipeline", back_populates="pipeline_runs",
#     primaryjoin="PipelineRun.pipeline_id == Pipeline.pipeline_id"
# )
#
# task_runs = relationship("TaskRun", back_populates="pipeline_run")
