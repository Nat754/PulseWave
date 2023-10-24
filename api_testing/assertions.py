import json
from requests import Response
from logger.logger import get_logs


logger = get_logs(r"src\utils\assertions")


class Assertion:

    @staticmethod
    def assert_status_code(response: Response, expected_status_code: int):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, \
            logger.error(f"Unexpected status code. Expected: {expected_status_code}, Actual: {actual_status_code}")

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_json = response.json()
            assert name in response_json, logger.error(f"response JSON doesn't have key {name}")
        except json.JSONDecodeError as e:
            logger.error(e)
            logger.error(f"Response is not JSON format. Response text is {response.text}")

