from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage
import allure
from tests.test_password_recovery.test_password_recovery import PasswordRecoveryConstant
from tests.constant import Messages


class PasswordRecoveryPage(BasePage):
    recovery = PasswordRecoveryConstant
    locator = PasswordRecoveryLocators
    message = Messages

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

    @allure.step(f"Нажать кнопку '{recovery.RESUME_BUTTON_TEXT}'")
    def click_resume_button(self):
        return self.element_is_clickable(self.locator.SUBMIT_BUTTON).click()

    @allure.step("Получить текст сообщения")
    def get_message_text(self):
        return self.element_is_visible(self.locator.MESSAGE_SENT_EMAIL).text