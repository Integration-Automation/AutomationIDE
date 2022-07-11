from tkinter import Menu

from je_editor import EditorMain
from integration_testing_environment.utils.manager.redirect_manager.redirect_manager_class import redirect_manager_instance


class ITEUI(EditorMain):

    def __init__(self, use_theme=None, debug=False, **kwargs):
        super().__init__(use_theme, debug, **kwargs)
        self.debug_run: bool = debug
        # Testing tool menu
        self.testing_tool_menu: Menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Testing Tool", menu=self.testing_tool_menu)


def start_ite(use_theme=None, debug: bool = False, **kwargs):
    ite_ui: ITEUI = ITEUI(use_theme, debug, **kwargs)
    ite_ui.start_editor()
    # set use ui is true then we will redirect output to ui
    redirect_manager_instance.set_ui_setting(ite_ui, True)
    return ite_ui


