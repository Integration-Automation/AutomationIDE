import types

from integration_testing_environment.utils.exception.exception_tag import add_command_type_exception_tag, \
    add_command_not_allow_package_exception_tag
from integration_testing_environment.utils.exception.exceptions import ITEAddCommandException
from integration_testing_environment.utils.manager.package_manager.package_manager_class import package_manager


class ExecutorManager(object):

    def __init__(self):
        self.executor_manager_dict = {
            "je_auto_control": None,
            "je_api_testka": None,
            "je_load_density": None,
            "je_web_runner": None,
        }
        for package in package_manager.installed_package_dict.keys():
            if package in self.executor_manager_dict.keys() and package_manager.installed_package_dict.get(
                    package) is not None:
                self.executor_manager_dict.update(
                    {
                        package: package_manager.installed_package_dict.get(package).execute_action
                    }
                )


executor_manager = ExecutorManager()


def add_command_to_executor(package: str, command_dict: dict):
    for command_name, command in command_dict.items():
        if isinstance(command, (types.MethodType, types.FunctionType)):
            if package_manager.installed_package_dict.get(package, None) is not None \
                    and package in ["je_auto_control", "je_api_testka", "je_load_density", "je_web_runner"]:
                package_manager.installed_package_dict.get(package).add_command_to_executor(command_dict)
            else:
                raise ITEAddCommandException(add_command_not_allow_package_exception_tag)
        else:
            raise ITEAddCommandException(add_command_type_exception_tag)


def get_command_dict(package: str):
    if package_manager.installed_package_dict.get(package, None) is not None \
            and package in ["je_auto_control", "je_api_testka", "je_load_density", "je_web_runner"]:
        return package_manager.installed_package_dict.get(package).executor.event_dict
    else:
        return False

