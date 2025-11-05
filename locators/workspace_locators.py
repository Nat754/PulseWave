from selenium.webdriver.common.by import By


class WorkspaceLocators:
    AVATAR_ICON = (By.ID, 'v-3')
    WORKSPACES_BUTTON = (By.ID, 'v-0')
    WORKSPACES_DROP = (By.CSS_SELECTOR, '.body .item')
    CREATE_BUTTON = (By.ID, 'v-1')
    LEFT_MENU_TITLE = (By.CLASS_NAME, 'title-wrapper')
    LEFT_MENU = (By.CSS_SELECTOR, 'span[class="name"]')
    LEFT_MENU_LETTER = (By.CLASS_NAME, 'name-letter')
    RIGHT_MENU = (By.CSS_SELECTOR, 'div[class="name"]')
    TO_MAIM_LINK = (By.CLASS_NAME, 'navigat__item-home')
    RIGHT_TITLE = (By.CSS_SELECTOR, '.workspaces__content h2.title')
    LOADER = (By.CSS_SELECTOR, '.loader .icon')
    NOTIFY = (By.ID, 'v-2')
    READ_ALL_BUTTON = (By.CLASS_NAME, 'read-all')
    TOGGLE = (By.CLASS_NAME, 'styled-toggle')
    NOTIFICATIONS = (By.CLASS_NAME, 'notification__text')
    NO_NOTIFICATIONS = (By.CLASS_NAME, 'no-notifications')
