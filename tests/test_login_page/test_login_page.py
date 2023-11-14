import allure
import pytest
from tests.test_login_page.constant import TEXT_LOGIN, LOGIN_PAGE_TITLE, BUTTON_TEXT_SIZE, TITLE_COLOR, \
    TITLE_FONT_FAMILY, CHECK_TITLE


@allure.epic("Тестирование страницы авторизации")
class TestLoginPage:

    @allure.title(f"Проверка текста заголовка '{TEXT_LOGIN}'")
    @pytest.mark.regress
    def test_get_title_login(self, login_page_open):
        title = login_page_open.get_title_login().text
        assert title == LOGIN_PAGE_TITLE, f'Неверный заголовок "{title}"'

    @pytest.mark.parametrize('css_property, mean', CHECK_TITLE)
    @pytest.mark.regress
    def test_get_size_login(self, login_page_open, css_property, mean):
        element = login_page_open.get_title_login()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == mean, f"Свойство {mean_css} элемента не соответствует макету"
