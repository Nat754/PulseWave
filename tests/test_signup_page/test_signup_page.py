import allure
import pytest

from tests.constant import Constant, Messages
from tests.test_signup_page.constant import SignUpConstants


@allure.epic(f"Тестирование страницы '{SignUpConstants.TEXT_SIGNUP}'")
class TestSignupPage:
    const = Constant
    signup = SignUpConstants
    message = Messages

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

    @allure.title("Проверка редиректа на главную страницу при клике на логотип")
    @pytest.mark.smoke
    def test_redirect_logo_signup(self, signup_page_open, driver):
        signup_page_open.get_header_logo_signup().click()
        assert driver.current_url == self.const.MAIN_PAGE_HOME, \
            'Не произошел переход на главную страницу при клике на лого'

    @allure.title(f"Окно регистрации сообщение '{message.PASSWORD_RULES_MSG}'")
    @pytest.mark.smoke
    def test_signup_message_password_rules(self, signup_page_open):
        element = signup_page_open.check_password_rules_message()
        with allure.step(f'Проверить текст сообщения: "{self.message.PASSWORD_RULES_MSG}"'):
            assert element == self.message.PASSWORD_RULES_MSG, f'Нет сообщения: "{self.message.PASSWORD_RULES_MSG}"'
        with allure.step(f'Проверить цвет шрифта сообщения: "{self.message.PASSWORD_RULES_MSG}"'):
            assert element.value_of_css_property('color') == self.signup.PASSWORD_RULES_CSS['color'], \
                'Цвет сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить размер шрифта сообщения: "{self.message.PASSWORD_RULES_MSG}"'):
            assert element.value_of_css_property('font-size') == self.signup.PASSWORD_RULES_CSS['font-size'], \
                'Размер шрифта сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить шрифт сообщения: "{self.message.PASSWORD_RULES_MSG}"'):
            assert element.value_of_css_property('font-family') == self.signup.PASSWORD_RULES_CSS['font-family'], \
                'Шрифт сообщения о неверном пароле не соответствует макету'

    @allure.title(f"Окно регистрации сообщение '{message.PULSEWAVE_POLICY_MSG}'")
    @pytest.mark.smoke
    def test_signup_message_pulsewave_policy(self, signup_page_open):
        element = signup_page_open.check_pulsewave_policy_message()
        with allure.step(f'Проверить текст сообщения: "{self.message.PULSEWAVE_POLICY_MSG}"'):
            assert element == self.message.PULSEWAVE_POLICY_MSG, f'Нет сообщения: "{self.message.PULSEWAVE_POLICY_MSG}"'
        with allure.step(f'Проверить цвет шрифта сообщения: "{self.message.PULSEWAVE_POLICY_MSG}"'):
            assert element.value_of_css_property('color') == self.signup.PULSEWAVE_POLICY_CSS['color'], \
                'Цвет сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить размер шрифта сообщения: "{self.message.PULSEWAVE_POLICY_MSG}"'):
            assert element.value_of_css_property('font-size') == self.signup.PULSEWAVE_POLICY_CSS['font-size'], \
                'Размер шрифта сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить шрифт сообщения: "{self.message.PULSEWAVE_POLICY_MSG}"'):
            assert element.value_of_css_property('font-family') == self.signup.PULSEWAVE_POLICY_CSS['font-family'], \
                'Шрифт сообщения о неверном пароле не соответствует макету'

    @allure.title(f"Окно регистрации сообщение '{message.AGREEMENT_MSG}'")
    @pytest.mark.smoke
    def test_signup_message_agreement(self, signup_page_open):
        element = signup_page_open.check_agreement_message()
        with allure.step(f'Проверить текст сообщения: "{self.message.AGREEMENT_MSG}"'):
            assert element.text == self.message.AGREEMENT_MSG, f'Нет сообщения: "{self.message.AGREEMENT_MSG}"'
        with allure.step(f'Проверить цвет шрифта сообщения: "{self.message.AGREEMENT_MSG}"'):
            assert element.value_of_css_property('color') == self.signup.AGREEMENT_CSS['color'], \
                'Цвет сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить размер шрифта сообщения: "{self.message.AGREEMENT_MSG}"'):
            assert element.value_of_css_property('font-size') == self.signup.AGREEMENT_CSS['font-size'], \
                'Размер шрифта сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить шрифт сообщения: "{self.message.AGREEMENT_MSG}"'):
            assert element.value_of_css_property('font-family') == self.signup.AGREEMENT_CSS['font-family'], \
                'Шрифт сообщения о неверном пароле не соответствует макету'

    @allure.title(f"Окно регистрации сообщение '{message.AGREEMENT_MSG[30:51]}' проверка корректности перехода")
    @pytest.mark.smoke
    def test_check_redirect_to_terms_of_service(self, signup_page_open):
        signup_page_open.check_agreement_message()
        url = signup_page_open.check_agreement_message_terms_of_service()
        assert url == self.const.TERMS_OF_SERVICE, f'Нет перехода на: "{self.const.TERMS_OF_SERVICE}"'

    @allure.title(f"Окно регистрации сообщение '{message.AGREEMENT_MSG[54:83]}' проверка корректности перехода")
    @pytest.mark.smoke
    def test_check_redirect_to_policy_service(self, signup_page_open):
        signup_page_open.check_agreement_message()
        url = signup_page_open.check_agreement_message_policy_service()
        assert url == self.const.PULSEWAVE_PRIVACY, f'Нет перехода на: "{self.const.PULSEWAVE_PRIVACY}"'
