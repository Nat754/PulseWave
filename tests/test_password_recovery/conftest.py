import pytest
from pages.password_recovery_page import PasswordRecoveryPage
from tests.constant import Constant


@pytest.fixture(scope='function')
def recovery_page_open(driver):
    recovery_page = PasswordRecoveryPage(driver)
    driver.get(Constant.PASSWORD_RECOVERY)
    recovery_page.get_allow_all_cookies().click()
    return recovery_page
