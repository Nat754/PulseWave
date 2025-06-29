from pages.base_page import BasePage
import allure
from tests.constant import FooterConstant
from tests.constant import MainConstant
from locators.main_locators import MainPageLocators


class MainPage(BasePage):
    main = MainConstant()
    footer = FooterConstant()
    locator = MainPageLocators()

    @allure.step(f"Проверка видимости кнопки '{main.TEXT_SIGNUP}' на главной странице")
    def get_body_auth_signup(self):
        return self.element_is_visible(self.locator.SIGNUP)

    @allure.step(f"Проверка видимости надписи '{main.MAIN_TITLE}' на Главной странице")
    def get_body_main_title(self):
        return self.element_is_visible(self.locator.MAIN_TITLE)

    @allure.step(f"Проверка видимости кнопки '{footer.COOKIES_BUTTON}' "
                 f"в сообщении о принятии файлов cookie на Главной странице")
    def get_allow_all_cookies(self):
        return self.element_is_visible(self.locator.ALLOW_ALL_COOKIES)

    @allure.step("Проверка видимости текста сообщения о принятии файлов cookie на Главной странице")
    def get_cookies_text(self):
        return self.element_is_visible(self.locator.COOKIES_TEXT)

    @allure.step("Проверка видимости ссылки для просмотра информации о файлах cookie на Главной странице")
    def get_cookies_link(self):
        return self.element_is_visible(self.locator.COOKIES_LINK)

    @allure.step(f"Проверка видимости надписи '{main.USEFUL_INTERFACE}' на Главной странице")
    def get_body_useful_interface(self):
        return self.element_is_visible(self.locator.USERFUL_INTERFACE)

    @allure.step(f"Проверка видимости надписи '{main.ALL_TIME}' на Главной странице")
    def get_body_all_time(self):
        return self.element_is_visible(self.locator.ALL_TIME)

    @allure.step(f"Проверка видимости надписи '{main.FIRST_SAFETY}' на Главной странице")
    def get_body_first_safety(self):
        return self.element_is_visible(self.locator.FIRST_SAFETY)

    @allure.step(f"Проверка видимости надписи '{main.FULL_FUNCTIONALITY}' на Главной странице")
    def get_body_main_descr(self):
        return self.element_is_visible(self.locator.MAIN_DESCR)

    @allure.step(f"Проверка видимости надписи '{main.ONE_APP}' на Главной странице")
    def get_body_main_subtitle(self):
        return self.element_is_visible(self.locator.MAIN_SUBTITLE)
