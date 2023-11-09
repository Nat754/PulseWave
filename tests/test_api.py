import requests
import allure

from tests.constant import BASE_URL, STATUS_OK, CREATE_USER, CREATE_JWT, TOKENS, STATUS_IS, NEW_EMAIL, STATUS_CHANGE, \
    RESET_PASSWRD


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

    @allure.title("Обновить все данные авторизованного пользователя")
    def test_put_auth_user_id(self, create_jwt):
        jwt = create_jwt
        url = f'{BASE_URL}auth/users/112'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Частично обновить данные авторизованного пользователя")
    def test_patch_auth_user_id(self, create_jwt):
        jwt = create_jwt
        url = f'{BASE_URL}auth/users/112'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Получить ссылку на email")
    def test_get_token_on_email(self, get_email_tokens):
        pass

    @allure.title("Получить данные авторизованного пользователя")
    def test_get_auth_user_me(self, create_jwt):
        jwt = create_jwt
        url = f'{BASE_URL}auth/users/me/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Обновить все данные авторизованного пользователя")
    def test_put_auth_user_me(self, create_jwt):
        jwt = create_jwt
        url = f'{BASE_URL}auth/users/me/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        print(response.text)
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Запрос на смену почты. Пользователю будет отправлена ссылка для подтверждения на указанную почту.")
    def test_post_auth_change_email(self, create_jwt):
        jwt = create_jwt
        url = f'{BASE_URL}auth/change_email/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"}, json=NEW_EMAIL)
        print(response.text)
        assert response.status_code == STATUS_CHANGE, \
            f"Expected status {STATUS_CHANGE}, actual status {response.status_code}"

    @allure.title("Сброс пароля. Используется на экране входа, если пользователь забыл свой пароль. \
    Пользователю отправится письмо с ссылкой подтверждения.")
    def test_post_auth_users_reset_password(self, create_jwt):
        jwt = create_jwt
        url = f'{BASE_URL}auth/users/reset_password/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=RESET_PASSWRD)
        print(response.text)
        assert response.status_code == STATUS_CHANGE, \
            f"Expected status {STATUS_CHANGE}, actual status {response.status_code}"
