import allure
import pytest
from data import email_auth, email2, password0
from tests.constant import Constant, Messages
from tests.test_login_page.login_constant import LoginConstant


@pytest.mark.parametrize('browser', Constant.SET_OF_BROWSERS)
@allure.epic(f"Тестирование страницы '{LoginConstant.TEXT_LOGIN}'")
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

    @allure.title(f"Проверка редиректа на страницу восстановления пароля при клике на ссылку "
                  f"\'{message.FORGOT_PASSWORD_MSG}'")
    @pytest.mark.smoke
    def test_redirect_password_recovery(self, login_page_open, driver):
        login_page_open.check_forgot_password_message().click()
        assert driver.current_url == self.const.PASSWORD_RECOVERY, \
            'Не произошел переход на страницу восстановления пароля'

    @allure.title("Авторизация с корректными данными")
    @pytest.mark.smoke
    def test_login(self, login_page_open, driver):
        with allure.step('Ввести в поле емайл корректные данные'):
            login_page_open.input_email(email_auth)
        with allure.step('Ввести в поле пароль корректные данные'):
            login_page_open.input_password(password0)
        login_page_open.click_submit()
        login_page_open.check_changed_url_login()
        assert driver.current_url == self.const.WORKSPACE, 'Не прошла авторизация с корректными данными'

    @allure.title("Авторизация с некорректным паролем")
    @pytest.mark.smoke
    def test_login_wrong_password(self, login_page_open):
        with allure.step('Ввести в поле емайл корректные данные'):
            login_page_open.input_email(email_auth)
        with allure.step('Ввести в поле пароль некорректные данные'):
            login_page_open.input_password('password')
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

    @allure.title("Авторизация с некорректным емайл")
    @pytest.mark.smoke
    def test_login_not_auth_email(self, login_page_open):
        with allure.step('Ввести в поле емайл некорректные данные'):
            login_page_open.input_email(email2)
        with allure.step('Ввести в поле пароль корректные данные'):
            login_page_open.input_password(password0)
        login_page_open.click_submit()
        element = login_page_open.check_wrong_password_message()
        with allure.step(f'Проверить текст сообщения: "{self.message.WRONG_PASSWORD_MSG}"'):
            assert element, f'Нет сообщения: "{self.message.WRONG_PASSWORD_MSG}"'

    @allure.title("Авторизация с пустым емайл")
    @pytest.mark.smoke
    def test_login_without_email(self, login_page_open):
        with allure.step('Оставить поле e-mail пустым'):
            login_page_open.input_email('')
        with allure.step('Ввести в поле пароль корректные данные'):
            login_page_open.input_password(password0)
        assert login_page_open.button_login_not_active(), 'Нет проверки на заполнение обязательного поля емайл'

    @allure.title("Авторизация с пустым паролем")
    @pytest.mark.smoke
    def test_login_without_password(self, login_page_open):
        with allure.step('Ввести в поле емайл корректные данные'):
            login_page_open.input_email(email_auth)
        login_page_open.input_password('')
        assert login_page_open.button_login_not_active(), 'Нет проверки на заполнение обязательного поля пароль'
