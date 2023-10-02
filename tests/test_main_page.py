import allure
import pytest
from page.main_page import MainPage
from tests.constant import MAIN_PAGE_URL, MAIN_PAGE_TITLE


@allure.epic("Main Page")
class TestMainPage:

    @allure.title("Проверка логотипа на главной странице")
    @pytest.mark.regression
    def test_visibility_logo(self, driver):
        main_page = MainPage(driver)
        driver.get(MAIN_PAGE_URL)
        assert main_page.get_header_logo().text == MAIN_PAGE_TITLE, 'Логотип потерялся'
