import time
import allure
import pytest
from pages.main_page import MainPage
from tests.constant import MAIN_PAGE_HOME, MAIN_PAGE_URL, COOKIES, TERMS_OF_SERVICE
from tests.test_main_page.constant import TEXT_SIGNUP, TEXT_LOGIN, TEXT_SIGNUP_HEADER, BUTTON_COLOR, LICENSE_TITLE, \
    LICENSE_LINK, EMAIL_TEXT, YEAR_COOPERATION, COOKIES_TEXT, COOKIES_BUTTON, TEXT_COLOR, ALL_TIME, FIRST_SAFETY, \
    USEFUL_INTERFACE, EMAIL_TEXT_HOVER, TEXT_SIZE, FULL_FUNCTIONALITY, ONE_APP, PULSEWAVE_SIZE, TITLE_COLOR, \
    MAIN_PAGE_TITLE, BUTTON_TEXT_SIZE, BUTTONS_URL, BUTTONS, ITEMS, ITEMS_PULSEWAVE_COLOR, ITEMS_TEXT


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
    def test_get_footer_link(self, main_page_open, driver):
        main_page_open.get_footer_license()
        time.sleep(1)
        text = main_page_open.get_footer_license().text
        main_page_open.get_footer_license().click()
        title = main_page_open.get_license_title().text
        assert text == LICENSE_LINK, f"Неверный текст ссылки '{LICENSE_LINK}"
        assert driver.current_url == TERMS_OF_SERVICE, f"Произошел переход на страницу '{driver.current_url}'"
        assert title == LICENSE_TITLE, f"ОР: '{LICENSE_TITLE}', ФР: '{title}'"

    @allure.title(f"Проверка элемента '{EMAIL_TEXT}'в хедере")
    @pytest.mark.smoke
    def test_get_footer_email(self, main_page_open):
        text = main_page_open.get_footer_email().text
        assert text == EMAIL_TEXT, f"email адрес '{text}' неверный"
        element = main_page_open.get_footer_email_hover()
        link = element.get_attribute("href")
        assert link == EMAIL_TEXT_HOVER, f"Неверный вызов '{link}'"

    @allure.title(f"Проверка года © PulseWave, {YEAR_COOPERATION} в хедере")
    @pytest.mark.smoke
    def test_get_year_cooperation(self, main_page_open):
        year = int(main_page_open.get_footer_cooperation().text[-4:])
        assert year == YEAR_COOPERATION, f"Пора поменять год '{year}', уже '{YEAR_COOPERATION}'"

    @pytest.mark.parametrize('url, button', BUTTONS_URL)
    @pytest.mark.smoke
    def test_get_button(self, main_page_open, driver, url, button):
        allure.dynamic.title(f"Проверка перехода на страницу {url} по кнопке '{button}'")
        main_page_open.get_button_is_visible(button).click()
        assert driver.current_url == url, f"Произошел переход на страницу '{driver.current_url}'"

    @pytest.mark.parametrize('item', ITEMS)
    @pytest.mark.regress
    def test_get_element_text(self, main_page_open, item):
        allure.dynamic.title(f"Проверка текста элемента '{item}'")
        text = main_page_open.get_element_text(item).text
        assert text == item, f"Текст элемента '{item}' не соответствует макету"

    @pytest.mark.parametrize('button', BUTTONS)
    @pytest.mark.regress
    def test_get_button_color(self, main_page_open, driver, button):
        allure.dynamic.title(f"Проверка цвета кнопки '{button}'")
        element = main_page_open.get_button_is_visible(button)
        color = element.value_of_css_property("background-color")
        assert color == BUTTON_COLOR, f"Цвет кнопки '{button}' не соответствует макету"

    @pytest.mark.parametrize('item', ITEMS_PULSEWAVE_COLOR)
    @pytest.mark.regress
    def test_get_item_text_color(self, main_page_open, item, element=None):
        allure.dynamic.title(f"Проверка цвета текста элемента '{item}'")
        if item == TEXT_LOGIN:
            element = main_page_open.get_header_auth_login()
        elif item == TEXT_SIGNUP_HEADER:
            element = main_page_open.get_header_auth_signup()
        elif item == TEXT_SIGNUP:
            element = main_page_open.get_body_auth_signup()
        elif item == MAIN_PAGE_TITLE:
            element = main_page_open.get_body_main_title()
        color = element.value_of_css_property("color")
        assert color == TITLE_COLOR, f"Цвет текста элемента '{item}' не соответствует макету"

    @pytest.mark.parametrize('item', ITEMS_TEXT)
    @pytest.mark.regress
    def test_get_item_text_color2(self, main_page_open, item, element=None):
        allure.dynamic.title(f"Проверка цвета текста элемента '{item}'")
        if item == FIRST_SAFETY:
            element = main_page_open.get_body_first_safety()
        elif item == ALL_TIME:
            element = main_page_open.get_body_all_time()
        elif item == USEFUL_INTERFACE:
            element = main_page_open.get_body_useful_interface()
        elif item == FULL_FUNCTIONALITY:
            element = main_page_open.get_body_main_descr()
        elif item == ONE_APP:
            element = main_page_open.get_body_main_subtitle()
        elif item == LICENSE_LINK:
            element = main_page_open.get_footer_license()
        elif item == EMAIL_TEXT:
            element = main_page_open.get_footer_email()
        elif item == YEAR_COOPERATION:
            element = main_page_open.get_footer_cooperation()
        color = element.value_of_css_property("color")
        assert color == TEXT_COLOR, f"Цвет текста элемента '{item}' не соответствует макету"

    @pytest.mark.parametrize('button', BUTTONS)
    @pytest.mark.regress
    def test_get_button_text_size(self, main_page_open, button):
        allure.dynamic.title(f"Проверка размера текста кнопки '{button}' в хедере")
        size = main_page_open.get_button_is_visible(button).value_of_css_property("font-size")
        assert size == BUTTON_TEXT_SIZE, f"Размер текста кнопки '{button}' не соответствует макету"

    @pytest.mark.parametrize('item', ITEMS_TEXT)
    @pytest.mark.regress
    def test_get_body_first_safety_size(self, main_page_open, item):
        allure.dynamic.title(f"Проверка размера шрифта элемента '{item}'")
        element = main_page_open.get_font_size(item)
        size = element.value_of_css_property("font-size")
        assert size == TEXT_SIZE, f"Размер шрифта элемента '{item}' не соответствует макету"

    @allure.title(f"Проверка размера шрифта элемента '{MAIN_PAGE_TITLE}' на Главной странице")
    @pytest.mark.regress
    def test_get_body_main_title_size(self, main_page_open):
        element = main_page_open.get_body_main_title()
        size = element.value_of_css_property("font-size")
        assert size == PULSEWAVE_SIZE, f"Размер шрифта элемента '{MAIN_PAGE_TITLE}' не соответствует макету"
