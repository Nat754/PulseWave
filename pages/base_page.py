import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 60

    @allure.step('Проверить видимость элемента')
    def element_is_visible(self, locator):
        """
        Проверка того, что элемент присутствует в DOM-дереве, не только отображается,
        но также имеет высоту и ширину больше 0.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        """
        element = self.element_is_present(locator)
        self.go_to_element(element)
        return Wait(self.driver, self.timeout).until(es.visibility_of_element_located(locator))

    @allure.step('Проверить видимость группы элементов')
    def elements_are_visible(self, locator):
        """
        Проверка того, что элементы присутствуют в DOM-дереве, не только отображаются,
        но также имеет высоту и ширину больше 0.
        Локатор - используется для поиска элементов. Возвращает WebElements.
        """
        return Wait(self.driver, self.timeout).until(es.visibility_of_all_elements_located(locator))

    @allure.step('Проверить присутствие элемента в DOM')
    def element_is_present(self, locator):
        """
        Проверка того, что элемент присутствует в DOM-дереве, но не обязательно отображается на странице.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        """
        return Wait(self.driver, self.timeout).until(es.presence_of_element_located(locator))

    @allure.step('Проверить присутствие группы элементов в DOM')
    def elements_are_present(self, locator):
        """
        Проверка того, что элементы присутствуют в DOM-дереве, но не обязательно,
        что видны и отображаются на странице.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        return Wait(self.driver, self.timeout).until(es.presence_of_all_elements_located(locator))

    @allure.step('Проверить невидимость, но присутствие элемента в DOM')
    def element_is_not_visible(self, locator):
        """
        Проверка того, что элемент является невидимым. Элемент присутствует в DOM-дереве.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        Timeout - время в течение которого он будет ожидать.
        """
        return Wait(self.driver, self.timeout).until(es.invisibility_of_element_located(locator))

    @allure.step('Проверить кликабельность элемента')
    def element_is_clickable(self, locator):
        """
        Проверка того, что элемент виден, отображается на странице, кликабелен.
        Элемент присутствует в DOM-дереве. Локатор - используется для поиска элемента.
        """
        self.element_is_visible(locator)
        return Wait(self.driver, self.timeout).until(es.element_to_be_clickable(locator))

    @allure.step('Проскролить до элемента')
    def go_to_element(self, element):
        """
        Скролит страницу к выбранному элементу так, чтобы элемент стал видимым
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Проверка количества открытых окон в браузере')
    def check_number_of_windows_to_be_equal(self, number):
        """Проверка количества открытых окон в браузере (number)"""
        return Wait(self.driver, self.timeout).until(es.number_of_windows_to_be(number))

    @allure.step('Переместить курсор мыши к центру элемента, показывая ховер')
    def action_move_to_element(self, element):
        """Этот метод перемещает курсор мыши к центру элемента, показывая ховер."""
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @allure.step('Проверка CSS свойства элемента')
    def check_element_css_style(self, locator, css_property):
        """Проверяет CSS свойство элемента {css_property}"""
        element = self.element_is_visible(locator)  # Get the WebElement using locator
        Wait(self.driver, self.timeout).until(self.action_move_to_element(element))  # Move to the element
        return element.value_of_css_property(css_property)

    @allure.step('Проверка смены url')
    def wait_changed_url(self, url):
        """Проверка смены url"""
        try:
            Wait(self.driver, self.timeout).until(es.url_changes(url))
            return self.driver.current_url
        except TimeoutException:
            return False

    @allure.step('Проверка некликабельности видимого элемента')
    def element_is_not_clickable(self, locator):
        """
        Проверка того, что элемент виден, отображается на странице, но некликабелен.
        Элемент присутствует в DOM-дереве. Локатор - используется для поиска элемента.
        """
        self.timeout = 2
        try:
            Wait(self.driver, self.timeout).until(es.element_to_be_clickable(locator))
            return False
        except TimeoutException:
            return True
