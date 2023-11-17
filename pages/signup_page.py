from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

from tests.test_signup_page.constant import TEXT_SIGNUP


class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._title_signup = (By.TAG_NAME, 'h1')
        self._allow_all_cookies = (By.CSS_SELECTOR, '.cookies__body .button__small')

    @allure.step(f"Проверка видимости заголовка {TEXT_SIGNUP}")
    def get_title_login(self):
        return self.element_is_visible(self._title_signup)

    @allure.step("Проверка видимости кнопки 'Принимаю все' в сообщении о принятии файлов cookie")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self._allow_all_cookies)
