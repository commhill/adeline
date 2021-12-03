"""
Tests for the main adeline entry point.
"""
import requests
from starlette.testclient import TestClient


def test_root_endpoint(testclient: TestClient):
    """
    Test the root rest endpoint
    """
    response = testclient.get("/")
    assert response.status_code == requests.codes.ok  # pylint: disable=no-member
