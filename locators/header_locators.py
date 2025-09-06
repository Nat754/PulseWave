from selenium.webdriver.common.by import By


class HeaderLocators:

    LOGO = (By.CLASS_NAME, 'header__logo')
    AUTH_LOGIN = (By.CLASS_NAME, 'button__small')
    AUTH_SIGNUP = (By.CLASS_NAME, 'button__small')
    START_SIGNUP = (By.XPATH, '//span[text()="Бесплатная регистрация"]')
