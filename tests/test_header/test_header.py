import allure
import pytest
from tests.constant import Links
from tests.test_header.constant import HeaderConstant


@pytest.mark.parametrize('browser', Links.SET_OF_BROWSERS)
@allure.epic("Тестирование Хедера")
class TestHeader:
    header = HeaderConstant()
    const = Links()

    @pytest.mark.parametrize('url', [const.MAIN_PAGE])
    @allure.title("Проверка некликабельности логотипа на Главной странице")
    @pytest.mark.smoke
    def test_visibility_logo(self, header_open, driver, url):
        header_open.get_header_logo_is_not_clickable()
        with ((allure.step("Логотип некликабельный на Главной странице"))):
            assert driver.current_url == self.const.MAIN_PAGE, \
              'Произошел переход на другую страницу при клике на лого'

    @pytest.mark.parametrize('url', [const.LOGIN_PAGE, const.SIGNUP_PAGE, const.PASSWORD_RECOVERY])
    @allure.title(f"1.13 Проверка редиректа на главную страницу при клике на логотип")
    @pytest.mark.smoke
    def test_redirect_logo_login(self, header_open, driver, url):
        link = driver.current_url
        header_open.get_header_logo().click()
        header_open.wait_changed_url(link)
        with allure.step("Произошел переход на Главную страницу"):
            assert driver.current_url == self.const.MAIN_PAGE, \
                'Не произошел переход на главную страницу при клике на лого'

    @pytest.mark.parametrize('url', [const.MAIN_PAGE, const.SIGNUP_PAGE, const.PASSWORD_RECOVERY])
    @allure.title(f"Проверка текста кнопки '{header.TEXT_LOGIN}'")
    @pytest.mark.regress
    def test_get_text_header_auth_login(self, header_open, url):
        text = header_open.get_header_auth_login().text
        with allure.step(f"Текст кнопки '{self.header.TEXT_LOGIN}' соответствует макету"):
            assert text == self.header.TEXT_LOGIN, f"Текст кнопки '{self.header.TEXT_LOGIN}' не соответствует макету"

    @pytest.mark.parametrize('url', [const.MAIN_PAGE, const.LOGIN_PAGE, const.PASSWORD_RECOVERY])
    @allure.title(f"Проверка текста кнопки '{header.TEXT_SIGNUP}'")
    @pytest.mark.regress
    def test_get_text_header_auth_signup(self, header_open, url):
        text = header_open.get_header_auth_signup().text
        with allure.step(f"Текст кнопки '{self.header.TEXT_SIGNUP}' соответствует макету"):
            assert text == self.header.TEXT_SIGNUP, \
              f"Текст кнопки '{self.header.TEXT_SIGNUP}' не соответствует макету"

    @pytest.mark.parametrize('url', [const.MAIN_PAGE, const.SIGNUP_PAGE, const.PASSWORD_RECOVERY])
    @allure.title(f"Проверка перехода на страницу '{const.LOGIN_PAGE}' по кнопке '{header.TEXT_LOGIN}'")
    @pytest.mark.smoke
    def test_get_header_auth_login(self, header_open, driver, url):
        link = driver.current_url
        header_open.get_header_auth_login().click()
        header_open.wait_changed_url(link)
        with allure.step(f"Произошел переход на страницу '{self.const.LOGIN_PAGE}'"):
            assert driver.current_url == self.const.LOGIN_PAGE, f"Произошел переход на страницу '{driver.current_url}'"

    @pytest.mark.parametrize('url', [const.MAIN_PAGE, const.LOGIN_PAGE, const.PASSWORD_RECOVERY])
    @allure.title(f"1.2 Проверка перехода на страницу '{const.SIGNUP_PAGE}' по кнопке '{header.TEXT_SIGNUP}'")
    @pytest.mark.smoke
    def test_get_header_auth_signup(self, header_open, driver, url):
        link = driver.current_url
        header_open.get_header_auth_signup().click()
        header_open.wait_changed_url(link)
        with allure.step(f"Произошел переход на страницу '{self.const.SIGNUP_PAGE}'"):
            assert driver.current_url == self.const.SIGNUP_PAGE, f"Произошел переход на страницу '{driver.current_url}'"

    @pytest.mark.parametrize('url', [const.MAIN_PAGE, const.SIGNUP_PAGE, const.PASSWORD_RECOVERY])
    @pytest.mark.parametrize('css_property, figma, name', header.CHECK_BUTTON)
    @pytest.mark.regress
    def test_get_css_property_header_auth_login(self, header_open, css_property, figma, name, url):
        allure.dynamic.title(f"Проверка {name} кнопки '{self.header.TEXT_LOGIN}' в хедере {url}")
        element = header_open.get_header_auth_login()
        mean_css = element.value_of_css_property(css_property)
        with allure.step(f"Прошла проверка соответствия {name} кнопки '{self.header.TEXT_LOGIN}' макету"):
            assert mean_css == figma, f"Не прошла проверка соответствия {name} кнопки '{self.header.TEXT_LOGIN}' макету"

    @pytest.mark.parametrize('url', [const.MAIN_PAGE, const.LOGIN_PAGE, const.PASSWORD_RECOVERY])
    @pytest.mark.parametrize('css_property, figma, name', header.CHECK_BUTTON)
    @pytest.mark.regress
    def test_get_css_property_header_auth_signup(self, header_open, css_property, figma, name, url):
        allure.dynamic.title(f"Проверка {name} кнопки '{self.header.TEXT_SIGNUP} в хедере {url}'")
        element = header_open.get_header_auth_login()
        mean_css = element.value_of_css_property(css_property)
        with allure.step(f"Прошла проверка соответствия {name} кнопки '{self.header.TEXT_SIGNUP}' макету"):
            assert mean_css == figma, \
                f"Не прошла проверка соответствия {name} кнопки '{self.header.TEXT_SIGNUP}' макету"
