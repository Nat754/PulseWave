import pytest

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from tests.constant import ALL_TIME, FIRST_SAFETY, USEFUL_INTERFACE, FULL_FUNCTIONALITY, ONE_APP, TEXT_LOGIN, \
    TEXT_SIGNUP_HEADER, TEXT_SIGNUP, LICENSE_LINK, LICENSE_TITLE, EMAIL_TEXT, EMAIL_TEXT_HOVER, TEXT_COOPERATION, \
    MAIN_TITLE, COOKIES_BUTTON, ITEMS, ITEMS_TEXT, YEAR_COOPERATION, TEXT_SIZE, BUTTONS, BUTTON_TEXT_SIZE


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._logo = (By.CLASS_NAME, 'header__logo')
        self._auth_login = (By.CSS_SELECTOR, '.button__small')
        self._auth_signup = (By.CSS_SELECTOR, 'a[href="/auth/signup"] button')
        self._signup = (By.CLASS_NAME, 'button__big')
        self._license = (By.XPATH, '(//span[@class="item__text"])[1]')
        self._email = (By.CLASS_NAME, 'item__link-desc')
        self._email_hover = (By. XPATH, '//a[contains(@href, "mailto")]')
        self._cooperation = (By.XPATH, '(//span[@class="item__text"])[3]')
        self._license_title = (By.CLASS_NAME, 'privacy__title')
        self._main_title = (By.TAG_NAME, 'h1')
        self._main_subtitle = (By.CLASS_NAME, 'main__subtitle')
        self._main_descr = (By.CLASS_NAME, 'main__descr')
        self._allow_all_cookies = (By.CSS_SELECTOR, '.cookies__body .button__small')
        self._cookies_link = (By.CLASS_NAME, 'cookies__link')
        self._cookies_text = (By.CLASS_NAME, 'cookies__text')
        self._useful_interface = (By.XPATH, '//p[text()="Удобный и понятный интерфейс!"]')
        self._all_time = (By.XPATH, '//p[text()="Самый высокий уровень бесперебойной работы!"]')
        self._first_safety = (By.XPATH, '//p[contains(text(), "Ваша безопасность")]')

    @allure.step("Проверка видимости логотипа в хедере")
    def get_header_logo(self):
        return self.element_is_visible(self._logo)

    @allure.step(f"Проверка видимости ссылки '{TEXT_LOGIN}' в хэдере")
    def get_header_auth_login(self):
        return self.element_is_visible(self._auth_login)

    @allure.step(f"Проверка видимости ссылки '{TEXT_SIGNUP_HEADER}' в хэдере")
    def get_header_auth_signup(self):
        return self.element_is_visible(self._auth_signup)

    @allure.step(f"Проверка видимости ссылки '{TEXT_SIGNUP}' на главной странице")
    def get_body_auth_signup(self):
        return self.element_is_visible(self._signup)

    @allure.step(f"Проверка видимости ссылки '{LICENSE_LINK}' в футере")
    def get_futer_license(self):
        # self.go_to_element(self.element_is_clickable(self._license))
        return self.element_is_visible(self._license)

    @allure.step(f"Проверка видимости заголовка '{LICENSE_TITLE}'")
    def get_license_title(self):
        return self.element_is_visible(self._license_title)

    @allure.step(f"Проверка видимости надписи '{EMAIL_TEXT}' в футере")
    def get_futer_email(self):
        return self.element_is_visible(self._email)

    @allure.step(f"Проверка видимости перенаправления '{EMAIL_TEXT_HOVER}' в футере")
    def get_futer_email_hover(self):
        return self.element_is_visible(self._email_hover)

    @allure.step(f"Проверка видимости надписи '{TEXT_COOPERATION}' в футере")
    def get_futer_cooperation(self):
        return self.element_is_visible(self._cooperation)

    @allure.step(f"Проверка видимости надписи '{MAIN_TITLE}' на Главной странице")
    def get_body_main_title(self):
        return self.element_is_visible(self._main_title)

    @allure.step(f"Проверка видимости кнопки '{COOKIES_BUTTON}' в сообщении о принятии файлов cookie на Главной странице")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self._allow_all_cookies)

    @allure.step("Проверка видимости текста сообщения о принятии файлов cookie на Главной странице")
    def get_cookies_text(self):
        return self.element_is_visible(self._cookies_text)

    @allure.step("Проверка видимости ссылки для просмотра информации о файлах cookie на Главной странице")
    def get_cookies_link(self):
        return self.element_is_visible(self._cookies_link)

    @allure.step(f"Проверка видимости надписи '{USEFUL_INTERFACE}' на Главной странице")
    def get_body_useful_interface(self):
        return self.element_is_visible(self._useful_interface)

    @allure.step(f"Проверка видимости надписи '{ALL_TIME}' на Главной странице")
    def get_body_all_time(self):
        return self.element_is_visible(self._all_time)

    @allure.step(f"Проверка видимости надписи '{FIRST_SAFETY}' на Главной странице")
    def get_body_first_safety(self):
        return self.element_is_visible(self._first_safety)

    @allure.step(f"Проверка видимости надписи '{FULL_FUNCTIONALITY}' на Главной странице")
    def get_body_main_descr(self):
        return self.element_is_visible(self._main_descr)

    @allure.step(f"Проверка видимости надписи '{ONE_APP}' на Главной странице")
    def get_body_main_subtitle(self):
        return self.element_is_visible(self._main_subtitle)

    @pytest.mark.parametrize('item', ITEMS)
    def get_element_text(self, item, element=None):
        allure.dynamic.tag(f"Проверка видимости элемента '{item}'")
        if item == TEXT_LOGIN:
            element = self.get_header_auth_login()
        elif item == TEXT_SIGNUP_HEADER:
            element = self.get_header_auth_signup()
        elif item == TEXT_SIGNUP:
            element = self.get_body_auth_signup()
        elif item == MAIN_TITLE:
            element = self.get_body_main_title()
        elif item == USEFUL_INTERFACE:
            element = self.get_body_useful_interface()
        elif item == ALL_TIME:
            element = self.get_body_all_time()
        elif item == FIRST_SAFETY:
            element = self.get_body_first_safety()
        elif item == FULL_FUNCTIONALITY:
            element = self.get_body_main_descr()
        elif item == ONE_APP:
            element = self.get_body_main_subtitle()
        return element

    @pytest.mark.parametrize('item', ITEMS_TEXT)
    def get_font_size(self, item, element=None):
        """Проверка видимости элемента '{item}'"""
        if item == FIRST_SAFETY:
            element = self.get_body_first_safety()
        elif item == ALL_TIME:
            element = self.get_body_all_time()
        elif item == USEFUL_INTERFACE:
            element = self.get_body_useful_interface()
        elif item == FULL_FUNCTIONALITY:
            element = self.get_body_main_descr()
        elif item == ONE_APP:
            element = self.get_body_main_subtitle()
        elif item == LICENSE_LINK:
            element = self.get_futer_license()
        elif item == EMAIL_TEXT:
            element = self.get_futer_email()
        elif item == YEAR_COOPERATION:
            element = self.get_futer_cooperation()
        return element

    @pytest.mark.parametrize('button', BUTTONS)
    def get_button_text_size(self, button, element=None):
        """Проверка видимости текста кнопки в хедере"""
        if button == TEXT_LOGIN:
            element = self.get_header_auth_login()
        elif button == TEXT_SIGNUP_HEADER:
            element = self.get_header_auth_signup()
        elif button == TEXT_SIGNUP:
            element = self.get_body_auth_signup()
        return element
