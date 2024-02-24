import datetime
import os
from requests import Response


class Logger:
    log_file_name = 'log_api_test.log'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    logs_dir = os.path.join(project_dir, 'logs')
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    log_file = os.path.join(logs_dir, log_file_name)

    @classmethod
    def _write_log_to_file(cls, data: str):
        with open(cls.log_file, 'a', encoding="utf=8") as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, headers: dict, json: dict, method: str):
        data_to_add = f"***\n\n"
        data_to_add += f'{str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))}\n'
        data_to_add += f"Test name: {os.environ.get('PYTEST_CURRENT_TEST')}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"Request data: {json}\n"
        data_to_add += f"Request headers: {headers}\n"
        # data_to_add += f"Request cookies: {cookies}\n\n"

        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        data_to_add = f"Response code: {response.status_code}\n"
        data_to_add += f"Response json: {response.json()}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n\n"

        cls._write_log_to_file(data_to_add)
