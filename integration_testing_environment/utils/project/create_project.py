from os import getcwd
from pathlib import Path


def create_project():
    Path(getcwd() + "/.je_editor").mkdir(parents=True, exist_ok=True)


def check_project_is_exist() -> bool:
    return Path(getcwd() + "/.je_editor").is_dir()


def check_project_content_is_exist() -> bool:
    return Path(getcwd() + "/.je_editor/je_editor_content.json").is_file()
