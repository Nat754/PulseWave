import allure
import pytest
from tests.constant import Links, LendingConstant
from pages.lending_page import LendingPage


@pytest.mark.smoke
@allure.epic("Тестирование страницы лендинга")
class TestLendingPage:
    const = LendingConstant
    link = Links

    @allure.title("M.1 Проверка редиректа с /home на страницу лендинга")
    @pytest.mark.smoke
    def test_get_redirect_to_lending(self, driver):
        page = LendingPage(driver)
        url = self.link.MAIN_PAGE_HOME
        driver.get(url)
        page.wait_changed_url(url)
        url = driver.current_url
        assert url == self.link.START_PAGE, "Не произошел редирект на Главную страницу"

    @pytest.mark.smoke
    @allure.title("M.2 Проверка кликабельности логотипа на лендинге")
    @pytest.mark.parametrize('url', [link.START_PAGE])
    def test_visibility_logo(self, lending_open, url):
        assert lending_open.get_lending_logo_is_clickable(), 'Логотип кликабельный на Главной странице'

    @pytest.mark.smoke
    @allure.title(f"M.3 Проверка текста кнопки '{const.TEXT_LOGIN}' на лендинге")
    @pytest.mark.parametrize('url', [link.START_PAGE])
    def test_visibility_auth_text(self, lending_open, url):
        assert lending_open.get_lending_auth_login().text == self.const.TEXT_LOGIN, \
            'Неверный текст кнопки'

    @pytest.mark.smoke
    @allure.title(f"M.4 Проверка текста кнопки '{const.TEXT_AUTH_FREE}' на лендинге")
    @pytest.mark.parametrize('url', [link.START_PAGE])
    def test_visibility_auth_free(self, lending_open, url):
        assert lending_open.get_lending_auth_free().text == self.const.TEXT_AUTH_FREE, \
            'Неверный текст кнопки'
