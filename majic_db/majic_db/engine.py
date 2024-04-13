from sqlalchemy import create_engine



def create_majic_db_engine():
    engine = create_engine(
        "postgresql+psycopg2://postgres:password@172.17.0.2/majic",
        isolation_level="SERIALIZABLE",
    )
    return engine


