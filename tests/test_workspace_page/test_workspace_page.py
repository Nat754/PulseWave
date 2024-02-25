import allure
import pytest
from tests.constant import Constant
from tests.test_workspace_page.constant import WorkspaceConstant


@pytest.mark.parametrize('browser', Constant.SET_OF_BROWSERS)
@allure.epic(f"Тестирование страницы '{Constant.WORKSPACE}'")
class TestWorkspacePage:
    const = Constant
    wsconst = WorkspaceConstant

    @allure.title("Проверка перехода в рабочее пространство авторизованного пользователя")
    @pytest.mark.regress
    def test_auth_user_redirect_to_workspace(self, auth_user, driver):
        with allure.step('Авторизоваться пользователем'):
            link = driver.current_url
        with allure.step('Проверить переход в рабочее пространство'):
            assert link == self.const.WORKSPACE, 'Не произошел переход в рабочее пространство'

    @allure.title("Проверка заголовка рабочего пространства")
    @pytest.mark.regress
    def test_auth_user_get_title_workspace(self, auth_user, driver):
        with allure.step('Авторизоваться пользователем'):
            title = driver.title
        with allure.step('Проверить заголовок рабочее пространство'):
            assert title == self.wsconst.WORKSPACE_TITLE, 'Неверный заголовок'
