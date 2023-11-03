import allure
import pytest
from tests.constant import TEXT_LOGIN, LOGIN_PAGE_TITLE


@allure.epic(f"Тестирование страницы '{TEXT_LOGIN}'")
class TestLoginPage:

    @allure.title(f"Проверка текста заголовка '{TEXT_LOGIN}'")
    @pytest.mark.smoke
    def test_get_title_login(self, login_page_open):
        title = login_page_open.get_title_login().text
        assert title == LOGIN_PAGE_TITLE, f'Неверный заголовок "{title}"'
