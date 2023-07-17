import sys
import webbrowser

import je_auto_control
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QPlainTextEdit

from automation_editor.utils.test_executor.auto_control.auto_control_process import \
    call_auto_control_test, call_auto_control_test_with_send, call_auto_control_test_multi_file, \
    call_auto_control_test_multi_file_and_send


def set_autocontrol_menu(ui_we_want_to_set: QMainWindow):
    """
    Build menu include AutoControl feature.
    :param ui_we_want_to_set: main window to add menu.
    :return: None
    """
    ui_we_want_to_set.autocontrol_menu = ui_we_want_to_set.menu.addMenu("AutoControl")
    ui_we_want_to_set.autocontrol_run_menu = ui_we_want_to_set.autocontrol_menu.addMenu("Run")
    # Run AutoControl Script
    ui_we_want_to_set.run_autocontrol_action = QAction("Run AutoControl Script")
    ui_we_want_to_set.run_autocontrol_action.triggered.connect(
        lambda: call_auto_control_test(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.autocontrol_run_menu.addAction(ui_we_want_to_set.run_autocontrol_action)
    # Run AutoControl Script With Send
    ui_we_want_to_set.run_autocontrol_action_with_send = QAction("Run AutoControl With Send")
    ui_we_want_to_set.run_autocontrol_action_with_send.triggered.connect(
        lambda: call_auto_control_test_with_send(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.autocontrol_run_menu.addAction(
        ui_we_want_to_set.run_autocontrol_action_with_send
    )
    # Run Multi AutoControl Script
    ui_we_want_to_set.run_multi_autocontrol_action = QAction("Run Multi AutoControl Script")
    ui_we_want_to_set.run_multi_autocontrol_action.triggered.connect(
        lambda: call_auto_control_test_multi_file(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.autocontrol_run_menu.addAction(
        ui_we_want_to_set.run_multi_autocontrol_action
    )
    # Run Multi AutoControl Script With Send
    ui_we_want_to_set.run_multi_autocontrol_action_with_send = QAction("Run Multi AutoControl Script With Send")
    ui_we_want_to_set.run_multi_autocontrol_action_with_send.triggered.connect(
        lambda: call_auto_control_test_multi_file_and_send(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.autocontrol_run_menu.addAction(
        ui_we_want_to_set.run_multi_autocontrol_action_with_send
    )
    ui_we_want_to_set.autocontrol_help_menu = ui_we_want_to_set.autocontrol_menu.addMenu("HELP")
    # Open Doc
    ui_we_want_to_set.open_autocontrol_doc_action = QAction("Open AutoControl Doc")
    ui_we_want_to_set.open_autocontrol_doc_action.triggered.connect(
        lambda: open_web_browser(
            "https://autocontrol.readthedocs.io/en/latest/"
        )
    )
    ui_we_want_to_set.autocontrol_help_menu.addAction(
        ui_we_want_to_set.open_autocontrol_doc_action
    )
    # Open Github
    ui_we_want_to_set.open_autocontrol_github_action = QAction("Open AutoControl GitHub")
    ui_we_want_to_set.open_autocontrol_github_action.triggered.connect(
        lambda: open_web_browser(
            "https://github.com/Intergration-Automation-Testing/AutoControl"
        )
    )
    ui_we_want_to_set.autocontrol_help_menu.addAction(
        ui_we_want_to_set.open_autocontrol_github_action
    )
    ui_we_want_to_set.autocontrol_project_menu = ui_we_want_to_set.autocontrol_menu.addMenu("Project")
    # Create Project
    ui_we_want_to_set.create_autocontrol_project_action = QAction("Create AutoControl Project")
    ui_we_want_to_set.create_autocontrol_project_action.triggered.connect(
        create_project
    )
    ui_we_want_to_set.autocontrol_project_menu.addAction(
        ui_we_want_to_set.create_autocontrol_project_action
    )
    # Record
    ui_we_want_to_set.autocontrol_record_menu = ui_we_want_to_set.autocontrol_menu.addMenu("Record")
    ui_we_want_to_set.record_action = QAction("Start Record")
    ui_we_want_to_set.record_action.triggered.connect(
        je_auto_control.record
    )
    ui_we_want_to_set.autocontrol_record_menu.addAction(
        ui_we_want_to_set.record_action
    )
    # Stop Record
    ui_we_want_to_set.stop_record_action = QAction("Stop Record")
    ui_we_want_to_set.stop_record_action.triggered.connect(
        lambda: stop_record(ui_we_want_to_set.code_edit)
    )
    ui_we_want_to_set.autocontrol_record_menu.addAction(
        ui_we_want_to_set.stop_record_action
    )


def open_web_browser(url: str) -> None:
    webbrowser.open(url=url)


def create_project() -> None:
    try:
        import je_auto_control
        package = je_auto_control
        if package is not None:
            package.create_project_dir()
    except ImportError as error:
        print(repr(error), file=sys.stderr)


def stop_record(set_stop_record_text_container: QPlainTextEdit):
    set_stop_record_text_container.appendPlainText(str(je_auto_control.stop_record()))
