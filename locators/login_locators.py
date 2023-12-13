from selenium.webdriver.common.by import By


class LoginPageLocators:

    TITLE_LOGIN = (By.TAG_NAME, 'h1')
    ALLOW_ALL_COOKIES = (By.CSS_SELECTOR, '.cookies__body .button__small')
    LOGO = (By.CLASS_NAME, 'header__logo')
    EMAIL = (By.XPATH, '//input[@type="email"]')
    PASSWORD = (By.XPATH, '//input[@type="password"]')
    SUBMIT =(By.XPATH, '//button[@type="submit"]')
    WRONG_PASSWORD = (By.XPATH, '//span[text()="Некорректный e-mail или пароль."]')
    FORGOT_PASSWORD = (By.XPATH, '//span[text()="Забыли пароль?"]')
