import sys

from PySide6.QtWidgets import QApplication
from je_editor import EditorMain


class ITE(EditorMain):

    def __init__(self):
        super().__init__()


def start_editor():
    new_editor = QApplication(sys.argv)
    window = ITE()
    window.show()
    sys.exit(new_editor.exec_())
