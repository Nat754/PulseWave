import allure
import pytest

from tests.constant import Constant
from tests.test_signup_page.constant import SignUpConstants


@allure.epic("Тестирование страницы авторизации")
class TestSignupPage:
    const = Constant()
    signup = SignUpConstants()

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
