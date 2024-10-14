from data import email1


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
