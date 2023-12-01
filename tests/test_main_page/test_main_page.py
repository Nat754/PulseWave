import allure
import pytest
from tests.constant import MAIN_PAGE_HOME, LOGIN_PAGE, SIGNUP_PAGE
from tests.test_main_page.constant import TEXT_SIGNUP, TEXT_LOGIN, TEXT_SIGNUP_HEADER, ALL_TIME, FIRST_SAFETY, \
    USEFUL_INTERFACE, FULL_FUNCTIONALITY, ONE_APP, CHECK_BUTTON, CHECK_TEXT, MAIN_TITLE, CHECK_TITLE


@allure.epic("Тестирование Главной страницы")
class TestMainPage:

    @allure.title("Проверка некликабельности логотипа на главной странице")
    @pytest.mark.smoke
    def test_visibility_logo(self, main_page_open, driver):
        try:
            with allure.step("Кликнуть на логотип на Главной странице"):
                main_page_open.get_header_logo.click()
        except AttributeError:
            with allure.step("Логотип некликабельный на Главной странице"):
                pass
        assert driver.current_url == MAIN_PAGE_HOME, 'Произошел переход на другую страницу при клике на лого'

    @allure.title(f"Проверка перехода на страницу '{LOGIN_PAGE}' по кнопке '{TEXT_LOGIN}'")
    @pytest.mark.smoke
    def test_get_header_auth_login(self, main_page_open, driver):
        main_page_open.get_header_auth_login().click()
        assert driver.current_url == LOGIN_PAGE, f"Произошел переход на страницу '{driver.current_url}'"

    @allure.title(f"Проверка перехода на страницу '{SIGNUP_PAGE}' по кнопке '{TEXT_SIGNUP_HEADER}'")
    @pytest.mark.smoke
    def test_get_header_auth_signup(self, main_page_open, driver):
        main_page_open.get_header_auth_signup().click()
        assert driver.current_url == SIGNUP_PAGE, f"Произошел переход на страницу '{driver.current_url}'"

    @allure.title(f"Проверка перехода на страницу {SIGNUP_PAGE} по кнопке '{TEXT_SIGNUP}'")
    @pytest.mark.smoke
    def test_get_body_auth_signup(self, main_page_open, driver):
        main_page_open.get_body_auth_signup().click()
        assert driver.current_url == SIGNUP_PAGE, f"Произошел переход на страницу '{driver.current_url}'"

    @pytest.mark.parametrize('css_property, figma, name', CHECK_TITLE)
    @pytest.mark.regress
    def test_get_body_main_title_size(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} элемента '{MAIN_TITLE}'")
        element = main_page_open.get_body_main_title()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} кнопки '{MAIN_TITLE}' макету"

    @pytest.mark.parametrize('css_property, figma, name', CHECK_BUTTON)
    @pytest.mark.regress
    def test_get_css_property_header_auth_login(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} кнопки '{TEXT_LOGIN}'")
        element = main_page_open.get_header_auth_login()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} кнопки '{TEXT_LOGIN}' макету"

    @pytest.mark.parametrize('css_property, figma, name', CHECK_BUTTON)
    @pytest.mark.regress
    def test_get_css_property_header_auth_signup(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} кнопки '{TEXT_SIGNUP_HEADER}'")
        element = main_page_open.get_header_auth_login()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} кнопки '{TEXT_SIGNUP_HEADER}' макету"

    @pytest.mark.parametrize('css_property, figma, name', CHECK_BUTTON)
    @pytest.mark.regress
    def test_get_css_property_body_auth_signup(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} кнопки '{TEXT_SIGNUP}'")
        element = main_page_open.get_body_auth_signup()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} кнопки '{TEXT_SIGNUP}' макету"

    @pytest.mark.parametrize('css_property, figma, name', CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_body_useful_interface(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} элемента '{USEFUL_INTERFACE}' в футере")
        element = main_page_open.get_body_useful_interface()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} элемента '{USEFUL_INTERFACE}' макету"

    @pytest.mark.parametrize('css_property, figma, name', CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_body_all_time(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} элемента '{ALL_TIME}' в футере")
        element = main_page_open.get_body_all_time()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} элемента '{ALL_TIME}' макету"

    @pytest.mark.parametrize('css_property, figma, name', CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_body_first_safety(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} элемента '{FIRST_SAFETY}' в футере")
        element = main_page_open.get_body_first_safety()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} элемента '{FIRST_SAFETY}' макету"

    @pytest.mark.parametrize('css_property, figma, name', CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_body_main_descr(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} элемента '{FULL_FUNCTIONALITY}' в футере")
        element = main_page_open.get_body_main_descr()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} элемента '{FULL_FUNCTIONALITY}' макету"

    @pytest.mark.parametrize('css_property, figma, name', CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_body_main_subtitle(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} элемента '{ONE_APP}' в футере")
        element = main_page_open.get_body_main_subtitle()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} элемента '{ONE_APP}' макету"

    @allure.title(f"Проверка текста кнопки '{TEXT_LOGIN}'")
    @pytest.mark.regress
    def test_get_text_header_auth_login(self, main_page_open):
        text = main_page_open.get_header_auth_login().text
        assert text == TEXT_LOGIN, f"Текст кнопки '{TEXT_LOGIN}' не соответствует макету"

    @allure.title(f"Проверка текста кнопки '{TEXT_SIGNUP_HEADER}'")
    @pytest.mark.regress
    def test_get_text_header_auth_signup(self, main_page_open):
        text = main_page_open.get_header_auth_signup().text
        assert text == TEXT_SIGNUP_HEADER, f"Текст кнопки '{TEXT_SIGNUP_HEADER}' не соответствует макету"

    @allure.title(f"Проверка текста кнопки '{TEXT_SIGNUP}'")
    @pytest.mark.regress
    def test_get_text_body_auth_signup(self, main_page_open):
        text = main_page_open.get_body_auth_signup().text
        assert text == TEXT_SIGNUP, f"Текст кнопки '{TEXT_SIGNUP}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{MAIN_TITLE}'")
    @pytest.mark.regress
    def test_get_text_body_main_title(self, main_page_open):
        text = main_page_open.get_body_main_title().text
        assert text == MAIN_TITLE, f"Текст элемента '{MAIN_TITLE}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{USEFUL_INTERFACE}'")
    @pytest.mark.regress
    def test_get_text_body_useful_interface(self, main_page_open):
        text = main_page_open.get_body_useful_interface().text
        assert text == USEFUL_INTERFACE, f"Текст элемента '{USEFUL_INTERFACE}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{ALL_TIME}'")
    @pytest.mark.regress
    def test_get_text_body_all_time(self, main_page_open):
        text = main_page_open.get_body_all_time().text
        assert text == ALL_TIME, f"Текст элемента '{ALL_TIME}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{FIRST_SAFETY}'")
    @pytest.mark.regress
    def test_get_text_body_first_safety(self, main_page_open):
        text = main_page_open.get_body_first_safety().text
        assert text == FIRST_SAFETY, f"Текст элемента '{FIRST_SAFETY}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{FULL_FUNCTIONALITY}'")
    @pytest.mark.regress
    def test_get_text_body_main_descr(self, main_page_open):
        text = main_page_open.get_body_main_descr().text
        assert text == FULL_FUNCTIONALITY, f"Текст элемента '{FULL_FUNCTIONALITY}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{ONE_APP}'")
    @pytest.mark.regress
    def test_get_text_body_main_subtitle(self, main_page_open):
        text = main_page_open.get_body_main_subtitle().text
        assert text == ONE_APP, f"Текст элемента '{ONE_APP}' не соответствует макету"
