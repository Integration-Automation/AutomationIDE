import json
import sys

from PySide6.QtWidgets import QMainWindow

from integration_testing_environment.extend.mail_thunder_extend.mail_thunder_setting import send_after_test
from integration_testing_environment.integration_testing_environment_ui.show_code_window.code_window import CodeWindow
from integration_testing_environment.utils.exception.exception_tags import wrong_test_data_format_exception_tag
from integration_testing_environment.utils.exception.exceptions import ITETestExecutorException
from integration_testing_environment.utils.file_process.get_dir_file_list import ask_and_get_dir_files_as_list
from integration_testing_environment.utils.test_executor.check_mail_thunder import check_mail_thunder_install
from integration_testing_environment.utils.test_executor.task_process_manager import TaskProcessManager


def call_load_density_test(
        main_window: QMainWindow,
        test_format_code: str,
        program_buffer: int = 1024000
):
    try:
        check_mail_thunder_install()
        code_window = CodeWindow()
        main_window.current_run_code_window.append(code_window)
        TaskProcessManager(
            main_window=code_window,
            program_buffer_size=program_buffer
        ).start_test_process(
            "je_load_density",
            exec_str=test_format_code,
        )
    except json.decoder.JSONDecodeError as error:
        print(
            repr(error) +
            "\n"
            + wrong_test_data_format_exception_tag,
            file=sys.stderr
        )
    except ITETestExecutorException as error:
        print(repr(error), file=sys.stderr)


def call_load_density_test_with_send(
        main_window: QMainWindow,
        test_format_code: str,
        program_buffer: int = 1024000
):
    try:
        code_window = CodeWindow()
        main_window.current_run_code_window.append(code_window)
        TaskProcessManager(
            main_window=code_window,
            task_done_trigger_function=send_after_test,
            program_buffer_size=program_buffer
        ).start_test_process(
            "je_load_density",
            exec_str=test_format_code,
        )
    except json.decoder.JSONDecodeError as error:
        print(
            repr(error) +
            "\n"
            + wrong_test_data_format_exception_tag,
            file=sys.stderr
        )
    except ITETestExecutorException as error:
        print(repr(error), file=sys.stderr)


def call_load_density_test_multi_file(
        main_window: QMainWindow,
        program_buffer: int = 1024000
):
    try:
        need_to_execute_list: list = ask_and_get_dir_files_as_list(main_window)
        if need_to_execute_list is not None and isinstance(need_to_execute_list, list) and len(
                need_to_execute_list) > 0:
            for execute_file in need_to_execute_list:
                with open(execute_file, "r+") as test_script_json:
                    call_load_density_test(
                        main_window,
                        test_script_json.read(),
                        program_buffer
                    )
    except Exception as error:
        print(repr(error), file=sys.stderr)


def call_load_density_test_multi_file_and_send(
        main_window: QMainWindow,
        program_buffer: int = 1024000
):
    try:
        check_mail_thunder_install()
        need_to_execute_list: list = ask_and_get_dir_files_as_list(main_window)
        if need_to_execute_list is not None and isinstance(need_to_execute_list, list) and len(
                need_to_execute_list) > 0:
            for execute_file in need_to_execute_list:
                with open(execute_file, "r+") as test_script_json:
                    call_load_density_test_with_send(
                        main_window,
                        test_script_json.read(),
                        program_buffer
                    )
    except Exception as error:
        print(repr(error), file=sys.stderr)
