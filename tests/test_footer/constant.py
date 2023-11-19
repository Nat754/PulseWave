import datetime

from tests.constant import MAIN_PAGE, LOGIN_PAGE, SIGNUP_PAGE

COOKIES = f'{MAIN_PAGE}documents/cookies'
LICENSE_TITLE = 'ЛИЦЕНЗИОННЫЙ ДОГОВОР (ОФЕРТА)'
LICENSE_LINK = 'Условия пользования'
YEAR_COOPERATION = datetime.datetime.now().year
TEXT_COOPERATION = '© PulseWave, 2023'
EMAIL_TEXT = 'pulsewave@gmail.com'
EMAIL_TEXT_HOVER = 'mailto:pulsewave@gmail.com'
COOKIES_TEXT = ('Наш сайт использует файлы cookie, чтобы улучшить работу сайта, повысить его эффективность и удобство. '
                'Продолжая использовать сайт, вы соглашаетесь на использование файлов cookie')
COOKIES_BUTTON = 'Принимаю всё'
CHECK_TEXT = [
    ('font-size', '16px', 'размера шрифта'),
    ('color', 'rgba(16, 16, 18, 1)', 'цвета шрифта'),
    ('font-family', 'Mulish, sans-serif', 'шрифта')
]
PAGES = [MAIN_PAGE, LOGIN_PAGE, SIGNUP_PAGE]
