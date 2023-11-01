import allure
import pytest
from pages.main_page import MainPage
from tests.constant import (MAIN_PAGE_HOME, LOGIN_PAGE_URL, SIGNUP_PAGE, TEXT_SIGNUP, TEXT_LOGIN, TEXT_SIGNUP_HEADER,
                            BUTTON_COLOR, TERMS_OF_SERVICE, LICENSE_TITLE, LICENSE_LINK, EMAIL_TEXT, YEAR_COOPERATION,
                            MAIN_TITLE, COOKIES_TEXT, COOKIES, COOKIES_BUTTON, MAIN_PAGE_URL, ALL_TIME, FIRST_SAFETY,
                            USEFUL_INTERFACE, EMAIL_TEXT_HOVER, TEXT_SIZE, TEXT_COLOR, FULL_FUNCTIONALITY, ONE_APP,
                            PULSEWAVE_SIZE, PULSEWAVE_COLOR, MAIN_PAGE_TITLE)


@allure.epic("Тестирование Главной страницы")
class TestMainPage:

    @allure.title("Проверка некликабельности логотипа на главной странице")
    @pytest.mark.smoke
    def test_visibility_logo(self, main_page_open, driver):
        try:
            main_page_open.get_header_logo.click()
        except AttributeError:
            pass
        assert driver.current_url == MAIN_PAGE_HOME, 'Произошел переход на другую страницу при клике на лого'

    @allure.title(f"Проверка перехода на страницу авторизации по кнопке '{TEXT_LOGIN}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_login_link(self, main_page_open, driver):
        main_page_open.get_header_auth_login().click()
        assert driver.current_url == LOGIN_PAGE_URL, f"Произошел переход на страницу {driver.current_url}"

    @allure.title(f"Проверка текста кнопки '{TEXT_LOGIN}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_login_text(self, main_page_open):
        text = main_page_open.get_header_auth_login().text
        assert text == TEXT_LOGIN, f"Текст кнопки {text} не соответствует макету"

    @allure.title(f"Проверка цвета кнопки '{TEXT_LOGIN}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_login_color(self, main_page_open):
        element = main_page_open.get_header_auth_login()
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки {TEXT_LOGIN} не соответствует макету"

    @allure.title(f"Проверка перехода на страницу регистрации по кнопке '{TEXT_SIGNUP_HEADER}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_signup_link(self, main_page_open, driver):
        main_page_open.get_header_auth_signup().click()
        assert driver.current_url == SIGNUP_PAGE, f"Произошел переход на страницу {driver.current_url}"

    @allure.title(f"Проверка текста кнопки '{TEXT_SIGNUP_HEADER}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_signup_text(self, main_page_open):
        text = main_page_open.get_header_auth_signup().text
        assert text == TEXT_SIGNUP_HEADER, f"Текст кнопки {text} не соответствует макету"

    @allure.title(f"Проверка цвета кнопки '{TEXT_SIGNUP_HEADER}' в хедере")
    @pytest.mark.smoke
    def test_get_header_auth_signup_color(self, main_page_open):
        element = main_page_open.get_header_auth_signup()
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки {TEXT_SIGNUP_HEADER} не соответствует макету"

    @allure.title(f"Проверка перехода на страницу регистрации по кнопке '{TEXT_SIGNUP}' на странице")
    @pytest.mark.smoke
    def test_get_body_auth_signup_link(self, main_page_open, driver):
        main_page_open.get_body_auth_signup().click()
        assert driver.current_url == SIGNUP_PAGE, f"Произошел переход на страницу {driver.current_url}"

    @allure.title(f"Проверка текста кнопки '{TEXT_SIGNUP}' в хедере")
    @pytest.mark.smoke
    def test_get_body_auth_signup_text(self, main_page_open):
        text = main_page_open.get_body_auth_signup().text
        assert text == TEXT_SIGNUP, f"Текст кнопки {text} не соответствует макету"

    @allure.title(f"Проверка цвета кнопки '{TEXT_SIGNUP}' в хедере")
    @pytest.mark.smoke
    def test_get_body_auth_signup_color(self, main_page_open):
        element = main_page_open.get_body_auth_signup()
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки {TEXT_SIGNUP} не соответствует макету"

    @allure.title("Проверка перехода на страницу c лицензионным соглашением")
    @pytest.mark.smoke
    def test_get_futer_link(self, main_page_open, driver):
        license_link = main_page_open.get_futer_license().text
        main_page_open.get_futer_license().click()
        title = main_page_open.get_license_title().text
        assert license_link == LICENSE_LINK, f"Неверный текст ссылки '{LICENSE_LINK}"
        assert driver.current_url == TERMS_OF_SERVICE, f"Произошел переход на страницу {driver.current_url}"
        assert title == LICENSE_TITLE, f"ОР: {LICENSE_TITLE}, ФР: {title}"

    @allure.title(f"Проверка текста элемента '{EMAIL_TEXT}'в хедере")
    @pytest.mark.smoke
    def test_get_futer_email(self, main_page_open, driver):
        text = main_page_open.get_futer_email().text
        assert text == EMAIL_TEXT, f"email адрес {text} неверный"
        element = main_page_open.get_futer_email_hover()
        link = element.get_attribute("href")
        assert link == EMAIL_TEXT_HOVER, f"Неверный вызов {link}"

    @allure.title(f"Проверка года © PulseWave, {YEAR_COOPERATION} в хедере")
    @pytest.mark.smoke
    def test_get_year_cooperation(self, main_page_open, driver):
        year = int(main_page_open.get_futer_cooperation().text[-4:])
        assert year == YEAR_COOPERATION, f"Пора поменять год {year}, уже {YEAR_COOPERATION}"

    @allure.title(f"Проверка текста '{MAIN_TITLE}' на Главной странице")
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

    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @allure.title(f"Проверка цвета и размера '{FIRST_SAFETY}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_first_safety_size_and_color(self, main_page_open, driver):
        element = main_page_open.get_body_first_safety()
        assert element.value_of_css_property("color") == TEXT_COLOR, "Цвет не соответствует"
        assert element.value_of_css_property("font-size") == TEXT_SIZE, "Размер не соответствует"

    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @allure.title(f"Проверка цвета и размера '{ALL_TIME}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_first_all_time_size_and_color(self, main_page_open, driver):
        element = main_page_open.get_body_all_time()
        assert element.value_of_css_property("color") == TEXT_COLOR, "Цвет не соответствует"
        assert element.value_of_css_property("font-size") == TEXT_SIZE, "Размер не соответствует"

    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @allure.title(f"Проверка цвета и размера '{USEFUL_INTERFACE}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_useful_interface_size_and_color(self, main_page_open, driver):
        element = main_page_open.get_body_useful_interface()
        assert element.value_of_css_property("color") == TEXT_COLOR, "Цвет не соответствует"
        assert element.value_of_css_property("font-size") == TEXT_SIZE, "Размер не соответствует"

    @allure.title(f"Проверка текста '{FULL_FUNCTIONALITY}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_descr(self, main_page_open, driver):
        title = main_page_open.get_body_main_descr().text
        assert title == FULL_FUNCTIONALITY, "Неверный текст"

    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @allure.title(f"Проверка цвета и размера '{FULL_FUNCTIONALITY}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_descr_size_and_color(self, main_page_open, driver):
        element = main_page_open.get_body_main_descr()
        assert element.value_of_css_property("color") == TEXT_COLOR, "Цвет не соответствует"
        assert element.value_of_css_property("font-size") == TEXT_SIZE, "Размер не соответствует"

    @allure.title(f"Проверка текста '{ONE_APP}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_subtitle(self, main_page_open, driver):
        title = main_page_open.get_body_main_subtitle().text
        assert title == ONE_APP, "Неверный текст"

    @allure.title(f"Проверка цвета и размера '{ONE_APP}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_subtitle_size_and_color(self, main_page_open, driver):
        element = main_page_open.get_body_main_subtitle()
        assert element.value_of_css_property("color") == TEXT_COLOR, "Цвет не соответствует"
        assert element.value_of_css_property("font-size") == TEXT_SIZE, "Размер не соответствует"

    @allure.title(f"Проверка цвета и размера '{MAIN_PAGE_TITLE}' на Главной странице")
    @pytest.mark.smoke
    def test_get_body_main_title_size_and_color(self, main_page_open):
        element = main_page_open.get_body_main_title()
        assert element.value_of_css_property("color") == PULSEWAVE_COLOR, "Цвет не соответствует"
        assert element.value_of_css_property("font-size") == PULSEWAVE_SIZE, "Размер не соответствует"

    @allure.title(f"Проверка цвета '{LICENSE_LINK}' на Главной странице")
    @pytest.mark.xfail(reason="ОР 'rgba(16, 16, 18, 1)', ФР 'rgba(66, 66, 66, 1)'")
    @pytest.mark.smoke
    def test_get_futer_license_color(self, main_page_open, driver):
        element = main_page_open.get_futer_license()
        assert element.value_of_css_property("color") == TEXT_COLOR, "Цвет не соответствует"

    @allure.title(f"Проверка размера '{LICENSE_LINK}' на Главной странице")
    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @pytest.mark.smoke
    def test_get_futer_license_size(self, main_page_open, driver):
        element = main_page_open.get_futer_license()
        assert element.value_of_css_property("font-size") == TEXT_SIZE, "Размер не соответствует"

    @allure.title(f"Проверка цвета '{EMAIL_TEXT}' на Главной странице")
    @pytest.mark.xfail(reason="ОР 'rgba(16, 16, 18, 1)', ФР 'rgba(66, 66, 66, 1)'")
    @pytest.mark.smoke
    def test_get_body_futer_email_color(self, main_page_open, driver):
        element = main_page_open.get_futer_email()
        assert element.value_of_css_property("color") == TEXT_COLOR, "Цвет не соответствует"

    @allure.title(f"Проверка размера '{EMAIL_TEXT}' на Главной странице")
    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @pytest.mark.smoke
    def test_get_body_futer_email_size(self, main_page_open, driver):
        element = main_page_open.get_futer_email()
        assert element.value_of_css_property("font-size") == TEXT_SIZE, "Размер не соответствует"

    @allure.title(f"Проверка цвета '{YEAR_COOPERATION}' на Главной странице")
    @pytest.mark.xfail(reason="ОР 'rgba(16, 16, 18, 1)', ФР 'rgba(66, 66, 66, 1)'")
    @pytest.mark.smoke
    def test_get_futer_cooperation_color(self, main_page_open, driver):
        element = main_page_open.get_futer_cooperation()
        assert element.value_of_css_property("color") == TEXT_COLOR, "Цвет не соответствует"

    @allure.title(f"Проверка размера '{YEAR_COOPERATION}' на Главной странице")
    @pytest.mark.xfail(reason="ОР шрифт 16, ФР шрифт 14")
    @pytest.mark.smoke
    def test_get_futer_cooperation_size(self, main_page_open, driver):
        element = main_page_open.get_futer_cooperation()
        assert element.value_of_css_property("font-size") == TEXT_SIZE, "Размер не соответствует"
