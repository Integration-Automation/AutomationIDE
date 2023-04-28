import webbrowser

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow

from integration_testing_environment.utils.manager.package_manager.package_manager_class import package_manager
from integration_testing_environment.utils.test_executor.web_runner.web_runner_process import call_web_runner_test, \
    call_web_runner_test_with_send, call_web_runner_test_multi_file, call_web_runner_test_multi_file_and_send


def set_web_runner_menu(ui_we_want_to_set: QMainWindow):
    ui_we_want_to_set.web_runner_menu = ui_we_want_to_set.menu.addMenu("WebRunner")
    ui_we_want_to_set.web_runner_run_menu = ui_we_want_to_set.web_runner_menu.addMenu("Run")
    # Run WebRunner Script
    ui_we_want_to_set.run_web_runner_action = QAction("Run WebRunner Script")
    ui_we_want_to_set.run_web_runner_action.triggered.connect(
        lambda: call_web_runner_test(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.web_runner_run_menu.addAction(ui_we_want_to_set.run_web_runner_action)
    # Run AutoControl Script With Send
    ui_we_want_to_set.run_web_runner_action_with_send = QAction("Run WebRunner With Send")
    ui_we_want_to_set.run_web_runner_action_with_send.triggered.connect(
        lambda: call_web_runner_test_with_send(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.web_runner_run_menu.addAction(
        ui_we_want_to_set.run_web_runner_action_with_send
    )
    # Run Multi AutoControl Script
    ui_we_want_to_set.run_multi_web_runner_action = QAction("Run Multi WebRunner Script")
    ui_we_want_to_set.run_multi_web_runner_action.triggered.connect(
        lambda: call_web_runner_test_multi_file(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.web_runner_run_menu.addAction(
        ui_we_want_to_set.run_multi_web_runner_action
    )
    # Run Multi AutoControl Script With Send
    ui_we_want_to_set.run_multi_web_runner_action_with_send = QAction("Run Multi WebRunner Script With Send")
    ui_we_want_to_set.run_multi_web_runner_action_with_send.triggered.connect(
        lambda: call_web_runner_test_multi_file_and_send(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.web_runner_run_menu.addAction(
        ui_we_want_to_set.run_multi_web_runner_action_with_send
    )
    ui_we_want_to_set.web_runner_help_menu = ui_we_want_to_set.web_runner_menu.addMenu("HELP")
    # Open Doc
    ui_we_want_to_set.open_web_runner_doc_action = QAction("Open WebRunner Doc")
    ui_we_want_to_set.open_web_runner_doc_action.triggered.connect(
        lambda: open_web_browser(
            "https://webrunner.readthedocs.io/en/latest/"
        )
    )
    ui_we_want_to_set.web_runner_help_menu.addAction(
        ui_we_want_to_set.open_web_runner_doc_action
    )
    # Open Github
    ui_we_want_to_set.open_web_runner_github_action = QAction("Open WebRunner GitHub")
    ui_we_want_to_set.open_web_runner_github_action.triggered.connect(
        lambda: open_web_browser(
            "https://github.com/Integrated-Testing-Environment/LoadDensity"
        )
    )
    ui_we_want_to_set.web_runner_help_menu.addAction(
        ui_we_want_to_set.open_web_runner_github_action
    )
    ui_we_want_to_set.web_runner_project_menu = ui_we_want_to_set.web_runner_menu.addMenu("Project")
    # Create Project
    ui_we_want_to_set.create_web_runner_project_action = QAction("Create WebRunner Project")
    ui_we_want_to_set.create_web_runner_project_action.triggered.connect(
        create_project
    )
    ui_we_want_to_set.web_runner_project_menu.addAction(
        ui_we_want_to_set.create_web_runner_project_action
    )


def open_web_browser(url: str):
    webbrowser.open(url=url)


def create_project():
    package = package_manager.installed_package_dict.get("je_web_runner", None)
    if package is not None:
        package.create_project_dir()
