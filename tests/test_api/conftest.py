import imaplib
import pytest
import requests

from data import password1, email1, password0, email2, password2
from tests.test_api.constant import BASE_URL


@pytest.fixture(scope='function')
def create_jwt():
    url = f'{BASE_URL}auth/jwt/create/'
    response = requests.post(url, json={"email": email1, "password": password0})
    jwt = f"JWT {response.json()['access']}"
    return jwt


@pytest.fixture(scope='function')
def create_refresh():
    url = f'{BASE_URL}auth/jwt/create/'
    response = requests.post(url, json={"email": email1, "password": password0})
    refresh = f"{response.json()['refresh']}"
    return refresh


@pytest.fixture(scope='function')
def get_email_tokens():
    mail = imaplib.IMAP4_SSL('imap.mail.ru')
    mail.login(email1, password1)
    mail.select('INBOX')
    result, data_id = mail.search(None, 'UNSEEN')
    message_ids = data_id[0].split()
    result, data_id = mail.fetch(message_ids[-1], '(RFC822)')
    raw_email = str(data_id[0][1])
    mail.logout()
    first = raw_email.find('activate')
    link = raw_email[first + 9:first + 53].split('/')
    # tokens = {"uid": link[0], "token": link[1]}
    return link


@pytest.fixture(scope='function')
def get_activate_token2():
    mail = imaplib.IMAP4_SSL('imap.mail.ru')
    mail.login(email2, password2)
    mail.select('INBOX')
    result, data_id = mail.search(None, 'ALL')
    message_ids = data_id[0].split()
    result, data_id = mail.fetch(message_ids[-1], '(RFC822)')
    raw_email = str(data_id[0][1])
    print(raw_email)
    first = raw_email.find('token=')
    token = raw_email[first + 6:first + 253]
    mail.logout()
    print()
    print(token)
    return token


@pytest.fixture(scope='function')
def get_user_id(create_jwt):
    jwt = create_jwt
    url = f'{BASE_URL}auth/users/me/'
    response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
    user_id = response.json()['id']
    return user_id


@pytest.fixture(scope='function')
def create_jwt2():
    url = f'{BASE_URL}auth/jwt/create/'
    response = requests.post(url, json={"email": email2, "password": password0})
    jwt = f"JWT {response.json()['access']}"
    return jwt


@pytest.fixture(scope='function')
def get_email_tokens2():
    mail = imaplib.IMAP4_SSL('imap.mail.ru')
    mail.login(email2, password2)
    mail.select('INBOX')
    result, data_id = mail.search(None, 'ALL')
    message_ids = data_id[0].split()
    result, data_id = mail.fetch(message_ids[-1], '(RFC822)')
    raw_email = str(data_id[0][1])
    mail.logout()
    first = raw_email.find('confirm')
    link = raw_email[first + 8:first + 52].split('/')
    # tokens = {"uid": link[0], "token": link[1]}
    return link
