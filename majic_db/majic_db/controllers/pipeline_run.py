
from majic_db.controllers.controller import MajicController

class PipelineRunController(MajicController):
    def __init__(self, engine):
        super.__init__(engine)


    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self, pipeline_run_id):
        pass

# class PipelineRun(MajicBaseModel):
#     __tablename__ = "pipeline_run"
#     id: Mapped[int] = mapped_column(primary_key=True)
#
#     pipeline_id: Mapped[int] = mapped_column(ForeignKey("pipeline.id"))
#     pipeline: Mapped["Pipeline"] = relationship(back_populates="pipeline_runs")
#
#     task_runs: Mapped[List["TaskRun"]] = relationship(back_populates="pipeline_run")
#
#     def __repr__(self) -> str:
#         return f"PipelineRun(id={self.id!r})"
