import pytest
from pages.signup_page import SignUpPage
from tests.constant import Links


@pytest.fixture(scope='function')
def signup_page_open(driver):
    signup_page = SignUpPage(driver)
    driver.get(Links.SIGNUP_PAGE)
    signup_page.get_allow_all_cookies().click()
    return signup_page
