import datetime

from data import e_mail, password, email_new

# Главная страница

MAIN_PAGE_URL = 'https://pulse-wave.netlify.app/'
MAIN_PAGE_HOME = f'{MAIN_PAGE_URL}home'
MAIN_PAGE_TITLE = 'PulseWave'
LOGIN_PAGE_URL = f'{MAIN_PAGE_URL}auth/login'
SIGNUP_PAGE = f'{MAIN_PAGE_URL}auth/signup'
TERMS_OF_SERVICE = f'{MAIN_PAGE_URL}documents/terms-of-service'
COOKIES = f'{MAIN_PAGE_URL}documents/cookies'

TEXT_LOGIN = 'Войти'
TEXT_SIGNUP_HEADER = 'Регистрация'
TEXT_SIGNUP = 'Зарегистрироваться'
LICENSE_TITLE = 'ЛИЦЕНЗИОННЫЙ ДОГОВОР (ОФЕРТА)'
LICENSE_LINK = 'Условия пользования'
YEAR_COOPERATION = datetime.datetime.now().year
TEXT_COOPERATION = '© PulseWave, 2023'
EMAIL_TEXT = 'pulsewave@gmail.com'
MAIN_TITLE = 'PULSEWAVE'
COOKIES_TEXT = ('Наш сайт использует файлы cookie, чтобы улучшить работу сайта, повысить его эффективность и удобство. '
                'Продолжая использовать сайт, вы соглашаетесь на использование файлов cookie')
COOKIES_BUTTON = 'Принимаю всё'
USEFUL_INTERFACE = 'Удобный и понятный интерфейс!'
ALL_TIME = 'Самый высокий уровень бесперебойной работы!'
FIRST_SAFETY = 'Ваша безопасность и конфиденциальность для нас на первом месте!'
EMAIL_TEXT_HOVER = 'mailto:pulsewave@gmail.com'
FULL_FUNCTIONALITY = (f'Неограниченный функционал, понятный интерфейс и большое количество возможностей\nпомогут Вам '
                      'улучшить рабочий процесс.')
ONE_APP = 'Одно приложениe для решения всех Ваших задач!'

BUTTON_COLOR = 'rgba(252, 224, 88, 1)'
TEXT_COLOR = 'rgba(16, 16, 18, 1)'
PULSEWAVE_COLOR = 'rgba(66, 66, 66, 1)'

PULSEWAVE_SIZE = '80px'
BUTTON_TEXT_SIZE = '18px'
TEXT_SIZE = '16px'

BUTTONS_URL = [
    (LOGIN_PAGE_URL, TEXT_LOGIN),
    (SIGNUP_PAGE, TEXT_SIGNUP_HEADER),
    (SIGNUP_PAGE, TEXT_SIGNUP)
]
BUTTONS = [TEXT_LOGIN, TEXT_SIGNUP_HEADER, TEXT_SIGNUP]
ITEMS = [TEXT_LOGIN, TEXT_SIGNUP_HEADER, TEXT_SIGNUP, MAIN_TITLE, USEFUL_INTERFACE, ALL_TIME, FIRST_SAFETY,
         FULL_FUNCTIONALITY, ONE_APP]
ITEMS_PULSEWAVE_COLOR = [TEXT_LOGIN, TEXT_SIGNUP_HEADER, TEXT_SIGNUP, MAIN_PAGE_TITLE]
ITEMS_TEXT = [USEFUL_INTERFACE, ALL_TIME, FIRST_SAFETY, FULL_FUNCTIONALITY, ONE_APP, LICENSE_LINK, EMAIL_TEXT,
              YEAR_COOPERATION]

# Страница 'Войти'
LOGIN_PAGE_TITLE = 'Вход'

# Страница 'Регистрация'


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
  "email": e_mail,
  "password": password,
  "re_password": password
}

CREATE_JWT = {
  "email": e_mail,
  "password": password
}

TOKENS = {
        "uid": "",
        "token": ""
}
nata = {'name': 'Nata'}

NEW_EMAIL = {
  "new_email": email_new,
  "password": password
}

RESET_PASSWRD = {
    "email": e_mail
}
