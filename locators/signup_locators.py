from selenium.webdriver.common.by import By
from locators.general_locators import GeneralLocators


class SignUpLocators(GeneralLocators):

    TITLE_SIGNUP = (By.TAG_NAME, 'h1')
    PASSWORD_RULES = (By.CSS_SELECTOR, '.invalid-form span')
    PULSEWAVE_POLICY = (By.CLASS_NAME, 'styled-checkbox')
    AGREEMENT_MSG = (By.CLASS_NAME, 'agreement')
    TERMS_OF_SERVICE = (By.XPATH, '(//a[@class="agreement__link"])[1]')
    POLICY_SERVICE = (By.XPATH, '(//a[@class="agreement__link"])[2]')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_FIELD = (By.XPATH, '(//input[@type="password"])[1]')
    CONFIRM_PASSWORD_FIELD = (By.XPATH, '(//input[@type="password"])[2]')
    EYES = (By.CSS_SELECTOR, 'svg.input-password__type')
    CHECK_BOX = (By.CLASS_NAME, 'styled-checkbox')
    WEAK_PASSWORD = (By.CLASS_NAME, 'invalid-form')
    SEND_INVITE_EMAIL = (By.CLASS_NAME, 'form__texts')
    BUTTON_AVATAR = (By.CLASS_NAME, 'avatar')
    PROFILE_SETTINGS = (By.XPATH, '(//div[@class="nav__item"])[1]')
    DELETE_PROFILE = (By.XPATH, '//span[text()="Удалить профиль"]')
    CONFIRM_PASSWORD = (By.XPATH, '//input[@type="password"]')
    DELETE_BUTTON = (By.XPATH, '(//button[contains(@class, "modal__btn")])[1]')
    DELETE_MESSAGE = (By.CSS_SELECTOR, '.form p.text')
    AGREE_RADIO_BUTTON = (By.CSS_SELECTOR, 'for="myCheckbox"')
    AVATAR_LOGOUT = (By.CLASS_NAME, 'avatar__logout')
    LOGOUT_MSG = (By.CLASS_NAME, 'exit-text')
    MODAL = (By.ID, 'modal')
