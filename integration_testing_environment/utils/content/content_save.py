import json
import os
from pathlib import Path
from threading import Lock

from integration_testing_environment.utils.content.ite_content_data import ite_content_data_dict
from integration_testing_environment.utils.exception.exceptions import ITEContentFileException
from integration_testing_environment.utils.json_format.json_process import reformat_json
from integration_testing_environment.utils.project.create_project import check_project_is_exist, check_project_content_is_exist
from integration_testing_environment.utils.project.create_project import create_project


def read_output_content():
    """
    read the editor content
    """
    lock = Lock()
    try:
        lock.acquire()
        cwd = os.getcwd()
        if check_project_is_exist() and check_project_content_is_exist():
            file_path = Path(cwd + "/.ite/ite_content.json")
            if file_path.exists() and file_path.is_file():
                with open(cwd + "/.ite/ite_content.json", "r+") as read_file:
                    return read_file.read()
    except ITEContentFileException:
        raise ITEContentFileException
    finally:
        lock.release()


def write_output_content():
    """
    write the editor content
    """
    lock = Lock()
    try:
        lock.acquire()
        cwd = os.getcwd()
        if check_project_is_exist():
            with open(cwd + "/.ite/ite_content.json", "w+") as file_to_write:
                file_to_write.write(reformat_json(json.dumps(ite_content_data_dict)))
        else:
            create_project()
            with open(cwd + "/.ite/ite_content.json", "w+") as file_to_write:
                file_to_write.write(reformat_json(json.dumps(ite_content_data_dict)))
    except ITEContentFileException:
        raise ITEContentFileException
    finally:
        lock.release()


def save_content_and_quit():
    """
    set content data and write
    """
    write_output_content()


def open_content_and_start():
    """
    read data and set content
    """
    temp_content = read_output_content()
    if temp_content is not None:
        return json.loads(temp_content)
