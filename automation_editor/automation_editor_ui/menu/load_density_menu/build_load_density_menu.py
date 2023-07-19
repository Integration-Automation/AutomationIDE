import sys
import webbrowser

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow

from automation_editor.extend.process_executor.load_density.load_density_process import \
    call_load_density, call_load_density_with_send, call_load_density_multi_file, \
    call_load_density_multi_file_and_send


def set_load_density_menu(ui_we_want_to_set: QMainWindow):
    """
    Build menu include LoadDensity feature.
    :param ui_we_want_to_set: main window to add menu.
    :return: None
    """
    ui_we_want_to_set.load_density_menu = ui_we_want_to_set.menu.addMenu("LoadDensity")
    ui_we_want_to_set.load_density_run_menu = ui_we_want_to_set.load_density_menu.addMenu("Run")
    # Run LoadDensity Script
    ui_we_want_to_set.run_load_density_action = QAction("Run LoadDensity Script")
    ui_we_want_to_set.run_load_density_action.triggered.connect(
        lambda: call_load_density(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.load_density_run_menu.addAction(ui_we_want_to_set.run_load_density_action)
    # Run LoadDensity Script With Send
    ui_we_want_to_set.run_load_density_action_with_send = QAction("Run LoadDensity With Send")
    ui_we_want_to_set.run_load_density_action_with_send.triggered.connect(
        lambda: call_load_density_with_send(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.load_density_run_menu.addAction(
        ui_we_want_to_set.run_load_density_action_with_send
    )
    # Run Multi LoadDensity Script
    ui_we_want_to_set.run_multi_load_density_action = QAction("Run Multi LoadDensity Script")
    ui_we_want_to_set.run_multi_load_density_action.triggered.connect(
        lambda: call_load_density_multi_file(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.load_density_run_menu.addAction(
        ui_we_want_to_set.run_multi_load_density_action
    )
    # Run Multi LoadDensity Script With Send
    ui_we_want_to_set.run_multi_load_density_action_with_send = QAction("Run Multi LoadDensity Script With Send")
    ui_we_want_to_set.run_multi_load_density_action_with_send.triggered.connect(
        lambda: call_load_density_multi_file_and_send(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.load_density_run_menu.addAction(
        ui_we_want_to_set.run_multi_load_density_action_with_send
    )
    ui_we_want_to_set.load_density_help_menu = ui_we_want_to_set.load_density_menu.addMenu("HELP")
    # Open Doc
    ui_we_want_to_set.open_load_density_doc_action = QAction("Open LoadDensity Doc")
    ui_we_want_to_set.open_load_density_doc_action.triggered.connect(
        lambda: open_web_browser(
            "https://loaddensity.readthedocs.io/en/latest/"
        )
    )
    ui_we_want_to_set.load_density_help_menu.addAction(
        ui_we_want_to_set.open_load_density_doc_action
    )
    # Open Github
    ui_we_want_to_set.open_load_density_github_action = QAction("Open LoadDensity GitHub")
    ui_we_want_to_set.open_load_density_github_action.triggered.connect(
        lambda: open_web_browser(
            "https://github.com/Intergration-Automation-Testing/LoadDensity"
        )
    )
    ui_we_want_to_set.load_density_help_menu.addAction(
        ui_we_want_to_set.open_load_density_github_action
    )
    ui_we_want_to_set.load_density_project_menu = ui_we_want_to_set.load_density_menu.addMenu("Project")
    # Create Project
    ui_we_want_to_set.create_load_density_project_action = QAction("Create LoadDensity Project")
    ui_we_want_to_set.create_load_density_project_action.triggered.connect(
        create_project
    )
    ui_we_want_to_set.load_density_project_menu.addAction(
        ui_we_want_to_set.create_load_density_project_action
    )


def open_web_browser(url: str) -> None:
    webbrowser.open(url=url)


def create_project() -> None:
    try:
        import je_load_density
        package = je_load_density
        if package is not None:
            package.create_project_dir()
    except ImportError as error:
        print(repr(error), file=sys.stderr)
