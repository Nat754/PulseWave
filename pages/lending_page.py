from pages.base_page import BasePage
import allure
from tests.constant import LendingConstant
from locators.lending_locators import LendingPageLocators


class LendingPage(BasePage):
    const = LendingConstant
    locator = LendingPageLocators

    @allure.step("Проверка кликабельности логотипа в хедере")
    def get_lending_logo_is_clickable(self):
        return self.element_is_clickable(self.locator.LOGO)

    @allure.step(f"Проверка видимости кнопки '{const.TEXT_LOGIN}' в хэдере")
    def get_lending_auth_login(self):
        return self.element_is_visible(self.locator.AUTH_LOGIN)

    @allure.step(f"Проверка видимости кнопки '{const.TEXT_AUTH_FREE}' в хэдере")
    def get_lending_auth_free(self):
        return self.element_is_visible(self.locator.AUTH_FREE)
