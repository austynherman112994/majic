from sys import pycache_prefix

from sqlalchemy import select, func, text
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import array_agg, ARRAY

from sunstrike_db.controllers.controller import BaseController
from sunstrike_db.models.data_types.status import PipelineStatus
from sunstrike_db.models.data_types.status import PipelineStateStatus
from sunstrike_db.models.pipeline import Pipeline
from sunstrike_db.models import Task, PipelineState
from sunstrike_db.models import Edge




class PipelineController(BaseController):
    def __init__(self, engine):
        super().__init__(engine)

    @classmethod
    def _construct_tasks(cls, raw_tasks: list[dict]):
        tasks = []

        for raw_task in raw_tasks:
            tasks.append(
                Task(
                    name=raw_task['name'],
                    # component_id=raw_task['component_id'],
                    concurrency=raw_task['concurrency']
                )
            )
        return tasks

    def create(
        self, name: str, status: PipelineStatus, state_status: PipelineStateStatus,
        raw_tasks: list[dict] = None, links: list[tuple] | None = None
    ):
        with Session(self.engine) as session:
            edges = []
            tasks = self._construct_tasks(raw_tasks)
            for i, link in enumerate(links):
                upstream_task, downstream_task = link
                edge = Edge()

                upstream_task = tasks[upstream_task]
                downstream_task = tasks[downstream_task]

                upstream_task.downstream_edges.append(edge)
                downstream_task.upstream_edges.append(edge)
                edges.append(edge)

            pipeline_state = PipelineState(
                version="v0.0.1",
                status=state_status,
                tasks=tasks,
                edges=edges
            )

            pipeline = Pipeline(
                name=name,
                status=status,
                pipeline_states=[pipeline_state]
            )

            session.add(pipeline)
            return session.commit()

    @classmethod
    def _get_by_id(cls, session: Session, primary_id):
        query = select(Pipeline).where(Pipeline.id == primary_id)
        return session.execute(query).one()[0]

    def get_by_id(self, primary_id):
        with Session(self.engine) as session:
            pipeline = self._get_by_id(session, primary_id)
        return pipeline

    def get_pipeline_states(cls, session, primary_id):
        query = select(PipelineState).where(PipelineState.pipeline_id == primary_id)
        return session.execute(query).all()

    def read(self, primary_id):
        with Session(self.engine) as session:

            pipeline = self._get_by_id(session, primary_id)
            pipeline_states = self.get_pipeline_states(session, primary_id)
            print(pipeline_states)
            pipeline_dict = pipeline.to_dict()
            pipeline_states_dict = [state[0].to_dict() for state in pipeline_states]
            pipeline_dict['pipeline_states'] = pipeline_states_dict
            return pipeline_dict

    def read_all(self):
        with Session(self.engine) as session:
            return [pipeline.to_dict() for pipeline in session.query(Pipeline).all()]

    def update(self, primary_id, name, status):
        with Session(self.engine) as session:
            pipeline = self._get_by_id(session, primary_id)
            pipeline.name = name
            pipeline.status = status
            session.commit()
        return pipeline

    def delete(self, primary_id):
        with Session(self.engine) as session:
            pipeline = self._get_by_id(session, primary_id)
            session.delete(pipeline)
        return pipeline
