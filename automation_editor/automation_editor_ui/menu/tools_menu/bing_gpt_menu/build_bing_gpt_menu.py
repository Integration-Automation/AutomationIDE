from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtGui import QAction
from je_editor import language_wrapper

from automation_editor.automation_editor_ui.menu.menu_utils import open_web_browser

if TYPE_CHECKING:
    from automation_editor.automation_editor_ui.editor_main.main_ui import AutomationEditor


def set_bing_gpt_menu(ui_we_want_to_set: AutomationEditor):
    ui_we_want_to_set.bing_gpt_menu = ui_we_want_to_set.menu.addMenu(
        language_wrapper.language_word_dict.get("tools_menu_re_edge_gpt_label"))
    ui_we_want_to_set.bing_gpt_menu.help_menu = ui_we_want_to_set.bing_gpt_menu.addMenu(
        language_wrapper.language_word_dict.get("help_label"))
    # Open Doc
    ui_we_want_to_set.bing_gpt_menu.help_menu.open_bing_gpt_menu_doc_action = QAction(
        language_wrapper.language_word_dict.get("tools_menu_re_edge_gpt_doc_label"))
    ui_we_want_to_set.bing_gpt_menu.help_menu.open_bing_gpt_menu_doc_action.triggered.connect(
        lambda: open_web_browser(
            ui_we_want_to_set,
            "https://reedgegpt.readthedocs.io/en/latest/",
            language_wrapper.language_word_dict.get("tools_menu_re_edge_gpt_doc_tab_label")
        )
    )
    ui_we_want_to_set.bing_gpt_menu.help_menu.addAction(
        ui_we_want_to_set.bing_gpt_menu.help_menu.open_bing_gpt_menu_doc_action
    )
    # Open Github
    ui_we_want_to_set.bing_gpt_menu.help_menu.open_re_edge_gpt_github_action = QAction(
        language_wrapper.language_word_dict.get("tools_menu_re_edge_gpt_github_label"))
    ui_we_want_to_set.bing_gpt_menu.help_menu.open_re_edge_gpt_github_action.triggered.connect(
        lambda: open_web_browser(
            ui_we_want_to_set,
            "https://github.com/Integration-Automation/ReEdgeGPT",
            language_wrapper.language_word_dict.get("tools_menu_re_edge_gpt_github_tab_label")
        )
    )
    ui_we_want_to_set.bing_gpt_menu.help_menu.addAction(
        ui_we_want_to_set.bing_gpt_menu.help_menu.open_re_edge_gpt_github_action
    )
