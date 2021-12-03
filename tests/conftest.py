"""
Pytest configuration
"""

import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="function")
def testclient():
    """
    Test client fixture for talking to the rest api
    """
    with TestClient(app) as client:
        yield client
