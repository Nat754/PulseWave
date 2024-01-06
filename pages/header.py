import allure
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage
from tests.test_footer.constant import FooterConstant
from tests.test_header.constant import HeaderConstant
from locators.footer_locators import FooterLocators


class HeaderPage(BasePage):
    header = HeaderConstant
    footer = FooterConstant
    locator = HeaderLocators

    @allure.step("Проверка видимости логотипа в хедере")
    def get_header_logo(self):
        return self.element_is_visible(self.locator.LOGO)

    @allure.step(f"Проверка видимости кнопки '{header.TEXT_LOGIN}' в хэдере")
    def get_header_auth_login(self):
        return self.element_is_visible(self.locator.AUTH_LOGIN)

    @allure.step(f"Проверка видимости кнопки '{header.TEXT_SIGNUP}' в хэдере")
    def get_header_auth_signup(self):
        return self.element_is_visible(self.locator.AUTH_SIGNUP)

    @allure.step(f"Проверка видимости кнопки '{footer.COOKIES_BUTTON}' "
                 f"в сообщении о принятии файлов cookie на Главной странице")
    def get_allow_all_cookies(self):
        return self.element_is_visible(FooterLocators.ALLOW_ALL_COOKIES)
