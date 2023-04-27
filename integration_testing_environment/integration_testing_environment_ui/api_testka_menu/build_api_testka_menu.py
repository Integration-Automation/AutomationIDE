from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow

from integration_testing_environment.utils.test_executor.api_testka.api_testka_process import call_api_testka_test, \
    call_api_testka_test_with_send, call_api_testka_test_multi_file, call_api_testka_test_multi_file_and_send


def set_apitestka_menu(ui_we_want_to_set: QMainWindow):
    ui_we_want_to_set.apitestka_menu = ui_we_want_to_set.menu.addMenu("APITestka")
    # Run APITestka Script
    ui_we_want_to_set.run_apitestka_action = QAction("Run APITestka Script")
    ui_we_want_to_set.run_apitestka_action.triggered.connect(
        lambda: call_api_testka_test(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.apitestka_menu.addAction(ui_we_want_to_set.run_apitestka_action)
    # Run APITestka Script With Send
    ui_we_want_to_set.run_apitestka_action_with_send = QAction("Run APITestka With Send")
    ui_we_want_to_set.run_apitestka_action_with_send.triggered.connect(
        lambda: call_api_testka_test_with_send(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.apitestka_menu.addAction(
        ui_we_want_to_set.run_apitestka_action_with_send
    )
    # Run Multi APITestka Script
    ui_we_want_to_set.run_multi_apitestka_action = QAction("Run Multi APITestka Script")
    ui_we_want_to_set.run_multi_apitestka_action.triggered.connect(
        lambda: call_api_testka_test_multi_file(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.apitestka_menu.addAction(
        ui_we_want_to_set.run_multi_apitestka_action
    )
    # Run Multi APITestka Script With Send
    ui_we_want_to_set.run_multi_apitestka_action_with_send = QAction("Run Multi APITestka Script With Send")
    ui_we_want_to_set.run_multi_apitestka_action_with_send.triggered.connect(
        lambda: call_api_testka_test_multi_file_and_send(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.apitestka_menu.addAction(
        ui_we_want_to_set.run_multi_apitestka_action_with_send
    )
