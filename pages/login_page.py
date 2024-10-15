from locators.login_locators import LoginPageLocators
from pages.base_page import BasePage
import allure
from tests.test_login_page.login_constant import LoginConstant
from tests.constant import Messages, Links


class LoginPage(BasePage):
    login = LoginConstant()
    locator = LoginPageLocators()
    message = Messages()
    link = Links()

    @allure.step(f"Проверка видимости заголовка {login.TEXT_LOGIN}")
    def get_title_login(self):
        return self.element_is_visible(self.locator.TITLE_LOGIN)

    @allure.step("Проверка видимости кнопки 'Принимаю все' в сообщении о принятии файлов cookie")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self.locator.ALLOW_ALL_COOKIES)

    def input_email(self, email):
        return self.element_is_visible(self.locator.EMAIL).send_keys(email)

    def input_password(self, password):
        return self.element_is_visible(self.locator.PASSWORD).send_keys(password)

    @allure.step(f"Нажать кнопку '{login.TEXT_LOGIN}'")
    def click_submit(self):
        return self.element_is_clickable(self.locator.SUBMIT).click()

    @allure.step(f"Высветилась ошибка: '{message.WRONG_PASSWORD_MSG}'")
    def check_wrong_password_message(self):
        return self.element_is_visible(self.locator.WRONG_PASSWORD)

    @allure.step(f"Видимость подсказки: '{message.FORGOT_PASSWORD_MSG}'")
    def check_forgot_password_message(self):
        return self.element_is_visible(self.locator.FORGOT_PASSWORD)

    @allure.step(f"Проверка неактивности кнопки '{login.TEXT_LOGIN}'")
    def button_login_not_active(self):
        return self.element_is_not_clickable(self.locator.SUBMIT)

    @allure.step('Ждать обновление страницы')
    def check_changed_url_login(self):
        return self.wait_changed_url(self.link.LOGIN_PAGE)
