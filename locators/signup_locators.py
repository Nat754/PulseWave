from selenium.webdriver.common.by import By


class SignUpLocators:

    TITLE_SIGNUP = (By.TAG_NAME, 'h1')
    ALLOW_ALL_COOKIES = (By.CSS_SELECTOR, '.cookies__body .button__small')
    LOGO = (By.CLASS_NAME, 'header__logo')
    PASSWORD_RULES = (By.CLASS_NAME, 'explanation')
    PULSEWAVE_POLICY = (By.CLASS_NAME, 'styled-checkbox')
    AGREEMENT_MSG = (By.CLASS_NAME, 'agreement')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    TERMS_OF_SERVICE = (By.XPATH, '(//a[@class="agreement__link"])[1]')
    POLICY_SERVICE = (By.XPATH, '(//a[@class="agreement__link"])[2]')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_FIELD = (By.XPATH, '(//input[@type="password"])[1]')
    CONFIRM_PASSWORD_FIELD = (By.XPATH, '(//input[@type="password"])[2]')
    EYES = (By.CSS_SELECTOR, 'svg.input-password__type')
    CHECK_BOX = (By.CLASS_NAME, 'styled-checkbox')
    WEAK_PASSWORD = (By.CLASS_NAME, 'invalid-form')
    SEND_INVITE_EMAIL = (By.CLASS_NAME, 'form__texts')
    WELCOME_TO_WORKSPACE = (By.CSS_SELECTOR, 'button[type="submit"]')
    BUTTON_AVATAR = (By.CLASS_NAME, 'avatar__button')
    PROFILE_SETTINGS = (By.XPATH, '(//div[@class="nav__item"])[1]')
    DELETE_PROFILE = (By.XPATH, '//span[text()="Удалить профиль"]')
    CONFIRM_PASSWORD = (By.XPATH, '(//input[@class="input"])[2]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    DELETE_MESSAGE = (By.XPATH, '//p[@class="text"]')
    AGREE_RADIO_BUTTON = (By.CSS_SELECTOR, 'for="myCheckbox"')
