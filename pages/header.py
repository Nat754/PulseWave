import allure
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage
from tests.constant import FooterConstant, HeaderConstant
from locators.footer_locators import FooterLocators


class HeaderPage(BasePage):
    const = HeaderConstant()
    footer = FooterConstant()
    locator = HeaderLocators()

    @allure.step("Проверка видимости логотипа в хедере")
    def get_header_logo(self):
        return self.element_is_visible(self.locator.LOGO)

    @allure.step("Проверка кликабельности логотипа в хедере")
    def get_header_logo_is_clickable(self):
        return self.element_is_clickable(self.locator.LOGO)

    @allure.step(f"Проверка видимости кнопки '{const.TEXT_LOGIN}' в хэдере")
    def get_header_auth_login(self):
        return self.elements_are_visible(self.locator.AUTH_LOGIN)[0]

    @allure.step(f"Проверка видимости кнопки '{const.TEXT_SIGNUP}' в хэдере")
    def get_header_auth_signup(self):
        return self.elements_are_visible(self.locator.AUTH_SIGNUP)[-1]

    @allure.step(f"Проверка видимости кнопки '{footer.COOKIES_BUTTON}' "
                 f"в сообщении о принятии файлов cookie на Главной странице")
    def get_allow_all_cookies(self):
        return self.element_is_visible(FooterLocators.ALLOW_ALL_COOKIES)
