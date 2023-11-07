import os
import imaplib
import hashlib
import email
import email.message
import os.path
import subprocess
import re
import pytest
import requests

from data import email_mail, password_mail, e_mail
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
def get_email_tokens(driver):
    # mail_pass = password_mail
    # username = e_mail
    # imap_server = "imap.mail.ru"
    # imap = imaplib.IMAP4_SSL(imap_server)
    # imap.login(username, mail_pass)
    # status, select_data = (imap.select("INBOX"))
    # message_ids = data[0].split()

    # Подключение к серверу почты
    mail = imaplib.IMAP4_SSL('imap.mail.ru')

    # Авторизация
    username = e_mail
    password = password_mail
    mail.login(username, password)

    # Выбор почтового ящика
    mail.select('INBOX')

    # Поиск сообщений
    result, data = mail.search(None, 'ALL')

    # Получение списка ID сообщений
    message_ids = data[0].split()

    # Чтение сообщений
    for message_id in message_ids:
        result, data = mail.fetch(message_id, '(RFC822)')
        raw_email = data[0][1]
        print(raw_email)  # или обработайте сообщение по своему усмотрению

    # Закрытие соединения
    mail.logout()
