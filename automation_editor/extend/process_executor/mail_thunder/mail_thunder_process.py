import json
import sys

from PySide6.QtWidgets import QMainWindow

from automation_editor.automation_editor_ui.show_code_window.code_window import CodeWindow
from automation_editor.extend.process_executor.task_process_manager import TaskProcessManager
from automation_editor.utils.exception.exception_tags import wrong_test_data_format_exception_tag
from automation_editor.utils.exception.exceptions import ITETestExecutorException


def call_mail_thunder(
        main_window: QMainWindow,
        test_format_code: str,
        program_buffer: int = 1024000
):
    try:
        code_window = CodeWindow()
        main_window.current_run_code_window.append(code_window)
        TaskProcessManager(
            main_window=code_window,
            program_buffer_size=program_buffer
        ).start_test_process(
            "je_mail_thunder",
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
