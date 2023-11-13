import time
import requests
import allure
from data import email1, password0, email2, password3
from tests.test_api.constant import BASE_URL, STATUS_OK, CREATE_USER, NEW_EMAIL, STATUS_CHANGE, STATUS_CREATED


@allure.epic("Тестирование API")
class TestAPI:

    @allure.title("Создать пользователя")
    def test_post_create_user(self):
        url = f'{BASE_URL}auth/users/'
        response = requests.post(url, json=CREATE_USER)
        time.sleep(10)
        assert response.status_code == STATUS_CREATED, \
            f"Expected status {STATUS_CREATED}, actual status {response.status_code}"

    @allure.title("Активация пользователя")
    def test_post_users_activation(self, get_email_tokens):
        url = f'{BASE_URL}auth/users/activation/'
        response = requests.post(url, json={"uid": get_email_tokens[0], "token": get_email_tokens[1]})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Создать пару токенов")
    def test_post_create_jwt(self):
        url = f'{BASE_URL}auth/jwt/create/'
        response = requests.post(url, json={"email": email1, "password": password0})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Обновление JWT access_token")
    def test_post_refresh_jwt(self, create_refresh):
        refresh = create_refresh
        url = f'{BASE_URL}auth/jwt/refresh/'
        response = requests.post(url, json={"refresh": refresh})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Данные пользователя")
    def test_get_auth_users(self, create_jwt):
        jwt = create_jwt
        url = f'{BASE_URL}auth/users/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Получить данные авторизованного пользователя")
    def test_get_auth_user_me(self, create_jwt):
        jwt = create_jwt
        url = f'{BASE_URL}auth/users/me/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        user_id = response.json()['id']
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"
        return user_id

    @allure.title("Данные пользователя по id")
    def test_get_auth_user_id(self, create_jwt, get_user_id):
        jwt = create_jwt
        user_id = get_user_id
        url = f'{BASE_URL}auth/users/{user_id}'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Обновить все данные авторизованного пользователя по id")
    def test_put_auth_user_id(self, create_jwt, get_user_id):
        jwt = create_jwt
        user_id = get_user_id
        url = f'{BASE_URL}auth/users/{user_id}'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Частично обновить данные авторизованного пользователя")
    def test_patch_auth_user_id(self, create_jwt, get_user_id):
        jwt = create_jwt
        user_id = get_user_id
        url = f'{BASE_URL}auth/users/{user_id}'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}",
                                                'name': 'Nata'})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Обновить все данные авторизованного пользователя")
    def test_put_auth_user_me(self, create_jwt):
        jwt = create_jwt
        url = f'{BASE_URL}auth/users/me/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_OK, \
            f"Expected status {STATUS_OK}, actual status {response.status_code}"

    @allure.title("Запрос на смену почты. Пользователю будет отправлена ссылка для подтверждения на указанную почту.")
    def test_post_auth_change_email(self, create_jwt):
        jwt = create_jwt
        url = f'{BASE_URL}auth/change_email/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"}, json=NEW_EMAIL)
        time.sleep(10)
        assert response.status_code == STATUS_CHANGE, \
            f"Expected status {STATUS_CHANGE}, actual status {response.status_code}"

    @allure.title("Подтверждение смены почты пользователя. Токен получить из ссылки auth/change_email/{token}.")
    def test_post_auth_change_email_confirm(self, create_jwt, change_email_confirm_token):
        jwt = create_jwt
        url = f'{BASE_URL}auth/change_email_confirm/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"token": change_email_confirm_token, "email": email2, "password": password0})
        assert response.status_code == STATUS_CHANGE, \
            f"Expected status {STATUS_CHANGE}, actual status {response.status_code}"

    @allure.title("Сброс пароля. Используется на экране входа, если пользователь забыл свой пароль. \
    Пользователю отправится письмо с ссылкой подтверждения.")
    def test_post_auth_users_reset_password(self, create_jwt2):
        jwt = create_jwt2
        url = f'{BASE_URL}auth/users/reset_password/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"email": email2})
        time.sleep(10)
        assert response.status_code == STATUS_CHANGE, \
            f"Expected status {STATUS_CHANGE}, actual status {response.status_code}"

    @allure.title("Подтверждение сброса пароля. Когда пользователь переходит по ссылке \
    auth/password/reset/confirm/{uid}/{token}")
    def test_post_auth_users_reset_password_confirm(self, create_jwt2, get_email_tokens2):
        jwt = create_jwt2
        url = f'{BASE_URL}auth/users/reset_password_confirm/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"uid": get_email_tokens2[0], "token": get_email_tokens2[1],
                                 "new_password": password3, "re_new_password": password3})
        assert response.status_code == STATUS_CHANGE, \
            f"Expected status {STATUS_CHANGE}, actual status {response.status_code}"

    @allure.title("Удалить авторизованного пользователя")
    def test_delete_auth_users_me(self, create_jwt3):
        jwt = create_jwt3
        url = f'{BASE_URL}auth/users/me/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                   json={"current_password": password3})
        assert response.status_code == STATUS_CHANGE, \
            f"Expected status {STATUS_CHANGE}, actual status {response.status_code}"
