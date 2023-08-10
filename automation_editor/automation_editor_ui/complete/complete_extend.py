from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from automation_editor.automation_editor_ui.editor_main.main_ui import AutomationEditor
from automation_editor.automation_editor_ui.syntax.syntax_keyword import package_keyword_list
from automation_editor.utils.manager.package_manager.package_manager_class import package_manager


def complete_extend_package(main_window: AutomationEditor) -> None:
    """
    Add complete keyword to JEditor complete_list.
    :param main_window: main ui.
    :return: None
    """
    for package in package_manager.syntax_check_list:
        for word in package_keyword_list.get(package):
            # Complete
            main_window.code_edit.complete_list.append(word)
        main_window.code_edit.set_complete(main_window.code_edit.complete_list)
