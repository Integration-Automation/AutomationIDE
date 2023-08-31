from __future__ import annotations

from typing import TYPE_CHECKING

from je_editor import EditorWidget

if TYPE_CHECKING:
    from automation_editor.automation_editor_ui.editor_main.main_ui import AutomationEditor
from automation_editor.automation_editor_ui.syntax.syntax_keyword import package_keyword_list
from automation_editor.utils.manager.package_manager.package_manager_class import package_manager

from je_editor import complete_list


def complete_extend_package(main_window: AutomationEditor) -> None:
    """
    Add complete keyword to JEditor complete_list.
    :param main_window: main ui.
    :return: None
    """
    widget = main_window.tab_widget.currentWidget()
    if type(widget) is EditorWidget:
        for package in package_manager.syntax_check_list:
            for word in package_keyword_list.get(package):
                # Complete
                widget.code_edit.complete_list.append(word)
                complete_list.append(word)
            widget.code_edit.set_complete(widget.code_edit.complete_list)

