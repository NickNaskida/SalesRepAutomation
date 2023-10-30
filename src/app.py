from fastapi import FastAPI

from src.router import router


def create_app():
    """
    Create FastAPI app

    :return: FastAPI app
    """
    app = FastAPI(docs_url="/docs")
    app.include_router(router)

    return app
