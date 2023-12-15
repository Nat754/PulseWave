from locators.signup_locators import SignUpLocators
from pages.base_page import BasePage
import allure
from tests.test_signup_page.constant import SignUpConstants
from tests.constant import Messages


class SignUpPage(BasePage):
    signup = SignUpConstants
    locator = SignUpLocators
    message = Messages

    @allure.step(f"Проверка видимости заголовка {signup.TEXT_SIGNUP}")
    def get_title_login(self):
        return self.element_is_visible(self.locator.TITLE_SIGNUP)

    @allure.step("Проверка видимости кнопки 'Принимаю все' в сообщении о принятии файлов cookie")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self.locator.ALLOW_ALL_COOKIES)

    @allure.step("Проверка видимости логотипа в хедере")
    def get_header_logo_signup(self):
        return self.element_is_visible(self.locator.LOGO)

    @allure.step(f"Видимость подсказки: '{message.PASSWORD_RULES_MSG}'")
    def check_password_rules_message(self):
        return self.element_is_visible(self.locator.PASSWORD_RULES)

    @allure.step(f"Видимость сообщения: '{message.PULSEWAVE_POLICY_MSG}'")
    def check_pulsewave_policy_message(self):
        return self.element_is_visible(self.locator.PULSEWAVE_POLICY)

    @allure.step(f"Видимость сообщения: '{message.AGREEMENT_MSG}'")
    def check_agreement_message(self):
        return self.element_is_visible(self.locator.AGREEMENT_MSG)

    @allure.step(f"Проверка перехода по ссылке: '{message.AGREEMENT_MSG[30:51]}")
    def check_agreement_message_terms_of_service(self):
        self.element_is_visible(self.locator.TERMS_OF_SERVICE).click()
        url = self.driver.current_url
        return url

    @allure.step(f"Проверка перехода по ссылке: '{message.AGREEMENT_MSG[54:83]}'")
    def check_agreement_message_policy_service(self):
        self.element_is_visible(self.locator.POLICY_SERVICE).click()
        url = self.driver.current_url
        return url
