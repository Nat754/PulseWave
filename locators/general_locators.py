from selenium.webdriver.common.by import By


class GeneralLocators:

    TITLE_MODAL = (By.CLASS_NAME, 'form__title')
    TEXT_MODAL = (By.CLASS_NAME, 'text-content')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    LOGO = (By.CLASS_NAME, 'header__logo')
    SIGNUP = (By.CLASS_NAME, 'button__big')
    ALLOW_ALL_COOKIES = (By.CLASS_NAME, 'btn-cookies')

    EMAIL = (By.CLASS_NAME, 'item__link-desc')
    EMAIL_HOVER = (By.XPATH, '//a[contains(@href, "mailto")]')
    COOPERATION = (By.XPATH, '(//span[@class="item__text"])[3]')
    LICENSE_TITLE = (By.CLASS_NAME, 'privacy__title')
    MAIN_TITLE = (By.TAG_NAME, 'h1')
    MAIN_SUBTITLE = (By.CLASS_NAME, 'main__subtitle')
    MAIN_DESCR = (By.CLASS_NAME, 'main__descr')

    # COOKIES_LINK = (By.CLASS_NAME, 'cookies__link')
    COOKIES_TEXT = (By.CLASS_NAME, 'cookies__text')
    USERFUL_INTERFACE = (By.XPATH, '//p[text()="Удобный и понятный интерфейс!"]')
    ALL_TIME = (By.XPATH, '//p[text()="Самый высокий уровень бесперебойной работы!"]')
    FIRST_SAFETY = (By.XPATH, '//p[contains(text(), "Ваша безопасность")]')

    # FOOTER
    LICENSE = (By.XPATH, '(//span[@class="item__text"])[1]')
    # EMAIL = (By.CSS_SELECTOR, 'a .item__text')
    # EMAIL_HOVER = (By.XPATH, '//a[contains(@href, "mailto")]')
    # COOPERATION = (By.XPATH, '(//span[@class="item__text"])[2]')
    # LICENSE_TITLE = (By.CLASS_NAME, 'privacy__title')

    COOKIES_LINK = (By.CLASS_NAME, 'cookies__link')
    LINKEDIN_BUTTON = (By.CLASS_NAME, 'social')
    FOOTER = (By.CSS_SELECTOR, 'span.item__text')

    # HEADER

    AUTH_LOGIN = (By.CLASS_NAME, 'button__small')
    AUTH_SIGNUP = (By.CLASS_NAME, 'button__small')
    START_SIGNUP = (By.XPATH, '//span[text()="Бесплатная регистрация"]')

    # LENDING

    # AUTH_LOGIN = (By.CSS_SELECTOR, 'a.btn.btn--white')
    AUTH_FREE = (By.XPATH, '//a[text()="Бесплатная регистрация"]')

    # LOGIN
    TITLE_LOGIN = (By.TAG_NAME, 'h1')

    # EMAIL = (By.XPATH, '//input[@type="email"]')
    PASSWORD = (By.XPATH, '//input[@type="password"]')
    ERROR_MSG = (By.CSS_SELECTOR, '.invalid-form span')
    FORGOT_PASSWORD = (By.XPATH, '//span[text()="Забыли пароль?"]')

    # PasswordRecoveryLocators:
    RECOVERY_TITLE = (By.TAG_NAME, 'h1')

    INPUT_EMAIL = (By.CLASS_NAME, 'input')
    MESSAGE_SENT_EMAIL = (By.CSS_SELECTOR, '.auth p')
    INPUT_PASSWORD = (By.XPATH, '(//input[@type="password"])[1]')
    INPUT_CONFIRM_PASSWORD = (By.XPATH, '(//input[@type="password"])[2]')
    INVALID_EMAIL = (By.CSS_SELECTOR, '.invalid.invalid-form')

    # WorkspaceLocators:
    AVATAR_ICON = (By.CLASS_NAME, 'avatar')
    DROP_WORKSPACES = (By.CLASS_NAME, 'desctop')
    DROP_CREATE = (By.CLASS_NAME, 'create')
    LEFT_MENU_TITLE = (By.CLASS_NAME, 'title-wrapper')
    LEFT_MENU = (By.CSS_SELECTOR, 'span[class="name"]')
    LEFT_MENU_LETTER = (By.CLASS_NAME, 'name-letter')
    RIGHT_MENU = (By.CSS_SELECTOR, 'div[class="name"]')
    TO_MAIM_LINK = (By.CLASS_NAME, 'navigat__item-home')
    RIGHT_TITLE = (By.CSS_SELECTOR, '.workspaces__content h2.title')
    LOADER = (By.CSS_SELECTOR, '.loader .icon')
    NOTIFY = (By.CLASS_NAME, 'header__notifications')
    READ_ALL_BUTTON = (By.CLASS_NAME, 'read-all')
    TOGGLE = (By.CLASS_NAME, 'styled-toggle')
    NOTIFICATIONS = (By.CLASS_NAME, 'notification__text')
    NO_NOTIFICATIONS = (By.CLASS_NAME, 'no-notifications')
