import allure
from locators.general_locators import GeneralLocators
from pages.base_page import BasePage
from tests.constant import FooterConstant, Links


class GeneralPage(BasePage):
    footer = FooterConstant()
    locator = GeneralLocators()
    link = Links

    @allure.step('Проверка заголовка модального окна')
    def get_title_modal(self):
        return self.element_is_visible(self.locator.TITLE_MODAL)

    @allure.step('Проверка текста модального окна')
    def get_text_modal(self):
        return self.element_is_visible(self.locator.TEXT_MODAL)
