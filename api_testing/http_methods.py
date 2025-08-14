import requests
from api_testing.logger import Logger
from tests.constant import Links


class BaseRequests:

    @staticmethod
    def _send(link: str, data: dict, headers: {}, cookies: {}, method: str):
        url = f"""{Links.BASE_URL}{link}"""

        Logger.add_request(url, data, headers, cookies, method)
        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == "PATCH":
            response = requests.patch(url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"""Bad method '{method}' was received""")
        Logger.add_response(response)
        return response

    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return BaseRequests._send(url, data, headers, cookies, "POST")

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return BaseRequests._send(url, data, headers, cookies, "GET")

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return BaseRequests._send(url, data, headers, cookies, "PUT")

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return BaseRequests._send(url, data, headers, cookies, "DELETE")
