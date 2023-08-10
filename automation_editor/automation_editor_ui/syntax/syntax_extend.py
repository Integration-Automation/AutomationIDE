from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from automation_editor.automation_editor_ui.editor_main.main_ui import AutomationEditor
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QTextCharFormat, QColor

from automation_editor.automation_editor_ui.syntax.syntax_keyword import \
    package_keyword_list
from automation_editor.utils.manager.package_manager.package_manager_class import package_manager


def syntax_extend_package(main_window: AutomationEditor) -> None:
    # Extend JEditor syntax to include more keyword.
    for package in package_manager.syntax_check_list:
        text_char_format = QTextCharFormat()
        text_char_format.setForeground(QColor(255, 255, 0))
        for word in package_keyword_list.get(package):
            # Highlight
            pattern = QRegularExpression(rf"\b{word}\b")
            main_window.code_edit.highlighter.highlight_rules.append((pattern, text_char_format))
