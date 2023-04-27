from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QTextCharFormat, QColor
from PySide6.QtWidgets import QMainWindow

from integration_testing_environment.utils.manager.package_manager.package_manager_class import package_manager


def syntax_extend_package(main_window: QMainWindow):
    package_manager.check_package()
    for package in package_manager.syntax_check_list:
        package = package_manager.installed_package_dict.get(package, None)
        if package is not None:
            text_char_format = QTextCharFormat()
            text_char_format.setForeground(QColor(255, 255, 0))
            for word in package.executor.event_dict.keys():
                pattern = QRegularExpression(rf"\b{word}\b")
                main_window.code_edit.highlighter.highlight_rules.append((pattern, text_char_format))
