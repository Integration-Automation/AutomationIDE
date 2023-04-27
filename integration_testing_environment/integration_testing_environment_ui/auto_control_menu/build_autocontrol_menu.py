from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow

from integration_testing_environment.utils.test_executor.auto_control.auto_control_process import \
    call_auto_control_test, call_auto_control_test_with_send, call_auto_control_test_multi_file, \
    call_auto_control_test_multi_file_and_send


def set_autocontrol_menu(ui_we_want_to_set: QMainWindow):
    ui_we_want_to_set.autocontrol_menu = ui_we_want_to_set.menu.addMenu("AutoControl")
    # Run AutoControl Script
    ui_we_want_to_set.run_autocontrol_action = QAction("Run AutoControl Script")
    ui_we_want_to_set.run_autocontrol_action.triggered.connect(
        lambda: call_auto_control_test(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.autocontrol_menu.addAction(ui_we_want_to_set.run_autocontrol_action)
    # Run AutoControl Script With Send
    ui_we_want_to_set.run_autocontrol_action_with_send = QAction("Run AutoControl With Send")
    ui_we_want_to_set.run_autocontrol_action_with_send.triggered.connect(
        lambda: call_auto_control_test_with_send(
            ui_we_want_to_set,
            ui_we_want_to_set.code_edit.toPlainText()
        )
    )
    ui_we_want_to_set.autocontrol_menu.addAction(
        ui_we_want_to_set.run_autocontrol_action_with_send
    )
    # Run Multi AutoControl Script
    ui_we_want_to_set.run_multi_autocontrol_action = QAction("Run Multi AutoControl Script")
    ui_we_want_to_set.run_multi_autocontrol_action.triggered.connect(
        lambda: call_auto_control_test_multi_file(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.autocontrol_menu.addAction(
        ui_we_want_to_set.run_multi_autocontrol_action
    )
    # Run Multi AutoControl Script With Send
    ui_we_want_to_set.run_multi_autocontrol_action_with_send = QAction("Run Multi AutoControl Script With Send")
    ui_we_want_to_set.run_multi_autocontrol_action_with_send.triggered.connect(
        lambda: call_auto_control_test_multi_file_and_send(
            ui_we_want_to_set,
        )
    )
    ui_we_want_to_set.autocontrol_menu.addAction(
        ui_we_want_to_set.run_multi_autocontrol_action_with_send
    )
