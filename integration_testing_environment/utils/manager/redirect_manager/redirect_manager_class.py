import sys
from contextlib import redirect_stderr
from io import StringIO
from tkinter import END


class RedirectManager(object):

    def __init__(self):
        self.is_use_ite_ui: bool = False
        self.ite_ui = None
        self.redirect_stringio: StringIO = StringIO()

    def set_ui_setting(self, ite_ui, is_use_ui: bool = False):
        self.ite_ui = ite_ui
        self.is_use_ite_ui = is_use_ui

    def redirect_std_err_to_ui(self, print_message):
        if self.is_use_ite_ui and self.ite_ui is not None:
            with redirect_stderr(self.redirect_stringio):
                print(print_message, file=sys.stderr)
            redirect_stderr_message = self.redirect_stringio.getvalue()
            self.ite_ui.program_run_result_textarea.insert(END, redirect_stderr_message)
        else:
            print(print_message, file=sys.stderr)


redirect_manager_instance = RedirectManager()
