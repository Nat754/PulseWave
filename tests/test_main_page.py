import allure
import pytest
from tests.constant import (MAIN_PAGE_HOME, LOGIN_PAGE, SIGNUP_PAGE, TEXT_SIGNUP, TEXT_LOGIN, TEXT_SIGNUP_HEADER,
                            BUTTON_COLOR)


@allure.epic("Main Page")
class TestMainPage:

    @allure.title("Проверка некликабельности логотипа на главной странице")
    @pytest.mark.smoke
    def test_visibility_logo(self, main_page_open, driver):
        try:
            main_page_open.get_header_logo.click()
        except AttributeError:
            pass
        assert driver.current_url == MAIN_PAGE_HOME, 'Произошел переход на другую страницу при клике на лого'

    @allure.title("Проверка перехода на страницу авторизации по кнопке 'Войти' в хедере")
    @pytest.mark.smoke
    def test_redirect_auth_login(self, main_page_open, driver):
        main_page_open.get_header_auth_login().click()
        assert driver.current_url == LOGIN_PAGE, f"Произошел переход на страницу {driver.current_url}"

    @allure.title(f"Проверка текста кнопки '{TEXT_LOGIN}' в хедере")
    @pytest.mark.smoke
    def test_get_auth_login_text(self, main_page_open, driver):
        text = main_page_open.get_header_auth_login().text
        assert text == TEXT_LOGIN, f"Текст кнопки {text} не соответствует макету"

    @allure.title(f"Проверка цвета кнопки '{TEXT_LOGIN}' в хедере")
    @pytest.mark.smoke
    def test_get_auth_login_color(self, main_page_open, driver):
        element = main_page_open.get_header_auth_login()
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки {TEXT_LOGIN} не соответствует макету"

    @allure.title("Проверка перехода на страницу регистрации по кнопке 'Регистрация' в хедере")
    @pytest.mark.smoke
    def test_get_auth_signup_link(self, main_page_open, driver):
        main_page_open.get_header_auth_signup().click()
        assert driver.current_url == SIGNUP_PAGE, f"Произошел переход на страницу {driver.current_url}"

    @allure.title(f"Проверка текста кнопки '{TEXT_SIGNUP_HEADER}' в хедере")
    @pytest.mark.smoke
    def test_get_auth_login_text(self, main_page_open, driver):
        text = main_page_open.get_header_auth_signup().text
        assert text == TEXT_SIGNUP_HEADER, f"Текст кнопки {text} не соответствует макету"

    @allure.title(f"Проверка цвета кнопки '{TEXT_SIGNUP_HEADER}' в хедере")
    @pytest.mark.smoke
    def test_get_auth_login_color(self, main_page_open, driver):
        element = main_page_open.get_header_auth_signup()
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки {TEXT_SIGNUP_HEADER} не соответствует макету"

    @allure.title("Проверка перехода на страницу регистрации по кнопке 'Регистрация' на странице")
    @pytest.mark.smoke
    def test_get_body_auth_signup_link(self, main_page_open, driver):
        main_page_open.get_body_auth_signup().click()
        assert driver.current_url == SIGNUP_PAGE, f"Произошел переход на страницу {driver.current_url}"

    @allure.title(f"Проверка текста кнопки '{TEXT_SIGNUP}' в хедере")
    @pytest.mark.smoke
    def test_get_body_auth_signup_text(self, main_page_open, driver):
        text = main_page_open.get_body_auth_signup().text
        assert text == TEXT_SIGNUP, f"Текст кнопки {text} не соответствует макету"

    @allure.title(f"Проверка цвета кнопки '{TEXT_SIGNUP}' в хедере")
    @pytest.mark.smoke
    def test_get_body_auth_signup_color(self, main_page_open, driver):
        element = main_page_open.get_body_auth_signup()
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки {TEXT_SIGNUP} не соответствует макету"
