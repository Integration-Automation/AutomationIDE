from je_editor import TkinterEditor, PySideEditor

from integration_testing_environment.integration_testing_environment_ui.editor \
    .ite_content_init.ite_content_init import content_init
from integration_testing_environment.integration_testing_environment_ui.editor.menu.build_ite_ui_menu import \
    build_ite_menu
from integration_testing_environment.utils.content.content_save import save_content_and_quit


class ITETkinterUI(TkinterEditor):

    def __init__(self, use_theme=None, debug=False, **kwargs):
        super().__init__(use_theme, debug, **kwargs)
        self.program_buffer: int = 1024000
        self.main_window.title("ITE")
        content_init(self)
        build_ite_menu(self)

    def before_close_event(self):
        save_content_and_quit()


class ITEPySide(PySideEditor):

    def __init__(self):
        super(ITEPySide, self).__init__()


def start_ite(editor: str = "tkinter", use_theme=None, debug=False, **kwargs):
    if editor == "pyside":
        pass
    else:
        ite_ui: ITETkinterUI = ITETkinterUI(use_theme=use_theme, debug=debug, **kwargs)
    if not debug:
        # set use ui is true then we will redirect output to ui
        # set some editor setting start main loop
        ite_ui.start_editor()
    return ite_ui
