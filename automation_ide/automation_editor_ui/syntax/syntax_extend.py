from __future__ import annotations

from typing import TYPE_CHECKING

from je_editor import EditorWidget

if TYPE_CHECKING:
    from automation_ide.automation_editor_ui.editor_main.main_ui import AutomationEditor
from PySide6.QtGui import QColor

from automation_ide.automation_editor_ui.syntax.syntax_keyword import \
    package_keyword_list
from automation_ide.utils.manager.package_manager.package_manager_class import package_manager

from je_editor import syntax_extend_setting_dict


def syntax_extend_package(main_window: AutomationEditor) -> None:
    syntax_extend_setting_dict.update({".json": {}})
    for package in package_manager.syntax_check_list:
        syntax_extend_setting_dict.get(".json").update(
            {
                package: {
                    "words": set(package_keyword_list.get(package)),
                    "color": QColor(255, 255, 0)
                }
            }
        )
    widget = main_window.tab_widget.currentWidget()
    if isinstance(widget, EditorWidget):
        widget.code_edit.reset_highlighter()
