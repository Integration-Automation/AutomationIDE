import datetime
import logging
from tkinter import Menu, END, NORMAL, DISABLED

from je_editor import EditorMain

from integration_testing_environment.integration_testing_environment_ui.editor_event.test_executor.api_testka.api_testka_executor import \
    call_api_testka_test_with_send, call_api_testka_test
from integration_testing_environment.integration_testing_environment_ui.editor_event.test_executor.auto_control.auto_control_executor import \
    call_auto_control_test, call_auto_control_test_with_send
from integration_testing_environment.integration_testing_environment_ui.editor_event.test_executor.load_density.load_density_executor import \
    call_load_density_test, call_load_density_test_with_send
from integration_testing_environment.integration_testing_environment_ui.editor_event.test_executor.web_runner.web_runner_executor import \
    call_web_runner_test, call_web_runner_test_with_send
from integration_testing_environment.utils.manager.redirect_manager.redirect_manager_class import \
    redirect_manager_instance


class ITEUI(EditorMain):

    def redirect_output(self):
        self.program_run_result_textarea.configure(state=NORMAL)
        if not redirect_manager_instance.std_out_queue.empty():
            self.program_run_result_textarea.insert(
                END,
                redirect_manager_instance.std_out_queue.get_nowait(),
            )
        if not redirect_manager_instance.std_err_queue.empty():
            self.program_run_result_textarea.tag_configure("warning", foreground="red")
            self.program_run_result_textarea.insert(
                END,
                redirect_manager_instance.std_err_queue.get_nowait(),
                "warning",
            )
        self.program_run_result_textarea.configure(state=DISABLED)
        self.program_run_result_textarea.after(10, self.redirect_output)

    def __init__(self, use_theme=None, debug=False, **kwargs):
        super().__init__(use_theme, debug, **kwargs)
        self.debug_run: bool = debug
        # Testing tool menu
        self.testing_tool_menu: Menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Testing Tool", menu=self.testing_tool_menu)
        # api testka menu
        self.api_testka_menu: Menu = Menu(self.testing_tool_menu, tearoff=0)
        self.api_testka_menu.add_command(
            label="Execute APITestka Script",
            command=lambda: call_api_testka_test(
                self.code_editor_textarea.get("1.0", "end-1c"),
            )
        )
        self.api_testka_menu.add_command(
            label="Execute And Send Mail",
            command=lambda: call_api_testka_test_with_send(
                self.code_editor_textarea.get("1.0", "end-1c"),
            )
        )
        # auto control menu
        self.auto_control_menu: Menu = Menu(self.testing_tool_menu, tearoff=0)
        self.auto_control_menu.add_command(
            label="Execute AutoControl Script",
            command=lambda: call_auto_control_test(
                self.code_editor_textarea.get("1.0", "end-1c"),
            )
        )
        self.auto_control_menu.add_command(
            label="Execute And Send Mail",
            command=lambda: call_auto_control_test_with_send(
                self.code_editor_textarea.get("1.0", "end-1c"),
            )
        )
        # web runner menu
        self.web_runner_menu: Menu = Menu(self.testing_tool_menu, tearoff=0)
        self.web_runner_menu.add_command(
            label="Execute WebRunner Script",
            command=lambda: call_web_runner_test(
                self.code_editor_textarea.get("1.0", "end-1c"),
            )
        )
        self.web_runner_menu.add_command(
            label="Execute And Send Mail",
            command=lambda: call_web_runner_test_with_send(
                self.code_editor_textarea.get("1.0", "end-1c"),
            )
        )
        # load density menu
        self.load_density_menu: Menu = Menu(self.testing_tool_menu, tearoff=0)
        self.load_density_menu.add_command(
            label="Execute LoadDensity Script",
            command=lambda: call_load_density_test(
                self.code_editor_textarea.get("1.0", "end-1c"),
            )
        )
        self.load_density_menu.add_command(
            label="Execute And Send Mail",
            command=lambda: call_load_density_test_with_send(
                self.code_editor_textarea.get("1.0", "end-1c"),
            )
        )
        # add all menu to Testing Tool menu
        self.testing_tool_menu.add_cascade(label="APITestka", menu=self.api_testka_menu)
        self.testing_tool_menu.add_cascade(label="AutoControl", menu=self.auto_control_menu)
        self.testing_tool_menu.add_cascade(label="WebRunner", menu=self.web_runner_menu)
        self.testing_tool_menu.add_cascade(label="LoadDensity", menu=self.load_density_menu)
        self.program_run_result_textarea.after(10, self.redirect_output)


def start_ite(use_theme=None, debug: bool = False, **kwargs):
    ite_ui: ITEUI = ITEUI(use_theme, debug, **kwargs)
    # set use ui is true then we will redirect output to ui
    redirect_manager_instance.set_ui_setting(ite_ui, True)
    # print current time
    print(datetime.datetime.now())
    # set some editor setting start main loop
    ite_ui.start_editor()
    return ite_ui


start_ite()
