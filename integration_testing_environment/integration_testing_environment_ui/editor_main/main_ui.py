import sys

from PySide6.QtWidgets import QApplication
from je_editor import EditorMain
from qt_material import apply_stylesheet

from integration_testing_environment.integration_testing_environment_ui.\
    menu.api_testka_menu.build_api_testka_menu import set_apitestka_menu
from integration_testing_environment.integration_testing_environment_ui.\
    menu.auto_control_menu.build_autocontrol_menu import set_autocontrol_menu
from integration_testing_environment.integration_testing_environment_ui.menu.dev_menu.build_dev_menu import set_dev_menu
from integration_testing_environment.integration_testing_environment_ui.menu.\
    load_density_menu.build_load_density_menu import set_load_density_menu
from integration_testing_environment.integration_testing_environment_ui\
    .menu.web_runner_menu.build_webrunner_menu import set_web_runner_menu


class ITE(EditorMain):

    def __init__(self):
        super().__init__()
        self.current_run_code_window = list()
        set_autocontrol_menu(self)
        set_apitestka_menu(self)
        set_load_density_menu(self)
        set_web_runner_menu(self)
        set_dev_menu(self)


def start_editor():
    new_editor = QApplication(sys.argv)
    window = ITE()
    apply_stylesheet(new_editor, theme='dark_amber.xml')
    window.show()
    sys.exit(new_editor.exec_())
