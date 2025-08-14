from pages.base_page import BasePage
import allure
from tests.constant import FooterConstant, MainConstant
from locators.main_locators import MainPageLocators


class MainPage(BasePage):
    main = MainConstant
    footer = FooterConstant
    locator = MainPageLocators
