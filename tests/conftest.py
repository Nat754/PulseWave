import pytest
import requests

from pages.login_page import LoginPage
from pages.main_page import MainPage
from tests.constant import MAIN_PAGE_URL, LOGIN_PAGE_URL, BASE_URL, CREATE_JWT


@pytest.fixture(scope='function')
def main_page_open(driver):
    main_page = MainPage(driver)
    driver.get(MAIN_PAGE_URL)
    main_page.get_allow_all_cookies().click()
    return main_page


@pytest.fixture(scope='function')
def login_page_open(driver):
    login_page = LoginPage(driver)
    driver.get(LOGIN_PAGE_URL)
    login_page.get_allow_all_cookies().click()
    return login_page


@pytest.fixture(scope='function')
def create_jwt():
    url = f'{BASE_URL}auth/jwt/create/'
    response = requests.post(url, json=CREATE_JWT)
    jwt = f"JWT {response.json()['access']}"
    return jwt