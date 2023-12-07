import time
import requests
import allure
from data import email1, password0, email2, password3, password1, password2
from pages.api_page import ApiPage
from tests.test_api.api_constant import ApiConstant, StatusCode


@allure.epic("Тестирование API")
class TestAPI:
    constant = ApiConstant()
    code = StatusCode()

    @allure.title("POST Создать пользователя с корректными данными")
    def test_post_create_user(self):
        url = f'{self.constant.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER)
        time.sleep(5)
        with allure.step(f"Expected status {self.code.STATUS_201}"):
            assert response.status_code == self.code.STATUS_201, \
                f"Expected status {self.code.STATUS_201}, actual status {response.status_code}"

    @allure.title("POST Активация пользователя с корректными данными")
    def test_post_users_activation(self, use_api_page):
        url = f'{self.constant.BASE_URL}auth/users/activation/'
        response = requests.post(url, json=use_api_page.get_activate_email_tokens(email1, password1))
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("POST Регистрация ранее зарегистрированного пользователя")
    def test_post_create_auth_user(self):
        url = f'{self.constant.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER)
        with allure.step(f"Expected status {self.code.STATUS_400}"):
            assert response.status_code == self.code.STATUS_400, \
                f"Expected status {self.code.STATUS_400}, actual status {response.status_code}"

    @allure.title("POST Создать пару токенов access и refresh")
    def test_post_create_jwt(self):
        url = f'{self.constant.BASE_URL}auth/jwt/create/'
        response = requests.post(url, json={"email": email1, "password": password0})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("POST Получить список всех Рабочих пространств авторизованного пользователя")
    def test_get_api_workspace(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}api/workspace/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        # print(response.json())
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("GET Получить список всех досок авторизованного пользователя")
    def test_get_api_boards(self, use_api_page):
        """Для получения досок конкретного РП нужно передать query 'space_id': /api/board/?space_id=4"""
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}api/boards/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        # print(response.text)
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
        actual status {response.status_code}"

    @allure.title("POST Создать Рабочее пространство")
    def test_post_api_workspace(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}api/workspace/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=self.constant.WORKSPACE)
        # print(response.text)
        with allure.step(f"Expected status {self.code.STATUS_201}"):
            assert response.status_code == self.code.STATUS_201, \
                f"Expected status {self.code.STATUS_201}, actual status {response.status_code}"

    @allure.title("GET Получить список всех пользователей для поиска")
    def test_get_api_user_list(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}api/user_list/?users=tes'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        # print(response.json())
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("POST Обновить JWT access_token авторизованного пользователя")
    def test_post_refresh_jwt(self, use_api_page):
        url = f'{self.constant.BASE_URL}auth/jwt/refresh/'
        refresh = use_api_page.create_refresh(email1, password0)
        response = requests.post(url, json={"refresh": refresh})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("GET Получить данные авторизованного пользователя")
    def test_get_auth_users(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}auth/users/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("GET Получить данные авторизованного пользователя me")
    def test_get_auth_user_me(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}auth/users/me/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("GET Получить данные авторизованного пользователя по id")
    def test_get_auth_user_id(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        user_id = use_api_page.get_auth_user_id()
        url = f'{self.constant.BASE_URL}auth/users/{user_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("PUT Обновить все данные авторизованного пользователя по id")
    def test_put_auth_user_id(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        user_id = use_api_page.get_auth_user_id()
        url = f'{self.constant.BASE_URL}auth/users/{user_id}/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("PATCH Частично обновить данные авторизованного пользователя")
    def test_patch_auth_user_id(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        user_id = use_api_page.get_auth_user_id()
        url = f'{self.constant.BASE_URL}auth/users/{user_id}/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}",
                                                'name': 'Nata'})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("PUT Обновить все данные авторизованного пользователя me")
    def test_put_auth_user_me(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}auth/users/me/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("POST Запрос на смену почты")
    def test_post_auth_change_email(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}auth/change_email/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=self.constant.NEW_EMAIL)
        time.sleep(5)
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("POST Подтверждение смены почты пользователя. Токен получить из ссылки auth/change_email/{token}.")
    def test_post_auth_change_email_confirm(self, use_api_page):
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}auth/change_email_confirm/'
        token_email = use_api_page.change_email_confirm_token(email2, password2)
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"token": token_email, "email": email2, "password": password0})
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("POST Сброс пароля")
    def test_post_auth_users_reset_password(self, use_api_page):
        jwt = use_api_page.create_jwt(email2, password0)
        url = f'{self.constant.BASE_URL}auth/users/reset_password/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"email": email2})
        time.sleep(5)
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("POST Подтверждение сброса пароля. Когда пользователь переходит по ссылке \
    auth/password/reset/confirm/{uid}/{token}")
    def test_post_auth_users_reset_password_confirm(self, use_api_page):
        jwt = use_api_page.create_jwt(email2, password0)
        page = ApiPage()
        url = f'{self.constant.BASE_URL}auth/users/reset_password_confirm/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=page.get_confirm_email_tokens(email2, password2) | {
                                 "new_password": password3, "re_new_password": password3})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("DELETE Удалить авторизованного пользователя")
    def test_delete_auth_users_me(self, use_api_page):
        jwt = use_api_page.create_jwt(email2, password3)
        url = f'{self.constant.BASE_URL}auth/users/me/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                   json={"current_password": password3})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("POST Регистрация пользователя без емайл")
    def test_post_create_user_no_email(self):
        url = f'{self.constant.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER_NO_EMAIL)
        with allure.step(f"Expected message: {self.constant.NO_DATA}"):
            assert response.json()["email"] == self.constant.NO_DATA, \
                f'Expected message: {self.constant.NO_DATA}, actual message: {response.json()["email"]}'
        with allure.step(f"Expected status {self.code.STATUS_400}"):
            assert response.status_code == self.code.STATUS_400, \
                f'Expected status {self.code.STATUS_400}, actual status {response.status_code}'

    @allure.title("POST Регистрация пользователя без пароля")
    def test_post_create_user_no_email(self):
        url = f'{self.constant.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER_NO_PASSWORD)
        with allure.step(f"Expected message: {self.constant.NO_DATA}"):
            assert response.json()["password"] == self.constant.NO_DATA, \
                f'Expected message: {self.constant.NO_DATA}, actual message: {response.json()["password"]}'
        with allure.step(f"Expected status {self.code.STATUS_400}"):
            assert response.status_code == self.code.STATUS_400, \
                f"Expected status {self.code.STATUS_400}, actual status {response.status_code}"

    @allure.title("POST Регистрация пользователя без подтверждения подписки")
    def test_post_create_user_no_subscriber(self, use_api_page):
        url = f'{self.constant.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER_NO_SUBSCRIBER)
        time.sleep(5)
        with allure.step(f"Expected status {self.code.STATUS_201}"):
            assert response.status_code == self.code.STATUS_201, \
                f"Expected status {self.code.STATUS_201}, actual status {response.status_code}"

    @allure.title("DELETE Активировать и удалить авторизованного пользователя")
    def test_delete_auth_users_me_new(self, use_api_page):
        self.test_post_users_activation(use_api_page)
        jwt = use_api_page.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}auth/users/me/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                   json={"current_password": password0})
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"
