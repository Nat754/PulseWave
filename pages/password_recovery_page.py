from data import email_auth, password_auth_email
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage
import allure
from tests.test_password_recovery.constant import PasswordRecoveryConstant
from tests.constant import Messages, Links
from api_testing.api_base import ApiBase


class PasswordRecoveryPage(BasePage):
    recovery = PasswordRecoveryConstant()
    locator = PasswordRecoveryLocators()
    message = Messages()
    const = Links()

    @staticmethod
    @allure.step('Получить ссылку для смены пароля на email')
    def get_link_recovery_password_by_email():
        msg = ApiBase.read_email(email_auth, password_auth_email)
        first = msg.find(Links.MAIN_PAGE)
        end = msg[first:].find('"')
        link = msg[first:first + end]
        return link

    @allure.step(f"Проверка видимости заголовка {recovery.RECOVERY_PAGE_TITLE}")
    def get_title_recovery(self):
        return self.element_is_visible(self.locator.RECOVERY_TITLE)

    @allure.step("Проверка видимости кнопки 'Принимаю все' в сообщении о принятии файлов cookie")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self.locator.ALLOW_ALL_COOKIES)

    @allure.step(f"Проверка некликабельности кнопки '{recovery.RESUME_BUTTON_TEXT}'")
    def check_resume_button_is_not_clickable(self):
        return self.element_is_not_clickable(self.locator.SUBMIT_BUTTON)

    def fill_email_to_recovery_password(self, email):
        return self.element_is_visible(self.locator.INPUT_EMAIL).send_keys(email)

    def click_resume_button(self):
        return self.element_is_clickable(self.locator.SUBMIT_BUTTON).click()

    @allure.step("Получить текст сообщения")
    def get_message_text(self):
        return self.element_is_visible(self.locator.MESSAGE_SENT_EMAIL).text

    def fill_password_recovery(self, password):
        return self.element_is_visible(self.locator.INPUT_PASSWORD).send_keys(password)

    def fill_confirm_password_recovery(self, password):
        return self.element_is_visible(self.locator.INPUT_CONFIRM_PASSWORD).send_keys(password)

    @allure.step('Ждать обновление страницы')
    def check_changed_url_login(self):
        return self.wait_changed_url(self.const.LOGIN_PAGE)

    @allure.step("Получить текст сообщения о неверном емайл")
    def get_invalid_email_message(self):
        return self.element_is_visible(self.locator.INVALID_EMAIL).text
