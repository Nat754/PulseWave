from locators.login_locators import LoginPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

from tests.test_login_page.login_constant import LoginConstant


class LoginPage(BasePage):
    login = LoginConstant
    locator = LoginPageLocators

    @allure.step(f"Проверка видимости заголовка {login.TEXT_LOGIN}")
    def get_title_login(self):
        return self.element_is_visible(self.locator.TITLE_LOGIN)

    @allure.step("Проверка видимости кнопки 'Принимаю все' в сообщении о принятии файлов cookie")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self.locator.ALLOW_ALL_COOKIES)

    @allure.step("Проверка видимости логотипа в хедере")
    def get_header_logo_login(self):
        return self.element_is_visible(self.locator.LOGO)
