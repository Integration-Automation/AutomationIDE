import json
import sys

from integration_testing_environment.extend.mail_thunder_extend.mail_thunder_setting import send_after_test
from integration_testing_environment.utils.exception.exception_tag import wrong_test_data_format_exception_tag
from integration_testing_environment.utils.exception.exceptions import ITETestExecutorException
from integration_testing_environment.utils.test_executor.task_process_manager import TaskProcessManager


def call_web_runner_test(test_format_code: str, program_buffer: int = 1024000):
    try:
        TaskProcessManager(
            "je_web_runner",
            program_buffer_size=program_buffer
        ).start_test_process(
            "je_web_runner",
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


def call_web_runner_test_with_send(test_format_code: str, program_buffer: int = 1024000):
    try:
        TaskProcessManager(
            title_name="je_web_runner",
            task_done_trigger_function=send_after_test,
            program_buffer_size=program_buffer
        ).start_test_process(
            "je_web_runner",
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
