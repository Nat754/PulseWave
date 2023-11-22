import pytest
from pages.api_page import ApiPage


@pytest.fixture(scope='function')
def use_api_page():
    page = ApiPage()
    return page
