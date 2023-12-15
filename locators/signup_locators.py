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
