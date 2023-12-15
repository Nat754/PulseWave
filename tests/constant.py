
class Constant:

    MAIN_PAGE = 'https://front.pwave.pnpl.tech/'
    MAIN_PAGE_HOME = f'{MAIN_PAGE}home'
    LOGIN_PAGE = f'{MAIN_PAGE}auth/login'
    SIGNUP_PAGE = f'{MAIN_PAGE}auth/signup'
    TERMS_OF_SERVICE = f'{MAIN_PAGE}documents/terms-of-service'
    WORKSPACE = f'{MAIN_PAGE}workspaces'
    PULSEWAVE_PRIVACY = f'{MAIN_PAGE}documents/privacy'


class Messages:

    WRONG_PASSWORD_MSG = 'Некорректный e-mail или пароль.'
    FORGOT_PASSWORD_MSG = 'Забыли пароль?'
    PASSWORD_RULES_MSG = ('Пароль должен содержать не менее 8 символов, включая минимум 1 цифру, '
                          '1 строчную и 1 заглавную буквы, 1 спецсимвол.')
    PULSEWAVE_POLICY_MSG = 'Я согласен получать новости и обновления PulseWave'
    AGREEMENT_MSG = 'Регистрируясь, я соглашаюсь с Условиями пользования и Политикой конфиденциальности'
    INVALID_PASSWORD_MSG = ('Слабый пароль. Пожалуйста, введите не менее 8 символов, включая минимум 1 цифру, 1 '
                            'строчную и 1 заглавную буквы, 1 спецсимвол')
