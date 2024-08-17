import uuid
import enum
from os import minor, major
from unittest.mock import patch

from sqlalchemy import select, func, text
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import array_agg, ARRAY

from sunstrike_db.controllers.controller import BaseController
from sunstrike_db.models.data_types.status import PipelineStateStatus
from sunstrike_db.models.pipeline import Pipeline
from sunstrike_db.models import Task, PipelineState
from sunstrike_db.models import Edge

id: Mapped[int] = mapped_column(primary_key=True)
version: Mapped[int] = mapped_column(default=0)
status: Mapped[PipelineStateStatus]

pipeline_id: Mapped[int] = mapped_column(ForeignKey("pipeline.id"))
pipeline = relationship("Pipeline", back_populates="pipeline_states")
tasks = relationship("Task", secondary="pipeline_state_task", back_populates="pipeline_states")
edges = relationship("Edge", secondary="pipeline_state_edge", back_populates="pipeline_states")

class VersionChange(enum.Enum):
    minor = 0
    major = 1
    patch = 3


class PipelineController(BaseController):
    def __init__(self, engine):
        super().__init__(engine)

    @classmethod
    def _construct_tasks(cls, raw_tasks: list[dict]):
        tasks = []

        for raw_task in raw_tasks:
            task_id = raw_task['task_id'] if 'task_id' in raw_task.keys() else uuid.uuid4()

            tasks.append(
                Task(
                    task_id=task_id,
                    name=raw_task['name'],
                    # component_id=raw_task['component_id'],
                    concurrency=raw_task['concurrency']
                )
            )
        return tasks

    @classmethod
    def _parse_versions(cls, current_version: str) -> tuple[int, int, int]:
        major, minor, patch = current_version.strip("v").split(".")
        return int(major), int(minor), int(patch)

    def update_version(cls, current_version: str, version_change: VersionChange):
        major, minor, patch = cls._parse_version(current_version)
        if version_change == VersionChange.patch:
            patch = patch + 1
        elif version_change == VersionChange.minor:
            minor = minor + 1
        else:
            major = major + 1

        return f"v{major}.{minor}.{patch}"

    def create_object(
        cls, session: Session, status: PipelineStateStatus, pipeline_id: int,
        version_change: VersionChange = VersionChange.patch,
        raw_tasks: list[dict] = None, links: list[tuple] | None = None
    ):
        if pipeline_id:
            current_version = cls._get_latest_pipeline_state_version(session, pipeline_id)
            version = cls.update_version(current_version, version_change)
        if current_version:
            version = "v0.0.1"

        edges = [Edge() for i in links]
        tasks = cls._construct_tasks(raw_tasks)
        for i, link in enumerate(links):
            upstream_task, downstream_task = link
            edge = edges[i]

            upstream_task = tasks[upstream_task]
            downstream_task = tasks[downstream_task]

            upstream_task.downstream_edges.append(edge)
            downstream_task.upstream_edges.append(edge)

        pipelineState = PipelineState(
            pipeline_id=pipeline_id,
            version=version,
            status=status,
            tasks=tasks,
            edges=edges
        )
        return pipelineState

    def create(
        self, status: PipelineStateStatus, pipeline_id: int, version_change: VersionChange = VersionChange.patch,
        raw_tasks: list[dict] = None, links: list[tuple] | None = None
    ):
        with Session(self.engine) as session:
            pipeline_state = self.create_object(
                session,
                status,
                pipeline_id,
                version_change,
                raw_tasks,
                links
            )
            session.add(pipeline_state)
            return session.commit()

    @classmethod
    def _get_latest_pipeline_state_version(cls, session: Session, pipeline_id):
        query = select(PipelineState.version) \
            .where(PipelineState.pipeline_id == pipeline_id) \
            .group_by(PipelineState.pipeline_id) \
            .filter(func.max(PipelineState.version))
        return session.execute(query).scalars().one()

    @classmethod
    def _get_by_id(cls, session: Session, primary_id):
        query = select(Pipeline).where(Pipeline.id == primary_id)
        return session.execute(query).one()

    def get_by_id(self, primary_id):
        with Session(self.engine) as session:
            pipeline_state = self._get_by_id(session, primary_id)
        return pipeline_state

    @classmethod
    def _get_pipeline_state_tasks(cls, session: Session, primary_id):
        query = select(Task).join(PipelineState).where(PipelineState.id == primary_id)
        return session.execute(query).all()

    @classmethod
    def _get_pipeline_edges(cls, session: Session, primary_id):
        query = select(Edge).join(PipelineState).where(PipelineState.id == primary_id)
        return session.execute(query).all()

    def read(self, primary_id):
        with Session(self.engine) as session:

            pipeline_state = self._get_by_id(session, primary_id)
            tasks = self._get_pipeline_tasks(session, primary_id)
            edges = self._get_pipeline_edges(session, primary_id)
            pipeline.tasks = tasks
            pipeline.edges = edges
            return pipeline_state

    def update(self, primary_id, status):
        with Session(self.engine) as session:
            pipeline_state = self._get_by_id(session, primary_id)
            pipeline_state.status = status
            session.commit()
        return pipeline

    def delete(self, primary_id):
        with Session(self.engine) as session:
            pipeline_state = self._get_by_id(session, primary_id)
            session.delete(pipeline_state)
        return pipeline_state
