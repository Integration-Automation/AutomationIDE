from __future__ import annotations

from typing import TYPE_CHECKING

from je_editor import EditorWidget

if TYPE_CHECKING:
    from automation_editor.automation_editor_ui.editor_main.main_ui import AutomationEditor
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QTextCharFormat, QColor

from automation_editor.automation_editor_ui.syntax.syntax_keyword import \
    package_keyword_list
from automation_editor.utils.manager.package_manager.package_manager_class import package_manager

from je_editor import syntax_word_setting_dict


def syntax_extend_package(main_window: AutomationEditor) -> None:
    widget = main_window.tab_widget.currentWidget()
    if isinstance(widget, EditorWidget):
        for package in package_manager.syntax_check_list:
            text_char_format = QTextCharFormat()
            text_char_format.setForeground(QColor(255, 255, 0))
            for word in package_keyword_list.get(package):
                # Highlight
                pattern = QRegularExpression(rf"\b{word}\b")
                widget.code_edit.highlighter.highlight_rules.append((pattern, text_char_format))
    for package in package_manager.syntax_check_list:
        syntax_word_setting_dict.update(
            {
                package: {
                    "words": set(package_keyword_list.get(package)),
                    "color": QColor(255, 255, 0)
                }
            }
        )

