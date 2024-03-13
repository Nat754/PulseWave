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
