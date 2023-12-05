from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGO = (By.CLASS_NAME, 'header__logo')
    AUTH_LOGIN = (By.CSS_SELECTOR, '.button__small')
    AUTH_SIGNUP = (By.CSS_SELECTOR, 'a[href="/auth/signup"] button')
    SIGNUP = (By.CLASS_NAME, 'button__big')
    LICENSE = (By.XPATH, '(//span[@class="item__text"])[1]')
    EMAIL = (By.CLASS_NAME, 'item__link-desc')
    EMAIL_HOVER = (By. XPATH, '//a[contains(@href, "mailto")]')
    COOPERATION = (By.XPATH, '(//span[@class="item__text"])[3]')
    LICENSE_TITLE = (By.CLASS_NAME, 'privacy__title')
    MAIN_TITLE = (By.TAG_NAME, 'h1')
    MAIN_SUBTITLE = (By.CLASS_NAME, 'main__subtitle')
    MAIN_DESCR = (By.CLASS_NAME, 'main__descr')
    ALLOW_ALL_COOKIES = (By.CSS_SELECTOR, '.cookies__body .button__small')
    COOKIES_LINK = (By.CLASS_NAME, 'cookies__link')
    COOKIES_TEXT = (By.CLASS_NAME, 'cookies__text')
    USERFUL_INTERFACE = (By.XPATH, '//p[text()="Удобный и понятный интерфейс!"]')
    ALL_TIME = (By.XPATH, '//p[text()="Самый высокий уровень бесперебойной работы!"]')
    FIRST_SAFETY = (By.XPATH, '//p[contains(text(), "Ваша безопасность")]')
