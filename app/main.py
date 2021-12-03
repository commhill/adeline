"""
Primary entry point for the adeline webapp.
"""

from typing import Dict

from fastapi import FastAPI

app = FastAPI(title="Communications Hill Neighborhood Association")


@app.get("/")
async def root() -> Dict[str, str]:
    """
    The root endpoint
    """
    return {"message": "Hello World"}
