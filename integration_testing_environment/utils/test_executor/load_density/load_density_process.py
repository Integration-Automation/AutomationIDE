import json
import sys

from integration_testing_environment.extend.mail_thunder_extend.mail_thunder_setting import send_after_test
from integration_testing_environment.utils.exception.exception_tag import wrong_test_data_format_exception_tag
from integration_testing_environment.utils.exception.exceptions import ITETestExecutorException
from integration_testing_environment.utils.test_executor.task_process_manager import TaskProcessManager


def call_load_density_test(test_format_code):
    try:
        TaskProcessManager("je_load_density").start_test_process(
            package="je_load_density",
            exec_str=json.loads(test_format_code)
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


def call_load_density_test_with_send(test_format_code):
    try:
        TaskProcessManager(
            title_name="je_load_density",
            task_done_trigger_function=send_after_test
        ).start_test_process(
            "je_load_density",
            json.loads(test_format_code),
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
