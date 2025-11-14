import pytest
import requests
import allure
from api_testing.assertions import Assertions
from tests.api_tests.api_constant import StatusCode
from tests.constant import Links
from data import TELEGRAM_TOKEN, my_chat


@allure.epic("Тестирование Доступности приложения")
@pytest.mark.smoke
class TestAvailability:
    link = Links
    code = StatusCode

    @pytest.mark.availability
    @pytest.mark.parametrize('url', link.AVAILABILITY_URLS)
    def test_get_availability(self, url):
        allure.dynamic.title(f'Проверка доступности {url}')
        try:
            response = requests.get(url)
            Assertions.assert_status_code(response, self.code.STATUS_OK)
            url1 = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
            params = {'chat_id': my_chat, 'text': f'✅ *Сервер {url} доступен* ✅'}
            response = requests.post(url1, data=params)
        except AssertionError:
            url2 = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
            params = {'chat_id': my_chat, 'text': f'❌ *Сервер {url} недоступен* ❌'}
            response = requests.post(url2, data=params)
            Assertions.assert_status_code(response, self.code.STATUS_OK)
