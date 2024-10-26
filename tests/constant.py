class Links:

    # MAIN_PAGE = 'https://web.dev.pulsewave.ru/'
    # BASE_URL = "https://api.dev.pulsewave.ru/"
    MAIN_PAGE = 'https://pulsewave.ru/'
    BASE_URL = 'https://api.pulsewave.ru/'
    # MAIN_PAGE_HOME = f'{MAIN_PAGE}home'
    LOGIN_PAGE = f'{MAIN_PAGE}auth/login'
    SIGNUP_PAGE = f'{MAIN_PAGE}auth/signup'
    TERMS_OF_SERVICE = f'{MAIN_PAGE}documents/terms-of-service'
    WORKSPACE = f'{MAIN_PAGE}workspaces'
    PULSEWAVE_PRIVACY = f'{MAIN_PAGE}documents/privacy'
    PASSWORD_RECOVERY = f'{MAIN_PAGE}auth/password?email='
    SET_OF_BROWSERS = ['chrome']

    MAIL_URL = 'https://mail.ru/'


class Messages:

    WRONG_PASSWORD_MSG = 'Некорректный e-mail или пароль.'
    FORGOT_PASSWORD_MSG = 'Забыли пароль?'
    # PASSWORD_RULES_MSG = ('Пароль должен содержать не менее 8 символов, включая минимум 1 цифру, '
    #                       '1 строчную и 1 заглавную буквы, 1 спецсимвол, без пробелов.')
    PASSWORD_RULES_MSG = 'Пароль должен содержать минимум 8 символов, включая буквы и цифры'
    PULSEWAVE_POLICY_MSG = 'Я согласен получать новости и обновления PulseWave'
    AGREEMENT_MSG = 'Регистрируясь, я соглашаюсь с Условиями пользования и Политикой конфиденциальности'
    # INVALID_PASSWORD_MSG = ('Слабый пароль. Пожалуйста, введите не менее 8 символов, включая минимум 1 цифру, 1 '
    #                         'строчную и 1 заглавную буквы, 1 спецсимвол, без пробелов')
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
