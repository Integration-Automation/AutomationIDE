from __future__ import annotations

from typing import TYPE_CHECKING

from automation_editor.automation_editor_ui.menu.menu_utils import open_web_browser

if TYPE_CHECKING:
    from automation_editor.automation_editor_ui.editor_main.main_ui import AutomationEditor
import sys

from PySide6.QtGui import QAction

from automation_editor.extend.process_executor.api_testka.api_testka_process import call_api_testka, \
    call_api_testka_with_send, call_api_testka_multi_file, call_api_testka_multi_file_and_send


def set_apitestka_menu(ui_we_want_to_set: AutomationEditor):
    """
    Build menu include APITestka feature.
    :param ui_we_want_to_set: main window to add menu.
    :return: None
    """
    ui_we_want_to_set.apitestka_menu = ui_we_want_to_set.menu.addMenu("APITestka")
    ui_we_want_to_set.apitestka_run_menu = ui_we_want_to_set.apitestka_menu.addMenu("Run")
    # Run APITestka Script
    ui_we_want_to_set.run_apitestka_action = QAction("Run APITestka Script")
    ui_we_want_to_set.run_apitestka_action.triggered.connect(
        lambda: call_api_testka(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.apitestka_run_menu.addAction(ui_we_want_to_set.run_apitestka_action)
    # Run APITestka Script With Send
    ui_we_want_to_set.run_apitestka_action_with_send = QAction("Run APITestka With Send")
    ui_we_want_to_set.run_apitestka_action_with_send.triggered.connect(
        lambda: call_api_testka_with_send(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.apitestka_run_menu.addAction(
        ui_we_want_to_set.run_apitestka_action_with_send
    )
    # Run Multi APITestka Script
    ui_we_want_to_set.run_multi_apitestka_action = QAction("Run Multi APITestka Script")
    ui_we_want_to_set.run_multi_apitestka_action.triggered.connect(
        lambda: call_api_testka_multi_file(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.apitestka_run_menu.addAction(
        ui_we_want_to_set.run_multi_apitestka_action
    )
    # Run Multi APITestka Script With Send
    ui_we_want_to_set.run_multi_apitestka_action_with_send = QAction("Run Multi APITestka Script With Send")
    ui_we_want_to_set.run_multi_apitestka_action_with_send.triggered.connect(
        lambda: call_api_testka_multi_file_and_send(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.apitestka_run_menu.addAction(
        ui_we_want_to_set.run_multi_apitestka_action_with_send
    )
    ui_we_want_to_set.apitestka_help_menu = ui_we_want_to_set.apitestka_menu.addMenu("HELP")
    # Open Doc
    ui_we_want_to_set.open_apitestka_doc_action = QAction("Open APITestka Doc")
    ui_we_want_to_set.open_apitestka_doc_action.triggered.connect(
        lambda: open_web_browser(
            ui_we_want_to_set,
            "https://apitestka.readthedocs.io/en/latest/",
            "APITestka Doc"
        )
    )
    ui_we_want_to_set.apitestka_help_menu.addAction(
        ui_we_want_to_set.open_apitestka_doc_action
    )
    # Open Github
    ui_we_want_to_set.open_apitestka_github_action = QAction("Open APITestka GitHub")
    ui_we_want_to_set.open_apitestka_github_action.triggered.connect(
        lambda: open_web_browser(
            ui_we_want_to_set,
            "https://github.com/Intergration-Automation-Testing/APITestka",
            "APITestka Github"
        )
    )
    ui_we_want_to_set.apitestka_help_menu.addAction(
        ui_we_want_to_set.open_apitestka_github_action
    )
    ui_we_want_to_set.apitestka_project_menu = ui_we_want_to_set.apitestka_menu.addMenu("Project")
    # Create Project
    ui_we_want_to_set.create_apitestka_project_action = QAction("Create APITestka Project")
    ui_we_want_to_set.create_apitestka_project_action.triggered.connect(
        create_project
    )
    ui_we_want_to_set.apitestka_project_menu.addAction(
        ui_we_want_to_set.create_apitestka_project_action
    )


def create_project() -> None:
    try:
        import je_api_testka
        package = je_api_testka
        if package is not None:
            package.create_project_dir()
    except ImportError as error:
        print(repr(error), file=sys.stderr)
