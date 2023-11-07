import requests
import allure

from tests.constant import BASE_URL, STATUS_OK, CREATE_USER, CREATE_JWT, TOKENS, STATUS_IS


@allure.epic("Тестирование API")
class TestAPI:

    @allure.title("Создать пользователя")
    def test_post_create_user(self):
        url = f'{BASE_URL}auth/users/'
        response = requests.post(url, json=CREATE_USER)
        assert response.status_code == STATUS_IS, \
            f"Expected status {STATUS_IS}, actual status {response.status_code}"

    @allure.title("Активация пользователя")
    def test_post_users_activation(self):
        url = f'{BASE_URL}auth/users/activation/'
        response = requests.post(url, json=TOKENS)
        assert response.status_code == STATUS_IS, \
            f"Expected status {STATUS_IS}, actual status {response.status_code}"

    @allure.title("Создать пару токенов")
    def test_post_create_jwt(self):
        url = f'{BASE_URL}auth/jwt/create/'
        response = requests.post(url, json=CREATE_JWT)
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Данные пользователя")
    def test_get_auth_users(self, create_jwt):
        jwt = create_jwt
        url = f'{BASE_URL}auth/users/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Данные пользователя по id")
    def test_get_auth_user_id(self, create_jwt):
        jwt = create_jwt
        url = f'{BASE_URL}auth/users/112'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Получить ссылку на email")
    def test_get_token_on_email(self, get_email_tokens):
        pass
