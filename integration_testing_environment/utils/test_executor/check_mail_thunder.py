from integration_testing_environment.utils.exception.exception_tags import not_install_exception
from integration_testing_environment.utils.exception.exceptions import ITETestExecutorException
from integration_testing_environment.utils.manager.package_manager.package_manager_class import package_manager


def check_mail_thunder_install():
    if package_manager.installed_package_dict.get("je_mail_thunder", None) is None:
        raise ITETestExecutorException(
            not_install_exception + " je_mail_thunder"
        )
