import sys
from concurrent.futures.thread import ThreadPoolExecutor

from integration_testing_environment.utils.exception.exception_tag import auto_control_test_executor_exception_tag
from integration_testing_environment.utils.exception.exception_tag import api_testka_test_executor_exception_tag
from integration_testing_environment.utils.exception.exception_tag import web_runner_test_executor_exception_tag
from integration_testing_environment.utils.exception.exception_tag import load_density_test_executor_exception_tag
from integration_testing_environment.utils.exception.exceptions import ITETestExecutorException
from integration_testing_environment.utils.manager.executor_manager.executor_manager import executor_manager
from integration_testing_environment.utils.manager.package_manager.package_manager_class import package_manager
from integration_testing_environment.extend.mail_thunder_extend.mail_thunder_setting import send_after_test

test_executor = ThreadPoolExecutor()


def auto_control_executor(execute_action_json_list: list):
    try:
        auto_control_package = package_manager.installed_package_dict.get("je_auto_control", None)
        if auto_control_package is not None:
            auto_control_package.test_record_instance.init_record = True
            test_future = test_executor.submit(
                executor_manager.executor_manager_dict.get("je_auto_control"), execute_action_json_list
            )
            return test_future.result()
        else:
            raise ITETestExecutorException(auto_control_test_executor_exception_tag)
    except ITETestExecutorException as error:
        print(repr(error), file=sys.stderr)


def auto_control_executor_with_send(execute_action_json_list: list):
    auto_control_executor(execute_action_json_list)
    send_after_test()


def api_testka_executor(execute_action_json_list: list):
    api_testka_package = package_manager.installed_package_dict.get("je_api_testka", None)
    try:
        if api_testka_package is not None:
            test_future = test_executor.submit(
                executor_manager.executor_manager_dict.get("je_api_testka"), execute_action_json_list
            )
            return test_future.result()
        else:
            raise ITETestExecutorException(api_testka_test_executor_exception_tag)
    except ITETestExecutorException as error:
        print(repr(error), file=sys.stderr)


def api_testka_executor_with_send(execute_action_json_list: list):
    api_testka_executor(execute_action_json_list)
    send_after_test()


def web_runner_executor(execute_action_json_list: list):
    web_runner_package = package_manager.installed_package_dict.get("je_web_runner", None)
    try:
        if web_runner_package is not None:
            web_runner_package.test_record_instance.set_record_enable(True)
            test_future = test_executor.submit(
                executor_manager.executor_manager_dict.get("je_web_runner"), execute_action_json_list
            )
            return test_future.result()
        else:
            raise ITETestExecutorException(web_runner_test_executor_exception_tag)
    except ITETestExecutorException as error:
        print(repr(error), file=sys.stderr)


def web_runner_executor_with_send(execute_action_json_list: list):
    web_runner_executor(execute_action_json_list)
    send_after_test()


def load_density_executor(execute_action_json_list: list):
    load_density_package = package_manager.installed_package_dict.get("je_load_density", None)
    try:
        if load_density_package is not None:
            test_future = test_executor.submit(
                executor_manager.executor_manager_dict.get("je_load_density"), execute_action_json_list
            )
            return test_future.result()
        else:
            raise ITETestExecutorException(load_density_test_executor_exception_tag)
    except ITETestExecutorException as error:
        print(repr(error), file=sys.stderr)


def load_density_executor_with_send(execute_action_json_list: list):
    load_density_executor(execute_action_json_list)
    send_after_test()
