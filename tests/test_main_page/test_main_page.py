import allure
import pytest
from tests.constant import Links
from tests.test_main_page.constant import MainConstant


@pytest.mark.parametrize('browser', Links.SET_OF_BROWSERS)
@allure.epic("Тестирование Главной страницы")
class TestMainPage:
    main = MainConstant()
    const = Links()

    @allure.title(f"1.1 Проверка перехода на страницу {const.SIGNUP_PAGE} по кнопке '{main.TEXT_SIGNUP}'")
    @pytest.mark.smoke
    def test_get_body_auth_signup(self, main_page_open, driver):
        main_page_open.get_body_auth_signup().click()
        assert driver.current_url == self.const.SIGNUP_PAGE, f"Произошел переход на страницу '{driver.current_url}'"

    @pytest.mark.parametrize('css_property, figma, name', main.CHECK_TITLE)
    @pytest.mark.regress
    def test_get_body_main_title_size(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} элемента '{self.main.MAIN_TITLE}'")
        element = main_page_open.get_body_main_title()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} кнопки '{self.main.MAIN_TITLE}' макету"

    @pytest.mark.parametrize('css_property, figma, name', main.CHECK_BUTTON)
    @pytest.mark.regress
    def test_get_css_property_body_auth_signup(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} кнопки '{self.main.TEXT_SIGNUP}'")
        element = main_page_open.get_body_auth_signup()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} кнопки '{self.main.TEXT_SIGNUP}' макету"

    @pytest.mark.parametrize('css_property, figma, name', main.CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_body_useful_interface(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} элемента '{self.main.USEFUL_INTERFACE}' в футере")
        element = main_page_open.get_body_useful_interface()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, \
            f"Не прошла проверка соответствия {name} элемента '{self.main.USEFUL_INTERFACE}' макету"

    @pytest.mark.parametrize('css_property, figma, name', main.CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_body_all_time(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} элемента '{self.main.ALL_TIME}' в футере")
        element = main_page_open.get_body_all_time()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} элемента '{self.main.ALL_TIME}' макету"

    @pytest.mark.parametrize('css_property, figma, name', main.CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_body_first_safety(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} элемента '{self.main.FIRST_SAFETY}' в футере")
        element = main_page_open.get_body_first_safety()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} элемента '{self.main.FIRST_SAFETY}' макету"

    @pytest.mark.parametrize('css_property, figma, name', main.CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_body_main_descr(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} элемента '{self.main.FULL_FUNCTIONALITY}' в футере")
        element = main_page_open.get_body_main_descr()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, \
            f"Не прошла проверка соответствия {name} элемента '{self.main.FULL_FUNCTIONALITY}' макету"

    @pytest.mark.parametrize('css_property, figma, name', main.CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_body_main_subtitle(self, main_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} элемента '{self.main.ONE_APP}' в футере")
        element = main_page_open.get_body_main_subtitle()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} элемента '{self.main.ONE_APP}' макету"

    @allure.title(f"Проверка текста кнопки '{main.TEXT_SIGNUP}'")
    @pytest.mark.regress
    def test_get_text_body_auth_signup(self, main_page_open):
        text = main_page_open.get_body_auth_signup().text
        assert text == self.main.TEXT_SIGNUP, f"Текст кнопки '{self.main.TEXT_SIGNUP}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{main.MAIN_TITLE}'")
    @pytest.mark.regress
    def test_get_text_body_main_title(self, main_page_open):
        text = main_page_open.get_body_main_title().text
        assert text == self.main.MAIN_TITLE, f"Текст элемента '{self.main.MAIN_TITLE}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{main.USEFUL_INTERFACE}'")
    @pytest.mark.regress
    def test_get_text_body_useful_interface(self, main_page_open):
        text = main_page_open.get_body_useful_interface().text
        assert text == self.main.USEFUL_INTERFACE, \
            f"Текст элемента '{self.main.USEFUL_INTERFACE}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{main.ALL_TIME}'")
    @pytest.mark.regress
    def test_get_text_body_all_time(self, main_page_open):
        text = main_page_open.get_body_all_time().text
        assert text == self.main.ALL_TIME, f"Текст элемента '{self.main.ALL_TIME}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{main.FIRST_SAFETY}'")
    @pytest.mark.regress
    def test_get_text_body_first_safety(self, main_page_open):
        text = main_page_open.get_body_first_safety().text
        assert text == self.main.FIRST_SAFETY, f"Текст элемента '{self.main.FIRST_SAFETY}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{main.FULL_FUNCTIONALITY}'")
    @pytest.mark.regress
    def test_get_text_body_main_descr(self, main_page_open):
        text = main_page_open.get_body_main_descr().text
        assert text == self.main.FULL_FUNCTIONALITY, \
            f"Текст элемента '{self.main.FULL_FUNCTIONALITY}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{main.ONE_APP}'")
    @pytest.mark.regress
    def test_get_text_body_main_subtitle(self, main_page_open):
        text = main_page_open.get_body_main_subtitle().text
        assert text == self.main.ONE_APP, f"Текст элемента '{self.main.ONE_APP}' не соответствует макету"
