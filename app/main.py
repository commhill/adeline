from typing import Dict

from fastapi import FastAPI

app = FastAPI(title="Communications Hill Neighborhood Association")


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}
