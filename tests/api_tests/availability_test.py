from tests.constant import TestData
import pytest
import requests
import allure
from api_testing.assertions import Assertions
from tests.api_tests.api_constant import ApiConstant, StatusCode
from tests.constant import Links


@allure.epic("Тестирование Доступности приложения")
@pytest.mark.smoke
class TestAvailability:
    link = Links
    constant = ApiConstant
    code = StatusCode
    test_data = TestData

    @pytest.mark.availability
    @pytest.mark.parametrize('url', [link.MAIN_PAGE, link.START_PAGE])
    def test_get_availability(self, url):
        allure.dynamic.title(f'Проверка доступности {url}')
        response = requests.get(url)
        Assertions.assert_status_code(response, self.code.STATUS_OK)
