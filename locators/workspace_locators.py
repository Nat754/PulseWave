from selenium.webdriver.common.by import By


class WorkspaceLocators:

    AVATAR_ICON = (By.CLASS_NAME, 'avatar__icon')
    DROP_WORKSPACES = (By.CLASS_NAME, 'desctop')
    DROP_CREATE = (By.CLASS_NAME, 'create')
    LEFT_MENU_TITLE = (By.CLASS_NAME, 'title-wrapper')
    LEFT_MENU = (By.CSS_SELECTOR, 'span[class="name"]')
    LEFT_MENU_LETTER = (By.CLASS_NAME, 'name-letter')
    RIGHT_MENU = (By.CSS_SELECTOR, 'div[class="name"]')
    TO_MAIM_LINK = (By.CLASS_NAME, 'navigation__item-home')
