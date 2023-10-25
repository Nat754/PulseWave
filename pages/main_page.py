from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._logo = (By.CLASS_NAME, 'header__logo')
        self._auth_login = (By.CSS_SELECTOR, 'a[href="/auth/login"] button')
        self._auth_signup = (By.CSS_SELECTOR, 'a[href="/auth/signup"] button')
        self._signup = (By.CLASS_NAME, 'button__big')
        self._license = (By.XPATH, '(//span[@class="item__text"])[1]')
        self._email = (By.XPATH, '(//span[@class="item__text"])[2]')
        self._cooperation = (By.XPATH, '(//span[@class="item__text"])[3]')
        self._license_title = (By.CLASS_NAME, 'privacy__title')

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

    @allure.step("Проверка видимости элемента 'pulsewave@gmail.com' в футере")
    def get_futer_email(self):
        return self.element_is_visible(self._email)

    @allure.step("Проверка видимости элемента '© PulseWave, 2023' в футере")
    def get_futer_cooperation(self):
        return self.element_is_visible(self._cooperation)
