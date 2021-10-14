from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings


def create_database(param: str):
    SQLALCHEMY_DATABASE_URL = settings[param].DB_URI_DEV
    current_engine = create_engine(SQLALCHEMY_DATABASE_URL)
    current_session = sessionmaker(autocommit=False, autoflush=False, bind=current_engine)

    current_base = declarative_base()

    return current_session, current_base, current_engine


SessionLocal, Base, engine = create_database("default")
