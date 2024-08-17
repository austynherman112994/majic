from sqlalchemy import select
from sqlalchemy.orm import Session

from sunstrike_db.controllers.controller import BaseController
from sunstrike_db.models.component import Component


class ComponentController(BaseController):
    def __init__(self, engine):
        super().__init__(engine)

    def create(self, name):
        with Session(self.engine) as session:
            component = Component(
                name=name
            )

            session.add(component)
            session.commit()

    @classmethod
    def _get_by_id(cls, session, primary_id):
        query = select(Component).where(Component.id == primary_id)
        return session.scalars(query).one()

    def get_by_id(self, primary_id):
        with Session(self.engine) as session:
            component = self._get_by_id(session, primary_id)
        return component

    def update(self, primary_id, name):
        with Session(self.engine) as session:
            component = self._get_by_id(session, primary_id)
            component.name = name
            session.commit()
        return component

    def delete(self, primary_id):
        with Session(self.engine) as session:
            component = self._get_by_id(session, primary_id)
            session.delete(component)
        return component
