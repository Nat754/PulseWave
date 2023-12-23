import pytest
from api_testing.api_base import ApiBase


@pytest.fixture(scope='function')
def use_api_base():
    page = ApiBase()
    return page
