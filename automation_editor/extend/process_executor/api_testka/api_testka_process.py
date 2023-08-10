from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from automation_editor.automation_editor_ui.editor_main.main_ui import AutomationEditor
import json
import sys

from automation_editor.automation_editor_ui.show_code_window.code_window import CodeWindow
from automation_editor.extend.mail_thunder_extend.mail_thunder_setting import send_after_test
from automation_editor.extend.process_executor.task_process_manager import TaskProcessManager
from automation_editor.utils.exception.exception_tags import wrong_test_data_format_exception_tag
from automation_editor.utils.exception.exceptions import ITETestExecutorException
from automation_editor.utils.file_process.get_dir_file_list import ask_and_get_dir_files_as_list


def call_api_testka(
        main_window: AutomationEditor,
        test_format_code: str,
        program_buffer: int = 1024000
):
    try:
        code_window = CodeWindow()
        main_window.current_run_code_window.append(code_window)
        main_window.clear_code_result()
        TaskProcessManager(
            main_window=code_window,
            program_buffer_size=program_buffer
        ).start_test_process(
            "je_api_testka",
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


def call_api_testka_with_send(
        main_window: AutomationEditor,
        test_format_code: str,
        program_buffer: int = 1024000
):
    try:

        code_window = CodeWindow()
        main_window.code_result.append(code_window)
        TaskProcessManager(
            main_window=code_window,
            task_done_trigger_function=send_after_test,
            program_buffer_size=program_buffer
        ).start_test_process(
            "je_api_testka",
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


def call_api_testka_multi_file(
        main_window: AutomationEditor,
        program_buffer: int = 1024000
):
    try:
        need_to_execute_list: list = ask_and_get_dir_files_as_list(main_window)
        if need_to_execute_list is not None \
                and isinstance(need_to_execute_list, list) and len(need_to_execute_list) > 0:
            for execute_file in need_to_execute_list:
                with open(execute_file, "r+") as test_script_json:
                    call_api_testka(
                        main_window,
                        test_script_json.read(),
                        program_buffer
                    )
    except Exception as error:
        print(repr(error), file=sys.stderr)


def call_api_testka_multi_file_and_send(
        main_window: AutomationEditor,
        program_buffer: int = 1024000
):
    try:

        need_to_execute_list: list = ask_and_get_dir_files_as_list(main_window)
        if need_to_execute_list is not None \
                and isinstance(need_to_execute_list, list) and len(need_to_execute_list) > 0:
            for execute_file in need_to_execute_list:
                with open(execute_file, "r+") as test_script_json:
                    call_api_testka_with_send(
                        main_window,
                        test_script_json.read(),
                        program_buffer
                    )
    except Exception as error:
        print(repr(error), file=sys.stderr)
