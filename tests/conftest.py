import imaplib
import pytest
import requests

from data import password_mail, e_mail
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


@pytest.fixture(scope='function')
def get_email_tokens():
    mail = imaplib.IMAP4_SSL('imap.mail.ru')
    mail.login(e_mail, password_mail)
    mail.select('INBOX')
    result, data_id = mail.search(None, 'ALL')
    message_ids = data_id[0].split()
    result, data_id = mail.fetch(message_ids[0], '(RFC822)')
    raw_email = str(data_id[0][1])
    mail.logout()
    first = raw_email.find('href')
    link = raw_email[first + 5:first + 110]
    return link
