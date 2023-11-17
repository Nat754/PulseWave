import pytest
from pages.signup_page import SignupPage
from tests.constant import SIGNUP_PAGE


@pytest.fixture(scope='function')
def signup_page_open(driver):
    signup_page = SignupPage(driver)
    driver.get(SIGNUP_PAGE)
    signup_page.get_allow_all_cookies().click()
    return signup_page
