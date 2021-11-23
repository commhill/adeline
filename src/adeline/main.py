from typing import Dict

import uvicorn  # type: ignore
from fastapi import FastAPI

app = FastAPI(title="Communications Hill Neighborhood Association")


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}


def start() -> None:
    """Launched with `poetry run start` at root level"""
    uvicorn.run("adeline.main:app", host="0.0.0.0", port=8000, reload=True)
