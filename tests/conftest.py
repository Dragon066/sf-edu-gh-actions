import os

import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="function")
def test_client():
    with TestClient(app) as client:
        yield client
