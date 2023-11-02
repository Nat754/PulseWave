import allure
import pytest
from pages.main_page import MainPage
from tests.constant import MAIN_PAGE_HOME, LOGIN_PAGE_URL, SIGNUP_PAGE, TEXT_SIGNUP, TEXT_LOGIN, TEXT_SIGNUP_HEADER, \
    BUTTON_COLOR, TERMS_OF_SERVICE, LICENSE_TITLE, LICENSE_LINK, EMAIL_TEXT, YEAR_COOPERATION, MAIN_TITLE, \
    COOKIES_TEXT, COOKIES, COOKIES_BUTTON, MAIN_PAGE_URL, ALL_TIME, FIRST_SAFETY, USEFUL_INTERFACE, EMAIL_TEXT_HOVER, \
    TEXT_SIZE, TEXT_COLOR, FULL_FUNCTIONALITY, ONE_APP, PULSEWAVE_SIZE, PULSEWAVE_COLOR, MAIN_PAGE_TITLE, \
    BUTTON_TEXT_SIZE, BUTTONS


@allure.epic("Тестирование Главной страницы")
class TestMainPage:

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

    @allure.title("Проверка некликабельности логотипа на главной странице")
    @pytest.mark.smoke
    def test_visibility_logo(self, main_page_open, driver):
        try:
            main_page_open.get_header_logo.click()
        except AttributeError:
            pass
        assert driver.current_url == MAIN_PAGE_HOME, 'Произошел переход на другую страницу при клике на лого'

    @allure.title("Проверка перехода на страницу c лицензионным соглашением")
    @pytest.mark.smoke
    def test_get_futer_link(self, main_page_open, driver):
        license_link = main_page_open.get_futer_license().text
        main_page_open.get_futer_license().click()
        title = main_page_open.get_license_title().text
        assert license_link == LICENSE_LINK, f"Неверный текст ссылки '{LICENSE_LINK}"
        assert driver.current_url == TERMS_OF_SERVICE, f"Произошел переход на страницу '{driver.current_url}'"
        assert title == LICENSE_TITLE, f"ОР: '{LICENSE_TITLE}', ФР: '{title}'"

    @allure.title(f"Проверка элемента '{EMAIL_TEXT}'в хедере")
    @pytest.mark.smoke
    def test_get_futer_email(self, main_page_open):
        text = main_page_open.get_futer_email().text
        assert text == EMAIL_TEXT, f"email адрес '{text}' неверный"
        element = main_page_open.get_futer_email_hover()
        link = element.get_attribute("href")
        assert link == EMAIL_TEXT_HOVER, f"Неверный вызов '{link}'"

    @allure.title(f"Проверка года © PulseWave, {YEAR_COOPERATION} в хедере")
    @pytest.mark.smoke
    def test_get_year_cooperation(self, main_page_open):
        year = int(main_page_open.get_futer_cooperation().text[-4:])
        assert year == YEAR_COOPERATION, f"Пора поменять год '{year}', уже '{YEAR_COOPERATION}'"

    @pytest.mark.parametrize('url, button', BUTTONS)
    @pytest.mark.smoke
    def test_get_button(self, main_page_open, driver, url, button):
        allure.dynamic.title(f"Проверка перехода на страницу {url} по кнопке '{button}' в хедере")
        if button == TEXT_LOGIN:
            main_page_open.get_header_auth_login().click()
        if button == TEXT_SIGNUP_HEADER:
            main_page_open.get_header_auth_signup().click()
        if button == TEXT_SIGNUP:
            main_page_open.get_body_auth_signup().click()
        assert driver.current_url == url, f"Произошел переход на страницу '{driver.current_url}'"


    # @allure.title(f"Проверка перехода на страницу {LOGIN_PAGE_URL} по кнопке '{TEXT_LOGIN}' в хедере")
    # @pytest.mark.smoke
    # def test_get_header_auth_login_link(self, main_page_open, driver):
    #     main_page_open.get_header_auth_login().click()
    #     assert driver.current_url == LOGIN_PAGE_URL, f"Произошел переход на страницу '{driver.current_url}'"
    #
    # @allure.title(f"Проверка перехода на страницу {SIGNUP_PAGE} по кнопке '{TEXT_SIGNUP_HEADER}' в хедере")
    # @pytest.mark.smoke
    # def test_get_header_auth_signup_link(self, main_page_open, driver):
    #     main_page_open.get_header_auth_signup().click()
    #     assert driver.current_url == SIGNUP_PAGE, f"Произошел переход на страницу '{driver.current_url}'"
    #
    # @allure.title(f"Проверка перехода на страницу {SIGNUP_PAGE} по кнопке '{TEXT_SIGNUP}' на странице")
    # @pytest.mark.smoke
    # def test_get_body_auth_signup_link(self, main_page_open, driver):
    #     main_page_open.get_body_auth_signup().click()
    #     assert driver.current_url == SIGNUP_PAGE, f"Произошел переход на страницу '{driver.current_url}'"

    @allure.title(f"Проверка текста кнопки '{TEXT_LOGIN}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_login_text(self, main_page_open):
        text = main_page_open.get_header_auth_login().text
        assert text == TEXT_LOGIN, f"Текст кнопки '{text}' не соответствует макету"

    @allure.title(f"Проверка текста кнопки '{TEXT_SIGNUP_HEADER}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_signup_text(self, main_page_open):
        text = main_page_open.get_header_auth_signup().text
        assert text == TEXT_SIGNUP_HEADER, f"Текст кнопки '{text}' не соответствует макету"

    @allure.title(f"Проверка текста кнопки '{TEXT_SIGNUP}' в хедере")
    @pytest.mark.smoke
    def test_get_body_auth_signup_text(self, main_page_open):
        text = main_page_open.get_body_auth_signup().text
        assert text == TEXT_SIGNUP, f"Текст кнопки '{text}' не соответствует макету"

    @allure.title(f"Проверка цвета кнопки '{TEXT_LOGIN}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_login_color(self, main_page_open):
        element = main_page_open.get_header_auth_login()
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки '{TEXT_LOGIN}' не соответствует макету"

    @allure.title(f"Проверка цвета кнопки '{TEXT_SIGNUP_HEADER}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_signup_color(self, main_page_open):
        element = main_page_open.get_header_auth_signup()
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки '{TEXT_SIGNUP_HEADER}' не соответствует макету"

    @allure.title(f"Проверка цвета кнопки '{TEXT_SIGNUP}' в хедере")
    @pytest.mark.smoke
    def test_get_body_auth_signup_color(self, main_page_open):
        element = main_page_open.get_body_auth_signup()
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки '{TEXT_SIGNUP}' не соответствует макету"

    @allure.title(f"Проверка цвета текста кнопки '{TEXT_LOGIN}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_login_text_color(self, main_page_open):
        element = main_page_open.get_header_auth_login()
        color = element.value_of_css_property("color")
        assert color == PULSEWAVE_COLOR, f"Цвет текста кнопки '{TEXT_LOGIN}' не соответствует макету"

    @allure.title(f"Проверка цвета текста кнопки '{TEXT_SIGNUP_HEADER}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_signup_text_color(self, main_page_open):
        element = main_page_open.get_header_auth_signup()
        color = element.value_of_css_property("color")
        assert color == PULSEWAVE_COLOR, f"Цвет кнопки '{TEXT_SIGNUP_HEADER}' не соответствует макету"

    @allure.title(f"Проверка цвета текста кнопки '{TEXT_SIGNUP}' в хедере")
    @pytest.mark.smoke
    def test_get_body_auth_signup_text_color(self, main_page_open):
        element = main_page_open.get_body_auth_signup()
        color = element.value_of_css_property("color")
        assert color == PULSEWAVE_COLOR, f"Цвет текста кнопки '{TEXT_SIGNUP}' не соответствует макету"

    @allure.title(f"Проверка размера текста кнопки '{TEXT_LOGIN}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_login_text_size(self, main_page_open):
        element = main_page_open.get_header_auth_login()
        size = element.value_of_css_property("font-size")
        assert size == BUTTON_TEXT_SIZE, f"Размер текста кнопки '{TEXT_LOGIN}' не соответствует макету"

    @allure.title(f"Проверка размера текста кнопки '{TEXT_SIGNUP_HEADER}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_signup_text_size(self, main_page_open):
        element = main_page_open.get_header_auth_signup()
        size = element.value_of_css_property("font-size")
        assert size == BUTTON_TEXT_SIZE, f"Размер кнопки '{TEXT_SIGNUP_HEADER}' не соответствует макету"

    @allure.title(f"Проверка размера текста кнопки '{TEXT_SIGNUP}' в хедере")
    @pytest.mark.smoke
    def test_get_body_auth_signup_text_size(self, main_page_open):
        element = main_page_open.get_body_auth_signup()
        size = element.value_of_css_property("font-size")
        assert size == BUTTON_TEXT_SIZE, f"Размер текста кнопки '{TEXT_SIGNUP}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{MAIN_TITLE}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_title(self, main_page_open):
        title = main_page_open.get_body_main_title().text
        assert title == MAIN_TITLE, f"Текст '{title}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{USEFUL_INTERFACE}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_useful_interface(self, main_page_open):
        text = main_page_open.get_body_useful_interface().text
        assert text == USEFUL_INTERFACE, f"Текст '{text}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{ALL_TIME}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_all_time(self, main_page_open):
        title = main_page_open.get_body_all_time().text
        assert title == ALL_TIME, f"Текст '{title}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{FIRST_SAFETY}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_first_safety(self, main_page_open):
        title = main_page_open.get_body_first_safety().text
        assert title == FIRST_SAFETY, f"Текст '{title}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{FULL_FUNCTIONALITY}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_descr(self, main_page_open):
        title = main_page_open.get_body_main_descr().text
        assert title == FULL_FUNCTIONALITY, f"Текст элемента '{title}' не соответствует макету"

    @allure.title(f"Проверка текста элемента '{ONE_APP}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_subtitle(self, main_page_open):
        title = main_page_open.get_body_main_subtitle().text
        assert title == ONE_APP, f"Текст элемента '{title}' не соответствует макету"

    @allure.title(f"Проверка цвета элемента '{FIRST_SAFETY}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_first_safety_color(self, main_page_open):
        element = main_page_open.get_body_first_safety()
        color = element.value_of_css_property("color")
        assert color == TEXT_COLOR, f"Цвет текста элемента '{FIRST_SAFETY}' не соответствует макету"

    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @allure.title(f"Проверка цвета элемента '{ALL_TIME}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_first_all_time_color(self, main_page_open):
        element = main_page_open.get_body_all_time()
        color = element.value_of_css_property("color")
        assert color == TEXT_COLOR, f"Цвет текста элемента '{ALL_TIME}' не соответствует макету"

    @allure.title(f"Проверка цвета элемента '{USEFUL_INTERFACE}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_useful_interface_color(self, main_page_open):
        element = main_page_open.get_body_useful_interface()
        color = element.value_of_css_property("color")
        assert color == TEXT_COLOR, f"Цвет текста элемента '{USEFUL_INTERFACE}' не соответствует макету"

    @allure.title(f"Проверка цвета элемента '{FULL_FUNCTIONALITY}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_descr_color(self, main_page_open):
        element = main_page_open.get_body_main_descr()
        color = element.value_of_css_property("color")
        assert color == TEXT_COLOR, f"Цвет текста элемента '{FULL_FUNCTIONALITY}' не соответствует макету"

    @allure.title(f"Проверка цвета элемента '{ONE_APP}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_subtitle_color(self, main_page_open):
        element = main_page_open.get_body_main_subtitle()
        color = element.value_of_css_property("color")
        assert color == TEXT_COLOR, f"Цвет текста элемента '{ONE_APP}' не соответствует макету"

    @allure.title(f"Проверка цвета элемента '{MAIN_PAGE_TITLE}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_title_color(self, main_page_open):
        element = main_page_open.get_body_main_title()
        color = element.value_of_css_property("color")
        assert color == PULSEWAVE_COLOR, f"Цвет текста элемента '{MAIN_PAGE_TITLE}' не соответствует макету"

    @allure.title(f"Проверка цвета элемента '{LICENSE_LINK}' на Главной странице")
    @pytest.mark.xfail(reason="ОР 'rgba(16, 16, 18, 1)', ФР 'rgba(66, 66, 66, 1)'")
    @pytest.mark.smoke
    def test_get_futer_license_color(self, main_page_open):
        element = main_page_open.get_futer_license()
        color = element.value_of_css_property("color")
        assert color == TEXT_COLOR, f"Цвет текста элемента '{LICENSE_LINK}' не соответствует макету"

    @allure.title(f"Проверка цвета элемента '{EMAIL_TEXT}' на Главной странице")
    @pytest.mark.xfail(reason="ОР 'rgba(16, 16, 18, 1)', ФР 'rgba(66, 66, 66, 1)'")
    @pytest.mark.smoke
    def test_get_body_futer_email_color(self, main_page_open):
        element = main_page_open.get_futer_email()
        color = element.value_of_css_property("color")
        assert color == TEXT_COLOR, f"Цвет текста элемента '{EMAIL_TEXT}' не соответствует макету"

    @allure.title(f"Проверка цвета элемента '{YEAR_COOPERATION}' на Главной странице")
    @pytest.mark.xfail(reason="ОР 'rgba(16, 16, 18, 1)', ФР 'rgba(66, 66, 66, 1)'")
    @pytest.mark.smoke
    def test_get_futer_cooperation_color(self, main_page_open):
        element = main_page_open.get_futer_cooperation()
        color = element.value_of_css_property("color")
        assert color == TEXT_COLOR, f"Цвет текста элемента '{YEAR_COOPERATION}' не соответствует макету"

    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @allure.title(f"Проверка размера шрифта элемента '{FIRST_SAFETY}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_first_safety_size(self, main_page_open):
        element = main_page_open.get_body_first_safety()
        size = element.value_of_css_property("font-size")
        assert size == TEXT_SIZE, f"Размер шрифта элемента '{FIRST_SAFETY}' не соответствует макету"

    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @allure.title(f"Проверка размера шрифта элемента '{ALL_TIME}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_first_all_time_size(self, main_page_open):
        element = main_page_open.get_body_all_time()
        size = element.value_of_css_property("font-size")
        assert size == TEXT_SIZE, f"Размер шрифта элемента '{ALL_TIME}' не соответствует макету"

    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @allure.title(f"Проверка размера шрифта элемента '{USEFUL_INTERFACE}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_useful_interface_size(self, main_page_open):
        element = main_page_open.get_body_useful_interface()
        size = element.value_of_css_property("font-size")
        assert size == TEXT_SIZE, f"Размер шрифта элемента '{USEFUL_INTERFACE}' не соответствует макету"

    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @allure.title(f"Проверка размера шрифта элемента '{FULL_FUNCTIONALITY}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_descr_size(self, main_page_open):
        element = main_page_open.get_body_main_descr()
        size = element.value_of_css_property("font-size")
        assert size == TEXT_SIZE, f"Размер шрифта элемента '{FULL_FUNCTIONALITY}' не соответствует макету"

    @allure.title(f"Проверка размера шрифта элемента '{ONE_APP}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_subtitle_size(self, main_page_open):
        element = main_page_open.get_body_main_subtitle()
        size = element.value_of_css_property("font-size")
        assert size == TEXT_SIZE, f"Размер шрифта элемента '{ONE_APP}' не соответствует макету"

    @allure.title(f"Проверка размера шрифта элемента '{MAIN_PAGE_TITLE}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_title_size(self, main_page_open):
        element = main_page_open.get_body_main_title()
        size = element.value_of_css_property("font-size")
        assert size == PULSEWAVE_SIZE, f"Размер шрифта элемента '{MAIN_PAGE_TITLE}' не соответствует макету"

    @allure.title(f"Проверка размера шрифта элемента '{LICENSE_LINK}' на Главной странице")
    @pytest.mark.xfail(reason=f"ОР шрифт {TEXT_SIZE}, ФР шрифт 14")
    @pytest.mark.smoke
    def test_get_futer_license_size(self, main_page_open):
        element = main_page_open.get_futer_license()
        size = element.value_of_css_property("font-size")
        assert size == TEXT_SIZE, f"Размер шрифта элемента '{LICENSE_LINK}' не соответствует макету"

    @allure.title(f"Проверка размера шрифта элемента '{EMAIL_TEXT}' на Главной странице")
    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @pytest.mark.smoke
    def test_get_body_futer_email_size(self, main_page_open):
        element = main_page_open.get_futer_email()
        size = element.value_of_css_property("font-size")
        assert size == TEXT_SIZE, f"Размер шрифта элемента '{EMAIL_TEXT}' не соответствует макету"

    @allure.title(f"Проверка размера шрифта элемента '{YEAR_COOPERATION}' на Главной странице")
    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @pytest.mark.smoke
    def test_get_futer_cooperation_size(self, main_page_open):
        element = main_page_open.get_futer_cooperation()
        size = element.value_of_css_property("font-size")
        assert size == TEXT_SIZE, f"Размер шрифта элемента '{YEAR_COOPERATION}' не соответствует макету"
