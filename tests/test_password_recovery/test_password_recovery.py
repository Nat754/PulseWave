import time

import allure
import pytest

from data import email_auth
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

    @pytest.mark.parametrize('css_property, figma, name', recovery.CHECK_TITLE)
    @pytest.mark.regress
    def test_get_css_property_recovery_title(self, recovery_page_open, css_property, figma, name):
        allure.dynamic.title(f"Проверка {name} заголовка '{self.recovery.RECOVERY_PAGE_TITLE}'")
        element = recovery_page_open.get_title_recovery()
        mean_css = element.value_of_css_property(css_property)
        assert mean_css == figma, \
            f"Не прошла проверка соответствия {name} заголовка '{self.recovery.RECOVERY_PAGE_TITLE}' макету"

    @allure.title(f"Проверка некликабельности кнопки '{recovery.RESUME_BUTTON_TEXT}'")
    @pytest.mark.regress
    def test_check_resume_button_is_not_clickable_without_email(self, recovery_page_open):
        assert recovery_page_open.check_resume_button_is_not_clickable(), \
            f"Кликабельна кнопка '{self.recovery.RESUME_BUTTON_TEXT}' без заполнения поля емайл"

    @allure.title("Восстановить пароль на корректный емайл")
    @pytest.mark.regress
    def test_fill_correct_email(self, recovery_page_open):
        recovery_page_open.fill_email_to_recovery_password(email_auth)
        recovery_page_open.click_resume_button()
        text = recovery_page_open.get_message_text()
        assert text == f'{self.message.EMAIL_WAS_SEND} {email_auth} {self.message.GO_TO_EMAIL}', \
            f"ОР: {self.message.EMAIL_WAS_SEND} {email_auth} {self.message.GO_TO_EMAIL}, ФР: {text}"
