from data import email1, email2, password0

# Тестирование API
BASE_URL = "https://api.pwave.pnpl.tech/"
MAIL_URL = 'https://mail.ru/'

# Статус-коды
STATUS_200 = 200
STATUS_201 = 201
STATUS_204 = 204
STATUS_400 = 400
STATUS_404 = 404

# Данные пользователя
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
