import time
from datetime import datetime
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
        time.sleep(10)
        Assertions.assert_status_code(response, self.code.STATUS_201)

    @allure.title("POST Активация пользователя с корректными данными")
    def test_post_users_activation(self, use_api_base):
        url = f'{self.link.BASE_URL}auth/users/activation/'
        user_token = use_api_base.get_activate_email_tokens(email1, password1)
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

    @allure.title("Проверка недействительности кеша доски")
    def test_api_invalidation_board(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}api/workspace/'
        with allure.step("GET Получить список всех Рабочих пространств авторизованного пользователя"):
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
            workspaces_id = [item['id'] for item in response.json()]
            workspace_id = random.choice(workspaces_id)
        with allure.step("Создать доску"):
            url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/boards/'
            response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                     json={"name": faker.job(), "work_space": f"{workspace_id}"})
            board_id = response.json()['id']
        with allure.step(f"GET Получить имя доски {board_id} Рабочего пространства {workspace_id}"):
            url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/boards/{board_id}/'
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
            board_name = response.json()['name']
        with allure.step("Изменить имя доски"):
            response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                    json=self.constant.BOARD_CREATE)
        board_name_new = response.json()['name']
        print('\n', board_name, '!=', board_name_new)
        with (allure.step(f"Проверить, что у доски изменилось имя")):
            assert board_name != board_name_new, 'Не изменилось имя у доски'

    @allure.title("Проверка недействительности кеша рабочего пространства")
    def test_api_invalidation_workspace(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}api/workspace/'
        with allure.step("GET Получить список всех Рабочих пространств авторизованного пользователя"):
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
            workspaces_id = [item['id'] for item in response.json()]
            workspace_id = random.choice(workspaces_id)
        with allure.step(f"GET Получить имя Рабочего пространства с id='{workspace_id}"):
            url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/'
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
            workspace_name = response.json()['name']
        with allure.step(f"PUT Изменить имя Рабочего пространства с id='{workspace_id}"):
            response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                    json={'name': f'{faker.job()}'})
        with allure.step(f"GET Получить имя Рабочего пространства с id={workspace_id}"):
            workspace_new_name = response.json()['name']
            print('\n', workspace_name, '!=', workspace_new_name)
        with (allure.step(f"Проверить, что у Рабочего пространства с id='{workspace_id} изменилось имя")):
            assert workspace_name != workspace_new_name, \
                f'Не изменилось имя у Рабочего пространства с id={workspace_id}'

    @allure.title("POST Регистрация ранее зарегистрированного пользователя")
    def test_post_create_auth_user(self):
        url = f'{self.link.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER)
        print(response.json())
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

    @allure.title("PUT Обновить все данные РП (на данный момент только имя)")
    def test_put_api_workspace_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                json=self.constant.WORKSPACE)
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PATCH Частично обновить данные РП (на данный момент только имя)")
    def test_patch_api_workspace_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                  json=self.constant.WORKSPACE)
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("DELETE Частично обновить данные РП (на данный момент только имя)")
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
        time.sleep(10)
        token = use_api_base.confirm_invite_token(email_auth, password_auth_email)
        url = f'{self.link.BASE_URL}api/workspace/confirm_invite/'
        response = requests.post(url, headers={'accept': 'application/json'},
                                 json={"token": token})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("GET Список всех досок указанного РП")
    def test_get_api_workspace_id_boards(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/boards/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("POST Создать доску")
    def test_post_api_workspace_id_boards(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/boards/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                 json=self.constant.BOARD_CREATE | {"work_space": f"{workspace_id}"})
        Assertions.assert_status_code(response, self.code.STATUS_201)

    @allure.title("GET Информация о конкретной доске")
    def test_get_api_workspace_id_boards_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id, board_id = use_api_base.get_board_id()
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/boards/{board_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PUT Обновить доску")
    def test_put_api_workspace_id_boards_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id, board_id = use_api_base.get_board_id()
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/boards/{board_id}/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                json=self.constant.BOARD_CREATE)
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PATCH Частично обновить доску")
    def test_patch_api_workspace_id_boards_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id, board_id = use_api_base.get_board_id()
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/boards/{board_id}/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                  json=self.constant.BOARD_CREATE)
        Assertions.assert_status_code(response, self.code.STATUS_200)

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

    @allure.title("POST Создать колонку на доске")
    def test_post_api_board_id_column(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        board_id = use_api_base.get_board_id()[1]
        url = f'{self.link.BASE_URL}api/boards/{board_id}/column/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                 json=self.constant.BOARD_CREATE)
        Assertions.assert_status_code(response, self.code.STATUS_201)

    @allure.title("GET Список всех колонок доски")
    def test_get_api_boards_id_column(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        board_id = use_api_base.get_board_id()[1]
        url = f'{self.link.BASE_URL}api/boards/{board_id}/column/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("GET Информация о конкретной колонке")
    def test_get_api_boards_id_column_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        board_id, column_id = use_api_base.get_board_column_id()
        url = f'{self.link.BASE_URL}api/boards/{board_id}/column/{column_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PUT Обновить колонку (название и порядковый номер)")
    def test_put_api_board_id_column_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        board_id, column_id = use_api_base.get_board_column_id()
        url = f'{self.link.BASE_URL}api/boards/{board_id}/column/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        columns_id = [i['id'] for i in response.json()]
        column_id_index = columns_id.index(column_id)
        column_id_new_index = random.randint(0, len(columns_id) - 1)
        print('board', board_id, 'all', columns_id, 'choice', column_id, column_id_index)
        url = f'{self.link.BASE_URL}api/boards/{board_id}/column/{column_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        column_name = response.json()['name']
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                json={'name': faker.job(), 'index': column_id_new_index})
        print('board', board_id, 'all', columns_id, 'choice', column_id, column_id_new_index)
        column_name_new = response.json()['name']
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
                    actual status {response.status_code}"
        with allure.step("Проверить, что изменилось имя колонки и индекс"):
            print(column_name, '!=', column_name_new)
            assert column_name != column_name_new, 'Не изменилось имя колонки'

    @allure.title("PATCH Частично обновить колонку (название/порядковый номер)")
    def test_patch_api_boards_id_column_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        board_id, column_id = use_api_base.get_board_column_id()
        url = f'{self.link.BASE_URL}api/boards/{board_id}/column/{column_id}/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("POST Создать задачу")
    def test_post_api_column_id_task(self, use_api_base):
        """
        responsible: Список ответственных пользователей. Передается массивом из id,например {"responsible": [1,2,3]}
        deadline: Срок выполнения задачи
        description: Описание
        priority: Приоритет, число от 0 до 3, где 0 - высочайший приоритет
        color_mark: Цвет метки
        name_mark: Название метки
        """
        jwt = use_api_base.create_jwt(email1, password0)
        column_id = use_api_base.get_board_column_id()[1]
        url = f'{self.link.BASE_URL}api/column/{column_id}/task/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                 json=self.constant.CREATE_TASK)
        Assertions.assert_status_code(response, self.code.STATUS_201)

    @allure.title("GET Список всех задач колонки")
    def test_get_column_id_task(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        column_id = use_api_base.get_board_column_id()[1]
        url = f'{self.link.BASE_URL}api/column/{column_id}/task/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("GET Получение одной задачи")
    def test_get_task_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.link.BASE_URL}api/task/{task_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PUT Обновить задачу")
    def test_put_api_column_id_task_id(self, use_api_base):
        """Для перемещения между колонок нужно передать column - id новой колонки и index - куда ее вставить"""
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.link.BASE_URL}api/column/{column_id}/task/{task_id}/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                json={"name": "name", "index": 0, "column": f"{column_id}",
                                      "responsible": [f'{use_api_base.get_auth_user_id()}']})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PATCH Частично обновить задачу")
    def test_patch_api_column_id_task_id(self, use_api_base):
        """Перемещение между колонками возможно только PUT запросом"""
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.link.BASE_URL}api/column/{column_id}/task/{task_id}/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                  json={"name": "name", "index": 0, "column": f"{column_id}",
                                        "responsible": [f'{use_api_base.get_auth_user_id()}']})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("DELETE Удалить задачу")
    def test_delete_column_id_task_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.link.BASE_URL}api/column/{column_id}/task/{task_id}/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("DELETE Удалить колонку")
    def test_delete_api_boards_id_column_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        board_id, column_id = use_api_base.get_board_column_id()
        url = f'{self.link.BASE_URL}api/boards/{board_id}/column/{column_id}/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("DELETE Удалить доску")
    def test_delete_api_workspace_id_boards_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id, board_id = use_api_base.get_board_id()
        url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/boards/{board_id}/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("POST Создать Рабочее пространство")
    def test_post_api_workspace(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}api/workspace/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=self.constant.WORKSPACE)
        Assertions.assert_status_code(response, self.code.STATUS_201)

    @allure.title("GET Список уведомлений текущего пользователя")
    def test_get_api_notification(self, use_api_base):
        jwt = use_api_base.create_jwt(email_auth, password0)
        url = f'{self.link.BASE_URL}api/notification/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PATCH Отметить прочтение уведомления")
    def test_patch_api_notification_id_read(self, use_api_base):
        jwt = use_api_base.create_jwt(email_auth, password0)
        url = f'{self.link.BASE_URL}api/notification/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        notifications_id = [item['id'] for item in response.json()]
        notification_id = random.choice(notifications_id)
        url = f'{self.link.BASE_URL}api/notification/{notification_id}/read/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                  json=self.constant.PUT_NOTIFICATION)
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PUT Отметить прочтение уведомления")
    def test_put_api_notification_id_read(self, use_api_base):
        jwt = use_api_base.create_jwt(email_auth, password0)
        url = f'{self.link.BASE_URL}api/notification/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        notifications_id = [item['id'] for item in response.json()]
        notification_id = random.choice(notifications_id)
        url = f'{self.link.BASE_URL}api/notification/{notification_id}/read/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                json=self.constant.PUT_NOTIFICATION)
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PATCH Отметить прочтение всех уведомлений")
    def test_patch_api_notification_read_all(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}api/notification/read_all/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("POST Создать комментарий")
    def test_post_api_task_id_comment(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.link.BASE_URL}api/task/{task_id}/comment/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                 json=self.constant.COMMENT)
        Assertions.assert_status_code(response, self.code.STATUS_201)

    @allure.title("DELETE Удалить комментарий")
    def test_delete_task_id_comment_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.link.BASE_URL}api/task/{task_id}/comment/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                 json=self.constant.COMMENT)
        comment_id = response.json()['id']
        url = f'{self.link.BASE_URL}api/task/{task_id}/comment/{comment_id}/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("GET Получение комментария")
    def test_get_task_id_comment(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.link.BASE_URL}api/task/{task_id}/comment/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("GET Получить список всех пользователей для поиска")
    def test_get_api_user_list(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}api/user_list/?users=tes'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("POST Обновить JWT access_token авторизованного пользователя")
    def test_post_auth_jwt_refresh(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}auth/jwt/refresh/'
        refresh = use_api_base.create_refresh(email1, password0)
        response = requests.post(url, json={"refresh": refresh})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("GET Получить данные авторизованного пользователя")
    def test_get_auth_users(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}auth/users/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("GET Получить данные авторизованного пользователя me")
    def test_get_auth_user_me(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}auth/users/me/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("GET Получить данные авторизованного пользователя по id")
    def test_get_auth_user_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        user_id = use_api_base.get_auth_user_id()
        url = f'{self.link.BASE_URL}auth/users/{user_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PUT Обновить все данные авторизованного пользователя по id")
    def test_put_auth_users_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        user_id = use_api_base.get_auth_user_id()
        url = f'{self.link.BASE_URL}auth/users/{user_id}/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PATCH Частично обновить данные авторизованного пользователя")
    def test_patch_auth_users_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        user_id = use_api_base.get_auth_user_id()
        url = f'{self.link.BASE_URL}auth/users/{user_id}/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}",
                                                'name': faker.first_name()})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("PUT Обновить все данные авторизованного пользователя me")
    def test_put_auth_users_me(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}auth/users/me/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        Assertions.assert_status_code(response, self.code.STATUS_200)

    @allure.title("POST Запрос на смену почты")
    def test_post_auth_change_email(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}auth/change_email/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=self.constant.NEW_EMAIL)
        time.sleep(10)
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("POST Подтверждение смены почты пользователя. Токен получить из ссылки auth/change_email/{token}.")
    def test_post_auth_change_email_confirm(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}auth/change_email_confirm/'
        token_email = use_api_base.change_email_confirm_token(email2, password2)
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"token": token_email, "email": email2, "password": password0})
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("POST Сброс пароля")
    def test_post_auth_users_reset_password(self, use_api_base):
        jwt = use_api_base.create_jwt(email2, password0)
        url = f'{self.link.BASE_URL}auth/users/reset_password/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"email": email2})
        time.sleep(10)
        Assertions.assert_status_code(response, self.code.STATUS_204)

    @allure.title("POST Подтверждение сброса пароля. Когда пользователь переходит по ссылке \
    auth/password/reset/confirm/{uid}/{token}")
    def test_post_auth_users_reset_password_confirm(self, use_api_base):
        jwt = use_api_base.create_jwt(email2, password0)
        page = ApiBase()
        url = f'{self.link.BASE_URL}auth/users/reset_password_confirm/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=page.get_confirm_email_tokens(email2, password2) | {
                                 "new_password": password3, "re_new_password": password3})
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
        time.sleep(10)
        Assertions.assert_status_code(response, self.code.STATUS_201)

    @allure.title("DELETE Активировать и удалить авторизованного пользователя")
    def test_delete_auth_users_me_new(self, use_api_base):
        url = f'{self.link.BASE_URL}auth/users/activation/'
        time.sleep(10)
        user_token = use_api_base.get_activate_email_tokens(email1, password1)
        requests.post(url, json=user_token)
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.link.BASE_URL}auth/users/me/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                   json={"current_password": password0})
        print(response.text)
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
        # print(response.status_code)
        # print(response.json())
        Assertions.assert_status_code(response, self.code.STATUS_400)

    @pytest.mark.skip('Только для ручного запуска')
    @allure.title("Создать задачи для теста")
    def test_post_api_column_id_task_new(self, use_api_base):
        """
        Создаёт {n} новых колонок в нашем тестовом пространстве и по {m} задач в случайной колонке со случайным
        приоритетом
        """
        n, m = 5, 20
        workspace_id, board_id = 192, 322
        # workspace_id, board_id = 386, 457
        jwt = use_api_base.create_jwt(email_auth, password0)
        for _ in range(n):
            # создать колонку
            url = f'{self.link.BASE_URL}api/boards/{board_id}/column/'
            requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                          json={"name": faker.job()})
            for _ in range(m):
                # получить id случайной колонки
                url = f'{self.link.BASE_URL.BASE_URL}api/boards/{board_id}/column/'
                response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
                columns_id = [i['id'] for i in response.json()]
                column_id = random.choice(columns_id)
                url = f'{self.link.BASE_URL}api/column/{column_id}/task/'
                # cоздать задачу в случайной колонке
                response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                         json={
                                             "name": faker.city(),
                                             "deadline": f"{datetime.now().date()}",
                                             "description": faker.name(),
                                             "priority": random.choice([random.randint(0, 3), None]),
                                             "color_mark": random.choice(self.constant.COLOR_STICKER),
                                             "name_mark": faker.first_name()
                                         })
                Assertions.assert_status_code(response, self.code.STATUS_201)
                # url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/boards/{board_id}/'
                # response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
                # pprint(response.json())
