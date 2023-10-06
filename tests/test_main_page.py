import allure
import pytest
from page.main_page import MainPage
from tests.constant import MAIN_PAGE_URL, MAIN_PAGE_TITLE, WORKSPACE


@allure.epic("Main Page")
class TestMainPage:

    @allure.title("Проверка видимости логотипа на главной странице")
    @pytest.mark.regression
    def test_visibility_logo(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_URL)
        assert main_page.get_header_logo().text == MAIN_PAGE_TITLE, 'Логотип потерялся'

    @allure.title("Проверка перехода на страницу 'Рабочее пространство'")
    @pytest.mark.regression
    def test_redirect_workspace(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_URL)
        main_page.get_header_workspace().click()
        assert driver.current_url == WORKSPACE, "'Переход на страницу 'Рабочее пространство' не произошел"
