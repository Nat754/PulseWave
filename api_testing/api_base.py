import base64
import email
import imaplib
import os
import random
import allure
from faker import Faker
import requests
from data import email1, password0
from tests.api_tests.api_constant import ApiConstant
from tests.constant import Links

faker = Faker('En')
Faker.seed()


class ApiBase:
    link = Links

    @staticmethod
    def get_root_path():
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return project_root

    def cleanup_folder(self):
        current_dir = self.get_root_path()
        logs_dir = os.path.join(current_dir, 'logs')
        max_files = 20
        if not os.path.exists(logs_dir):
            # Create an empty logs folder
            os.makedirs(logs_dir)
        # Getting a list of files in a folder
        files = [f for f in os.listdir(logs_dir) if os.path.isfile(os.path.join(logs_dir, f))]

        # If the number of files exceeds the maximum, we delete old files
        if len(files) > max_files:
            # Сортируем файлы по времени последнего изменения (от старых к новым)
            files.sort(key=lambda x: os.path.getmtime(os.path.join(logs_dir, x)))

            # Determining the number of files to be deleted
            files_to_delete = len(files) - max_files

            # Deleting old files
            for i in range(files_to_delete):
                file_to_delete = os.path.join(logs_dir, files[i])
                os.remove(file_to_delete)
                print(f"Удален файл: {file_to_delete}")

    @staticmethod
    @allure.step('Прочитать сообщение')
    def read_email(e_mail, passwrd):
        data_id = [b'']
        while data_id == [b'']:
            mail = imaplib.IMAP4_SSL('imap.mail.ru')
            mail.login(e_mail, passwrd)
            mail.select('INBOX')
            result, data_id = mail.search(None, 'UNSEEN')
        message_ids = data_id[0].split()
        result, data_id = mail.fetch(message_ids[-1], '(RFC822)')
        mail.logout()
        msg = email.message_from_bytes(data_id[0][1])
        for part in msg.walk():
            if part.get_content_maintype() == 'text':
                msg = base64.b64decode(part.get_payload()).decode()
        return msg

    @allure.step('Получить токен активации пользователя на емайл')
    def get_tokens_on_email(self, e_mail, passwrd, trigger):
        msg = self.read_email(e_mail, passwrd)
        first = msg.find(trigger)
        start = first + len(trigger)
        end = msg[start:].find('"')
        link = msg[start:start + end].split('/')
        tokens = {"uid": link[0], "token": link[1]}
        return tokens

    @allure.step("Получить ссылку на емайл")
    def get_token_on_email(self, e_mail, passwrd, trigger):
        msg = self.read_email(e_mail, passwrd)
        first = msg.find(trigger)
        start = first + len(trigger)
        end = msg[start:].find('"')
        link = msg[start:start + end] if msg[start:start + end][-1] != '/' else msg[start:start + end - 1]
        return link

    @staticmethod
    def create_tokens(e_mail, passwrd):
        with allure.step('Получить access токен пользователя'):
            url = f'{Links.BASE_URL}auth/jwt/create/'
            response = requests.post(url, json={"email": e_mail, "password": passwrd})
            jwt = f"JWT {response.json()['access']}"
            refresh = f"{response.json()['refresh']}"
            return jwt, refresh

    def get_auth_user_id(self):
        with allure.step("Получить id авторизованного пользователя"):
            jwt = self.create_tokens(email1, password0)[0]
            url = f'{self.link.BASE_URL}auth/users/me/'
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
            user_id = response.json()['id']
            return user_id

    def get_workspace_id(self):
        with allure.step("Получить id рабочего пространства"):
            jwt = self.create_tokens(email1, password0)[0]
            url = f'{self.link.BASE_URL}api/workspace/'
            response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"},
                                     json=ApiConstant.WORKSPACE)
            workspaces_id = [item['id'] for item in response.json()]
            workspace_id = random.choice(workspaces_id)
            return workspace_id

    def get_board_id(self):
        with allure.step("Получить id доски"):
            jwt = self.create_tokens(email1, password0)[0]
            workspace_id = self.get_workspace_id()
            url = f'{self.link.BASE_URL}api/workspace/{workspace_id}/boards/'
            response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                     json={"name": faker.job()[:50], "work_space": f"{workspace_id}"})
            board_id = response.json()['id']
            return workspace_id, board_id

    def get_board_column_id(self):
        with allure.step("Получить id колонки"):
            jwt = self.create_tokens(email1, password0)[0]
            workspace_id, board_id = self.get_board_id()
            url = f'{self.link.BASE_URL}api/boards/{board_id}/column/'
            requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                          json=ApiConstant.BOARD_CREATE)
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
            columns_id = [i['id'] for i in response.json()]
            column_id = random.choice(columns_id)
            return board_id, column_id

    def get_column_task_id(self):
        with allure.step("Получить id задачи"):
            jwt = self.create_tokens(email1, password0)[0]
            board_id, column_id = self.get_board_column_id()
            url = f'{self.link.BASE_URL}api/column/{column_id}/task/'
            response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                     json=ApiConstant.CREATE_TASK)
            task_id = response.json()['id']
            return column_id, task_id
