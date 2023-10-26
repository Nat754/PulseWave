import re


class BasicValidator:

    @staticmethod
    def is_valid_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email)

    @staticmethod
    def is_valid_status(status):
        valid_statuses = ["available", "pending", "sold"]
        return status in valid_statuses