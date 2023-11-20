import allure
import pytest
from pages.footer import Footer
from tests.constant import TERMS_OF_SERVICE
from tests.test_footer.constant import LICENSE_LINK, LICENSE_TITLE, EMAIL_TEXT, EMAIL_TEXT_HOVER, YEAR_COOPERATION, \
    CHECK_TEXT, TEXT_COOPERATION, COOKIES_TEXT, COOKIES_BUTTON, COOKIES, PAGES


@allure.epic("Тестирование Главной страницы")
class TestFooter:
    @allure.title("Проверка попапа о принятии файлов cookie")
    @pytest.mark.parametrize('url', PAGES)
    @pytest.mark.smoke
    def test_get_all_cookies(self, driver, url):
        page = Footer(driver)
        driver.get(url)
        text = page.get_cookies_text().text
        assert text == COOKIES_TEXT, f"Неверный текст '{text}'"
        button_text = page.get_allow_all_cookies().text
        assert button_text == COOKIES_BUTTON, f"Неверный текст '{button_text}'"
        page.get_cookies_link().click()
        link = driver.current_url
        assert link == COOKIES, f"Неверный url '{link}'"

    @allure.title("Проверка перехода на страницу c лицензионным соглашением")
    @pytest.mark.smoke
    @pytest.mark.parametrize('url', PAGES)
    def test_get_footer_link(self, footer_open, driver, url):
        footer_open.get_footer_license()
        text = footer_open.get_footer_license().text
        footer_open.get_footer_license().click()
        title = footer_open.get_license_title().text
        assert text == LICENSE_LINK, f"Неверный текст ссылки '{LICENSE_LINK}"
        assert driver.current_url == TERMS_OF_SERVICE, f"Произошел переход на страницу '{driver.current_url}'"
        assert title == LICENSE_TITLE, f"ОР: '{LICENSE_TITLE}', ФР: '{title}'"

    @allure.title(f"Проверка элемента '{EMAIL_TEXT}'в хедере")
    @pytest.mark.parametrize('url', PAGES)
    @pytest.mark.smoke
    def test_get_footer_email(self, footer_open, url):
        text = footer_open.get_footer_email().text
        assert text == EMAIL_TEXT, f"email адрес '{text}' неверный"
        element = footer_open.get_footer_email_hover()
        link = element.get_attribute("href")
        assert link == EMAIL_TEXT_HOVER, f"Неверный вызов '{link}'"

    @allure.title(f"Проверка года © PulseWave, {YEAR_COOPERATION} в хедере")
    @pytest.mark.parametrize('url', PAGES)
    @pytest.mark.smoke
    def test_get_year_cooperation(self, footer_open):
        year = int(footer_open.get_footer_cooperation().text[-4:])
        assert year == YEAR_COOPERATION, f"Пора поменять год '{year}', уже '{YEAR_COOPERATION}'"

    @pytest.mark.parametrize('url', PAGES)
    @pytest.mark.parametrize('css_property, figma, name', CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_footer_license(self, footer_open, css_property, figma, name, url):
        allure.dynamic.title(f"Проверка {name} ссылки '{LICENSE_LINK}' в футере")
        element = footer_open.get_footer_license()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} ссылки '{LICENSE_LINK}' макету"

    @pytest.mark.parametrize('url', PAGES)
    @pytest.mark.parametrize('css_property, figma, name', CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_footer_email(self, footer_open, css_property, figma, name, url):
        allure.dynamic.title(f"Проверка {name} надписи '{EMAIL_TEXT}' в футере")
        element = footer_open.get_footer_email()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} надписи '{EMAIL_TEXT}' макету"

    @pytest.mark.parametrize('url', PAGES)
    @pytest.mark.parametrize('css_property, figma, name', CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_footer_cooperation(self, footer_open, css_property, figma, name, url):
        allure.dynamic.title(f"Проверка {name} надписи '{TEXT_COOPERATION}' в футере")
        element = footer_open.get_footer_cooperation()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, f"Не прошла проверка соответствия {name} надписи '{TEXT_COOPERATION}' макету"
