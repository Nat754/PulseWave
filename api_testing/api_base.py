import imaplib
import os
import random
import allure
import requests
from data import email1, password0
from tests.test_api.api_constant import ApiConstant


class ApiBase:

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
    def get_activate_email_tokens(e_mail, passwrd):
        with allure.step('Получить токен активации пользователя на емайл'):
            mail = imaplib.IMAP4_SSL('imap.mail.ru')
            mail.login(e_mail, passwrd)
            mail.select('INBOX')
            result, data_id = mail.search(None, 'UNSEEN')
            message_ids = data_id[0].split()
            result, data_id = mail.fetch(message_ids[-1], '(RFC822)')
            raw_email = str(data_id[0][1])
            mail.logout()
            first = raw_email.find('activate')
            link = raw_email[first + 9:first + 53].split('/')
            tokens = {"uid": link[0], "token": link[1]}
            return tokens

    @staticmethod
    def get_confirm_email_tokens(e_mail, passwrd):
        with allure.step('Получить токен подтверждения пользователя на емайл'):
            mail = imaplib.IMAP4_SSL('imap.mail.ru')
            mail.login(e_mail, passwrd)
            mail.select('INBOX')
            result, data_id = mail.search(None, 'ALL')
            message_ids = data_id[0].split()
            result, data_id = mail.fetch(message_ids[-1], '(RFC822)')
            raw_email = str(data_id[0][1])
            mail.logout()
            first = raw_email.find('confirm')
            link = raw_email[first + 8:first + 52].split('/')
            tokens = {"uid": link[0], "token": link[1]}
            return tokens

    @staticmethod
    def create_jwt(e_mail, passwrd):
        with allure.step('Получить access токен пользователя на емайл'):
            url = f'{ApiConstant.BASE_URL}auth/jwt/create/'
            response = requests.post(url, json={"email": e_mail, "password": passwrd})
            jwt = f"JWT {response.json()['access']}"
            return jwt

    @staticmethod
    def create_refresh(e_mail, passwrd):
        with allure.step('Получить refresh токен пользователя на емайл'):
            url = f'{ApiConstant.BASE_URL}auth/jwt/create/'
            response = requests.post(url, json={"email": e_mail, "password": passwrd})
            refresh = f"{response.json()['refresh']}"
            return refresh

    @staticmethod
    def change_email_confirm_token(e_mail, passwrd):
        with allure.step("Получить подтверждение смены почты пользователя на емайл"):
            mail = imaplib.IMAP4_SSL('imap.mail.ru')
            mail.login(e_mail, passwrd)
            mail.select('INBOX')
            result, data_id = mail.search(None, 'UNSEEN')
            message_ids = data_id[0].split()
            result, data_id = mail.fetch(message_ids[-1], '(RFC822)')
            raw_email = str(data_id[0][1])
            first = raw_email.find('token=')
            token = raw_email[first + 6:first + 254]
            mail.logout()
            return token

    @staticmethod
    def confirm_invite_token(e_mail, passwrd):
        with allure.step("Получить токен подтверждения приглашения на емайл"):
            mail = imaplib.IMAP4_SSL('imap.mail.ru')
            mail.login(e_mail, passwrd)
            mail.select('INBOX')
            result, data_id = mail.search(None, 'UNSEEN')
            message_ids = data_id[0].split()
            result, data_id = mail.fetch(message_ids[-1], '(RFC822)')
            raw_email = str(data_id[0][1])
            first = raw_email.find('invite/workspace/')
            token = raw_email[first + 17:first + 49]
            mail.logout()
            return token

    def get_auth_user_id(self):
        with allure.step("Получить id авторизованного пользователя"):
            jwt = self.create_jwt(email1, password0)
            url = f'{ApiConstant.BASE_URL}auth/users/me/'
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
            user_id = response.json()['id']
            return user_id

    def get_workspace_id(self):
        with allure.step("Получить id рабочего пространства"):
            jwt = self.create_jwt(email1, password0)
            url = f'{ApiConstant.BASE_URL}api/workspace/'
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
            workspaces_id = [item['id'] for item in response.json()]
            workspace_id = workspaces_id[random.randint(0, len(workspaces_id) - 1)]
            return workspace_id

    def get_board_id(self):
        with allure.step("Получить id доски"):
            jwt = self.create_jwt(email1, password0)
            workspace_id = self.get_workspace_id()
            url = f'{ApiConstant.BASE_URL}api/workspace/{workspace_id}/boards/'
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
            boards_id = [item['id'] for item in response.json()]
            board_id = random.choice(boards_id)
            return workspace_id, board_id

    def get_board_column_id(self):
        with allure.step("Получить id колонки"):
            jwt = self.create_jwt(email1, password0)
            board_id = self.get_board_id()[1]
            url = f'{ApiConstant.BASE_URL}api/boards/{board_id}/column/'
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""})
            columns_id = [i['id'] for i in response.json()]
            column_id = random.choice(columns_id)
            return board_id, column_id

    def get_column_task_id(self):
        with allure.step("Получить id задачи"):
            jwt = self.create_jwt(email1, password0)
            column_id = self.get_board_column_id()[1]
            url = f'{ApiConstant.BASE_URL}api/column/{column_id}/task/'
            requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                          json=ApiConstant.CREATE_TASK)
            response = requests.post(url, headers={'accept': 'application/json', 'Authorization': f"""{jwt}"""},
                                     json=ApiConstant.CREATE_TASK)
            task_id = response.json()['id']
            return column_id, task_id

    def get_invite_user_id(self):
        with allure.step("Получить id приглашенного пользователя"):
            jwt = self.create_jwt(email1, password0)
            url = f'{ApiConstant.BASE_URL}api/workspace/'
            response = requests.get(url, headers={'accept': 'application/json', 'Authorization': f"{jwt}"})
            invite_user_id = response.json()[0]['invited'][0]['id']
            return invite_user_id

