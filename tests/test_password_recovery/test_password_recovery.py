import allure
import pytest
from tests.constant import Constant, Messages
from tests.test_password_recovery.constant import PasswordRecoveryConstant


@allure.epic(f"Тестирование страницы '{PasswordRecoveryConstant.RECOVERY_PAGE_TITLE}'")
class TestLoginPage:
    const = Constant
    recovery = PasswordRecoveryConstant
    message = Messages

    @allure.title(f"Проверка текста заголовка '{recovery.RECOVERY_PAGE_TITLE}'")
    @pytest.mark.regress
    def test_get_title_recovery(self, recovery_page_open):
        title = recovery_page_open.get_title_recovery().text
        assert title == self.recovery.RECOVERY_PAGE_TITLE, f'Неверный заголовок "{title}"'
