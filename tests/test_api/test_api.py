import time
import requests
import allure
from data import email1, password0, email2, password3, password1, password2
from pages.api_page import ApiPage
from tests.test_api.constant import BASE_URL, STATUS_200, CREATE_USER, NEW_EMAIL, STATUS_204, STATUS_201, \
    WORKSPACE, STATUS_400, CREATE_USER_NO_EMAIL, CREATE_USER_NO_PASSWORD, CREATE_USER_NO_SUBSCRIBER, NO_DATA


@allure.epic("Тестирование API")
class TestAPI:

    @allure.title("Создать пользователя")
    def test_post_create_user(self):
        url = f'{BASE_URL}auth/users/'
        response = requests.post(url, json=CREATE_USER)
        time.sleep(5)
        assert response.status_code == STATUS_201, \
            f"Expected status {STATUS_201}, actual status {response.status_code}"

    @allure.title("Активация пользователя")
    def test_post_users_activation(self, use_api_page):
        url = f'{BASE_URL}auth/users/activation/'
        response = requests.post(url, json=use_api_page.get_activate_email_tokens(email1, password1))
        assert response.status_code == STATUS_200, \
            f"Expected status {STATUS_200}, actual status {response.status_code}"

    @allure.title("Попытка создать уже авторизованного пользователя")
    def test_post_create_auth_user(self):
        url = f'{BASE_URL}auth/users/'
        response = requests.post(url, json=CREATE_USER)
        assert response.status_code == STATUS_400, \
            f"Expected status {STATUS_400}, actual status {response.status_code}"

    @allure.title("Создать пару токенов")
    def test_post_create_jwt(self):
        url = f'{BASE_URL}auth/jwt/create/'
        response = requests.post(url, json={"email": email1, "password": password0})
        assert response.status_code == STATUS_200, \
            f"Expected status {STATUS_200}, actual status {response.status_code}"

    @allure.title("Список всех Рабочих пространств авторизованного пользователя")
    def test_get_api_workspace(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{BASE_URL}api/workspace/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        # print(response.json())
        assert response.status_code == STATUS_200, \
            f"Expected status {STATUS_200}, actual status {response.status_code}"

    @allure.title("Список всех досок этого пользователя. Для получения досок конкретного РП нужно передать query "
                  "'space_id': /api/board/?space_id=4")
    def test_get_api_boards(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{BASE_URL}api/boards/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        # print(response.text)
        assert response.status_code == STATUS_200, f"Expected status {STATUS_200}, actual status {response.status_code}"

    @allure.title("Создать Рабочее пространство")
    def test_post_api_workspace(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{BASE_URL}api/workspace/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"}, json=WORKSPACE)
        print(response.text)
        assert response.status_code == STATUS_201, \
            f"Expected status {STATUS_201}, actual status {response.status_code}"

    @allure.title("Список всех пользователей для поиска")
    def test_get_api_user_list(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{BASE_URL}api/user_list/?users=tes'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        print(response.json())
        assert response.status_code == STATUS_200, \
            f"Expected status {STATUS_200}, actual status {response.status_code}"

    @allure.title("Обновление JWT access_token")
    def test_post_refresh_jwt(self, use_api_page):
        refresh = use_api_page.create_refresh(email1, password0)
        url = f'{BASE_URL}auth/jwt/refresh/'
        response = requests.post(url, json={"refresh": refresh})
        assert response.status_code == STATUS_200, \
            f"Expected status {STATUS_200}, actual status {response.status_code}"

    @allure.title("Данные пользователя")
    def test_get_auth_users(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{BASE_URL}auth/users/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_200, \
            f"Expected status {STATUS_200}, actual status {response.status_code}"

    @allure.title("Получить данные авторизованного пользователя")
    def test_get_auth_user_me(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{BASE_URL}auth/users/me/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_200, \
            f"Expected status {STATUS_200}, actual status {response.status_code}"

    @allure.title("Данные пользователя по id")
    def test_get_auth_user_id(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        user_id = use_api_page.get_auth_user_id()
        url = f'{BASE_URL}auth/users/{user_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_200, \
            f"Expected status {STATUS_200}, actual status {response.status_code}"

    @allure.title("Обновить все данные авторизованного пользователя по id")
    def test_put_auth_user_id(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        user_id = use_api_page.get_auth_user_id()
        url = f'{BASE_URL}auth/users/{user_id}/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_200, \
            f"Expected status {STATUS_200}, actual status {response.status_code}"

    @allure.title("Частично обновить данные авторизованного пользователя")
    def test_patch_auth_user_id(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        user_id = use_api_page.get_auth_user_id()
        url = f'{BASE_URL}auth/users/{user_id}/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}",
                                                'name': 'Nata'})
        assert response.status_code == STATUS_200, \
            f"Expected status {STATUS_200}, actual status {response.status_code}"

    @allure.title("Обновить все данные авторизованного пользователя")
    def test_put_auth_user_me(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{BASE_URL}auth/users/me/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        assert response.status_code == STATUS_200, \
            f"Expected status {STATUS_200}, actual status {response.status_code}"

    @allure.title("Запрос на смену почты. Пользователю будет отправлена ссылка для подтверждения на указанную почту.")
    def test_post_auth_change_email(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{BASE_URL}auth/change_email/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"}, json=NEW_EMAIL)
        time.sleep(5)
        assert response.status_code == STATUS_204, \
            f"Expected status {STATUS_204}, actual status {response.status_code}"

    @allure.title("Подтверждение смены почты пользователя. Токен получить из ссылки auth/change_email/{token}.")
    def test_post_auth_change_email_confirm(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{BASE_URL}auth/change_email_confirm/'
        token_email = use_api_page.change_email_confirm_token(email2, password2)
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"token": token_email, "email": email2, "password": password0})
        assert response.status_code == STATUS_204, \
            f"Expected status {STATUS_204}, actual status {response.status_code}"

    @allure.title("Сброс пароля. Используется на экране входа, если пользователь забыл свой пароль. \
    Пользователю отправится письмо с ссылкой подтверждения.")
    def test_post_auth_users_reset_password(self, use_api_page):
        jwt = use_api_page.create_jwt(email2, password0)
        url = f'{BASE_URL}auth/users/reset_password/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"email": email2})
        time.sleep(5)
        assert response.status_code == STATUS_204, \
            f"Expected status {STATUS_204}, actual status {response.status_code}"

    @allure.title("Подтверждение сброса пароля. Когда пользователь переходит по ссылке \
    auth/password/reset/confirm/{uid}/{token}")
    def test_post_auth_users_reset_password_confirm(self, use_api_page):
        jwt = use_api_page.create_jwt(email2, password0)
        page = ApiPage()
        url = f'{BASE_URL}auth/users/reset_password_confirm/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=page.get_confirm_email_tokens(email2, password2) | {
                                 "new_password": password3, "re_new_password": password3})
        assert response.status_code == STATUS_204, \
            f"Expected status {STATUS_204}, actual status {response.status_code}"

    @allure.title("Удалить авторизованного пользователя")
    def test_delete_auth_users_me(self, use_api_page):
        jwt = use_api_page.create_jwt(email2, password3)
        url = f'{BASE_URL}auth/users/me/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                   json={"current_password": password3})
        assert response.status_code == STATUS_204, \
            f"Expected status {STATUS_204}, actual status {response.status_code}"

    @allure.title("Попытка создать пользователя без емайл")
    def test_post_create_user_no_email(self):
        url = f'{BASE_URL}auth/users/'
        response = requests.post(url, json=CREATE_USER_NO_EMAIL)
        assert response.json()["email"] == NO_DATA, \
            f'Expected message: {NO_DATA}, actual message: {response.json()["email"]}'
        assert response.status_code == STATUS_400, \
            f'Expected status {STATUS_400}, actual status {response.status_code}'

    @allure.title("Попытка создать пользователя без пароля")
    def test_post_create_user_no_email(self):
        url = f'{BASE_URL}auth/users/'
        response = requests.post(url, json=CREATE_USER_NO_PASSWORD)
        assert response.json()["password"] == NO_DATA, \
            f'Expected message: {NO_DATA}, actual message: {response.json()["password"]}'
        assert response.status_code == STATUS_400, \
            f"Expected status {STATUS_400}, actual status {response.status_code}"

    @allure.title("Создать пользователя без подтверждения подписки")
    def test_post_create_user_no_subscriber(self, use_api_page):
        url = f'{BASE_URL}auth/users/'
        response = requests.post(url, json=CREATE_USER_NO_SUBSCRIBER)
        time.sleep(5)
        assert response.status_code == STATUS_201, \
            f"Expected status {STATUS_201}, actual status {response.status_code}"

    @allure.title("Активировать и удалить авторизованного пользователя")
    def test_delete_auth_users_me_new(self, use_api_page):
        self.test_post_users_activation(use_api_page)
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{BASE_URL}auth/users/me/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                   json={"current_password": password0})
        assert response.status_code == STATUS_204, \
            f"Expected status {STATUS_204}, actual status {response.status_code}"
