import datetime

MAIN_PAGE_URL = 'https://pulse-wave.netlify.app/'
MAIN_PAGE_HOME = f'{MAIN_PAGE_URL}home'
MAIN_PAGE_TITLE = 'PulseWave'
LOGIN_PAGE = f'{MAIN_PAGE_URL}auth/login'
SIGNUP_PAGE = f'{MAIN_PAGE_URL}auth/signup'
TERMS_OF_SERVICE = f'{MAIN_PAGE_URL}documents/terms-of-service'
COOKIES = f'{MAIN_PAGE_URL}documents/cookies'

TEXT_LOGIN = 'Войти'
TEXT_SIGNUP_HEADER = 'Регистрация'
TEXT_SIGNUP = 'Зарегистрироваться'
BUTTON_COLOR = 'rgba(252, 224, 88, 1)'  # #FCE058
LICENSE_TITLE = 'ЛИЦЕНЗИОННЫЙ ДОГОВОР (ОФЕРТА)'
LICENSE_LINK = 'Условия пользования'
YEAR_COOPERATION = datetime.datetime.now().year
EMAIL_TEXT = 'pulsewave@gmail.com'
MAIN_TITLE = 'PULSEWAVE'
COOKIES_TEXT = ('Наш сайт использует файлы cookie, чтобы улучшить работу сайта, повысить его эффективность и удобство. '
                'Продолжая использовать сайт, вы соглашаетесь на использование файлов cookie')
COOKIES_BUTTON = 'Принимаю всё'


class ApiUrls:
    BASE_URL = "https://api.pwave.pnpl.tech/api/schema/swagger-ui/#/"
