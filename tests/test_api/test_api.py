import time
from tests.constant import TestData
import pytest
import requests
import allure
import random
from faker import Faker
from data import email1, password0, email2, password3, password1, password2, email_auth, password_auth_email
from api_testing.api_base import ApiBase
from api_testing.assertions import Assertions
from tests.test_api.api_constant import ApiConstant, StatusCode
from tests.constant import Links

faker = Faker('En')
Faker.seed()


@allure.epic("Тестирование API")
class TestAPI:
    link = Links
    constant = ApiConstant
    code = StatusCode
    test_data = TestData

    @allure.title("POST Создать пользователя с корректными данными")
    def test_post_auth_user(self):
        url = f'{self.link.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER)
        time.sleep(15)
        Assertions.assert_status_code(response, self.code.STATUS_201)

    @allure.title("POST Активация пользователя с корректными данными")
    def test_post_users_activation(self, use_api_base):
        url = f'{self.link.BASE_URL}auth/users/activation/'
        user_token = use_api_base.get_tokens_on_email(email1, password1, 'activate/')
        response = requests.post(url, json=user_token)
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("POST Пригласить пользователя по email")
    def test_post_api_workspace_id_invite_user(self, use_api_base):
        """Пользователи добавляются по одному. Если пользователя не существует, он будет создан"""
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}api/workspace/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        workspaces_id = [item['id'] for item in response.json()]
        workspace_id = random.choice(workspaces_id)
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/invite_user/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=self.constant.INVITE_USER)
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("POST Повторная отправка ссылки с приглашением пользователя")
    def test_post_api_workspace_id_resend_invite(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}api/workspace/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        workspaces_id = [item['id'] for item in response.json()]
        workspace_id = random.choice(workspaces_id)
        invite_user_id = response.json()[0]['invited'][0]['id']
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/resend_invite/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"user_id": invite_user_id})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("POST Удаление приглашенного пользователей из РП")
    def test_post_api_workspace_id_kick_user(self, use_api_base):
        """Удаление как из участников так и из приглашенных"""
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}api/workspace/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        workspaces_id = [item['id'] for item in response.json()]
        workspace_id = random.choice(workspaces_id)
        invite_user_id = response.json()[0]['invited'][0]['id']
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/kick_user/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"user_id": invite_user_id} | self.constant.INVITE_USER)
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("POST Регистрация ранее зарегистрированного пользователя")
    def test_post_create_auth_user(self):
        url = f'{self.link.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER)
        Assertions.assert_status_code(response, self.code.STATUS_400)

    @allure.title("POST Создать пару токенов access и refresh")
    def test_post_auth_jwt_create(self):
        url = f'{self.link.BASE_URL}auth/jwt/create/'
        response = requests.post(url, json={"email": email1, "password": password0})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("GET Получить список всех Рабочих пространств авторизованного пользователя")
    def test_get_api_workspace(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}api/workspace/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("GET Информация о конкретном рабочем пространстве")
    def test_get_api_workspace_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PATCH Частично обновить данные РП (на данный момент только имя)")
    def test_patch_api_workspace_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                  json=self.constant.WORKSPACE)
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("DELETE Удалить РП")
    def test_delete_api_workspace_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("POST Подтверждение приглашения в РП")
    def test_post_api_workspace_confirm_invite(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/invite_user/'
        requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                      json=self.constant.INVITE_USER)
        time.sleep(15)
        token = use_api_base.get_token_on_email(email_auth, password_auth_email, 'invite/workspace/')
        url = f'{self.link.BASE_URL}api/workspace/confirm_invite/'
        response = requests.post(url, headers={'accept': 'application/json'},
                                 json={"token": token})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("POST Создать доску без указания РП")
    def test_post_api_board_create(self, use_api_base):
        """Создание доски без указания РП, будет создано дефолтное РП для этой доски"""
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}api/board_create/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                 json=self.constant.BOARD_CREATE)
        Assertions.assert_status_code(response, self.code.STATUS_201)

    @allure.title("GET Список всех пользователей доски для назначения ответственных")
    def test_get_api_board_users(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.link.BASE_URL}api/board_users/?workspace={workspace_id}'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("POST Создать Рабочее пространство")
    def test_post_api_workspace(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}api/workspace/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=self.constant.WORKSPACE)
        Assertions.assert_status_code(response, self.code.STATUS_201)

    @allure.title("GET Получить список всех пользователей для поиска")
    def test_get_api_user_list(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}api/user_list/?users=tes'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("POST Обновить JWT access_token авторизованного пользователя")
    def test_post_auth_jwt_refresh(self, use_api_base):
        url = f'{self.link.BASE_URL}auth/jwt/refresh/'
        refresh = use_api_base.create_refresh(email1, password0)
        response = requests.post(url, json={"refresh": refresh})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("GET Получить данные авторизованного пользователя me")
    def test_get_auth_user_me(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}auth/users/me/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("POST Запрос на смену почты")
    def test_post_auth_change_email(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}auth/change_email/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=self.constant.NEW_EMAIL)
        time.sleep(15)
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("POST Подтверждение смены почты пользователя. Токен получить из ссылки auth/change_email/{token}.")
    def test_post_auth_change_email_confirm(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}auth/change_email_confirm/'
        token_email = use_api_base.get_token_on_email(email2, password2, 'token=')
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"token": token_email, "email": email2, "password": password0})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("POST Сброс пароля")
    def test_post_auth_users_reset_password(self, use_api_base):
        jwt = use_api_base.create_jwt(email2, password0)
        url = f'{self.link.BASE_URL}auth/users/reset_password/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"email": email2})
        time.sleep(15)
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("POST Подтверждение сброса пароля. Когда пользователь переходит по ссылке \
    auth/password/reset/confirm/{uid}/{token}")
    def test_post_auth_users_reset_password_confirm(self, use_api_base):
        jwt = use_api_base.create_jwt(email2, password0)
        page = ApiBase()
        url = f'{self.link.BASE_URL}auth/users/reset_password_confirm/'
        tokens = page.get_tokens_on_email(email2, password2, 'confirm/')
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=tokens | {"new_password": password3, "re_new_password": password3})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("DELETE Удалить авторизованного пользователя")
    def test_delete_auth_users_me(self, use_api_base):
        jwt = use_api_base.create_jwt(email2, password3)
        url = f'{self.link.BASE_URL}auth/users/me/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                   json={"current_password": password3})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("POST Регистрация пользователя без электронной почты")
    def test_post_create_user_no_email(self):
        url = f'{self.link.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER_NO_EMAIL)
        with allure.step(f"Expected message: {self.constant.NO_DATA}"):
            assert response.json()["email"] == self.constant.NO_DATA, \
                f'Expected message: {self.constant.NO_DATA}, actual message: {response.json()["email"]}'
        Assertions.assert_status_code(response, self.code.STATUS_400)

    @allure.title("POST Регистрация пользователя без пароля")
    def test_post_create_user_no_passwrd(self):
        url = f'{self.link.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER_NO_PASSWORD)
        with allure.step(f"Expected message: {self.constant.NO_DATA}"):
            assert response.json()["password"] == self.constant.NO_DATA, \
                f'Expected message: {self.constant.NO_DATA}, actual message: {response.json()["password"]}'
        Assertions.assert_status_code(response, self.code.STATUS_400)

    @allure.title("POST Регистрация пользователя без подтверждения подписки")
    def test_post_create_user_no_subscriber(self, use_api_base):
        url = f'{self.link.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER_NO_SUBSCRIBER)
        time.sleep(15)
        Assertions.assert_status_code(response, self.code.STATUS_201)

    @allure.title("DELETE Активировать и удалить авторизованного пользователя")
    def test_delete_auth_users_me_new(self, use_api_base):
        url = f'{self.link.BASE_URL}auth/users/activation/'
        time.sleep(15)
        user_token = use_api_base.get_tokens_on_email(email1, password1, 'activate/')
        requests.post(url, json=user_token)
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}auth/users/me/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                   json={"current_password": password0})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @pytest.mark.parametrize('password', test_data.WEAK_PASSWORD)
    @allure.title("POST Создать пользователя с некорректными данными")
    def test_post_auth_user_weak_password(self, password):
        url = f'{self.link.BASE_URL}auth/users/'
        response = requests.post(url, json={
            "subscriber": "true",
            "email": email1,
            "password": password,
            "re_password": password
        })
        Assertions.assert_status_code(response, self.code.STATUS_400)
