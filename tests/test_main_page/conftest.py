import pytest
from pages.main_page import MainPage
from tests.constant import Constant


@pytest.fixture(scope='function')
def main_page_open(driver):
    main_page = MainPage(driver)
    driver.get(Constant.MAIN_PAGE)
    main_page.get_allow_all_cookies().click()
    return main_page
