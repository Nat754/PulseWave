import allure
import pytest
from selenium.common import TimeoutException
from conftest import driver
from pages.footer import FooterPage
from tests.constant import Links, FooterConstant, TestData


@allure.epic("Тестирование Футера")
class TestFooter:
    const = FooterConstant()
    link = Links()
    tdata = TestData

    @pytest.mark.parametrize('url', tdata.PAGES_ALL)
    @pytest.mark.smoke
    def test_get_all_cookies(self, driver, url):
        allure.dynamic.title(f"F.1 Проверка попапа о принятии файлов cookie на странице {url}")
        with allure.step(f"Открыть страницу '{url}'"):
            page = FooterPage(driver)
            driver.get(url)
        try:
            text = page.get_cookies_text()
            assert text == self.const.COOKIES_TEXT, f"Неверный текст '{text}'"
            button_text = page.get_allow_all_cookies().text
            assert button_text == self.const.COOKIES_BUTTON, f"Неверный текст '{button_text}'"
            link = driver.current_url
            page.get_cookies_link()
            page.wait_changed_url(link)
            link = driver.current_url
            assert link == self.const.COOKIES, f"Неверный url '{link}'"
        except TimeoutException:
            print('На странице нет сообщения о принятии файлов cookies')

    @pytest.mark.smoke
    @pytest.mark.parametrize('url', tdata.PAGES_ALL)
    def test_get_footer_link(self, footer_open, driver, url):
        allure.dynamic.title(f"F.2 Проверка отсутствия ссылки на Лицензионное соглашение со страницы '{url}")
        items = [item.text for item in footer_open.get_footer_list()]
        assert items == self.const.FOOTER_LIST, f"Неверный футер на странице '{url}'"

    @allure.title(f"F.3 Проверка элемента '{const.EMAIL_TEXT}'в хедере")
    @pytest.mark.parametrize('url', tdata.PAGES_ALL)
    @pytest.mark.smoke
    def test_get_footer_email(self, url, footer_open):
        text = footer_open.get_footer_email().text
        assert text == self.const.EMAIL_TEXT, f"email адрес '{text}' неверный"
        link = footer_open.get_footer_email_hover().get_attribute("href")
        assert link == self.const.EMAIL_TEXT_HOVER, f"Неверный вызов '{link}'"

    @allure.title(f"F.4 Проверка года © PulseWave, {const.YEAR_COOPERATION} в футере")
    @pytest.mark.parametrize('url', tdata.PAGES_ALL)
    @pytest.mark.smoke
    def test_get_year_cooperation(self, footer_open, url):
        year = int(footer_open.get_footer_cooperation().text[-4:])
        with allure.step(f"Проверить актуальность года элемента '{self.const.TEXT_COOPERATION}'"):
            assert year == self.const.YEAR_COOPERATION, f"Пора поменять год '{year}', \
                уже '{self.const.YEAR_COOPERATION}'"

    @pytest.mark.parametrize('url', tdata.PAGES_ALL)
    @pytest.mark.parametrize('css_property, figma, name', const.CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_footer_email(self, footer_open, css_property, figma, name, url):
        allure.dynamic.title(f"F.5 Проверка {name} надписи '{self.const.EMAIL_TEXT}' в футере")
        mean_css = footer_open.get_footer_email().value_of_css_property(css_property)
        with allure.step(f"Проверить соответствия {name} надписи '{self.const.EMAIL_TEXT}' макету"):
            assert mean_css == figma, \
                f"Не прошла проверка соответствия {name} надписи '{self.const.EMAIL_TEXT}' макету"

    @pytest.mark.parametrize('url', tdata.PAGES_ALL)
    @pytest.mark.parametrize('css_property, figma, name', const.CHECK_TEXT)
    @pytest.mark.regress
    def test_get_css_property_footer_cooperation(self, footer_open, css_property, figma, name, url):
        allure.dynamic.title(f"F.6 Проверка {name} надписи '{self.const.TEXT_COOPERATION}' в футере")
        mean_css = footer_open.get_footer_cooperation().value_of_css_property(css_property)
        with allure.step(f"Проверить соответствия {name} надписи '{self.const.TEXT_COOPERATION}' макету"):
            assert mean_css == figma, \
                f"Не прошла проверка соответствия {name} надписи '{self.const.TEXT_COOPERATION}' макету"

    @pytest.mark.parametrize('url', tdata.PAGES_ALL)
    @pytest.mark.regress
    def test_get_footer_linkedin(self, footer_open, url):
        allure.dynamic.title(f"F.7 Проверка значка LinkedIn на странице '{url}' в футере")
        assert footer_open.get_footer_linkedin(), f"Нет значка LinkedIn на странице '{url}' в футере"

    @pytest.mark.parametrize('url', tdata.PAGES_ALL)
    @pytest.mark.regress
    def test_get_footer_linkedin_is_clickable(self, footer_open, url):
        allure.dynamic.title(f"F.8 Проверка кликабельности значка LinkedIn на странице '{url}' в футере")
        element = footer_open.get_footer_linkedin()
        assert footer_open.element_is_clickable(element), f"Значок LinkedIn некликабельный на странице '{url}' в футере"

    @pytest.mark.parametrize('url', tdata.PAGES_ALL)
    @pytest.mark.regress
    def test_get_footer_linkedin_href(self, footer_open, url):
        allure.dynamic.title(f"F.9 Проверка перехода в LinkedIn на странице '{url}' в футере")
        element = footer_open.get_footer_linkedin()
        li_href = footer_open.element_is_clickable(element).get_attribute('href')
        assert li_href == self.link.LI_URL, f"Нет перехода в LinkedIn на странице '{url}' в футере"
