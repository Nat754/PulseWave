import allure
import pytest
from tests.constant import Links, MainConstant
from pages.main_page import MainPage


@pytest.mark.smoke
@allure.epic("Тестирование Главной страницы")
class TestMainPage:
    const = MainConstant
    link = Links

    @allure.title("Проверка редиректа с /home на Главную страницу")
    @pytest.mark.regress
    def test_get_redirect_to_main(self, driver):
        page = MainPage(driver)
        url = self.link.MAIN_PAGE_HOME
        driver.get(url)
        page.wait_changed_url(url)
        url = driver.current_url
        assert url == self.link.START_PAGE, "Не произошел редирект на Главную страницу"
