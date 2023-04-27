from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow

from integration_testing_environment.integration_testing_environment_ui.reload.reload_all import reload_all


def set_dev_menu(ui_we_want_to_set: QMainWindow):
    ui_we_want_to_set.dev_menu = ui_we_want_to_set.menu.addMenu("Dev")
    # Reload
    ui_we_want_to_set.reload_action = QAction("Reload")
    ui_we_want_to_set.reload_action.triggered.connect(
        reload_all
    )
    ui_we_want_to_set.dev_menu.addAction(ui_we_want_to_set.reload_action)
