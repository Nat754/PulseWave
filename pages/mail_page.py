from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._enter_button = (By.XPATH, '(//button[text()="Войти"])[1]')
        self._username = (By.CSS_SELECTOR, 'input[name="username"]')
        self._next_button = (By.CSS_SELECTOR, 'button[data-test-id="next-button"]')
        self._password = (By.CSS_SELECTOR, 'input[name="password"]')
        self._submit_button = (By.CSS_SELECTOR, 'data-test-id="submit-button"')

    @allure.step("Проверка видимости заголовка кнопки 'Войти'")
    def get_enter_button(self):
        return self.element_is_visible(self._enter_button)

    @allure.step("Проверка видимости поля username")
    def get_username(self):
        return self.element_is_visible(self._username)

    @allure.step("Проверка видимости кнопки 'Ввести пароль'")
    def get_next_button(self):
        return self.element_is_visible(self._next_button)

    @allure.step("Проверка видимости поля пароль")
    def get_password(self):
        return self.element_is_visible(self._password)

    @allure.step("Проверка видимости кнопки 'Войти'")
    def get_submit_button(self):
        return self.element_is_visible(self._submit_button)
