# tests/conftest.py

import pytest
from flask import Flask


@pytest.fixture
def app() -> Flask:
    """ Provides an instance of Helm Manager """
    from HelmManager.server import server

    assert isinstance(server.app, Flask)
    return server.app
