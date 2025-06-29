import allure
import pytest
from tests.constant import Links, MainConstant


@allure.epic("Тестирование Главной страницы")
class TestMainPage:
    main = MainConstant()
    const = Links()

    @allure.title("Проверка редиректа на Главную страницу")
    @pytest.mark.regress
    def test_get_redirect_to_main(self, driver):
        driver.get(Links.MAIN_PAGE_HOME)
        url = driver.current_url
        assert url == self.const.START_PAGE, "Не произошел редирект"
