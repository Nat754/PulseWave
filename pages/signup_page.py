from locators.signup_locators import SignUpLocators
from pages.base_page import BasePage
import allure
from tests.test_signup_page.constant import SignUpConstants


class SignUpPage(BasePage):
    signup = SignUpConstants
    locator = SignUpLocators

    @allure.step(f"Проверка видимости заголовка {signup.TEXT_SIGNUP}")
    def get_title_login(self):
        return self.element_is_visible(self.locator.TITLE_SIGNUP)

    @allure.step("Проверка видимости кнопки 'Принимаю все' в сообщении о принятии файлов cookie")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self.locator.ALLOW_ALL_COOKIES)

    @allure.step("Проверка видимости логотипа в хедере")
    def get_header_logo_signup(self):
        return self.element_is_visible(self.locator.LOGO)
