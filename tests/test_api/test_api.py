import time
import requests
import allure
import random
from faker import Faker
from data import email1, password0, email2, password3, password1, password2, email_auth, password_auth_email
from api_testing.api_base import ApiBase
from tests.test_api.api_constant import ApiConstant, StatusCode

faker = Faker('En')
Faker.seed()


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
    def test_post_users_activation(self, use_api_base):
        url = f'{self.constant.BASE_URL}auth/users/activation/'
        response = requests.post(url, json=use_api_base.get_activate_email_tokens(email1, password1))
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

    @allure.title("GET Получить список всех Рабочих пространств авторизованного пользователя")
    def test_get_api_workspace(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}api/workspace/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("POST Пригласить пользователя по email")
    def test_post_api_workspace_invite_user(self, use_api_base):
        """Пользователи добавляются по одному. Если пользователя не существует, он будет создан"""
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/invite_user/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=self.constant.INVITE_USER)
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("POST Повторная отправка ссылки с приглашением пользователя")
    def test_post_api_workspace_resend_invite(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        invite_user_id = use_api_base.get_invite_user_id()
        url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/resend_invite/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"user_id": invite_user_id} | self.constant.INVITE_USER)
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("POST Удаление приглашенного пользователей из РП")
    def test_post_api_workspace_kick_user(self, use_api_base):
        """Удаление как из участников так и из приглашенных"""
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        invite_user_id = use_api_base.get_invite_user_id()
        url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/kick_user/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"user_id": invite_user_id} | self.constant.INVITE_USER)
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("POST Подтверждение приглашения в РП")
    def test_post_api_workspace_confirm_invite(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/invite_user/'
        requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                      json=self.constant.INVITE_USER)
        time.sleep(5)
        token = use_api_base.confirm_invite_token(email_auth, password_auth_email)
        url = f'{self.constant.BASE_URL}api/workspace/confirm_invite/'
        response = requests.post(url, headers={'accept': 'application/json'},
                                 json={"token": token})
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("GET Список всех досок указанного РП")
    def test_get_api_workspace_id_boards(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/boards/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("POST Создать доску")
    def test_post_api_workspace_id_boards(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/boards/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                 json=self.constant.BOARD_CREATE | {"work_space": f"{workspace_id}"})
        with allure.step(f"Expected status {self.code.STATUS_201}"):
            assert response.status_code == self.code.STATUS_201, f"Expected status {self.code.STATUS_201}, \
            actual status {response.status_code}"

    @allure.title("GET Информация о конкретной доске")
    def test_get_api_workspace_id_boards_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id, board_id = use_api_base.get_board_id()
        url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/boards/{board_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
                actual status {response.status_code}"

    @allure.title("PUT Обновить доску")
    def test_put_api_workspace_id_boards_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id, board_id = use_api_base.get_board_id()
        url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/boards/{board_id}/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                json=self.constant.BOARD_CREATE)
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
                    actual status {response.status_code}"

    @allure.title("PATCH Частично обновить доску")
    def test_patch_api_workspace_id_boards_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id, board_id = use_api_base.get_board_id()
        url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/boards/{board_id}/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                  json=self.constant.BOARD_CREATE)
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
                        actual status {response.status_code}"

    @allure.title("DELETE Удалить доску")
    def test_delete_api_workspace_id_boards_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id, board_id = use_api_base.get_board_id()
        url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/boards/{board_id}/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, f"Expected status {self.code.STATUS_204}, \
                            actual status {response.status_code}"

    @allure.title("POST Создать доску без указания РП")
    def test_post_api_board_create(self, use_api_base):
        """Создание доски без указания РП, будет создано дефолтное РП для этой доски"""
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}api/board_create/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                 json=self.constant.BOARD_CREATE)
        with allure.step(f"Expected status {self.code.STATUS_201}"):
            assert response.status_code == self.code.STATUS_201, f"Expected status {self.code.STATUS_201}, \
        actual status {response.status_code}"

    @allure.title("GET Список всех пользователей доски для назначения ответственных")
    def test_get_api_board_users(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        workspace_id = use_api_base.get_workspace_id()
        url = f'{self.constant.BASE_URL}api/board_users/?workspace={workspace_id}'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
                actual status {response.status_code}"

    @allure.title("POST Создать колонку на доске")
    def test_post_api_board_column_create(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        board_id = use_api_base.get_board_id()[1]
        url = f'{self.constant.BASE_URL}api/boards/{board_id}/column/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                 json=self.constant.BOARD_CREATE)
        with allure.step(f"Expected status {self.code.STATUS_201}"):
            assert response.status_code == self.code.STATUS_201, f"Expected status {self.code.STATUS_201}, \
            actual status {response.status_code}"

    @allure.title("GET Список всех колонок доски")
    def test_get_api_boards_id_column(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        board_id = use_api_base.get_board_id()[1]
        url = f'{self.constant.BASE_URL}api/boards/{board_id}/column/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
                    actual status {response.status_code}"

    @allure.title("GET Информация о конкретной колонке")
    def test_get_api_boards_id_column_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        board_id, column_id = use_api_base.get_board_column_id()
        url = f'{self.constant.BASE_URL}api/boards/{board_id}/column/{column_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        print()
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
                actual status {response.status_code}"

    @allure.title("PUT Обновить колонку (название и порядковый номер)")
    def test_put_api_board_column_info(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        board_id, column_id = use_api_base.get_board_column_id()
        url = f'{ApiConstant.BASE_URL}api/boards/{board_id}/column/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        columns_id = [i['id'] for i in response.json()]
        column_id_index = columns_id.index(column_id)
        column_id_new_index = random.randint(0, len(columns_id) - 1)
        print('board', board_id, 'all', columns_id, 'choice', column_id, column_id_index)
        url = f'{self.constant.BASE_URL}api/boards/{board_id}/column/{column_id}/'
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
        url = f'{self.constant.BASE_URL}api/boards/{board_id}/column/{column_id}/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
                                    actual status {response.status_code}"

    @allure.title("POST Создать задачу")
    def test_post_column_task_create(self, use_api_base):
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
        url = f'{self.constant.BASE_URL}api/column/{column_id}/task/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                 json=self.constant.CREATE_TASK)
        with allure.step(f"Expected status {self.code.STATUS_201}"):
            assert response.status_code == self.code.STATUS_201, f"Expected status {self.code.STATUS_201}, \
                            actual status {response.status_code}"

    @allure.title("GET Список всех задач колонки")
    def test_get_column_tasks(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        column_id = use_api_base.get_board_column_id()[1]
        url = f'{self.constant.BASE_URL}api/column/{column_id}/task/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
                    actual status {response.status_code}"

    @allure.title("GET Информация о конкретной задаче")
    def test_get_task_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.constant.BASE_URL}api/task/{task_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        print(response.json())
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
                        actual status {response.status_code}"

    @allure.title("PUT Обновить задачу")
    def test_put_column_task_id(self, use_api_base):
        """Для перемещения между колонок нужно передать column - id новой колонки и index - куда ее вставить"""
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.constant.BASE_URL}api/column/{column_id}/task/{task_id}/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                json={"name": "name", "index": 0, "column": f"{column_id}",
                                      "responsible": [f'{use_api_base.get_auth_user_id()}']})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
                            actual status {response.status_code}"

    @allure.title("PATCH Частично обновить задачу")
    def test_patch_column_task_id(self, use_api_base):
        """Перемещение между колонками возможно только PUT запросом"""
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.constant.BASE_URL}api/column/{column_id}/task/{task_id}/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                  json={"name": "name", "index": 0, "column": f"{column_id}",
                                        "responsible": [f'{use_api_base.get_auth_user_id()}']})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, f"Expected status {self.code.STATUS_200}, \
                                actual status {response.status_code}"

    @allure.title("DELETE Удалить задачу")
    def test_delete_column_task_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.constant.BASE_URL}api/column/{column_id}/task/{task_id}/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, f"Expected status {self.code.STATUS_204}, \
                                    actual status {response.status_code}"

    @allure.title("DELETE Удалить колонку")
    def test_delete_api_board_column_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        board_id, column_id = use_api_base.get_board_column_id()
        url = f'{self.constant.BASE_URL}api/boards/{board_id}/column/{column_id}/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, (f"ОР: {self.code.STATUS_204}, "
                                                                  f"ФР: {response.status_code}")

    @allure.title("POST Создать Рабочее пространство")
    def test_post_api_workspace(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}api/workspace/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=self.constant.WORKSPACE)
        with allure.step(f"Expected status {self.code.STATUS_201}"):
            assert response.status_code == self.code.STATUS_201, \
                f"Expected status {self.code.STATUS_201}, actual status {response.status_code}"

    @allure.title("POST index fixed")
    def test_post_api_index_fixed(self):
        url = f'{self.constant.BASE_URL}api/index_fixed/'
        response = requests.post(url)
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("POST Создать SSE - передает случайную строку")
    def test_post_api_sse_random_string(self):
        """
        Слушать /events/
        channel: test
        event_type: test_message
        """
        url = f'{self.constant.BASE_URL}api/sse_random_string/'
        response = requests.post(url)
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("POST Создать SSE - передает текущего юзера")
    def test_post_api_sse_user(self, use_api_base):
        """
        Слушать /events/
        channel: test
        event_type: test_user
        """
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}api/sse_user/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        print(response.text)
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("GET Список стикеров задачи")
    def test_get_api_task_id_sticker(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.constant.BASE_URL}api/task/{task_id}/sticker/'
        requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                      json={"name": faker.first_name(), "color": faker.color()})
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("POST Создать стикер к задаче")
    def test_post_api_task_id_sticker(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.constant.BASE_URL}api/task/{task_id}/sticker/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"name": faker.first_name(), "color": faker.color()})
        print(response.json())
        with allure.step(f"Expected status {self.code.STATUS_201}"):
            assert response.status_code == self.code.STATUS_201, \
                f"Expected status {self.code.STATUS_201}, actual status {response.status_code}"

    @allure.title("GET Представление одного стикера")
    def test_get_api_task_id_sticker_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        column_id, task_id = use_api_base.get_column_task_id()
        url = f'{self.constant.BASE_URL}api/task/{task_id}/sticker/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"name": faker.first_name(), "color": faker.color()})
        sticker_id = response.json()['id']
        url = f'{self.constant.BASE_URL}api/task/{task_id}/sticker/{sticker_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("GET Получить список всех пользователей для поиска")
    def test_get_api_user_list(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}api/user_list/?users=tes'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("POST Обновить JWT access_token авторизованного пользователя")
    def test_post_refresh_jwt(self, use_api_base):
        url = f'{self.constant.BASE_URL}auth/jwt/refresh/'
        refresh = use_api_base.create_refresh(email1, password0)
        response = requests.post(url, json={"refresh": refresh})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("GET Получить данные авторизованного пользователя")
    def test_get_auth_users(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}auth/users/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("GET Получить данные авторизованного пользователя me")
    def test_get_auth_user_me(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}auth/users/me/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("GET Получить данные авторизованного пользователя по id")
    def test_get_auth_user_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        user_id = use_api_base.get_auth_user_id()
        url = f'{self.constant.BASE_URL}auth/users/{user_id}/'
        response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("PUT Обновить все данные авторизованного пользователя по id")
    def test_put_auth_user_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        user_id = use_api_base.get_auth_user_id()
        url = f'{self.constant.BASE_URL}auth/users/{user_id}/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("PATCH Частично обновить данные авторизованного пользователя")
    def test_patch_auth_user_id(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        user_id = use_api_base.get_auth_user_id()
        url = f'{self.constant.BASE_URL}auth/users/{user_id}/'
        response = requests.patch(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}",
                                                'name': faker.first_name()})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("PUT Обновить все данные авторизованного пользователя me")
    def test_put_auth_user_me(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}auth/users/me/'
        response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_200, \
                f"Expected status {self.code.STATUS_200}, actual status {response.status_code}"

    @allure.title("POST Запрос на смену почты")
    def test_post_auth_change_email(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}auth/change_email/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=self.constant.NEW_EMAIL)
        time.sleep(5)
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("POST Подтверждение смены почты пользователя. Токен получить из ссылки auth/change_email/{token}.")
    def test_post_auth_change_email_confirm(self, use_api_base):
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}auth/change_email_confirm/'
        token_email = use_api_base.change_email_confirm_token(email2, password2)
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"token": token_email, "email": email2, "password": password0})
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("POST Сброс пароля")
    def test_post_auth_users_reset_password(self, use_api_base):
        jwt = use_api_base.create_jwt(email2, password0)
        url = f'{self.constant.BASE_URL}auth/users/reset_password/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json={"email": email2})
        time.sleep(5)
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("POST Подтверждение сброса пароля. Когда пользователь переходит по ссылке \
    auth/password/reset/confirm/{uid}/{token}")
    def test_post_auth_users_reset_password_confirm(self, use_api_base):
        jwt = use_api_base.create_jwt(email2, password0)
        page = ApiBase()
        url = f'{self.constant.BASE_URL}auth/users/reset_password_confirm/'
        response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                 json=page.get_confirm_email_tokens(email2, password2) | {
                                 "new_password": password3, "re_new_password": password3})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("DELETE Удалить авторизованного пользователя")
    def test_delete_auth_users_me(self, use_api_base):
        jwt = use_api_base.create_jwt(email2, password3)
        url = f'{self.constant.BASE_URL}auth/users/me/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                   json={"current_password": password3})
        with allure.step(f"Expected status {self.code.STATUS_200}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("POST Регистрация пользователя без электронной почты")
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
    def test_post_create_user_no_passwrd(self):
        url = f'{self.constant.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER_NO_PASSWORD)
        with allure.step(f"Expected message: {self.constant.NO_DATA}"):
            assert response.json()["password"] == self.constant.NO_DATA, \
                f'Expected message: {self.constant.NO_DATA}, actual message: {response.json()["password"]}'
        with allure.step(f"Expected status {self.code.STATUS_400}"):
            assert response.status_code == self.code.STATUS_400, \
                f"Expected status {self.code.STATUS_400}, actual status {response.status_code}"

    @allure.title("POST Регистрация пользователя без подтверждения подписки")
    def test_post_create_user_no_subscriber(self, use_api_base):
        url = f'{self.constant.BASE_URL}auth/users/'
        response = requests.post(url, json=self.constant.CREATE_USER_NO_SUBSCRIBER)
        time.sleep(5)
        with allure.step(f"Expected status {self.code.STATUS_201}"):
            assert response.status_code == self.code.STATUS_201, \
                f"Expected status {self.code.STATUS_201}, actual status {response.status_code}"

    @allure.title("DELETE Активировать и удалить авторизованного пользователя")
    def test_delete_auth_users_me_new(self, use_api_base):
        self.test_post_users_activation(use_api_base)
        jwt = use_api_base.create_jwt(email1, password0)
        url = f'{self.constant.BASE_URL}auth/users/me/'
        response = requests.delete(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                   json={"current_password": password0})
        with allure.step(f"Expected status {self.code.STATUS_204}"):
            assert response.status_code == self.code.STATUS_204, \
                f"Expected status {self.code.STATUS_204}, actual status {response.status_code}"

    @allure.title("Проверка недействительности кеша рабочего пространства")
    def test_api_invalidation_workspace(self, use_api_base):
        jwt = use_api_base.create_jwt(email_auth, password0)
        url = f'{self.constant.BASE_URL}api/workspace/'
        with allure.step("GET Получить список всех Рабочих пространств авторизованного пользователя"):
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
            workspaces_id = [item['id'] for item in response.json()]
            workspace_id = workspaces_id[random.randint(0, len(workspaces_id) - 1)]
        with allure.step(f"GET Получить имя Рабочего пространства с id='{workspace_id}"):
            url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/'
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

    @allure.title("Проверка недействительности кеша доски")
    def test_api_invalidation_board(self, use_api_base):
        jwt = use_api_base.create_jwt(email_auth, password0)
        url = f'{self.constant.BASE_URL}api/workspace/'
        with allure.step("GET Получить список всех Рабочих пространств авторизованного пользователя"):
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
            workspaces_id = [item['id'] for item in response.json()]
            workspace_id = workspaces_id[random.randint(0, len(workspaces_id) - 1)]
        with allure.step("Создать доску"):
            url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/boards/'
            response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                     json={"name": faker.job(), "work_space": f"{workspace_id}"})
            print(response.json())
            board_id = response.json()['id']
        with allure.step(f"GET Получить имя доски {board_id} Рабочего пространства {workspace_id}"):
            url = f'{self.constant.BASE_URL}api/workspace/{workspace_id}/boards/{board_id}/'
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
            board_name = response.json()['name']
        with allure.step("Изменить имя доски"):
            response = requests.put(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                    json=self.constant.BOARD_CREATE)
        board_name_new = response.json()['name']
        print('\n', board_name, '!=', board_name_new)
        with (allure.step(f"Проверить, что у доски изменилось имя")):
            assert board_name != board_name_new, 'Не изменилось имя у доски'
