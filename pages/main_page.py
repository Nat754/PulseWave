from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

from tests.test_footer.constant import FooterConstant
from tests.test_main_page.constant import MainConstant


class MainPage(BasePage):
    main = MainConstant
    footer = FooterConstant

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

    @allure.step(f"Проверка видимости кнопки '{main.TEXT_LOGIN}' в хэдере")
    def get_header_auth_login(self):
        return self.element_is_visible(self._auth_login)

    @allure.step(f"Проверка видимости кнопки '{main.TEXT_SIGNUP_HEADER}' в хэдере")
    def get_header_auth_signup(self):
        return self.element_is_visible(self._auth_signup)

    @allure.step(f"Проверка видимости кнопки '{main.TEXT_SIGNUP}' на главной странице")
    def get_body_auth_signup(self):
        return self.element_is_visible(self._signup)

    @allure.step(f"Проверка видимости надписи '{main.MAIN_TITLE}' на Главной странице")
    def get_body_main_title(self):
        return self.element_is_visible(self._main_title)

    @allure.step(f"Проверка видимости кнопки '{footer.COOKIES_BUTTON}' "
                 f"в сообщении о принятии файлов cookie на Главной странице")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self._allow_all_cookies)

    @allure.step("Проверка видимости текста сообщения о принятии файлов cookie на Главной странице")
    def get_cookies_text(self):
        return self.element_is_visible(self._cookies_text)

    @allure.step("Проверка видимости ссылки для просмотра информации о файлах cookie на Главной странице")
    def get_cookies_link(self):
        return self.element_is_visible(self._cookies_link)

    @allure.step(f"Проверка видимости надписи '{main.USEFUL_INTERFACE}' на Главной странице")
    def get_body_useful_interface(self):
        return self.element_is_visible(self._useful_interface)

    @allure.step(f"Проверка видимости надписи '{main.ALL_TIME}' на Главной странице")
    def get_body_all_time(self):
        return self.element_is_visible(self._all_time)

    @allure.step(f"Проверка видимости надписи '{main.FIRST_SAFETY}' на Главной странице")
    def get_body_first_safety(self):
        return self.element_is_visible(self._first_safety)

    @allure.step(f"Проверка видимости надписи '{main.FULL_FUNCTIONALITY}' на Главной странице")
    def get_body_main_descr(self):
        return self.element_is_visible(self._main_descr)

    @allure.step(f"Проверка видимости надписи '{main.ONE_APP}' на Главной странице")
    def get_body_main_subtitle(self):
        return self.element_is_visible(self._main_subtitle)
