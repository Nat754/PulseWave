import allure
import pytest

from api_testing.api_base import ApiBase
from data import email_auth, password0, emailx, password_auth_email
from tests.constant import Links, Messages, PasswordRecoveryConstant


@allure.epic(f"Тестирование страницы '{PasswordRecoveryConstant.RECOVERY_PAGE_TITLE}'")
class TestPasswordRecoveryPage:
    const = Links
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

    @allure.title(f"3.4 Проверка некликабельности кнопки '{recovery.RESUME_BUTTON_TEXT}'")
    @pytest.mark.regress
    def test_check_resume_button_is_not_clickable_without_email(self, recovery_page_open):
        assert recovery_page_open.check_resume_button_is_not_clickable(), \
            f"Кликабельна кнопка '{self.recovery.RESUME_BUTTON_TEXT}' без заполнения поля емайл"

    @allure.title("Проверить сообщение об отправке ссылки восстановления пароля на емайл")
    @pytest.mark.regress
    def test_fill_correct_email(self, recovery_page_open):
        with allure.step('Заполнить поле емайл'):
            recovery_page_open.fill_email_to_recovery_password(email_auth)
        with allure.step("Нажать кнопку 'Продолжить'"):
            recovery_page_open.click_resume_button()
        text = recovery_page_open.get_message_text()
        ApiBase.read_email(email_auth, password_auth_email)
        assert text == f'{self.message.EMAIL_WAS_SEND} {email_auth} {self.message.GO_TO_EMAIL}', \
            f"ОР: {self.message.EMAIL_WAS_SEND} {email_auth} {self.message.GO_TO_EMAIL}, ФР: {text}"

    @allure.title("3.2, 3.2.1 Восстановить пароль на корректный емайл")
    @pytest.mark.regress
    def test_recovery_password_to_fill_correct_email(self, recovery_page_open, driver):
        with allure.step('Заполнить поле емайл'):
            recovery_page_open.fill_email_to_recovery_password(email_auth)
        with allure.step("Нажать кнопку 'Продолжить'"):
            recovery_page_open.click_resume_button()
        link = recovery_page_open.get_link_recovery_password_by_email()
        driver.get(link)
        with allure.step('Ввести пароль в поле пароль'):
            recovery_page_open.fill_password_recovery(password0)
        with allure.step('Ввести пароль в поле подтверждение пароля'):
            recovery_page_open.fill_confirm_password_recovery(password0)
        with allure.step("Нажать кнопку 'Сохранить пароль'"):
            recovery_page_open.click_resume_button()
        with allure.step("Нажать кнопку 'Ок' - подтвердить переход на страницу авторизации"):
            recovery_page_open.click_resume_button()
        with allure.step('Заполнить поле емайл'):
            recovery_page_open.fill_email_to_recovery_password(email_auth)
        with allure.step('Ввести пароль в поле пароль'):
            recovery_page_open.fill_password_recovery(password0)
        with allure.step("Нажать кнопку 'Войти'"):
            recovery_page_open.click_resume_button()
        recovery_page_open.check_changed_url_login()
        link = driver.current_url
        with allure.step('Проверка успешного перехода в рабочее пространство'):
            assert link == self.const.WORKSPACE, f'ОР: {self.const.WORKSPACE}, ФР: {link}'

    @allure.title("3.3 Восстановить пароль на некорректный емайл")
    @pytest.mark.regress
    def test_recovery_password_to_fill_incorrect_email(self, recovery_page_open, driver):
        with allure.step('Заполнить поле емайл'):
            recovery_page_open.fill_email_to_recovery_password(emailx)
        with allure.step("Нажать кнопку 'Продолжить'"):
            recovery_page_open.click_resume_button()
        text = recovery_page_open.get_invalid_email_message()
        assert text == f'{self.message.NON_EXISTENT_EMAIL}', f"ОР: {self.message.NON_EXISTENT_EMAIL}, ФР: {text}"
