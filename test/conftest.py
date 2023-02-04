import pytest

from cornerstone import create_app


@pytest.fixture
def app():
    return create_app()
