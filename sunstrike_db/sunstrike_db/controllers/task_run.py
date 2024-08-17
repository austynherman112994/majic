
from sunstrike_db.controllers.controller import BaseController

class TaskRunController(BaseController):
    def __init__(self, engine):
        super().__init__(engine)


    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self, task_run_id):
        pass



# class TaskRun(MajicBaseModel):
#     __tablename__ = "task_run"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     attempt: Mapped[int] = mapped_column(autoincrement=True)
#
#     task_id: Mapped[int] = mapped_column(ForeignKey("task.id"))
#     task: Mapped["Task"] = relationship(back_populates="task_runs")
#
#     pipeline_run_id: Mapped[int] = mapped_column(ForeignKey("pipeline_run.id"))
#     pipeline_run: Mapped["PipelineRun"] = relationship(back_populates="task_runs")
#     def __repr__(self) -> str:
#         return f"TaskRun(id={self.id!r})"
