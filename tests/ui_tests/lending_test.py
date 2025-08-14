import allure
import pytest
from tests.constant import Links, LendingConstant
from pages.main_page import MainPage


@allure.epic("Тестирование страницы лендинга")
class TestLendingPage:
    const = LendingConstant
    link = Links

    @allure.title("M.1 Проверка редиректа с /home на страницу лендинга")
    @pytest.mark.regress
    def test_get_redirect_to_lending(self, driver):
        page = MainPage(driver)
        url = self.link.MAIN_PAGE_HOME
        driver.get(url)
        page.wait_changed_url(url)
        url = driver.current_url
        assert url == self.link.START_PAGE, "Не произошел редирект на Главную страницу"
