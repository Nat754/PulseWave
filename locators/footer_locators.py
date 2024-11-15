from selenium.webdriver.common.by import By


class FooterLocators:

    LICENSE = (By.XPATH, '(//span[@class="item__text"])[1]')
    EMAIL = (By.CLASS_NAME, 'item__link-desc')
    EMAIL_HOVER = (By. XPATH, '//a[contains(@href, "mailto")]')
    COOPERATION = (By.XPATH, '(//span[@class="item__text"])[2]')
    LICENSE_TITLE = (By.CLASS_NAME, 'privacy__title')
    ALLOW_ALL_COOKIES = (By.CSS_SELECTOR, '.cookies__body .button__small')
    COOKIES_LINK = (By.CLASS_NAME, 'cookies__link')
    COOKIES_TEXT = (By.CLASS_NAME, 'cookies__text')
