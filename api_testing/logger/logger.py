import logging
import os
from logging.handlers import RotatingFileHandler
from api_testing.api_base import ApiBase


def create_logs_dir():
    api_base = ApiBase
    file_name = f"""logs.log"""
    project_dir = api_base.get_root_path()
    log_dir = os.path.join(project_dir, "log_files")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = os.path.join(log_dir, file_name)
    return log_file


def get_logs(name):
    log_file = create_logs_dir()
    max_byte = 1 * 1024 * 1024
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt="%(levelname)s :: %(asctime)s :: %(message)s :: [file:%(name)s :: line:%(lineno)d]",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler = logging.handlers.RotatingFileHandler(
        filename=log_file,
        encoding="utf-8",
        maxBytes=max_byte,
        backupCount=10
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
