from page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._logo = (By.CLASS_NAME, "logotype")
        self._workspace = (By.CSS_SELECTOR, "a[href='/workspace']")

    @allure.step("Проверяем что логотип виден в хедере")
    def get_header_logo(self):
        return self.element_is_visible(self._logo)

    @allure.step("Проверяем что ссылка 'Рабочее пространство' видна в хэдере")
    def get_header_workspace(self):
        return self.element_is_visible(self._workspace)
