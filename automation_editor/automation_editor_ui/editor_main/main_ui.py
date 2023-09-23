import sys
from typing import List, Dict, Type

from PySide6.QtCore import QTimer, QCoreApplication
from PySide6.QtWidgets import QApplication, QWidget
from je_editor import EditorMain, language_wrapper
from qt_material import apply_stylesheet

from automation_editor.automation_editor_ui.extend_multi_language.update_language_dict import update_language_dict
from automation_editor.automation_editor_ui.menu.build_menubar import add_menu_to_menubar
from automation_editor.automation_editor_ui.syntax.syntax_extend import \
    syntax_extend_package

EDITOR_EXTEND_TAB: Dict[str, Type[QWidget]] = {}


class AutomationEditor(EditorMain):

    def __init__(self, debug_mode: bool = False, show_system_tray_ray: bool = False):
        super().__init__(show_system_tray_ray=show_system_tray_ray)
        self.current_run_code_window: List[QWidget] = list()
        # Project compiler if user not choose this will use which to find
        self.python_compiler = None
        # Delete JEditor help
        self.help_menu.deleteLater()
        # System tray change
        if self.show_system_tray_ray:
            self.system_tray.main_window = self
            self.system_tray.setToolTip(language_wrapper.language_word_dict.get("automation_editor_application_name"))
        # Update language_dict
        update_language_dict()
        # Menu
        add_menu_to_menubar(self)
        syntax_extend_package(self)
        # Tab
        for widget_name, widget in EDITOR_EXTEND_TAB.items():
            self.tab_widget.addTab(widget(), widget_name)
        # Title
        self.setWindowTitle(language_wrapper.language_word_dict.get("automation_editor_application_name"))
        if debug_mode:
            close_timer = QTimer(self)
            close_timer.setInterval(10000)
            close_timer.timeout.connect(self.debug_close)
            close_timer.start()

    def closeEvent(self, event) -> None:
        for widget in self.current_run_code_window:
            widget.close()
        super().closeEvent(event)

    @classmethod
    def debug_close(cls) -> None:
        """
        Use to run CI test.
        :return: None
        """
        sys.exit(0)


def start_editor(debug_mode: bool = False, **kwargs) -> None:
    """
    Start editor instance
    :return: None
    """
    new_editor = QCoreApplication.instance()
    if new_editor is None:
        new_editor = QApplication(sys.argv)
    window = AutomationEditor(debug_mode, **kwargs)
    apply_stylesheet(new_editor, theme="dark_amber.xml")
    window.showMaximized()
    try:
        window.startup_setting()
    except Exception as error:
        print(repr(error))
    sys.exit(new_editor.exec())
