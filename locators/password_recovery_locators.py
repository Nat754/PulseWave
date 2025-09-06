from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:

    RECOVERY_TITLE = (By.TAG_NAME, 'h1')
    ALLOW_ALL_COOKIES = (By.CSS_SELECTOR, '.cookies__body .button__small')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    INPUT_EMAIL = (By.CLASS_NAME, 'input')
    MESSAGE_SENT_EMAIL = (By.CSS_SELECTOR, '.auth p')
    INPUT_PASSWORD = (By.XPATH, '(//input[@type="password"])[1]')
    INPUT_CONFIRM_PASSWORD = (By.XPATH, '(//input[@type="password"])[2]')
    INVALID_EMAIL = (By.CSS_SELECTOR, '.invalid.invalid-form')
