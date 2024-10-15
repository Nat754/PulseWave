import random
from datetime import datetime
from faker import Faker
from data import email1, email2, password0, email_auth

faker = Faker('en')
Faker.seed()


class StatusCode:
    STATUS_200 = 200
    STATUS_201 = 201
    STATUS_204 = 204
    STATUS_400 = 400
    STATUS_404 = 404


class ApiConstant:

    COLOR_STICKER = ['#FF5E5E', '#FF9A3C', '#FFC727', '#67A700', '#5ED8FF', '#0069B4', '#7849FF', '#C852FF']

    CREATE_USER = {
      "subscriber": "true",
      "email": email1,
      "password": password0,
      "re_password": password0
    }

    CREATE_USER_NO_SUBSCRIBER = {
      "subscriber": "false",
      "email": email1,
      "password": password0,
      "re_password": password0
    }

    CREATE_USER_NO_EMAIL = {
      "subscriber": "true",
      "email": "",
      "password": password0,
      "re_password": password0
    }

    CREATE_USER_NO_PASSWORD = {
      "subscriber": "true",
      "email": email1,
      "password": "",
      "re_password": ""
    }

    NEW_EMAIL = {
      "new_email": email2,
      "password": password0
    }

    RESET_PASSWRD = {
      "email": email2
    }

    WORKSPACE = {
      "name": faker.company()
    }

    NO_DATA = ['Это поле не может быть пустым.']

    BOARD_CREATE = {
        "name": faker.job()
    }

    PUT_COLUMN = {
      "name": faker.job()
    }

    CREATE_TASK = {
        "name": faker.city(),
        "deadline": f"{datetime.now().date()}",
        "description": faker.name(),
        "priority": 1,
        "color_mark": random.choice(COLOR_STICKER),
        "name_mark": faker.first_name()
    }

    MOVE_TASK = {
      "name": faker.city(),
      "index": 0,
      "column": 0,
      "responsible": [
        0
      ],
      "deadline": f"{datetime.now().date()}",
      "description": faker.text(),
      "priority": 0,
      "color_mark": random.choice(COLOR_STICKER),
      "name_mark": faker.first_name()
    }

    PUT_TASK = {
        "name": faker.city(),
        "index": 0,
        "column": 0,
        "responsible": [
          0
        ],
        "deadline": f"{datetime.now().date()}",
        "description": faker.text(),
        "priority": 0
    }

    PATCH_TASK = {
        "name": faker.city(),
        "index": 2147483647,
        "column": 0,
        "responsible": [0],
        "deadline": f"{datetime.now().date()}",
        "description": faker.text(),
        "priority": 0,
        "color_mark": random.choice(COLOR_STICKER),
        "name_mark": faker.first_name()
    }

    INVITE_USER = {"email": email_auth}

    PUT_NOTIFICATION = {"read": True}

    COMMENT = {"message": faker.text()}

    INVALID_PASSWORD = ['1ё3', 'qwertyui', '12345678', '      1й']


class ResponseJson:
    PASSWORD_SMALL = {'password': ['Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.']}
    NO_DIGIT = {'password': ['Пароль должен содержать хотя бы одну цифру.']}
    NO_LETTER = {'password': ['Пароль должен содержать хотя бы одну букву.']}
