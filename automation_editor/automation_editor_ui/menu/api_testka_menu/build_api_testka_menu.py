import webbrowser

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow

from automation_editor.utils.manager.package_manager.package_manager_class import package_manager
from automation_editor.utils.test_executor.api_testka.api_testka_process import call_api_testka_test, \
    call_api_testka_test_with_send, call_api_testka_test_multi_file, call_api_testka_test_multi_file_and_send


def set_apitestka_menu(ui_we_want_to_set: QMainWindow):
    ui_we_want_to_set.apitestka_menu = ui_we_want_to_set.menu.addMenu("APITestka")
    ui_we_want_to_set.apitestka_run_menu = ui_we_want_to_set.apitestka_menu.addMenu("Run")
    # Run APITestka Script
    ui_we_want_to_set.run_apitestka_action = QAction("Run APITestka Script")
    ui_we_want_to_set.run_apitestka_action.triggered.connect(
        lambda: call_api_testka_test(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.apitestka_run_menu.addAction(ui_we_want_to_set.run_apitestka_action)
    # Run APITestka Script With Send
    ui_we_want_to_set.run_apitestka_action_with_send = QAction("Run APITestka With Send")
    ui_we_want_to_set.run_apitestka_action_with_send.triggered.connect(
        lambda: call_api_testka_test_with_send(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.apitestka_run_menu.addAction(
        ui_we_want_to_set.run_apitestka_action_with_send
    )
    # Run Multi APITestka Script
    ui_we_want_to_set.run_multi_apitestka_action = QAction("Run Multi APITestka Script")
    ui_we_want_to_set.run_multi_apitestka_action.triggered.connect(
        lambda: call_api_testka_test_multi_file(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.apitestka_run_menu.addAction(
        ui_we_want_to_set.run_multi_apitestka_action
    )
    # Run Multi APITestka Script With Send
    ui_we_want_to_set.run_multi_apitestka_action_with_send = QAction("Run Multi APITestka Script With Send")
    ui_we_want_to_set.run_multi_apitestka_action_with_send.triggered.connect(
        lambda: call_api_testka_test_multi_file_and_send(
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
            "https://apitestka.readthedocs.io/en/latest/"
        )
    )
    ui_we_want_to_set.apitestka_help_menu.addAction(
        ui_we_want_to_set.open_apitestka_doc_action
    )
    # Open Github
    ui_we_want_to_set.open_apitestka_github_action = QAction("Open APITestka GitHub")
    ui_we_want_to_set.open_apitestka_github_action.triggered.connect(
        lambda: open_web_browser(
            "https://github.com/Intergration-Automation-Testing/APITestka"
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


def open_web_browser(url: str) -> None:
    webbrowser.open(url=url)


def create_project() -> None:
    package = package_manager.installed_package_dict.get("je_api_testka", None)
    if package is not None:
        package.create_project_dir()

