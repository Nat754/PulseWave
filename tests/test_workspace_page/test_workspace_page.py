import allure
import pytest
from tests.constant import Constant


@pytest.mark.parametrize('browser', Constant.SET_OF_BROWSERS)
@allure.epic(f"Тестирование страницы '{Constant.WORKSPACE}'")
class TestWorkspacePage:
    const = Constant

    @allure.title("Проверка перехода в рабочее пространство авторизованного пользователя")
    @pytest.mark.regress
    def test_auth_user_redirect_to_workspace(self, auth_user, driver):
        with allure.step('Авторизоваться пользователем'):
            link = driver.current_url
        with allure.step('Проверить переход в рабочее пространство'):
            assert link == self.const.WORKSPACE, 'Не произошел переход в рабочее пространство'
