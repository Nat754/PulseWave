from selenium.webdriver.common.by import By


class LoginPageLocators:

    TITLE_LOGIN = (By.TAG_NAME, 'h1')
    ALLOW_ALL_COOKIES = (By.CLASS_NAME, 'btn-cookies')
    LOGO = (By.CLASS_NAME, 'header__logo')
    EMAIL = (By.XPATH, '//input[@type="email"]')
    PASSWORD = (By.XPATH, '//input[@type="password"]')
    SUBMIT = (By.XPATH, '//button[@type="submit"]')
    ERROR_MSG = (By.CSS_SELECTOR, '.invalid-form span')
    FORGOT_PASSWORD = (By.XPATH, '//span[text()="Забыли пароль?"]')
