import datetime
from tests.constant import Links


class FooterConstant:
    COOKIES = f'{Links.MAIN_PAGE}documents/cookies'
    LICENSE_TITLE = 'ЛИЦЕНЗИОННЫЙ ДОГОВОР (ОФЕРТА)'
    LICENSE_LINK = 'Условия пользования'
    YEAR_COOPERATION = datetime.datetime.now().year
    TEXT_COOPERATION = f'© PulseWave, 2023-{YEAR_COOPERATION}'
    EMAIL_TEXT = 'info@pulsewave.ru'
    EMAIL_TEXT_HOVER = 'mailto:info@pulsewave.ru'
    COOKIES_TEXT = ('Наш сайт использует файлы cookie, чтобы улучшить работу сайта, повысить его эффективность и '
                    'удобство. Продолжая использовать сайт, вы соглашаетесь на использование файлов cookie')
    COOKIES_BUTTON = 'Принимаю всё'
    CHECK_TEXT = [
        ('font-size', '16px', 'размера шрифта'),
        ('color', 'rgba(16, 16, 18, 1)', 'цвета шрифта'),
        ('font-family', 'Mulish, sans-serif', 'шрифта')
    ]
    PAGES = [Links.MAIN_PAGE, Links.LOGIN_PAGE, Links.SIGNUP_PAGE, Links.PASSWORD_RECOVERY]
