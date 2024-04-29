import pytest
from app import create_app


@pytest.fixture()
def client():
    return create_app().test_client()


@pytest.fixture()
def cli():
    return create_app().test_cli_runner()
