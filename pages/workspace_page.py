from pages.base_page import BasePage
import allure
from locators.workspace_locators import WorkspaceLocators


class WorkspacePage(BasePage):
    locator = WorkspaceLocators()

    @allure.step(f"Проверка видимости аватара на главной странице")
    def get_avatar_is_visible(self):
        return self.element_is_present(self.locator.AVATAR_ICON)

    @allure.step(f"Проверка видимости ссылки 'На главную'")
    def get_link_to_main(self):
        return self.element_is_visible(self.locator.TO_MAIM_LINK)

    @allure.step(f"Проверка видимости заголовка 'Ваши рабочие пространства'")
    def get_title_main_workspace(self):
        return self.element_is_visible(self.locator.RIGHT_TITLE)

    @allure.step(f"Проверка отсутствия лоадера")
    def loader_is_not_visible(self):
        return self.element_is_not_visible(self.locator.LOADER)

    @allure.step(f"Проверка видимости колокольчика уведомлений на главной странице")
    def get_notify_button_is_visible(self):
        self.element_is_present(self.locator.NOTIFY)
        return self.element_is_clickable(self.locator.NOTIFY)

    @allure.step(f"Проверка видимости кнопки 'Отметить все как прочитанные'")
    def get_read_all_button_is_visible(self):
        return self.element_is_present(self.locator.READ_ALL_BUTTON)
