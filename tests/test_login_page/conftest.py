import pytest
from pages.login_page import LoginPage
from tests.constant import Constant


@pytest.fixture(scope='function')
def login_page_open(driver):
    login_page = LoginPage(driver)
    driver.get(Constant.LOGIN_PAGE)
    login_page.get_allow_all_cookies().click()
    return login_page
