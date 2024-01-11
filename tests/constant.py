from data import email_auth


class Constant:

    MAIN_PAGE = 'https://front.pwave.pnpl.tech/'
    MAIN_PAGE_HOME = f'{MAIN_PAGE}home'
    LOGIN_PAGE = f'{MAIN_PAGE}auth/login'
    SIGNUP_PAGE = f'{MAIN_PAGE}auth/signup'
    TERMS_OF_SERVICE = f'{MAIN_PAGE}documents/terms-of-service'
    WORKSPACE = f'{MAIN_PAGE}workspaces'
    PULSEWAVE_PRIVACY = f'{MAIN_PAGE}documents/privacy'
    PASSWORD_RECOVERY = f'{MAIN_PAGE}auth/password?email='


class Messages:

    WRONG_PASSWORD_MSG = 'Некорректный e-mail или пароль.'
    FORGOT_PASSWORD_MSG = 'Забыли пароль?'
    PASSWORD_RULES_MSG = ('Пароль должен содержать не менее 8 символов, включая минимум 1 цифру, '
                          '1 строчную и 1 заглавную буквы, 1 спецсимвол.')
    PULSEWAVE_POLICY_MSG = 'Я согласен получать новости и обновления PulseWave'
    AGREEMENT_MSG = 'Регистрируясь, я соглашаюсь с Условиями пользования и Политикой конфиденциальности'
    INVALID_PASSWORD_MSG = ('Слабый пароль. Пожалуйста, введите не менее 8 символов, включая минимум 1 цифру, 1 '
                            'строчную и 1 заглавную буквы, 1 спецсимвол')
    INVALID_EMAIL_MSG = 'Пожалуйста, введите корректную почту.'
    PASSWORDS_NOT_EQUAL_MSG = 'Пароли не совпадают. Повторите попытку, пожалуйста'
    EMAIL_WAS_SEND = 'На Ваш электронный адрес'
    GO_TO_EMAIL = ('выслана ссылка для восстановления пароля. '
                   'Пожалуйста, пройдите по ней и создайте новый пароль для учетной записи.')
