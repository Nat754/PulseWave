import allure
import pytest
from pages.main_page import MainPage
from tests.constant import (MAIN_PAGE_HOME, LOGIN_PAGE, SIGNUP_PAGE, TEXT_SIGNUP, TEXT_LOGIN, TEXT_SIGNUP_HEADER,
                            BUTTON_COLOR, TERMS_OF_SERVICE, LICENSE_TITLE, LICENSE_LINK, EMAIL_TEXT, YEAR_COOPERATION,
                            MAIN_TITLE, COOKIES_TEXT, COOKIES, COOKIES_BUTTON, MAIN_PAGE_URL, ALL_TIME, FIRST_SAFETY,
                            USEFUL_INTERFACE)


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
    def test_get_futer_email(self, main_page_open):
        text = main_page_open.get_futer_email().text
        assert text == EMAIL_TEXT, f"email адрес {text} неверный"
        main_page_open.get_futer_email().click()

    @allure.title(f"Проверка года © PulseWave, {YEAR_COOPERATION} в хедере")
    @pytest.mark.smoke
    def test_get_year_cooperation(self, main_page_open, driver):
        year = int(main_page_open.get_futer_cooperation().text[-4:])
        assert year == YEAR_COOPERATION, f"Пора поменять год {year}, уже {YEAR_COOPERATION}"

    @allure.title("Проверка текста 'PULSEWAVE' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_title(self, main_page_open, driver):
        title = main_page_open.get_body_main_title().text
        assert title == MAIN_TITLE, "Неверный текст"

    @allure.title("Проверка попапа о принятии файлов cookie")
    @pytest.mark.smoke
    def test_get_all_cookies(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_URL)
        text = main_page.get_cookies_text().text
        assert text == COOKIES_TEXT, f"Неверный текст '{text}'"
        button_text = main_page.get_allow_all_cookies().text
        assert button_text == COOKIES_BUTTON, f"Неверный текст '{button_text}'"
        main_page.get_cookies_link().click()
        link = driver.current_url
        assert link == COOKIES, f"Неверный url '{link}'"

    @allure.title(f"Проверка текста '{USEFUL_INTERFACE}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_useful_interface(self, main_page_open, driver):
        text = main_page_open.get_body_useful_interface().text
        assert text == USEFUL_INTERFACE, "Неверный текст"

    @allure.title(f"Проверка текста '{ALL_TIME}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_all_time(self, main_page_open, driver):
        title = main_page_open.get_body_all_time().text
        assert title == ALL_TIME, "Неверный текст"

    @allure.title(f"Проверка текста '{FIRST_SAFETY}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_first_safety(self, main_page_open, driver):
        title = main_page_open.get_body_first_safety().text
        assert title == FIRST_SAFETY, "Неверный текст"
