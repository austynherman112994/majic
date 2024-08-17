from sunstrike_db.engine import DbEngine

from sunstrike_db.models import *
engine = DbEngine.instance()


if __name__ == "__main__":
    BaseModel.metadata.create_all(engine)
