from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


def init_app(app: FastAPI):
    origins = [
        "http://localhost",
        "http://localhost:8080",
        "http://127.0.0.1:8000",
        "http://localhost:3000",
        "http://172.19.0.2:3000/",
        "http://172.18.0.1:45054/",
        "http://0.0.0.0/"
    ]
    app.add_middleware(CORSMiddleware,
                       allow_origins=origins,
                       allow_credentials=True,
                       allow_methods=['*'],
                       allow_headers=['*'],
                       )
