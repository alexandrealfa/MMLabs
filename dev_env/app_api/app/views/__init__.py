from fastapi import FastAPI

from app.views.status_view import router_status
from app.views.person_view import router_person
from app.views.user_view import router_user


def init_app(app: FastAPI):
    app.include_router(router_status, tags=["Status"])
    app.include_router(router_person, tags=["Person"])
    app.include_router(router_user, tags=['users'])
