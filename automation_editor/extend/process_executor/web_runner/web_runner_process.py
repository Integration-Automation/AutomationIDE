from __future__ import annotations

from typing import TYPE_CHECKING, Union

from je_editor import EditorWidget

from automation_editor.extend.process_executor.process_executor_utils import build_process

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


def call_web_runner_test(
        main_window: AutomationEditor,
        exec_str: Union[str, None] = None,
        program_buffer: int = 1024000
):
    build_process(main_window, "je_web_runner", exec_str, False, program_buffer)

def call_web_runner_test_with_send(
        main_window: AutomationEditor,
        exec_str: Union[str, None] = None,
        program_buffer: int = 1024000
):
    build_process(main_window, "je_web_runner", exec_str, True, program_buffer)


def call_web_runner_test_multi_file(
        main_window: AutomationEditor,
        program_buffer: int = 1024000
):
    try:
        need_to_execute_list: list = ask_and_get_dir_files_as_list(main_window)
        if need_to_execute_list is not None and isinstance(need_to_execute_list, list) and len(
                need_to_execute_list) > 0:
            for execute_file in need_to_execute_list:
                with open(execute_file, "r+") as test_script_json:
                    call_web_runner_test(
                        main_window,
                        test_script_json.read(),
                        program_buffer
                    )
    except Exception as error:
        print(repr(error), file=sys.stderr)


def call_web_runner_test_multi_file_and_send(
        main_window: AutomationEditor,
        program_buffer: int = 1024000
):
    try:

        need_to_execute_list: list = ask_and_get_dir_files_as_list(main_window)
        if need_to_execute_list is not None and isinstance(need_to_execute_list, list) and len(
                need_to_execute_list) > 0:
            for execute_file in need_to_execute_list:
                with open(execute_file, "r+") as test_script_json:
                    call_web_runner_test_with_send(
                        main_window,
                        test_script_json.read(),
                        program_buffer
                    )
    except Exception as error:
        print(repr(error), file=sys.stderr)
