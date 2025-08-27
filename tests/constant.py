import datetime
from data import email1


class Links:

    # START_PAGE = 'https://web.dev.pulsewave.ru/'
    # MAIN_PAGE = 'https://app.dev.pulsewave.ru/'
    # BASE_URL = "https://api.dev.pulsewave.ru/"
    START_PAGE = 'https://pulsewave.ru/'
    MAIN_PAGE = 'https://app.pulsewave.ru/'
    BASE_URL = 'https://api.pulsewave.ru/'
    MAIN_PAGE_HOME = f'{START_PAGE}home'
    LOGIN_PAGE = f'{MAIN_PAGE}auth/login'
    SIGNUP_PAGE = f'{MAIN_PAGE}auth/signup'
    TERMS_OF_SERVICE = f'{MAIN_PAGE}documents/terms-of-service'
    WORKSPACE = f'{MAIN_PAGE}workspaces'
    PULSEWAVE_PRIVACY = f'{MAIN_PAGE}documents/privacy'
    PASSWORD_RECOVERY = f'{MAIN_PAGE}auth/password?email='
    MAIL_URL = 'https://mail.ru/'
    LI_URL = 'https://www.linkedin.com/company/pulsewave-team'


class Messages:

    WRONG_PASSWORD_MSG = 'Некорректный e-mail или пароль'
    FORGOT_PASSWORD_MSG = 'Забыли пароль?'
    PASSWORD_RULES_MSG = 'Слабый пароль. Пароль должен содержать минимум 8 символов, включая буквы и цифры'
    PULSEWAVE_POLICY_MSG = 'Я согласен получать новости и обновления PulseWave'
    AGREEMENT_MSG = 'Регистрируясь, я соглашаюсь с Условиями пользования и Политикой конфиденциальности'
    INVALID_PASSWORD_MSG = ('Слабый пароль. Пароль должен содержать минимум 8 символов, включая буквы и '
                            'цифры')
    INVALID_EMAIL_MSG = 'Пожалуйста, введите корректную почту.'
    PASSWORDS_NOT_EQUAL_MSG = 'Пароли не совпадают. Повторите попытку, пожалуйста'
    EMAIL_WAS_SEND = 'На Ваш электронный адрес'
    GO_TO_EMAIL = ('выслана ссылка для восстановления пароля. '
                   'Пожалуйста, пройдите по ней и создайте новый пароль для учетной записи.')
    EXISTING_EMAIL = 'Данный электронный адрес уже зарегистрирован'
    NON_EXISTENT_EMAIL = 'Данный электронный адрес не найден'
    EXIT_CONFIRM_MSG = 'Вы уверены, что хотите выйти из учётной записи?\nВы будете перенаправлены на Главный экран'
    TO_MAIN_TEXT = 'На главную'


class TestData:
    WEAK_PASSWORD = ['1ё3', 'qwertyui', '12345678']
    SET_OF_BROWSERS = ['chrome']
    PAGES_ALL = [Links.START_PAGE, Links.LOGIN_PAGE, Links.SIGNUP_PAGE, Links.PASSWORD_RECOVERY]
    PAGES_APP = [Links.LOGIN_PAGE, Links.SIGNUP_PAGE, Links.PASSWORD_RECOVERY]


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
    FOOTER_LIST = ['info@pulsewave.ru', f'©PulseWave, 2023-{YEAR_COOPERATION}']


class HeaderConstant:

    TEXT_LOGIN = 'Войти'
    TEXT_SIGNUP = 'Регистрация'
    CHECK_BUTTON = [
        ('font-size', '18px', 'размера шрифта'),
        ('color', 'rgba(66, 66, 66, 1)', 'цвета шрифта'),
        ('font-family', 'Mulish, sans-serif', 'шрифта'),
        ('background-color', 'rgba(252, 224, 88, 1)', 'цвета')
    ]


class LoginConstant:

    LOGIN_PAGE_TITLE = 'Вход'
    TEXT_LOGIN = 'Войти'

    CHECK_TITLE = [
        ("font-size", '18px', 'размера шрифта'),
        ("color", 'rgba(66, 66, 66, 1)', 'цвета шрифта'),
        ("font-family", 'Mulish, sans-serif', 'шрифта')
    ]

    WRONG_PASSWORD_CSS = {
        'color': 'rgba(183, 183, 183, 1)',
        'font-size': '12px',
        'font-family': 'Mulish, sans-serif'
    }

    FORGOT_PASSWORD_CSS = {
        'color': 'rgba(66, 66, 66, 1)',
        'font-size': '12px',
        'font-family': 'Mulish, sans-serif'
    }


class WorkspaceConstant:

    WORKSPACE_TITLE = 'Рабочие пространства'
    MAIN_WORKSPACE_TITLE = 'Ваши рабочие пространства'
    READ_ALL_BUTTON_TEXT = 'Отметить все как прочитанные'
    TOGGLE_COLOR = ['rgba(252, 224, 88, 1)', 'rgba(251, 223, 89, 1)']
    NO_NOTIFICATIONS = 'Нет уведомлений'


class MainConstant:
    MAIN_PAGE_TITLE = 'PulseWave'
    TEXT_SIGNUP = 'Зарегистрироваться'
    MAIN_TITLE = 'PULSEWAVE'
    USEFUL_INTERFACE = 'Удобный и понятный интерфейс!'
    ALL_TIME = 'Самый высокий уровень бесперебойной работы!'
    FIRST_SAFETY = 'Ваша безопасность и конфиденциальность для нас на первом месте!'
    FULL_FUNCTIONALITY = (f'Неограниченный функционал, понятный интерфейс и большое количество '
                          f'возможностей\nпомогут Вам улучшить рабочий процесс.')
    ONE_APP = 'Одно приложениe для решения всех Ваших задач!'

    CHECK_BUTTON = [
        ('font-size', '18px', 'размера шрифта'),
        ('color', 'rgba(66, 66, 66, 1)', 'цвета шрифта'),
        ('font-family', 'Mulish, sans-serif', 'шрифта'),
        ('background-color', 'rgba(252, 224, 88, 1)', 'цвета')
    ]
    CHECK_TEXT = [
        ('font-size', '16px', 'размера шрифта'),
        ('color', 'rgba(16, 16, 18, 1)', 'цвета шрифта'),
        ('font-family', 'Mulish, sans-serif', 'шрифта')
    ]
    CHECK_TITLE = [
        ('font-size', '80px', 'размера шрифта'),
        ('color', 'rgba(66, 66, 66, 1)', 'цвета шрифта'),
        ('font-family', 'Mulish, sans-serif', 'шрифта')
    ]


class LendingConstant:
    pass


class PasswordRecoveryConstant:

    RECOVERY_PAGE_TITLE = 'Восстановление пароля'
    RESUME_BUTTON_TEXT = 'Продолжить'
    CHECK_TITLE = [
        ("font-size", '18px', 'размера шрифта'),
        ("color", 'rgba(66, 66, 66, 1)', 'цвета шрифта'),
        ("font-family", 'Mulish, sans-serif', 'шрифта')
    ]


class SignUpConstants:
    SIGNUP_PAGE_TITLE = 'Регистрация'
    TEXT_SIGNUP = 'Регистрация'

    CHECK_TITLE = [
        ("font-size", '18px', 'размера шрифта'),
        ("color", 'rgba(66, 66, 66, 1)', 'цвета шрифта'),
        ("font-family", 'Mulish, sans-serif', 'шрифта')
    ]

    PASSWORD_RULES_CSS = {
        'color': 'rgba(183, 183, 183, 1)',
        'font-size': '12px',
        'font-family': 'Mulish, sans-serif'
    }

    REGISTERED_YET_CSS = {
        'color': 'rgba(183, 183, 183, 1)',
        'font-size': '12px',
        'font-family': 'Mulish, sans-serif'
    }

    PULSEWAVE_POLICY_CSS = {
        'color': 'rgba(66, 66, 66, 1)',
        'font-size': '12px',
        'font-family': 'Mulish, sans-serif'
    }

    AGREEMENT_CSS = {
        'color': 'rgba(66, 66, 66, 1)',
        'font-size': '12px',
        'font-family': 'Mulish, sans-serif'
    }

    INCORRECT_EMAIL = ['test@test', 'test.test']
    # WEAK_PASSWORD = ['password', '12345678', '1Passw', '!1Pas  sword', '!1Password  ', '  !1Password']

    INVITE_MSG = f'Регистрация\nМы отправили вам письмо на {email1}.\nДля подтверждения регистрации и \
активации учётной записи пройдите по ссылке в письме.\nПисьмо не пришло?\nПроверьте папку Спам и нажмите кнопку \
«Отправить повторно».'
    DELETE_USER_MSG = 'Ваша учетная запись удалена.'
