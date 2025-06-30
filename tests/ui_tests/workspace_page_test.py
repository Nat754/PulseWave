import time
import allure
import pytest
from selenium.common import TimeoutException
from pages.signup_page import SignUpPage
from tests.constant import Links, Messages, WorkspaceConstant
from pages.workspace_page import WorkspacePage


@allure.epic(f"Тестирование страницы '{WorkspaceConstant.WORKSPACE_TITLE}'")
class TestWorkspacePage:
    const = Links()
    wsconst = WorkspaceConstant()
    message = Messages()

    @allure.title("W1. Проверка перехода в рабочее пространство авторизованного пользователя")
    @pytest.mark.regress
    def test_auth_user_redirect_to_workspace(self, auth_user, driver):
        with allure.step('Авторизоваться пользователем'):
            link = driver.current_url
        with allure.step('Проверить переход в рабочее пространство'):
            assert link == self.const.WORKSPACE, 'Не произошел переход в рабочее пространство'

    @allure.title("W2. Проверка заголовка рабочего пространства")
    @pytest.mark.regress
    def test_auth_user_get_title_workspace(self, auth_user, driver):
        with allure.step('Авторизоваться пользователем'):
            title = driver.title
        with allure.step('Проверить заголовок рабочее пространство'):
            assert title == self.wsconst.WORKSPACE_TITLE, 'Неверный заголовок'

    @allure.title("W3. Проверка видимости аватара")
    @pytest.mark.regress
    def test_avatar_is_visible(self, auth_user, driver):
        page = WorkspacePage(driver)
        with allure.step('Проверить заголовок рабочее пространство'):
            assert page.get_avatar_is_visible(), 'Не отображается аватар'

    @allure.title("W4. Проверка что авторизованный пользователь попадает в Рабочие пространства")
    @pytest.mark.regress
    def test_auth_user_into_workspace(self, auth_user, driver):
        url = driver.current_url
        with allure.step('Проверить что авторизованный пользователь попадает в Рабочие пространства'):
            assert url == self.const.WORKSPACE, 'Авторизованный пользователь не попал в Рабочие пространства'

    @allure.title("W5. Проверка что авторизованный пользователь может выйти из аккаунта")
    @pytest.mark.regress
    def test_auth_user_logout(self, auth_user, driver):
        page = SignUpPage(driver)
        page.click_button_avatar()
        page.click_exit_button()
        text = page.get_message_to_exit()
        with allure.step('Проверка что авторизованный пользователь вышел из аккаунта'):
            assert text == self.message.EXIT_CONFIRM_MSG, 'Авторизованный пользователь не вышел из аккаунта'

    @allure.title(f"W6. Проверка перехода в {wsconst.WORKSPACE_TITLE} по ссылке {message.TO_MAIN_TEXT}")
    @pytest.mark.regress
    def test_link_to_main(self, auth_user, driver):
        page = SignUpPage(driver)
        page.click_button_avatar()
        page.click_button_settings()
        page = WorkspacePage(driver)
        text = page.get_link_to_main().text
        with allure.step(f'Проверка текста ссылки {self.message.TO_MAIN_TEXT}'):
            assert text == self.message.TO_MAIN_TEXT, f'ОР: {self.message.TO_MAIN_TEXT}, ФР: {text}'

    @allure.title("W7. Проверка видимости заголовка 'Ваши рабочие пространства'")
    @pytest.mark.regress
    def test_check_right_title(self, auth_user, driver):
        page = WorkspacePage(driver)
        title = page.get_title_main_workspace().text
        with allure.step('Проверить заголовок "Ваши рабочие пространства"'):
            assert title == self.wsconst.MAIN_WORKSPACE_TITLE, 'Не отображается заголовок "Ваши рабочие пространства"'

    @allure.title(f"W8. Проверка невидимости кнопки '{wsconst.READ_ALL_BUTTON_TEXT}' в прочитанных уведомлениях")
    @pytest.mark.regress
    def test_check_read_all_button_is_not_visible(self, auth_user, driver):
        page = WorkspacePage(driver)
        page.get_notify_button_is_visible().click()
        color = page.get_toggle_is_visible().value_of_css_property('background-color')
        if color == self.wsconst.TOGGLE_COLOR[0]:
            page.get_toggle_is_visible().click()
        assert page.get_read_all_button_is_not_visible(), (f"Кнопка '{self.wsconst.READ_ALL_BUTTON_TEXT}' видна "
                                                           f"в прочитанных уведомлениях")

    @allure.title("W9. Проверка возможности изменить цвет переключателя 'Непрочитанные'")
    @pytest.mark.regress
    def test_check_toggle_read(self, auth_user, driver):
        page = WorkspacePage(driver)
        page.get_notify_button_is_visible().click()
        toggle = page.get_toggle_is_visible()
        color_old = toggle.value_of_css_property('background-color')
        toggle.click()
        time.sleep(1)
        toggle = page.get_toggle_is_visible()
        color_new = toggle.value_of_css_property('background-color')
        assert color_old != color_new, 'Не сменился цвет переключателя уведомлений'

    @allure.title("W10. Проверка цвета переключателя 'Непрочитанные'")
    @pytest.mark.regress
    def test_check_toggle_color(self, auth_user, driver):
        page = WorkspacePage(driver)
        page.get_notify_button_is_visible().click()
        color = page.get_toggle_is_visible().value_of_css_property('background-color')
        assert color in self.wsconst.TOGGLE_COLOR, 'Неверный цвет переключателя уведомлений'

    @allure.title("W11. Проверка видимости уведомлений")
    @pytest.mark.regress
    def test_check_notifications(self, auth_user, driver):
        page = WorkspacePage(driver)
        page.get_notify_button_is_visible().click()
        try:
            notifications = [_.text for _ in page.get_notifications_are_visible()]
        except TimeoutException:
            page.get_toggle_is_visible().click()
            notifications = [_.text for _ in page.get_notifications_are_visible()]
        assert notifications, 'Нет сообщений'

    @allure.title("W12. Проверка прочтения уведомлений")
    @pytest.mark.regress
    def test_check_no_notifications(self, auth_user, driver):
        page = WorkspacePage(driver)
        page.get_notify_button_is_visible().click()
        color = page.get_toggle_is_visible().value_of_css_property('background-color')
        if color == self.wsconst.TOGGLE_COLOR[1]:
            page.get_toggle_is_visible().click()
        try:
            page.get_read_all_button_is_visible().click()
        except TimeoutException:
            pass
        text = page.get_no_notifications_is_visible().text
        assert text == self.wsconst.NO_NOTIFICATIONS, 'Не удалось прочитать уведомления'
