from selenium.webdriver.common.by import By


class LoginPageLocators:

    TITLE_LOGIN = (By.TAG_NAME, 'h1')
    ALLOW_ALL_COOKIES = (By.CSS_SELECTOR, '.cookies__body .button__small')
    LOGO = (By.CLASS_NAME, 'header__logo')
