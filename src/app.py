from fastapi import FastAPI

from src.router import router


def create_app():
    app = FastAPI(docs_url="/")
    app.include_router(router)

    return app
