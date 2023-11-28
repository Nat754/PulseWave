from data import email1, email2, password0

# Тестирование API
BASE_URL = "https://api.pwave.pnpl.tech/"
MAIL_URL = 'https://mail.ru/'

# Статус-коды
STATUS_OK = 200
STATUS_CREATED = 201
STATUS_CHANGE = 204
STATUS_IS = 400

# Данные пользователя
CREATE_USER = {
  "subscriber": "true",
  "email": email1,
  "password": password0,
  "re_password": password0
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
