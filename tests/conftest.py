import pytest
from pages.main_page import MainPage
from tests.constant import MAIN_PAGE_URL


@pytest.fixture(scope='function')
def main_page_open(driver):
    main_page = MainPage(driver)
    driver.get(MAIN_PAGE_URL)
    return main_page
