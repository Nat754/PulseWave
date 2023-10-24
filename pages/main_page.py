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

    @allure.step("Проверяем что логотип виден в хедере")
    def get_header_logo(self):
        return self.element_is_visible(self._logo)

    @allure.step("Проверяем что ссылка 'Войти' видна в хэдере")
    def get_header_auth_login(self):
        return self.element_is_visible(self._auth_login)

    @allure.step("Проверяем что ссылка 'Регистрация' видна в хэдере")
    def get_header_auth_signup(self):
        return self.element_is_visible(self._auth_signup)

    @allure.step("Проверяем что ссылка 'Зарегистрироваться' видна на странице")
    def get_body_auth_signup(self):
        return self.element_is_visible(self._signup)
