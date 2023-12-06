import time
import allure
import pytest
from tests.constant import Constant
from tests.test_login_page.login_constant import LoginConstant


@allure.epic("Тестирование страницы авторизации")
class TestLoginPage:
    const = Constant()
    login = LoginConstant()

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
        time.sleep(1)
        assert driver.current_url == self.const.WORKSPACE, 'Не прошла авторизация с корректными данными'