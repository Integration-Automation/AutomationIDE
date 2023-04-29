from automation_editor.utils.exception.exception_tags import not_install_exception
from automation_editor.utils.exception.exceptions import ITETestExecutorException
from automation_editor.utils.manager.package_manager.package_manager_class import package_manager


def check_mail_thunder_install():
    if package_manager.installed_package_dict.get("je_mail_thunder", None) is None:
        raise ITETestExecutorException(
            not_install_exception + " je_mail_thunder"
        )
