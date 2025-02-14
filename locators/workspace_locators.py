from selenium.webdriver.common.by import By


class WorkspaceLocators:

    AVATAR_ICON = (By.CLASS_NAME, 'avatar')
    DROP_WORKSPACES = (By.CLASS_NAME, 'desctop')
    DROP_CREATE = (By.CLASS_NAME, 'create')
    LEFT_MENU_TITLE = (By.CLASS_NAME, 'title-wrapper')
    LEFT_MENU = (By.CSS_SELECTOR, 'span[class="name"]')
    LEFT_MENU_LETTER = (By.CLASS_NAME, 'name-letter')
    RIGHT_MENU = (By.CSS_SELECTOR, 'div[class="name"]')
    # TO_MAIM_LINK = (By.CLASS_NAME, 'navigation__item-home')
    TO_MAIM_LINK = (By.CLASS_NAME, 'navigat__item-home')
    RIGHT_TITLE = (By.CSS_SELECTOR, '.workspaces__content h2.title')
    LOADER = (By.CSS_SELECTOR, '.loader .icon')
    NOTIFY = (By.CLASS_NAME, 'notify')
    READ_ALL_BUTTON = (By.CLASS_NAME, 'read-all')
    TOGGLE = (By.CLASS_NAME, 'styled-toggle')
    NOTIFICATIONS = (By.CLASS_NAME, 'notification__text')
    NO_NOTIFICATIONS = (By.CLASS_NAME, 'no-notifications')
