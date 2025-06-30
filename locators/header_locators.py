from selenium.webdriver.common.by import By


class HeaderLocators:

    LOGO = (By.CLASS_NAME, 'header__logo')
    AUTH_LOGIN = (By.XPATH, '//*[text()=" Войти "]')
    AUTH_SIGNUP = (By.XPATH, '//span[text()=" Регистрация "]')
    START_SIGNUP = (By.XPATH, '//span[text()="Бесплатная регистрация"]')
