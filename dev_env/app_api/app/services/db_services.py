from app.configurations.database import Base, SessionLocal, engine


def get_db():
    """
    on this service we go get the current session of the database
    :return: the current database session
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
