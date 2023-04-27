from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QTextCharFormat, QColor
from PySide6.QtWidgets import QMainWindow

from integration_testing_environment.integration_testing_environment_ui.syntax.syntax_keyword import \
    package_keyword_list
from integration_testing_environment.utils.manager.package_manager.package_manager_class import package_manager


def syntax_extend_package(main_window: QMainWindow):
    for package in package_manager.syntax_check_list:
        package_instance = package_manager.installed_package_dict.get(package, None)
        if package_instance is not None:
            text_char_format = QTextCharFormat()
            text_char_format.setForeground(QColor(255, 255, 0))
            for word in package_keyword_list.get(package):
                pattern = QRegularExpression(rf"\b{word}\b")
                main_window.code_edit.highlighter.highlight_rules.append((pattern, text_char_format))
