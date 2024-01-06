import time
import allure
import pytest
from pages.base_page import BasePage
from data import *
from tests.constant import Constant, Messages
from tests.test_signup_page.constant import SignUpConstants
from pages.signup_page import get_confirm_signup_to_email


@allure.epic(f"Тестирование страницы '{SignUpConstants.TEXT_SIGNUP}'")
class TestSignupPage:
    const = Constant
    signup = SignUpConstants
    msg = Messages
    base = BasePage

    @allure.title(f"Проверка текста заголовка '{signup.TEXT_SIGNUP}'")
    @pytest.mark.regress
    def test_get_title_signup(self, signup_page_open):
        title = signup_page_open.get_title_login().text
        assert title == self.signup.SIGNUP_PAGE_TITLE, f'Неверный заголовок "{title}"'

    @pytest.mark.parametrize('css_property, figma, name', signup.CHECK_TITLE)
    @pytest.mark.regress
    def test_get_css_property_title_signup(self, signup_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} заголовка '{self.signup.TEXT_SIGNUP}'")
        element = signup_page_open.get_title_login()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} заголовка '{self.signup.TEXT_SIGNUP}' макету"

    @allure.title(f"Окно регистрации сообщение '{msg.PASSWORD_RULES_MSG}'")
    @pytest.mark.smoke
    def test_signup_message_password_rules(self, signup_page_open):
        element = signup_page_open.check_password_rules_message()
        with (allure.step(f'Проверить текст сообщения: "{self.msg.PASSWORD_RULES_MSG}"')):
            assert element.text == self.msg.PASSWORD_RULES_MSG, \
                f'Нет сообщения: "{self.msg.PASSWORD_RULES_MSG}"'
        with allure.step(f'Проверить цвет шрифта сообщения: "{self.msg.PASSWORD_RULES_MSG}"'):
            assert element.value_of_css_property('color') == self.signup.PASSWORD_RULES_CSS['color'], \
                'Цвет сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить размер шрифта сообщения: "{self.msg.PASSWORD_RULES_MSG}"'):
            assert element.value_of_css_property('font-size') == self.signup.PASSWORD_RULES_CSS['font-size'], \
                'Размер шрифта сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить шрифт сообщения: "{self.msg.PASSWORD_RULES_MSG}"'):
            assert element.value_of_css_property('font-family') == self.signup.PASSWORD_RULES_CSS['font-family'], \
                'Шрифт сообщения о неверном пароле не соответствует макету'

    @allure.title(f"Окно регистрации сообщение '{msg.PULSEWAVE_POLICY_MSG}'")
    @pytest.mark.smoke
    def test_signup_message_pulsewave_policy(self, signup_page_open):
        element = signup_page_open.check_pulsewave_policy_message()
        with (allure.step(f'Проверить текст сообщения: "{self.msg.PULSEWAVE_POLICY_MSG}"')):
            assert element.text == self.msg.PULSEWAVE_POLICY_MSG, \
                f'Нет сообщения: "{self.msg.PULSEWAVE_POLICY_MSG}"'
        with allure.step(f'Проверить цвет шрифта сообщения: "{self.msg.PULSEWAVE_POLICY_MSG}"'):
            assert element.value_of_css_property('color') == self.signup.PULSEWAVE_POLICY_CSS['color'], \
                'Цвет сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить размер шрифта сообщения: "{self.msg.PULSEWAVE_POLICY_MSG}"'):
            assert element.value_of_css_property('font-size') == self.signup.PULSEWAVE_POLICY_CSS['font-size'], \
                'Размер шрифта сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить шрифт сообщения: "{self.msg.PULSEWAVE_POLICY_MSG}"'):
            assert element.value_of_css_property('font-family') == self.signup.PULSEWAVE_POLICY_CSS['font-family'], \
                'Шрифт сообщения о неверном пароле не соответствует макету'

    @allure.title(f"Окно регистрации сообщение '{msg.AGREEMENT_MSG}'")
    @pytest.mark.smoke
    def test_signup_message_agreement(self, signup_page_open):
        element = signup_page_open.check_agreement_message()
        with allure.step(f'Проверить текст сообщения: "{self.msg.AGREEMENT_MSG}"'):
            assert element.text == self.msg.AGREEMENT_MSG, f'Нет сообщения: "{self.msg.AGREEMENT_MSG}"'
        with allure.step(f'Проверить цвет шрифта сообщения: "{self.msg.AGREEMENT_MSG}"'):
            assert element.value_of_css_property('color') == self.signup.AGREEMENT_CSS['color'], \
                'Цвет сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить размер шрифта сообщения: "{self.msg.AGREEMENT_MSG}"'):
            assert element.value_of_css_property('font-size') == self.signup.AGREEMENT_CSS['font-size'], \
                'Размер шрифта сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить шрифт сообщения: "{self.msg.AGREEMENT_MSG}"'):
            assert element.value_of_css_property('font-family') == self.signup.AGREEMENT_CSS['font-family'], \
                'Шрифт сообщения о неверном пароле не соответствует макету'

    @allure.title(f"Окно регистрации сообщение '{msg.AGREEMENT_MSG}', проверка корректности перехода по ссылке "
                  f"'{msg.AGREEMENT_MSG[30:51]}'")
    @pytest.mark.smoke
    def test_check_redirect_to_terms_of_service(self, signup_page_open):
        signup_page_open.check_agreement_message()
        url = signup_page_open.check_agreement_message_terms_of_service()
        assert url == self.const.TERMS_OF_SERVICE, f'Нет перехода на: "{self.const.TERMS_OF_SERVICE}"'

    @allure.title(f"Окно регистрации сообщение '{msg.AGREEMENT_MSG}' проверка корректности перехода по ссылке "
                  f"'{msg.AGREEMENT_MSG[54:83]}'")
    @pytest.mark.smoke
    def test_check_redirect_to_policy_service(self, signup_page_open):
        signup_page_open.check_agreement_message()
        url = signup_page_open.check_agreement_message_policy_service()
        assert url == self.const.PULSEWAVE_PRIVACY, f'Нет перехода на: "{self.const.PULSEWAVE_PRIVACY}"'

    @pytest.mark.parametrize('data_password', signup.WEAK_PASSWORD)
    @allure.title("Регистрация с корректным email и слабым паролем и подтверждением пароля")
    @pytest.mark.smoke
    def test_signup_with_weak_password(self, signup_page_open, data_password):
        with allure.step('Заполнить поле email корректными данными'):
            signup_page_open.put_data_to_email_field(email1)
        with allure.step('Заполнить поле пароль слабым паролем'):
            signup_page_open.put_data_to_password_field(data_password)
        with allure.step('Заполнить поле подтверждение пароля слабым паролем'):
            signup_page_open.put_data_to_confirm_password_field(data_password)
        signup_page_open.click_button_registration()
        element = signup_page_open.get_error_message()
        with allure.step(f'Получено сообщение об ошибке: "{self.msg.INVALID_PASSWORD_MSG}"'):
            assert element.text == self.msg.INVALID_PASSWORD_MSG, 'Нет сообщения о слабом пароле'

    @pytest.mark.parametrize('data_email', signup.INCORRECT_EMAIL)
    @allure.title("Регистрация с некорректным email и сильным паролем и подтверждением пароля")
    @pytest.mark.smoke
    def test_signup_with_incorrect_email_and_strong_password(self, signup_page_open, data_email):
        with allure.step('Заполнить поле email некорректными данными'):
            signup_page_open.put_data_to_email_field(data_email)
        with allure.step('Заполнить поле пароль сильным паролем'):
            signup_page_open.put_data_to_password_field(password0)
        with allure.step('Заполнить поле подтверждение пароля сильным паролем'):
            signup_page_open.put_data_to_confirm_password_field(password0)
        signup_page_open.click_button_registration()
        element = signup_page_open.get_error_message()
        with allure.step(f'Получено сообщение об ошибке: "{self.msg.INVALID_EMAIL_MSG}"'):
            assert element.text == self.msg.INVALID_EMAIL_MSG, 'Нет сообщения об ошибке'

    @allure.title("Регистрация с корректным email и не совпадающими паролем и подтверждением пароля")
    @pytest.mark.smoke
    def test_signup_with_correct_email_and_passwords_not_equal(self, signup_page_open):
        with allure.step('Заполнить поле email корректными данными'):
            signup_page_open.put_data_to_email_field(email1)
        with allure.step('Заполнить поле пароль сильным паролем'):
            signup_page_open.put_data_to_password_field(password0)
        with allure.step('Заполнить поле подтверждение пароля паролем отличным от предыдущего шага'):
            signup_page_open.put_data_to_confirm_password_field(password3)
        signup_page_open.click_button_registration()
        element = signup_page_open.get_error_message()
        with allure.step(f'Получено сообщение об ошибке: "{self.msg.PASSWORDS_NOT_EQUAL_MSG}"'):
            assert element.text == self.msg.PASSWORDS_NOT_EQUAL_MSG, 'Нет сообщения об ошибке'

    @allure.title("Регистрация с корректными email и паролем без согласия на подписку")
    @pytest.mark.smoke
    def test_signup_with_correct_email_and_password(self, signup_page_open, driver):
        with allure.step('Заполнить поле email корректными данными'):
            signup_page_open.put_data_to_email_field(email1)
        with allure.step('Заполнить поле пароль сильным паролем'):
            signup_page_open.put_data_to_password_field(password0)
        with allure.step('Заполнить поле подтверждение пароля сильным паролем'):
            signup_page_open.put_data_to_confirm_password_field(password0)
        signup_page_open.click_button_registration()
        element = signup_page_open.get_send_invite_message()
        with allure.step(f'Получено сообщение необходимости подтвердить регистрацию: "{self.signup.INVITE_MSG}"'):
            assert element.text == self.signup.INVITE_MSG, 'Нет сообщения успеха'
        time.sleep(2)
        link = get_confirm_signup_to_email(email1, password1)
        driver.get(link)
        signup_page_open.get_welcome_to_workspace_message()
        signup_page_open.click_button_avatar()
        signup_page_open.click_button_settings()
        signup_page_open.click_delete_profile()
        signup_page_open.send_field_email()
        text = signup_page_open.delete_user_profile_confirmation().text
        assert text == self.signup.DELETE_USER_MSG, "Пользователь не удален"

    @allure.title("Регистрация с корректными email и паролем и с согласием на подписку")
    @pytest.mark.smoke
    def test_signup_with_correct_data_and_agree(self, signup_page_open, driver):
        with allure.step('Заполнить поле email корректными данными'):
            signup_page_open.put_data_to_email_field(email1)
        with allure.step('Заполнить поле пароль сильным паролем'):
            signup_page_open.put_data_to_password_field(password0)
        with allure.step('Заполнить поле подтверждение пароля сильным паролем'):
            signup_page_open.put_data_to_confirm_password_field(password0)
        signup_page_open.check_pulsewave_policy_message().click()
        signup_page_open.click_button_registration()
        element = signup_page_open.get_send_invite_message()
        with allure.step(f'Получено сообщение необходимости подтвердить регистрацию: "{self.signup.INVITE_MSG}"'):
            assert element.text == self.signup.INVITE_MSG, 'Нет сообщения успеха'
        time.sleep(2)
        link = get_confirm_signup_to_email(email1, password1)
        driver.get(link)
        signup_page_open.get_welcome_to_workspace_message()
        signup_page_open.click_button_avatar()
        signup_page_open.click_button_settings()
        signup_page_open.click_delete_profile()
        signup_page_open.send_field_email()
        text = signup_page_open.delete_user_profile_confirmation().text
        assert text == self.signup.DELETE_USER_MSG, "Пользователь не удален"

    @allure.title("Регистрация с корректным email и паролем и пустым подтверждением пароля")
    @pytest.mark.smoke
    def test_signup_with_correct_email_and_password_without_confirm_password(self, signup_page_open):
        with allure.step('Заполнить поле email корректными данными'):
            signup_page_open.put_data_to_email_field(email1)
        with allure.step('Заполнить поле пароль сильным паролем'):
            signup_page_open.put_data_to_password_field(password0)
        with allure.step('Оставить поле подтверждение пароля пустым'):
            signup_page_open.put_data_to_confirm_password_field("")
        assert signup_page_open.button_registration_not_active(), \
            'Нет проверки на заполнение обязательного поля подтверждение пароля'

    @allure.title("Регистрация с корректным email и подтверждением пароля и пустым паролем")
    @pytest.mark.smoke
    def test_signup_with_correct_email_and_confirm_password_without_password(self, signup_page_open):
        with allure.step('Заполнить поле email корректными данными'):
            signup_page_open.put_data_to_email_field(email1)
        with allure.step('Оставить поле пароль пустым'):
            signup_page_open.put_data_to_password_field("")
        with allure.step('Заполнить поле подтверждение пароля сильным паролем'):
            signup_page_open.put_data_to_confirm_password_field(password0)
        assert signup_page_open.button_registration_not_active(), \
            'Нет проверки на заполнение обязательного поля пароль'

    @allure.title("Регистрация с пустым email и сильным паролем и подтверждением пароля")
    @pytest.mark.smoke
    def test_signup_without_email_and_strong_passwords(self, signup_page_open):
        with allure.step('Оставить поле email пустым'):
            signup_page_open.put_data_to_email_field('')
        with allure.step('Заполнить поле пароль сильным паролем'):
            signup_page_open.put_data_to_password_field(password0)
        with allure.step('Заполнить поле подтверждение пароля сильным паролем'):
            signup_page_open.put_data_to_confirm_password_field(password0)
        assert signup_page_open.button_registration_not_active(), \
            'Нет проверки на заполнение обязательного поля пароль'
