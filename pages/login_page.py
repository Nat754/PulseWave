from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

from tests.test_login_page.constant import TEXT_LOGIN


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._title_login = (By.TAG_NAME, 'h1')
        self._allow_all_cookies = (By.CSS_SELECTOR, '.cookies__body .button__small')
        self._logo = (By.CLASS_NAME, 'header__logo')

    @allure.step(f"Проверка видимости заголовка {TEXT_LOGIN}")
    def get_title_login(self):
        return self.element_is_visible(self._title_login)

    @allure.step("Проверка видимости кнопки 'Принимаю все' в сообщении о принятии файлов cookie")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self._allow_all_cookies)

    @allure.step("Проверка видимости логотипа в хедере")
    def get_header_logo_login(self):
        return self.element_is_visible(self._logo)
