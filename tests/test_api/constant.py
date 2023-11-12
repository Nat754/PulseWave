from data import email1, password1, email2, password2, password0

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

CREATE_USER_JWT = {
  "email": email1,
  "password": password0
}

CHANGE_EMAIL_JWT = {
  "email": email2,
  "password": password0
}
TOKENS = {
        "uid": "MTUz",
        "token": "bxkaot-cc5bf99da4714785c865c561ad41b2ae"
}
nata = {'name': 'Nata'}

NEW_EMAIL = {
  "new_email": email2,
  "password": password0
}

RESET_PASSWRD = {
    "email": email2
}

TOKEN = {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNTMsImN1cnJlbnRfZW1haWwiOiJ0ZXN0X3B1bHNld2F2ZUBtYWlsLnJ1IiwibmV3X2VtYWlsIjoidGVzdF9zdHJveXJlbUBtYWlsLnJ1IiwiZXhwaXJlZCI6IjIwMjMtMTEtMTIgMTg6Mjc6MzQifQ.dyQ-Pe-r7vbZCsnRO-O_Vl_F6xBbyn6deWkos2JFuA8"}
