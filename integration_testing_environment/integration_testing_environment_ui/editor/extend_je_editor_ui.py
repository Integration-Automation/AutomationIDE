from tkinter import Menu

from je_editor import EditorMain


class ITEUI(EditorMain):

    def __init__(self, use_theme=None, debug=False, **kwargs):
        super().__init__(use_theme, debug, **kwargs)
        self.debug_run = debug
        # Testing tool menu
        self.testing_tool_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Testing Tool", menu=self.testing_tool_menu)


def start_ite(use_theme=None, debug: bool = False, **kwargs):
    ite_editor = ITEUI(use_theme, debug, **kwargs)
    ite_editor.start_editor()
    return ite_editor

