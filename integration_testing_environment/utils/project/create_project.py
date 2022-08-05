from os import getcwd
from pathlib import Path


def create_project():
    Path(getcwd() + "/.ite").mkdir(parents=True, exist_ok=True)


def check_project_is_exist() -> bool:
    return Path(getcwd() + "/.ite").is_dir()


def check_project_content_is_exist() -> bool:
    return Path(getcwd() + "/.ite/ite_content.json").is_file()
