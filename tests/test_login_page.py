import allure
import pytest
from tests.constant import TEXT_LOGIN, LOGIN_PAGE_TITLE, BUTTON_TEXT_SIZE, PULSEWAVE_COLOR


@allure.epic("Тестирование страницы авторизации")
class TestLoginPage:

    @allure.title(f"Проверка текста заголовка '{TEXT_LOGIN}'")
    @pytest.mark.smoke
    def test_get_title_login(self, login_page_open):
        title = login_page_open.get_title_login().text
        assert title == LOGIN_PAGE_TITLE, f'Неверный заголовок "{title}"'

    @allure.title(f"Проверка размера заголовка '{TEXT_LOGIN}'")
    @pytest.mark.smoke
    def test_get_size_login(self, login_page_open):
        element = login_page_open.get_title_login()
        size = element.value_of_css_property("font-size")
        assert size == BUTTON_TEXT_SIZE, f"Размер текста кнопки '{TEXT_LOGIN}' не соответствует макету"

    @allure.title(f"Проверка цвета текста заголовка '{TEXT_LOGIN}'")
    @pytest.mark.smoke
    def test_get_color_login(self, login_page_open):
        element = login_page_open.get_title_login()
        color = element.value_of_css_property("color")
        assert color == PULSEWAVE_COLOR, f"Цвет текста кнопки '{TEXT_LOGIN}' не соответствует макету"
