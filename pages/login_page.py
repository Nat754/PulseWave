from data import email_auth, password0, incorrect_email, email2
from locators.login_locators import LoginPageLocators
from pages.base_page import BasePage
import allure
from tests.test_login_page.login_constant import LoginConstant
from tests.constant import Messages


class LoginPage(BasePage):
    login = LoginConstant
    locator = LoginPageLocators
    message = Messages

    @allure.step(f"Проверка видимости заголовка {login.TEXT_LOGIN}")
    def get_title_login(self):
        return self.element_is_visible(self.locator.TITLE_LOGIN)

    @allure.step("Проверка видимости кнопки 'Принимаю все' в сообщении о принятии файлов cookie")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self.locator.ALLOW_ALL_COOKIES)

    @allure.step("Проверка видимости логотипа в хедере")
    def get_header_logo_login(self):
        return self.element_is_visible(self.locator.LOGO)

    @allure.step("Ввести в поле e-mail корректные данные")
    def input_e_mail(self):
        return self.element_is_visible(self.locator.EMAIL).send_keys(email_auth)

    @allure.step("Ввести в поле e-mail некорректные данные")
    def input_not_auth_email(self):
        return self.element_is_visible(self.locator.EMAIL).send_keys(email2)

    @allure.step("Оставить поле e-mail пустым")
    def empty_email(self):
        return self.element_is_visible(self.locator.EMAIL).send_keys('')

    @allure.step("Ввести в поле пароль сильный пароль")
    def input_password(self):
        return self.element_is_visible(self.locator.PASSWORD).send_keys(password0)

    @allure.step("Оставить поле пароль пустым")
    def empty_password(self):
        return self.element_is_visible(self.locator.PASSWORD).send_keys('')

    @allure.step(f"Нажать кнопку '{login.TEXT_LOGIN}'")
    def click_submit(self):
        return self.element_is_clickable(self.locator.SUBMIT).click()

    @allure.step("Ввести в поле пароль некорректный пароль")
    def input_wrong_password(self):
        return self.element_is_visible(self.locator.PASSWORD).send_keys('password')

    @allure.step(f"Высветилась ошибка: '{message.WRONG_PASSWORD_MSG}'")
    def check_wrong_password_message(self):
        return self.element_is_visible(self.locator.WRONG_PASSWORD)

    @allure.step(f"Видимость подсказки: '{message.FORGOT_PASSWORD_MSG}'")
    def check_forgot_password_message(self):
        return self.element_is_visible(self.locator.FORGOT_PASSWORD)

    @allure.step(f"Проверка неактивности кнопки '{login.TEXT_LOGIN}'")
    def button_login_not_active(self):
        return self.element_is_not_clickable(self.locator.SUBMIT)
