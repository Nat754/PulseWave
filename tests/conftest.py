import pytest
from data import email_auth, password0
from pages.login_page import LoginPage
from tests.constant import Constant


@pytest.fixture(scope='function')
def auth_user(driver):
    page_auth_user = LoginPage(driver)
    driver.get(Constant.LOGIN_PAGE)
    page_auth_user.get_allow_all_cookies().click()
    page_auth_user.input_email(email_auth)
    page_auth_user.input_password(password0)
    page_auth_user.click_submit()
    page_auth_user.check_changed_url_login()
    return page_auth_user
