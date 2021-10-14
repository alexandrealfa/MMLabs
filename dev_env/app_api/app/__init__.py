from fastapi import FastAPI

from app import views
from app.configurations.database import Base, engine
from app.configurations import cors


def create_app():
    Base.metadata.create_all(engine)
    app = FastAPI()
    views.init_app(app)
    cors.init_app(app)
    return app
