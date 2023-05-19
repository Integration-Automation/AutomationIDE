import sys

from PySide6.QtWidgets import QApplication
from je_editor import EditorMain, ShellManager
from qt_material import apply_stylesheet

from automation_editor.automation_editor_ui. \
    menu.api_testka_menu.build_api_testka_menu import set_apitestka_menu
from automation_editor.automation_editor_ui. \
    menu.auto_control_menu.build_autocontrol_menu import set_autocontrol_menu
from automation_editor.automation_editor_ui.menu.install_menu.build_install_menu import set_install_menu
from automation_editor.automation_editor_ui.menu. \
    load_density_menu.build_load_density_menu import set_load_density_menu
from automation_editor.automation_editor_ui \
    .menu.web_runner_menu.build_webrunner_menu import set_web_runner_menu
from automation_editor.automation_editor_ui.syntax.syntax_extend import \
    syntax_extend_package


class AutomationEditor(EditorMain):

    def __init__(self):
        super().__init__()
        self.current_run_code_window = list()
        self.help_menu.deleteLater()
        set_autocontrol_menu(self)
        set_apitestka_menu(self)
        set_load_density_menu(self)
        set_web_runner_menu(self)
        set_install_menu(self)
        syntax_extend_package(self)
        self.setWindowTitle("Automation Editor")


def start_editor():
    new_editor = QApplication(sys.argv)
    window = AutomationEditor()
    apply_stylesheet(new_editor, theme="dark_amber.xml")
    window.showMaximized()
    try:
        window.startup_setting()
    except Exception as error:
        print(repr(error))
    sys.exit(new_editor.exec())
