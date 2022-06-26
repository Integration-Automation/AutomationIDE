from tkinter import Menu

from je_editor import EditorMain


class ITEUI(EditorMain):

    def __init__(self):
        super().__init__()
        # Testing tool menu
        self.testing_tool_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Testing Tool", menu=self.testing_tool_menu)
