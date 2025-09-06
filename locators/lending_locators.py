from selenium.webdriver.common.by import By


class LendingPageLocators:
    LOGO = (By.CLASS_NAME, 'header__logo')
    AUTH_LOGIN = (By.CSS_SELECTOR, 'a.btn.btn--white')
    AUTH_FREE = (By.XPATH, '//a[text()="Бесплатная регистрация"]')
