import allure
import pytest

from tests.constant import MAIN_PAGE_HOME
from tests.test_signup_page.constant import SIGNUP_PAGE_TITLE, CHECK_TITLE, TEXT_SIGNUP


@allure.epic("Тестирование страницы авторизации")
class TestSignupPage:

    @allure.title(f"Проверка текста заголовка '{TEXT_SIGNUP}'")
    @pytest.mark.regress
    def test_get_title_signup(self, signup_page_open):
        title = signup_page_open.get_title_login().text
        assert title == SIGNUP_PAGE_TITLE, f'Неверный заголовок "{title}"'

    @pytest.mark.parametrize('css_property, figma, name', CHECK_TITLE)
    @pytest.mark.regress
    def test_get_css_property_title_signup(self, signup_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} заголовка '{TEXT_SIGNUP}'")
        element = signup_page_open.get_title_login()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} заголовка '{TEXT_SIGNUP}' макету"

    @allure.title("Проверка редиректа на главную страницу при клике на логотип")
    @pytest.mark.smoke
    def test_redirect_logo_signup(self, signup_page_open, driver):
        signup_page_open.get_header_logo_signup().click()
        assert driver.current_url == MAIN_PAGE_HOME, 'Не произошел переход на главную страницу при клике на лого'
