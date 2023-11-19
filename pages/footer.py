import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.test_footer.constant import COOKIES_BUTTON, TEXT_COOPERATION, EMAIL_TEXT_HOVER, EMAIL_TEXT, LICENSE_TITLE, \
    LICENSE_LINK


class Footer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._license = (By.CSS_SELECTOR, 'a.link.item__link')
        self._email = (By.CLASS_NAME, 'item__link-desc')
        self._email_hover = (By. XPATH, '//a[contains(@href, "mailto")]')
        self._cooperation = (By.XPATH, '(//span[@class="item__text"])[3]')
        self._license_title = (By.CLASS_NAME, 'privacy__title')
        self._allow_all_cookies = (By.CSS_SELECTOR, '.cookies__body .button__small')
        self._cookies_link = (By.CLASS_NAME, 'cookies__link')
        self._cookies_text = (By.CLASS_NAME, 'cookies__text')

    @allure.step(f"Проверка видимости ссылки '{LICENSE_LINK}' в футере")
    def get_footer_license(self):
        return self.element_is_visible(self._license)

    @allure.step(f"Проверка видимости заголовка '{LICENSE_TITLE}'")
    def get_license_title(self):
        return self.element_is_visible(self._license_title)

    @allure.step(f"Проверка видимости надписи '{EMAIL_TEXT}' в футере")
    def get_footer_email(self):
        return self.element_is_visible(self._email)

    @allure.step(f"Проверка видимости перенаправления '{EMAIL_TEXT_HOVER}' в футере")
    def get_footer_email_hover(self):
        return self.element_is_visible(self._email_hover)

    @allure.step(f"Проверка видимости надписи '{TEXT_COOPERATION}' в футере")
    def get_footer_cooperation(self):
        return self.element_is_visible(self._cooperation)

    @allure.step(f"Проверка видимости кнопки '{COOKIES_BUTTON}' "
                 f"в сообщении о принятии файлов cookie на Главной странице")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self._allow_all_cookies)

    @allure.step("Проверка видимости текста сообщения о принятии файлов cookie на Главной странице")
    def get_cookies_text(self):
        return self.element_is_visible(self._cookies_text)

    @allure.step("Проверка видимости ссылки для просмотра информации о файлах cookie на Главной странице")
    def get_cookies_link(self):
        return self.element_is_visible(self._cookies_link)
