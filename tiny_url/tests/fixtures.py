# pylint: disable=redefined-outer-name

import pytest

from tiny_url.settings import get_config
from tiny_url.factory import create_app


@pytest.fixture
def app():
    return create_app(get_config('test'))


@pytest.fixture
def client(app):
    return app.test_client()
