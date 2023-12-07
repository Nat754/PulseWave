from data import email_auth, password0
from locators.login_locators import LoginPageLocators
from pages.base_page import BasePage
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

    @allure.step("Ввести в поле e-mail данные")
    def input_e_mail(self):
        return self.element_is_visible(self.locator.EMAIL).send_keys(email_auth)

    @allure.step("Ввести в поле пароль данные")
    def input_password(self):
        return self.element_is_visible(self.locator.PASSWORD).send_keys(password0)

    @allure.step(f"Нажать кнопку '{login.TEXT_LOGIN}")
    def click_submit(self):
        return self.element_is_clickable(self.locator.SUBMIT).click()
