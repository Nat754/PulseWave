import allure
from locators.footer_locators import FooterLocators
from pages.base_page import BasePage
from tests.test_footer.constant import FooterConstant


class FooterPage(BasePage):
    footer = FooterConstant
    locator = FooterLocators

    @allure.step(f"Проверка видимости ссылки '{footer.LICENSE_LINK}' в футере")
    def get_footer_license(self):
        return self.element_is_visible(self.locator.LICENSE)

    @allure.step(f"Проверка видимости заголовка '{footer.LICENSE_TITLE}'")
    def get_license_title(self):
        return self.element_is_visible(self.locator.LICENSE_TITLE)

    @allure.step(f"Получить элемент '{footer.EMAIL_TEXT}' в футере")
    def get_footer_email(self):
        return self.element_is_visible(self.locator.EMAIL)

    @allure.step(f"Проверка ссылки для открытия почтового приложения у элемента '{footer.EMAIL_TEXT_HOVER}' в футере")
    def get_footer_email_hover(self):
        return self.element_is_visible(self.locator.EMAIL_HOVER)

    @allure.step(f"Получить элемент '{footer.TEXT_COOPERATION}' в футере")
    def get_footer_cooperation(self):
        return self.element_is_visible(self.locator.COOPERATION)

    @allure.step(f"Получить текст кнопки '{footer.COOKIES_BUTTON}' "
                 f"в сообщении о принятии файлов cookie на Главной странице")
    def get_allow_all_cookies(self):
        button_text = self.element_is_visible(self.locator.ALLOW_ALL_COOKIES).text
        return button_text

    @allure.step("Получить текст сообщения о принятии файлов cookie на Главной странице")
    def get_cookies_text(self):
        text = self.element_is_visible(self.locator.COOKIES_TEXT).text
        return text

    @allure.step("Проверка перехода по ссылке для просмотра информации о файлах cookie на Главной странице")
    def get_cookies_link(self):
        return self.element_is_visible(self.locator.COOKIES_LINK).click()

    def get_page_open(self, driver, url):
        with allure.step(f"Открыть страницу '{url}'"):
            page = FooterPage(driver)
            driver.get(url)
        return page
