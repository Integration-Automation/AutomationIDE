from je_editor import EditorMain

from integration_testing_environment.integration_testing_environment_ui.editor.ite_content_init.ite_content_init import \
    content_init
from integration_testing_environment.integration_testing_environment_ui.editor.menu.build_ite_ui_menu import \
    build_ite_menu
from integration_testing_environment.integration_testing_environment_ui.editor.redirect_output. \
    redirect_output_to_tkinter_ui import redirect_output
from integration_testing_environment.utils.content.content_save import save_content_and_quit
from integration_testing_environment.utils.manager.redirect_manager.redirect_manager_class import \
    redirect_manager_instance


class ITEUI(EditorMain):

    def __init__(self, use_theme=None, debug=False, **kwargs):
        super().__init__(use_theme, debug, **kwargs)
        self.program_buffer = 1024000
        self.main_window.title("ITE")
        content_init(self)
        build_ite_menu(self)
        self.program_run_result_textarea.after(10, lambda: redirect_output(self))

    def before_close_event(self):
        save_content_and_quit()


def start_ite(use_theme=None, debug: bool = False, **kwargs):
    ite_ui: ITEUI = ITEUI(use_theme=use_theme, debug=debug, **kwargs)
    if not debug:
        # set use ui is true then we will redirect output to ui
        redirect_manager_instance.set_ui_setting(ite_ui, True)
        # set some editor setting start main loop
        ite_ui.start_editor()
    return ite_ui


if __name__ == "__main__":
    start_ite()
