from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:

    RECOVERY_TITLE = (By.TAG_NAME, 'h1')
    ALLOW_ALL_COOKIES = (By.CSS_SELECTOR, '.cookies__body .button__small')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
