import allure
import pytest
from tests.constant import (MAIN_PAGE_HOME, LOGIN_PAGE, SIGNUP_PAGE, TEXT_SIGNUP, TEXT_LOGIN, TEXT_SIGNUP_HEADER,
                            BUTTON_COLOR, TERMS_OF_SERVICE, LICENSE_TITLE, LICENSE_LINK, EMAIL_TEXT, YEAR_COOPERATION)


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
    def test_get_header_auth_login_link(self, main_page_open, driver):
        main_page_open.get_header_auth_login().click()
        assert driver.current_url == LOGIN_PAGE, f"Произошел переход на страницу {driver.current_url}"

    @allure.title("Проверка текста кнопки 'Войти' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_login_text(self, main_page_open):
        text = main_page_open.get_header_auth_login().text
        assert text == TEXT_LOGIN, f"Текст кнопки {text} не соответствует макету"

    @allure.title("Проверка цвета кнопки 'Войти' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_login_color(self, main_page_open):
        element = main_page_open.get_header_auth_login()
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки {TEXT_LOGIN} не соответствует макету"

    @allure.title("Проверка перехода на страницу регистрации по кнопке 'Регистрация' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_signup_link(self, main_page_open, driver):
        main_page_open.get_header_auth_signup().click()
        assert driver.current_url == SIGNUP_PAGE, f"Произошел переход на страницу {driver.current_url}"

    @allure.title("Проверка текста кнопки 'Регистрация' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_signup_text(self, main_page_open):
        text = main_page_open.get_header_auth_signup().text
        assert text == TEXT_SIGNUP_HEADER, f"Текст кнопки {text} не соответствует макету"

    @allure.title("Проверка цвета кнопки 'Регистрация' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_signup_color(self, main_page_open):
        element = main_page_open.get_header_auth_signup()
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки {TEXT_SIGNUP_HEADER} не соответствует макету"

    @allure.title("Проверка перехода на страницу регистрации по кнопке 'Зарегистрироваться' на странице")
    @pytest.mark.smoke
    def test_get_body_auth_signup_link(self, main_page_open, driver):
        main_page_open.get_body_auth_signup().click()
        assert driver.current_url == SIGNUP_PAGE, f"Произошел переход на страницу {driver.current_url}"

    @allure.title("Проверка текста кнопки 'Зарегистрироваться' в хедере")
    @pytest.mark.smoke
    def test_get_body_auth_signup_text(self, main_page_open):
        text = main_page_open.get_body_auth_signup().text
        assert text == TEXT_SIGNUP, f"Текст кнопки {text} не соответствует макету"

    @allure.title("Проверка цвета кнопки 'Зарегистрироваться' в хедере")
    @pytest.mark.smoke
    def test_get_body_auth_signup_color(self, main_page_open):
        element = main_page_open.get_body_auth_signup()
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки {TEXT_SIGNUP} не соответствует макету"

    @allure.title("Проверка перехода на страницу c лицензионным соглашением")
    @allure.step(title='Проверка: ')
    @pytest.mark.smoke
    def test_get_futer_link(self, main_page_open, driver):
        license_link = main_page_open.get_futer_license().text
        main_page_open.get_futer_license().click()
        title = main_page_open.get_license_title().text
        assert license_link == LICENSE_LINK, "Неверный текст ссылки 'Условия пользования"
        assert driver.current_url == TERMS_OF_SERVICE, f"Произошел переход на страницу {driver.current_url}"
        assert title == LICENSE_TITLE, f"ОР: {LICENSE_TITLE}, ФР: {title}"

    @allure.title("Проверка текста элемента 'pulsewave@gmail.com'в хедере")
    @pytest.mark.smoke
    def test_get_futer_email(self, main_page_open, driver):
        text = main_page_open.get_futer_email().text
        assert text == EMAIL_TEXT, f"email адрес {text} неверный"
        # main_page_open.get_futer_email().click()

    @allure.title(f"Проверка года © PulseWave, {YEAR_COOPERATION} в хедере")
    @pytest.mark.smoke
    def test_get_year_cooperation(self, main_page_open, driver):
        year = int(main_page_open.get_futer_cooperation().text[-4:])
        assert year == YEAR_COOPERATION, f"Пора поменять год {year}, уже {YEAR_COOPERATION}"
