from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtGui import QAction, Qt
from je_editor import language_wrapper
from je_editor.pyside_ui.main_ui.dock.destroy_dock import DestroyDock
from je_editor.utils.logging.loggin_instance import jeditor_logger

from automation_ide.automation_editor_ui.connect_gui.ssh.ssh_main_widget import SSHMainWidget
from automation_ide.automation_editor_ui.connect_gui.url.ai_code_review_gui import AICodeReviewClient
from automation_ide.automation_editor_ui.prompt_edit_gui.main_prompt_edit_widget import PromptEditor

if TYPE_CHECKING:
    from automation_ide.automation_editor_ui.editor_main.main_ui import AutomationEditor


def build_tools_menu(ui_we_want_to_set: AutomationEditor):
    # Menus
    ui_we_want_to_set.tools_menu = ui_we_want_to_set.menu.addMenu(language_wrapper.language_word_dict.get(
        "extend_tools_menu_tools_menu"
    ))
    ui_we_want_to_set.tools_ssh_menu = ui_we_want_to_set.tools_menu.addMenu(language_wrapper.language_word_dict.get(
        "extend_tools_menu_tools_ssh_menu"
    ))
    ui_we_want_to_set.tools_ai_menu = ui_we_want_to_set.tools_menu.addMenu(language_wrapper.language_word_dict.get(
        "extend_tools_menu_tools_ai_menu"
    ))

    ui_we_want_to_set.tools_ssh_client_tab_action = QAction(language_wrapper.language_word_dict.get(
        "extend_tools_menu_ssh_client_tab_action"
    ))
    ui_we_want_to_set.tools_ssh_client_tab_action.triggered.connect(lambda: ui_we_want_to_set.tab_widget.addTab(
        SSHMainWidget(), language_wrapper.language_word_dict.get("extend_tools_menu_ssh_client_tab_label")
    ))
    ui_we_want_to_set.tools_ssh_menu.addAction(ui_we_want_to_set.tools_ssh_client_tab_action)

    ui_we_want_to_set.tools_ai_code_review_action = QAction(language_wrapper.language_word_dict.get(
        "extend_tools_menu_ai_code_review_tab_action"
    ))
    ui_we_want_to_set.tools_ai_code_review_action.triggered.connect(lambda: ui_we_want_to_set.tab_widget.addTab(
        AICodeReviewClient(), language_wrapper.language_word_dict.get(
            "extend_tools_menu_ai_code_review_tab_label"
        )
    ))
    ui_we_want_to_set.tools_ai_menu.addAction(ui_we_want_to_set.tools_ai_code_review_action)

    ui_we_want_to_set.tools_ai_prompt_editor_action = QAction(language_wrapper.language_word_dict.get(
        "extend_tools_menu_prompt_editor_tab_action"
    ))
    ui_we_want_to_set.tools_ai_prompt_editor_action.triggered.connect(lambda: ui_we_want_to_set.tab_widget.addTab(
        PromptEditor(), language_wrapper.language_word_dict.get(
            "extend_tools_menu_prompt_editor_tab_label"
        )
    ))
    ui_we_want_to_set.tools_ai_menu.addAction(ui_we_want_to_set.tools_ai_prompt_editor_action)


def extend_dock_menu(ui_we_want_to_set: AutomationEditor):
    # Sub menu
    ui_we_want_to_set.dock_ssh_menu = ui_we_want_to_set.dock_menu.addMenu(
        language_wrapper.language_word_dict.get("extend_tools_menu_dock_ssh_menu")
    )
    ui_we_want_to_set.dock_ai_menu = ui_we_want_to_set.dock_menu.addMenu(
        language_wrapper.language_word_dict.get("extend_tools_menu_dock_ai_menu")
    )
    # SSH
    ui_we_want_to_set.tools_ssh_client_dock_action = QAction(
        language_wrapper.language_word_dict.get("extend_tools_menu_ssh_client_dock_action")
    )
    ui_we_want_to_set.tools_ssh_client_dock_action.triggered.connect(
        lambda: add_dock(ui_we_want_to_set, language_wrapper.language_word_dict.get(
            "extend_tools_menu_dock_ssh_menu"
        ))
    )
    ui_we_want_to_set.dock_ssh_menu.addAction(ui_we_want_to_set.tools_ssh_client_dock_action)
    # AI
    ui_we_want_to_set.tools_ai_code_review_dock_action = QAction(language_wrapper.language_word_dict.get(
        "extend_tools_menu_ai_code_review_dock_action"
    ))
    ui_we_want_to_set.tools_ai_code_review_dock_action.triggered.connect(
        lambda: add_dock(ui_we_want_to_set, language_wrapper.language_word_dict.get(
            "extend_tools_menu_prompt_editor_dock_action"
        ))
    )
    ui_we_want_to_set.dock_ai_menu.addAction(ui_we_want_to_set.tools_ai_code_review_dock_action)

    ui_we_want_to_set.tools_prompt_editor_dock_action = QAction(language_wrapper.language_word_dict.get(
        "extend_tools_menu_prompt_editor_dock_action"))
    ui_we_want_to_set.tools_prompt_editor_dock_action.triggered.connect(
        lambda: add_dock(ui_we_want_to_set, language_wrapper.language_word_dict.get(
            "extend_tools_menu_prompt_editor_dock_action"
        ))
    )
    ui_we_want_to_set.dock_ai_menu.addAction(ui_we_want_to_set.tools_prompt_editor_dock_action)

def add_dock(ui_we_want_to_set: AutomationEditor, widget_type: str = None):
    jeditor_logger.info("build_dock_menu.py add_dock_widget "
                        f"ui_we_want_to_set: {ui_we_want_to_set} "
                        f"widget_type: {widget_type}")

    # 建立一個可銷毀的 Dock 容器
    # Create a destroyable dock container
    dock_widget = DestroyDock()

    if widget_type == "SSH":
        dock_widget.setWindowTitle(language_wrapper.language_word_dict.get(
            "extend_tools_menu_ssh_client_dock_title"
        ))
        dock_widget.setWidget(SSHMainWidget())
    elif widget_type == "AICodeReview":
        dock_widget.setWindowTitle(language_wrapper.language_word_dict.get(
            "extend_tools_menu_ai_code_review_dock_title"
        ))
        dock_widget.setWidget(AICodeReviewClient())
    elif widget_type == "PromptEditor":
        dock_widget.setWindowTitle(language_wrapper.language_word_dict.get(
            "extend_tools_menu_prompt_editor_dock_title"
        ))
        dock_widget.setWidget(PromptEditor())

    # 如果成功建立了 widget，將其加到主視窗右側 Dock 區域
    # If widget is created, add it to the right dock area of the main window
    if dock_widget.widget() is not None:
        ui_we_want_to_set.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock_widget)
