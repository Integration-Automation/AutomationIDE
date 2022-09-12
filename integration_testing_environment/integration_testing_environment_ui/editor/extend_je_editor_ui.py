from je_editor import EditorMain

from integration_testing_environment.integration_testing_environment_ui.editor\
    .ite_content_init.ite_content_init import content_init
from integration_testing_environment.integration_testing_environment_ui.editor.menu.build_ite_ui_menu import \
    build_ite_menu
from integration_testing_environment.utils.content.content_save import save_content_and_quit


class ITEUI(EditorMain):

    def __init__(self, use_theme=None, debug=False, **kwargs):
        super().__init__(use_theme, debug, **kwargs)
        self.program_buffer = 1024000
        self.main_window.title("ITE")
        content_init(self)
        build_ite_menu(self)

    def before_close_event(self):
        save_content_and_quit()


def start_ite(use_theme=None, debug: bool = False, **kwargs):
    ite_ui: ITEUI = ITEUI(use_theme=use_theme, debug=debug, **kwargs)
    if not debug:
        # set use ui is true then we will redirect output to ui
        # set some editor setting start main loop
        ite_ui.start_editor()
    return ite_ui


if __name__ == "__main__":
    start_ite()
