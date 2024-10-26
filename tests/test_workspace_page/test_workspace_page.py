import time

import allure
import pytest
from pages.signup_page import SignUpPage
from tests.constant import Links, Messages
from tests.test_workspace_page.constant import WorkspaceConstant
from pages.workspace_page import WorkspacePage


@pytest.mark.parametrize('browser', Links.SET_OF_BROWSERS)
@allure.epic(f"Тестирование страницы '{WorkspaceConstant.WORKSPACE_TITLE}'")
class TestWorkspacePage:
    const = Links()
    wsconst = WorkspaceConstant()
    message = Messages()

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

    @allure.title("Проверка видимости аватара")
    @pytest.mark.regress
    def test_avatar_is_visible(self, auth_user, driver):
        page = WorkspacePage(driver)
        with allure.step('Проверить заголовок рабочее пространство'):
            assert page.get_avatar_is_visible(), 'Не отображается аватар'

    @allure.title("Проверка что авторизованный пользователь попадает в Рабочие пространства")
    @pytest.mark.regress
    def test_auth_user_into_workspace(self, auth_user, driver):
        url = driver.current_url
        with allure.step('Проверить что авторизованный пользователь попадает в Рабочие пространства'):
            assert url == self.const.WORKSPACE, 'Авторизованный пользователь не попал в Рабочие пространства'

    @allure.title("Проверка что авторизованный пользователь может выйти из аккаунта")
    @pytest.mark.regress
    def test_auth_user_logout(self, auth_user, driver):
        page = SignUpPage(driver)
        page.click_button_avatar()
        page.click_exit_button()
        text = page.get_message_to_exit()
        with allure.step('Проверка что авторизованный пользователь вышел из аккаунта'):
            assert text == self.message.EXIT_CONFIRM_MSG, 'Авторизованный пользователь не вышел из аккаунта'

    @allure.title(f"Проверка перехода в {wsconst.WORKSPACE_TITLE} по ссылке {message.TO_MAIN_TEXT}")
    @pytest.mark.regress
    def test_link_to_main(self, auth_user, driver):
        page = SignUpPage(driver)
        page.click_button_avatar()
        page.click_button_settings()
        page = WorkspacePage(driver)
        text = page.get_link_to_main().text
        with allure.step(f'Проверка текста ссылки {self.message.TO_MAIN_TEXT}'):
            assert text == self.message.TO_MAIN_TEXT, f'ОР: {self.message.TO_MAIN_TEXT}, ФР: {text}'

    @allure.title("Проверка видимости заголовка 'Ваши рабочие пространства'")
    @pytest.mark.regress
    def test_check_right_title(self, auth_user, driver):
        page = WorkspacePage(driver)
        title = page.get_title_main_workspace().text
        with allure.step('Проверить заголовок "Ваши рабочие пространства"'):
            assert title == self.wsconst.MAIN_WORKSPACE_TITLE, 'Не отображается заголовок "Ваши рабочие пространства"'

    @allure.title(f"Проверка видимости  кнопки '{wsconst.READ_ALL_BUTTON_TEXT}'")
    @pytest.mark.regress
    def test_check_read_all_button(self, auth_user, driver):
        page = WorkspacePage(driver)
        page.get_notify_button_is_visible().click()
        text = page.get_read_all_button_is_visible().text
        assert text == self.wsconst.READ_ALL_BUTTON_TEXT, f'Не отображается "{self.wsconst.READ_ALL_BUTTON_TEXT}"'
