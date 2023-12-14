import time
import allure
import pytest
from tests.constant import Constant, Messages
from tests.test_login_page.login_constant import LoginConstant


@allure.epic(f"Тестирование страницы {LoginConstant.TEXT_LOGIN}")
class TestLoginPage:
    const = Constant
    login = LoginConstant
    message = Messages

    @allure.title(f"Проверка текста заголовка '{login.TEXT_LOGIN}'")
    @pytest.mark.regress
    def test_get_title_login(self, login_page_open):
        title = login_page_open.get_title_login().text
        assert title == self.login.LOGIN_PAGE_TITLE, f'Неверный заголовок "{title}"'

    @pytest.mark.parametrize('css_property, figma, name', login.CHECK_TITLE)
    @pytest.mark.regress
    def test_get_css_property(self, login_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} заголовка '{self.login.TEXT_LOGIN}'")
        element = login_page_open.get_title_login()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} заголовка '{self.login.TEXT_LOGIN}' макету"

    @allure.title("Проверка редиректа на главную страницу при клике на логотип")
    @pytest.mark.smoke
    def test_redirect_logo_login(self, login_page_open, driver):
        login_page_open.get_header_logo_login().click()
        assert driver.current_url == self.const.MAIN_PAGE_HOME, \
            'Не произошел переход на главную страницу при клике на лого'

    @allure.title("Авторизация с корректными данными")
    @pytest.mark.smoke
    def test_login(self, login_page_open, driver):
        login_page_open.input_e_mail()
        login_page_open.input_password()
        login_page_open.click_submit()
        time.sleep(3)
        assert driver.current_url == self.const.WORKSPACE, 'Не прошла авторизация с корректными данными'

    @allure.title("Авторизация с некорректным паролем")
    @pytest.mark.smoke
    def test_login_wrong_password(self, login_page_open):
        login_page_open.input_e_mail()
        login_page_open.input_wrong_password()
        login_page_open.click_submit()
        element = login_page_open.check_wrong_password_message()
        with allure.step(f'Проверить текст сообщения: "{self.message.WRONG_PASSWORD_MSG}"'):
            assert element, f'Нет сообщения: "{self.message.WRONG_PASSWORD_MSG}"'
        with allure.step(f'Проверить цвет шрифта сообщения: "{self.message.WRONG_PASSWORD_MSG}"'):
            assert element.value_of_css_property('color') == self.login.WRONG_PASSWORD_CSS['color'], \
                f'Цвет сообщения {self.message.WRONG_PASSWORD_MSG} не соответствует макету'
        with allure.step(f'Проверить размер шрифта сообщения: "{self.message.WRONG_PASSWORD_MSG}"'):
            assert element.value_of_css_property('font-size') == self.login.WRONG_PASSWORD_CSS['font-size'], \
                'Размер шрифта сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить шрифт сообщения: "{self.message.WRONG_PASSWORD_MSG}"'):
            assert element.value_of_css_property('font-family') == self.login.WRONG_PASSWORD_CSS['font-family'], \
                'Шрифт сообщения о неверном пароле не соответствует макету'

    @allure.title(f"Окно авторизации сообщение '{message.FORGOT_PASSWORD_MSG}'")
    @pytest.mark.smoke
    def test_login_message_forgot_password(self, login_page_open):
        element = login_page_open.check_forgot_password_message()
        with allure.step(f'Проверить текст сообщения: "{self.message.FORGOT_PASSWORD_MSG}"'):
            assert element, f'Нет сообщения: "{self.message.FORGOT_PASSWORD_MSG}"'
        with allure.step(f'Проверить цвет шрифта сообщения: "{self.message.FORGOT_PASSWORD_MSG}"'):
            assert element.value_of_css_property('color') == self.login.FORGOT_PASSWORD_CSS['color'], \
                'Цвет шрифта сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить размер шрифта сообщения: "{self.message.FORGOT_PASSWORD_MSG}"'):
            assert element.value_of_css_property('font-size') == self.login.FORGOT_PASSWORD_CSS['font-size'], \
                'Размер шрифта сообщения о неверном пароле не соответствует макету'
        with allure.step(f'Проверить шрифт сообщения: "{self.message.FORGOT_PASSWORD_MSG}"'):
            assert element.value_of_css_property('font-family') == self.login.FORGOT_PASSWORD_CSS['font-family'], \
                'Шрифт сообщения о неверном пароле не соответствует макету'
