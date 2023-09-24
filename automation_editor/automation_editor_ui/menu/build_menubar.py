from __future__ import annotations

from typing import TYPE_CHECKING

from automation_editor.automation_editor_ui.menu.automation_menu.api_testka_menu.build_api_testka_menu import \
    set_apitestka_menu
from automation_editor.automation_editor_ui.menu.automation_menu.auto_control_menu.build_autocontrol_menu import \
    set_autocontrol_menu
from automation_editor.automation_editor_ui.menu.automation_menu.automation_file_menu.build_automation_file_menu import \
    set_automation_file_menu
from automation_editor.automation_editor_ui.menu.automation_menu.load_density_menu.build_load_density_menu import \
    set_load_density_menu
from automation_editor.automation_editor_ui.menu.automation_menu.mail_thunder_menu.build_mail_thunder_menu import \
    set_mail_thunder_menu
from automation_editor.automation_editor_ui.menu.automation_menu.web_runner_menu.build_webrunner_menu import \
    set_web_runner_menu
from automation_editor.automation_editor_ui.menu.install_menu.automation_menu.build_automation_install_menu import \
    build_automation_install_menu
from automation_editor.automation_editor_ui.menu.install_menu.tools_menu.build_tool_install_menu import \
    build_tool_install_menu
from automation_editor.automation_editor_ui.menu.tools_menu.bing_gpt_menu.build_bing_gpt_menu import set_bing_gpt_menu

if TYPE_CHECKING:
    from automation_editor.automation_editor_ui.editor_main.main_ui import AutomationEditor

from je_editor import language_wrapper


def add_menu_to_menubar(ui_we_want_to_set: AutomationEditor):
    ui_we_want_to_set.automation_menu = ui_we_want_to_set.menu.addMenu(
        language_wrapper.language_word_dict.get("automation_menu_label"))
    ui_we_want_to_set.install_menu = ui_we_want_to_set.menu.addMenu(
        language_wrapper.language_word_dict.get("install_menu_label"))
    set_apitestka_menu(ui_we_want_to_set)
    set_autocontrol_menu(ui_we_want_to_set)
    set_automation_file_menu(ui_we_want_to_set)
    set_load_density_menu(ui_we_want_to_set)
    set_mail_thunder_menu(ui_we_want_to_set)
    set_web_runner_menu(ui_we_want_to_set)
    build_automation_install_menu(ui_we_want_to_set)
    build_tool_install_menu(ui_we_want_to_set)
    set_bing_gpt_menu(ui_we_want_to_set)
