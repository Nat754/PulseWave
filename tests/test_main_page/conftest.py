import pytest
from pages.main_page import MainPage
from tests.test_main_page.constant import MAIN_PAGE_URL


@pytest.fixture(scope='function')
def main_page_open(driver):
    main_page = MainPage(driver)
    driver.get(MAIN_PAGE_URL)
    main_page.get_allow_all_cookies().click()
    return main_page
