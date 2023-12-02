import allure
import pytest
from pages.footer import Footer
from tests.constant import Constant
from tests.test_footer.constant import FooterConstant


@allure.epic("Тестирование Главной страницы")
class TestFooter:
    footer = FooterConstant()
    const = Constant()

    @pytest.mark.parametrize('url', FooterConstant.PAGES)
    @pytest.mark.smoke
    def test_get_all_cookies(self, driver, url):
        allure.dynamic.title(f"Проверка попапа о принятии файлов cookie на странице {url}")
        page = Footer(driver)
        driver.get(url)
        text = page.get_cookies_text().text
        assert text == self.footer.COOKIES_TEXT, f"Неверный текст '{text}'"
        button_text = page.get_allow_all_cookies().text
        assert button_text == self.footer.COOKIES_BUTTON, f"Неверный текст '{button_text}'"
        page.get_cookies_link().click()
        link = driver.current_url
        assert link == self.footer.COOKIES, f"Неверный url '{link}'"

    @allure.title("Проверка перехода на страницу c лицензионным соглашением")
    @pytest.mark.smoke
    @pytest.mark.parametrize('url', footer.PAGES)
    def test_get_footer_link(self, footer_open, driver, url):
        footer_open.get_footer_license()
        text = footer_open.get_footer_license().text
        footer_open.get_footer_license().click()
        title = footer_open.get_license_title().text
        assert text == self.footer.LICENSE_LINK, f"Неверный текст ссылки '{self.footer.LICENSE_LINK}"
        assert driver.current_url == self.const.TERMS_OF_SERVICE, \
            f"Произошел переход на страницу '{driver.current_url}'"
        assert title == self.footer.LICENSE_TITLE, f"ОР: '{self.footer.LICENSE_TITLE}', ФР: '{title}'"

    @allure.title(f"Проверка элемента '{footer.EMAIL_TEXT}'в хедере")
    @pytest.mark.parametrize('url', footer.PAGES)
    @pytest.mark.smoke
    def test_get_footer_email(self, footer_open, url):
        text = footer_open.get_footer_email().text
        assert text == self.footer.EMAIL_TEXT, f"email адрес '{text}' неверный"
        element = footer_open.get_footer_email_hover()
        link = element.get_attribute("href")
        assert link == self.footer.EMAIL_TEXT_HOVER, f"Неверный вызов '{link}'"

    @allure.title(f"Проверка года © PulseWave, {footer.YEAR_COOPERATION} в хедере")
    @pytest.mark.parametrize('url', footer.PAGES)
    @pytest.mark.smoke
    def test_get_year_cooperation(self, footer_open, url):
        year = int(footer_open.get_footer_cooperation().text[-4:])
        assert year == self.footer.YEAR_COOPERATION, f"Пора поменять год '{year}', уже '{self.footer.YEAR_COOPERATION}'"

    @pytest.mark.parametrize('url', footer.PAGES)
    @pytest.mark.parametrize('css_property, figma, name', footer.CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_footer_license(self, footer_open, css_property, figma, name, url):
        allure.dynamic.title(f"Проверка {name} ссылки '{self.footer.LICENSE_LINK}' в футере")
        element = footer_open.get_footer_license()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} ссылки '{self.footer.LICENSE_LINK}' макету"

    @pytest.mark.parametrize('url', footer.PAGES)
    @pytest.mark.parametrize('css_property, figma, name', footer.CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_footer_email(self, footer_open, css_property, figma, name, url):
        allure.dynamic.title(f"Проверка {name} надписи '{self.footer.EMAIL_TEXT}' в футере")
        element = footer_open.get_footer_email()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} надписи '{self.footer.EMAIL_TEXT}' макету"

    @pytest.mark.parametrize('url', footer.PAGES)
    @pytest.mark.parametrize('css_property, figma, name', footer.CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_footer_cooperation(self, footer_open, css_property, figma, name, url):
        allure.dynamic.title(f"Проверка {name} надписи '{self.footer.TEXT_COOPERATION}' в футере")
        element = footer_open.get_footer_cooperation()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, (f"Не прошла проверка соответствия {name} надписи '{self.footer.TEXT_COOPERATION}' "
                                   f"макету")
