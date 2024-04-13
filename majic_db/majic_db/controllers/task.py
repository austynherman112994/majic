
from majic_db.controllers.controller import MajicController

class TaskController(MajicController):
    def __init__(self, engine):
        super.__init__(engine)


    def createTaskObject(self, ):

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self, task_id):
        pass


# class Task(MajicBaseModel):
#     __tablename__ = "task"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     version: Mapped[int] = mapped_column(autoincrement=True)
#     name: Mapped[str] = mapped_column(String(30))
#
#     task_runs: Mapped[List["TaskRun"]] = relationship(back_populates="task")
#
#     pipeline_id: Mapped[int] = mapped_column(ForeignKey("pipeline.id"))
#     pipeline: Mapped["Pipeline"] = relationship(back_populates="tasks")
#
#     component_id: Mapped[int] = mapped_column(ForeignKey("component.id"))
#     component: Mapped["Component"] = relationship(back_populates="tasks")
#
#
#     upstream_tasks: Mapped[List["Task"]] = relationship(
#         secondary=upstream_downstream_task_table,
#         primaryjoin=upstream_downstream_task_table.c.downstream_task_id == id,
#         secondaryjoin=upstream_downstream_task_table.c.upstream_task_id == id,
#         backref="downstream_tasks")
#     downstream_tasks: Mapped[List["Task"]] = relationship(
#         secondary=upstream_downstream_task_table,
#         primaryjoin=upstream_downstream_task_table.c.upstream_task_id == id,
#         secondaryjoin=upstream_downstream_task_table.c.downstream_task_id == id,
#         backref="upstream_tasks")
#
#     # config_id: Mapped[int] = mapped_column(ForeignKey("config.id"))
#     # config: Mapped["Config"] = relationship(back_populates="tasks")
#     def __repr__(self) -> str:
#         return f"Task(id={self.id!r})"
