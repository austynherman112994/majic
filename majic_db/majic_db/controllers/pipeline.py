import uuid

from majic_db.controllers.controller import MajicController

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from majic_db.controllers.controller import MajicController
from majic_db.models.data_types.status import PipelineStatus
from majic_db.models.pipeline import Pipeline
from majic_db.models.task import Task


class PipelineController(MajicController):
    def __init__(self, engine):
        super().__init__(engine)

    def create(self, pipeline_id: uuid.UUID | None, name: str, status: PipelineStatus, tasks: list[dict]|None, edges: list[tuple[int]]|None):
        with Session(self.engine) as session:
            if pipeline_id:
                latest_version = self._get_latest_pipeline_version(session, pipeline_id)
                version = latest_version + 1
            else:
                pipeline_id = uuid.uuid4()
                version = 0

            # TODO generate tasks
            pipeline = Pipeline(
                pipeline_id=pipeline_id,
                name=name,
                version=version,
                status=status,

            )

            session.add(pipeline)
            session.commit()

    @classmethod
    def _get_latest_pipeline_version(cls, session: Session, pipeline_id):
        query = select(Pipeline.version)\
            .where(Pipeline.pipeline_id == pipeline_id)\
            .group_by(Pipeline.pipeline_id)\
            .filter(func.max(Pipeline.version))
        return session.execute(query).scalars().one()

    @classmethod
    def _get_by_id(cls, session: Session, primary_id):
        query = select(Pipeline).where(Pipeline.id == primary_id)
        return session.execute(query).one()

    def get_by_id(self, primary_id):
        with Session(self.engine) as session:
            pipeline = self._get_by_id(session, primary_id)
        return pipeline

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


# id: Mapped[int] = mapped_column(primary_key=True)
# version: Mapped[int] = mapped_column(autoincrement=True)
# name: Mapped[str] = mapped_column(String(128))
# tasks: Mapped[List["Task"]] = relationship(back_populates="pipeline")
# status: Mapped[PipelineStatus]
