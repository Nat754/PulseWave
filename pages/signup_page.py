import imaplib
from selenium.webdriver import Keys
from data import password0
from locators.signup_locators import SignUpLocators
from pages.base_page import BasePage
import allure
from tests.test_signup_page.constant import SignUpConstants
from tests.constant import Messages, Links


class SignUpPage(BasePage):
    signup = SignUpConstants()
    locator = SignUpLocators()
    message = Messages()
    const = Links()

    @staticmethod
    def get_confirm_signup_to_email(e_mail, passwrd):
        with allure.step('Получить ссылку подтверждения регистрации пользователя на емайл'):
            mail = imaplib.IMAP4_SSL('imap.mail.ru')
            mail.login(e_mail, passwrd)
            mail.select('INBOX')
            result, data_id = mail.search(None, 'ALL')
            message_ids = data_id[0].split()
            result, data_id = mail.fetch(message_ids[-1], '(RFC822)')
            raw_email = str(data_id[0][1])
            mail.logout()
            first = raw_email.find(Links.MAIN_PAGE)
            end = raw_email[first:].find('"')
            link = raw_email[first:first + end]
            return link

    @allure.step(f"Проверка видимости заголовка {signup.TEXT_SIGNUP}")
    def get_title_login(self):
        return self.element_is_visible(self.locator.TITLE_SIGNUP)

    @allure.step("Проверка видимости кнопки 'Принимаю все' в сообщении о принятии файлов cookie")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self.locator.ALLOW_ALL_COOKIES)

    @allure.step(f"Видимость подсказки: '{message.INVALID_PASSWORD_MSG}'")
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

    def put_data_to_email_field(self, data_email):
        """Put data to email field"""
        return self.element_is_visible(self.locator.EMAIL_FIELD).send_keys(data_email)

    def put_data_to_password_field(self, data_password):
        """Put data to password field"""
        return self.element_is_visible(self.locator.PASSWORD_FIELD).send_keys(data_password)

    def put_data_to_confirm_password_field(self, data_confirm_password):
        """Put data to confirm password field"""
        return self.element_is_visible(self.locator.CONFIRM_PASSWORD_FIELD).send_keys(data_confirm_password)

    @allure.step(f"Подтвердить изменения'")
    def click_button_submit(self):
        return self.element_is_visible(self.locator.SUBMIT_BUTTON).click()

    @allure.step("Проверка сообщения")
    def get_error_message(self):
        return self.element_is_visible(self.locator.WEAK_PASSWORD)

    @allure.step("Получено сообщения о подтверждении регистрации")
    def get_send_invite_message(self):
        return self.element_is_visible(self.locator.SEND_INVITE_EMAIL)

    @allure.step("Нажать на иконку аватара")
    def click_button_avatar(self):
        element = self.element_is_present(self.locator.BUTTON_AVATAR)
        self.action_move_to_element(element)
        self.element_is_clickable(self.locator.BUTTON_AVATAR).click()

    @allure.step("Перейти в настройки")
    def click_button_settings(self):
        return self.element_is_visible(self.locator.PROFILE_SETTINGS).click()

    @allure.step("Нажать ссылку 'Удалить профиль'")
    def click_delete_profile(self):
        return self.element_is_visible(self.locator.DELETE_PROFILE).click()

    @allure.step("Ввести пароль для подтверждения удаления профиля")
    def send_field_email(self):
        self.go_to_element(self.element_is_present(self.locator.CONFIRM_PASSWORD))
        self.element_is_visible(self.locator.CONFIRM_PASSWORD).send_keys(password0)
        self.element_is_visible(self.locator.CONFIRM_PASSWORD).send_keys(Keys.ENTER)

    @allure.step("Удалить учетную запись")
    def delete_user_profile(self):
        return self.element_is_clickable(self.locator.DELETE_BUTTON).click()

    @allure.step("Получено сообщение об успешном удалении пользователя")
    def delete_user_profile_confirmation(self):
        return self.element_is_present(self.locator.DELETE_MESSAGE).text

    @allure.step(f"Проверка неактивности кнопки '{signup.TEXT_SIGNUP}'")
    def button_registration_not_active(self):
        return self.element_is_not_clickable(self.locator.SUBMIT_BUTTON)

    @allure.step("Нажать ссылку 'Выйти'")
    def click_exit_button(self):
        self.element_is_clickable(self.locator.AVATAR_LOGOUT).click()

    @allure.step("Получить сообщение")
    def get_message_to_exit(self):
        return self.element_is_visible(self.locator.LOGOUT_MSG).text
