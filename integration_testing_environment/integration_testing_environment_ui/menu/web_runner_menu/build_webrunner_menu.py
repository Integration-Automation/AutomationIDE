from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow

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
