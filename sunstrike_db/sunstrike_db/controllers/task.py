from sqlalchemy import select
from sqlalchemy.orm import Session

from sunstrike_db.controllers.controller import BaseController
from sunstrike_db.models.task import Task


class TaskController(BaseController):
    def __init__(self, engine):
        super().__init__(engine)

    def create(self, name, pipeline_id, component_id, concurrency):
        with Session(self.engine) as session:
            task = Task(
                name=name,
                pipeline_id=pipeline_id,
                component_id=component_id,
                concurrency=concurrency
            )
            session.add(task)
            session.commit()

    @classmethod
    def _get_by_id(cls, session, primary_id):
        query = select(Task).where(Task.id == primary_id)
        return session.scalars(query).one()

    def get_by_id(self, primary_id):
        with Session(self.engine) as session:
            task = self._get_by_id(session, primary_id)
        return task

    def update(self, primary_id, name, concurrency):

        with Session(self.engine) as session:
            task = self._get_by_id(session, primary_id)
            task.name = name
            session.commit()
        return task

    def delete(self, primary_id):
        with Session(self.engine) as session:
            task = self._get_by_id(session, primary_id)
            session.delete(task)
        return task
