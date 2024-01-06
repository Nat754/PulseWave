from selenium.webdriver.common.by import By


class HeaderLocators:

    LOGO = (By.CLASS_NAME, 'header__logo')
    AUTH_LOGIN = (By.XPATH, '(//button[@class="button button__small"])[1]')
    AUTH_SIGNUP = (By.XPATH, '//span[text()=" Регистрация "]')
