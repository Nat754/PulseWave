from data import email1, email2, password0


class ApiConstant:

    BASE_URL = "https://api.pwave.pnpl.tech/"
    MAIL_URL = 'https://mail.ru/'
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
      "name": "My workspace"
    }

    NO_DATA = ['Это поле не может быть пустым.']

    BOARD_WITHOUT_WS = {
        "name": "MyBoard"
    }

    PUT_COLUMN = {
      "name": "My_Column"
    }

    CREATE_TASK = {
        "name": "string",
        "deadline": "2023-12-22",
        "description": "string",
        "priority": 0,
        "color_mark": "string",
        "name_mark": "string"
    }
    MOVE_TASK = {
      "name": "string",
      "index": 2147483647,
      "column": 0,
      "responsible": [
        0
      ],
      "deadline": "2023-12-23",
      "description": "string",
      "priority": 0,
      "color_mark": "string",
      "name_mark": "string"
    }
    PATCH_TASK = {
        "name": "string",
        "index": 2147483647,
        "column": 0,
        "responsible": [0],
        "deadline": "2023-12-23",
        "description": "string",
        "priority": 0,
        "color_mark": "string",
        "name_mark": "string"
    }


class StatusCode:
    STATUS_200 = 200
    STATUS_201 = 201
    STATUS_204 = 204
    STATUS_400 = 400
    STATUS_404 = 404
