from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = Wait(driver, 15, 1)

    def element_is_visible(self, locator):
        """
        Проверка того, что элемент присутствует в DOM-дереве, не только отображается,
        но также имеет высоту и ширину больше 0.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        """
        self.go_to_element(self.element_is_present(locator))
        return self.wait.until(es.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        """
        Проверка того, что элементы присутствуют в DOM-дереве, не только отображаются,
        но также имеет высоту и ширину больше 0.
        Локатор - используется для поиска элементов. Возвращает WebElements.
        """
        return self.wait.until(es.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator):
        """
        Проверка того, что элемент присутствует в DOM-дереве, но не обязательно отображается на странице.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        """
        return self.wait.until(es.presence_of_element_located(locator))

    def elements_are_present(self, locator):
        """
        Проверка того, что элементы присутствуют в DOM-дереве, но не обязательно,
        что видны и отображаются на странице.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        Timeout - время в течение которого он будет ожидать. По умолчанию стоит 5 секунд,
        при необходимости можно будет изменить.
        """
        return self.wait.until(es.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator):
        """
        Проверка того, что элемент является невидимым. Элемент присутствует в DOM-дереве.
        Локатор - используется для поиска элемента. Возвращает WebElement.
        Timeout - время в течение которого он будет ожидать.
        """
        return self.wait.until(es.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator):
        """
        Проверка того, что элемент виден, отображается на странице, кликабелен.
        Элемент присутствует в DOM-дереве. Локатор - используется для поиска элемента.
        """
        return self.wait.until(es.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """
        Скролит страницу к выбранному элементу так, чтобы элемент стал видимым
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def check_number_of_windows_to_be_equal(self, number):
        """Проверка количества открытых окон в браузере (number)"""
        return self.wait.until(es.number_of_windows_to_be(number))

    def action_move_to_element(self, element):
        """Этот метод перемещает курсор мыши к центру элемента, показывая ховер."""
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def check_element_css_style(self, locator, css_property):
        """Проверяет CSS свойство элемента"""
        element = self.element_is_visible(locator)  # Get the WebElement using locator
        self.wait.until(self.action_move_to_element(element))  # Move to the element
        return element.value_of_css_property(css_property)
