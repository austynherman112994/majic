from sqlalchemy import create_engine


class DbEngine:
    _engine = None
    def __init__(self):
        raise NotImplementedError("Use the instance classmethod to access the db engine")

    @classmethod
    def instance(cls):
        if not cls._engine:
            cls._engine = create_engine(
                "postgresql+psycopg2://postgres:password@172.17.0.2/majic",
                isolation_level="SERIALIZABLE",
            )
        return cls._engine


