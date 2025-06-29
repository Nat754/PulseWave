import allure
import pytest
from pages.header import HeaderPage
from tests.constant import Links, HeaderConstant, TestData


@allure.epic("Тестирование Хедера")
class TestHeader:
    const = HeaderConstant
    link = Links
    page = HeaderPage
    tdata = TestData

    @allure.title("Проверка некликабельности логотипа на Главной странице")
    @pytest.mark.xfail(reazon='Лого пока кликабельный на лендинге')
    @pytest.mark.regress
    @pytest.mark.parametrize('url', [link.START_PAGE])
    def test_visibility_logo(self, header_open, url):
        assert header_open.get_header_logo_is_not_clickable(), 'Логотип кликабельный на Главной странице'

    @pytest.mark.parametrize('url', tdata.PAGES_APP)
    @allure.title(f"+1.13 Проверка редиректа на главную страницу при клике на логотип")
    @pytest.mark.smoke
    def test_redirect_logo_login(self, header_open, driver, url):
        link = driver.current_url
        header_open.get_header_logo().click()
        header_open.wait_changed_url(link)
        with allure.step("Произошел переход на Главную страницу"):
            assert driver.current_url == self.link.START_PAGE, \
                'Не произошел переход на главную страницу при клике на лого'

    @pytest.mark.parametrize('url', [link.SIGNUP_PAGE, link.PASSWORD_RECOVERY])
    @allure.title(f"+Проверка текста кнопки '{const.TEXT_LOGIN}'")
    @pytest.mark.regress
    def test_get_text_header_auth_login(self, header_open, url):
        text = header_open.get_header_auth_login().text
        with allure.step(f"Текст кнопки '{self.const.TEXT_LOGIN}' соответствует макету"):
            assert text == self.const.TEXT_LOGIN, f"Текст кнопки '{self.const.TEXT_LOGIN}' не соответствует макету"

    @pytest.mark.parametrize('url', [link.LOGIN_PAGE, link.PASSWORD_RECOVERY])
    @allure.title(f"+Проверка текста кнопки '{const.TEXT_SIGNUP}'")
    @pytest.mark.regress
    def test_get_text_header_auth_signup(self, header_open, url):
        text = header_open.get_header_auth_signup().text
        with allure.step(f"+Текст кнопки '{self.const.TEXT_SIGNUP}' соответствует макету"):
            assert text == self.const.TEXT_SIGNUP, \
              f"Текст кнопки '{self.const.TEXT_SIGNUP}' не соответствует макету"

    @pytest.mark.parametrize('url', [link.START_PAGE, link.SIGNUP_PAGE, link.PASSWORD_RECOVERY])
    @allure.title(f"+Проверка перехода на страницу '{link.LOGIN_PAGE}' по кнопке '{const.TEXT_LOGIN}'")
    @pytest.mark.smoke
    def test_get_header_auth_login(self, header_open, driver, url):
        link = driver.current_url
        header_open.get_header_auth_login().click()
        header_open.wait_changed_url(link)
        with allure.step(f"Произошел переход на страницу '{self.link.LOGIN_PAGE}'"):
            assert driver.current_url == self.link.LOGIN_PAGE, f"Произошел переход на страницу '{driver.current_url}'"

    @pytest.mark.parametrize('url', [link.LOGIN_PAGE, link.PASSWORD_RECOVERY])
    @allure.title(f"+1.2 Проверка перехода на страницу '{link.SIGNUP_PAGE}' по кнопке '{const.TEXT_SIGNUP}'")
    @pytest.mark.smoke
    def test_get_header_auth_signup(self, header_open, driver, url):
        link = driver.current_url
        header_open.get_header_auth_signup().click()
        header_open.wait_changed_url(link)
        with allure.step(f"Произошел переход на страницу '{self.link.SIGNUP_PAGE}'"):
            assert driver.current_url == self.link.SIGNUP_PAGE, f"Произошел переход на страницу '{driver.current_url}'"

    @pytest.mark.xfail
    @pytest.mark.parametrize('url', [link.SIGNUP_PAGE, link.PASSWORD_RECOVERY])
    @pytest.mark.parametrize('css_property, figma, name', const.CHECK_BUTTON)
    @pytest.mark.regress
    def test_get_css_property_header_auth_login(self, header_open, css_property, figma, name, url):
        allure.dynamic.title(f"Проверка {name} кнопки '{self.const.TEXT_LOGIN}' в хедере {url}")
        element = header_open.get_header_auth_login()
        mean_css = element.value_of_css_property(css_property)
        with allure.step(f"Прошла проверка соответствия {name} кнопки '{self.const.TEXT_LOGIN}' макету"):
            assert mean_css == figma, f"Не прошла проверка соответствия {name} кнопки '{self.const.TEXT_LOGIN}' макету"

    @pytest.mark.xfail
    @pytest.mark.parametrize('url', [link.LOGIN_PAGE, link.PASSWORD_RECOVERY])
    @pytest.mark.parametrize('css_property, figma, name', const.CHECK_BUTTON)
    @pytest.mark.regress
    def test_get_css_property_header_auth_signup(self, header_open, css_property, figma, name, url):
        allure.dynamic.title(f"Проверка {name} кнопки '{self.const.TEXT_SIGNUP} в хедере {url}'")
        element = header_open.get_header_auth_login()
        mean_css = element.value_of_css_property(css_property)
        with allure.step(f"Прошла проверка соответствия {name} кнопки '{self.const.TEXT_SIGNUP}' макету"):
            assert mean_css == figma, \
                f"Не прошла проверка соответствия {name} кнопки '{self.const.TEXT_SIGNUP}' макету"
