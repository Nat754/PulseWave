from selenium.webdriver.common.by import By


class FooterLocators:

    license = (By.XPATH, '(//span[@class="item__text"])[1]')
    email = (By.CLASS_NAME, 'item__link-desc')
    email_hover = (By. XPATH, '//a[contains(@href, "mailto")]')
    cooperation = (By.XPATH, '(//span[@class="item__text"])[3]')
    license_title = (By.CLASS_NAME, 'privacy__title')
    allow_all_cookies = (By.CSS_SELECTOR, '.cookies__body .button__small')
    cookies_link = (By.CLASS_NAME, 'cookies__link')
    cookies_text = (By.CLASS_NAME, 'cookies__text')
