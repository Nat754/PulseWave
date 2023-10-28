from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from tests.constant import ALL_TIME, FIRST_SAFETY, USEFUL_INTERFACE


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

    @allure.step("Проверка видимости ссылки 'Войти' в хэдере")
    def get_header_auth_login(self):
        return self.element_is_visible(self._auth_login)

    @allure.step("Проверка видимости ссылки 'Регистрация' в хэдере")
    def get_header_auth_signup(self):
        return self.element_is_visible(self._auth_signup)

    @allure.step("Проверка видимости ссылки 'Зарегистрироваться' на главной странице")
    def get_body_auth_signup(self):
        return self.element_is_visible(self._signup)

    @allure.step("Проверка видимости ссылки 'Условия пользования' в футере")
    def get_futer_license(self):
        return self.element_is_visible(self._license)

    @allure.step("Проверка видимости заголовка 'ЛИЦЕНЗИОННЫЙ ДОГОВОР (ОФЕРТА)'")
    def get_license_title(self):
        return self.element_is_visible(self._license_title)

    @allure.step("Проверка видимости надписи 'pulsewave@gmail.com' в футере")
    def get_futer_email(self):
        return self.element_is_visible(self._email)

    @allure.step("Проверка видимости надписи '© PulseWave, 2023' в футере")
    def get_futer_cooperation(self):
        return self.element_is_visible(self._cooperation)

    @allure.step("Проверка видимости надписи 'PULSEWAVE' на Главной странице")
    def get_body_main_title(self):
        return self.element_is_visible(self._main_title)

    @allure.step("Проверка видимости кнопки 'Принимаю все' в сообщении о принятии файлов cookie на Главной странице")
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
