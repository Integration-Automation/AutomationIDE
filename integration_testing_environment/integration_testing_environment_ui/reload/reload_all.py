from PySide6.QtWidgets import QMainWindow

from integration_testing_environment.integration_testing_environment_ui.syntax.syntax_extend import \
    syntax_extend_package
from integration_testing_environment.utils.manager.package_manager.package_manager_class import package_manager


def reload_all(main_window: QMainWindow):
    syntax_extend_package(main_window)
