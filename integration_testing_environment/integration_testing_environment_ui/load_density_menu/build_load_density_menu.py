from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow

from integration_testing_environment.utils.test_executor.load_density.load_density_process import \
    call_load_density_test, call_load_density_test_with_send, call_load_density_test_multi_file, \
    call_load_density_test_multi_file_and_send


def set_load_density_menu(ui_we_want_to_set: QMainWindow):
    ui_we_want_to_set.load_density_menu = ui_we_want_to_set.menu.addMenu("LoadDensity")
    # Run LoadDensity Script
    ui_we_want_to_set.run_load_density_action = QAction("Run LoadDensity Script")
    ui_we_want_to_set.run_load_density_action.triggered.connect(
        lambda: call_load_density_test(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.load_density_menu.addAction(ui_we_want_to_set.run_load_density_action)
    # Run LoadDensity Script With Send
    ui_we_want_to_set.run_load_density_action_with_send = QAction("Run LoadDensity With Send")
    ui_we_want_to_set.run_load_density_action_with_send.triggered.connect(
        lambda: call_load_density_test_with_send(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.load_density_menu.addAction(
        ui_we_want_to_set.run_load_density_action_with_send
    )
    # Run Multi LoadDensity Script
    ui_we_want_to_set.run_multi_load_density_action = QAction("Run Multi LoadDensity Script")
    ui_we_want_to_set.run_multi_load_density_action.triggered.connect(
        lambda: call_load_density_test_multi_file(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.load_density_menu.addAction(
        ui_we_want_to_set.run_multi_load_density_action
    )
    # Run Multi LoadDensity Script With Send
    ui_we_want_to_set.run_multi_load_density_action_with_send = QAction("Run Multi LoadDensity Script With Send")
    ui_we_want_to_set.run_multi_load_density_action_with_send.triggered.connect(
        lambda: call_load_density_test_multi_file_and_send(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.load_density_menu.addAction(
        ui_we_want_to_set.run_multi_load_density_action_with_send
    )
