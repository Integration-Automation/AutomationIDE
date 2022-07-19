import json
import sys

from integration_testing_environment.extend.mail_thunder_extend.mail_thunder_setting import send_after_test
from integration_testing_environment.utils.exception.exception_tag import wrong_test_data_format_exception_tag, \
    load_density_test_executor_exception_tag
from integration_testing_environment.utils.exception.exceptions import ITETestExecutorException
from integration_testing_environment.utils.manager.executor_manager.executor_manager import executor_manager
from integration_testing_environment.utils.manager.package_manager.package_manager_class import package_manager


def call_load_density_test(test_format_code: str) -> dict:
    try:
        load_density_package = package_manager.installed_package_dict.get("je_load_density", None)
        test_executor_need_list = json.loads(test_format_code)
        if load_density_package is not None:
            load_density_package.test_record_instance.clean_record()
            return executor_manager.executor_manager_dict.get("je_load_density")(test_executor_need_list)
        else:
            raise ITETestExecutorException(load_density_test_executor_exception_tag)
    except json.decoder.JSONDecodeError as error:
        print(
            repr(error) +
            "\n"
            + wrong_test_data_format_exception_tag,
            file=sys.stderr
        )
    except ITETestExecutorException as error:
        print(repr(error), file=sys.stderr)


def call_load_density_test_with_send(test_format_code: str) -> dict:
    try:
        test_result_data = call_load_density_test(test_format_code)
        send_after_test()
        return test_result_data
    except ITETestExecutorException as error:
        print(repr(error), file=sys.stderr)
