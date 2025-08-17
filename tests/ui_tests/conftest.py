import allure
import pytest
from selenium.common import TimeoutException
from data import email_auth, password0
from pages.footer import FooterPage
from pages.header import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.signup_page import SignUpPage
from pages.workspace_page import WorkspacePage
from tests.constant import Links


@pytest.fixture()
def auth_user(driver):
    page_auth_user = LoginPage(driver)
    driver.get(Links.LOGIN_PAGE)
    # page_auth_user.get_allow_all_cookies().click()
    page_auth_user.input_email(email_auth)
    page_auth_user.input_password(password0)
    page_auth_user.click_submit()
    page_auth_user.check_changed_url_login()
    page = WorkspacePage(driver)
    page.loader_is_not_visible()
    return page_auth_user


@allure.step('Согласиться с использованием файлов cookies, если высветилось окно')
def accept_all_cookies(driver):
    page = FooterPage(driver)
    try:
        page.get_allow_all_cookies().click()
    except TimeoutException:
        pass


@pytest.fixture()
def footer_open(driver, url):
    with allure.step(f"Открыть страницу '{url}'"):
        page = FooterPage(driver)
        driver.get(url)
        accept_all_cookies(driver)
    return page


@pytest.fixture()
def header_open(driver, url):
    with allure.step(f"Открыть страницу '{url}'"):
        page = HeaderPage(driver)
        driver.get(url)
        accept_all_cookies(driver)
    return page


@pytest.fixture()
@allure.step("Открыть страницу Регистрации")
def signup_page_open(driver):
    page = SignUpPage(driver)
    driver.get(Links.SIGNUP_PAGE)
    accept_all_cookies(driver)
    return page


@pytest.fixture()
@allure.step("Открыть страницу входа")
def login_page_open(driver):
    page = LoginPage(driver)
    driver.get(Links.LOGIN_PAGE)
    accept_all_cookies(driver)
    return page


@pytest.fixture()
@allure.step("Открыть главную страницу")
def main_page_open(driver):
    page = MainPage(driver)
    driver.get(Links.START_PAGE)
    return page


@pytest.fixture()
@allure.step("Открыть страницу восстановления пароля")
def recovery_page_open(driver):
    page = PasswordRecoveryPage(driver)
    driver.get(Links.PASSWORD_RECOVERY)
    accept_all_cookies(driver)
    return page
