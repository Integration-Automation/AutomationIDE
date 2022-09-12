from tkinter import Menu, END

from integration_testing_environment.utils.test_executor.api_testka.api_testka_process import call_api_testka_test, \
    call_api_testka_test_with_send, call_api_testka_test_multi_file, call_api_testka_test_multi_file_and_send
from integration_testing_environment.utils.test_executor.auto_control.auto_control_process import \
    call_auto_control_test, call_auto_control_test_with_send, call_auto_control_test_multi_file, \
    call_auto_control_test_multi_file_and_send
from integration_testing_environment.utils.test_executor.load_density.load_density_process import \
    call_load_density_test, call_load_density_test_with_send, call_load_density_test_multi_file, \
    call_load_density_test_multi_file_and_send
from integration_testing_environment.utils.test_executor.web_runner.web_runner_process import call_web_runner_test, \
    call_web_runner_test_with_send, call_web_runner_test_multi_file, call_web_runner_test_multi_file_and_send


def build_ite_menu(ite_instance):
    # Testing tool menu
    # api testka menu
    ite_instance.api_testka_menu = Menu(ite_instance.menu, tearoff=0)
    ite_instance.api_testka_menu.add_command(
        label="Execute APITestka script",
        command=lambda: call_api_testka_test(
            ite_instance.code_editor_textarea.get(
                "1.0", END
            ),
            ite_instance.program_buffer
        )
    )
    ite_instance.api_testka_menu.add_command(
        label="Execute and send mail",
        command=lambda: call_api_testka_test_with_send(
            ite_instance.code_editor_textarea.get(
                "1.0", END
            ),
            ite_instance.program_buffer
        )
    )
    ite_instance.api_testka_menu.add_command(
        label="Execute multi script",
        command=lambda: call_api_testka_test_multi_file(
            ite_instance.program_buffer
        )
    )
    ite_instance.api_testka_menu.add_command(
        label="Execute multi script with send",
        command=lambda: call_api_testka_test_multi_file_and_send(
            ite_instance.program_buffer
        )
    )
    # auto control menu
    ite_instance.auto_control_menu = Menu(ite_instance.menu, tearoff=0)
    ite_instance.auto_control_menu.add_command(
        label="Execute AutoControl script",
        command=lambda: call_auto_control_test(
            ite_instance.code_editor_textarea.get(
                "1.0", END
            ),
            ite_instance.program_buffer
        )
    )
    ite_instance.auto_control_menu.add_command(
        label="Execute and send mail",
        command=lambda: call_auto_control_test_with_send(
            ite_instance.code_editor_textarea.get(
                "1.0", END
            ),
            ite_instance.program_buffer
        )
    )
    ite_instance.auto_control_menu.add_command(
        label="Execute multi script",
        command=lambda: call_auto_control_test_multi_file(
            ite_instance.program_buffer
        )
    )
    ite_instance.auto_control_menu.add_command(
        label="Execute multi script with send",
        command=lambda: call_auto_control_test_multi_file_and_send(
            ite_instance.program_buffer
        )
    )
    # web runner menu
    ite_instance.web_runner_menu = Menu(ite_instance.menu, tearoff=0)
    ite_instance.web_runner_menu.add_command(
        label="Execute WebRunner Script",
        command=lambda: call_web_runner_test(
            ite_instance.code_editor_textarea.get(
                "1.0", END
            ),
            ite_instance.program_buffer
        )
    )
    ite_instance.web_runner_menu.add_command(
        label="Execute And Send Mail",
        command=lambda: call_web_runner_test_with_send(
            ite_instance.code_editor_textarea.get(
                "1.0", END
            ),
            ite_instance.program_buffer
        )
    )
    ite_instance.web_runner_menu.add_command(
        label="Execute multi script",
        command=lambda:  call_web_runner_test_multi_file(
            ite_instance.program_buffer
        )
    )
    ite_instance.web_runner_menu.add_command(
        label="Execute multi script with send",
        command=lambda:  call_web_runner_test_multi_file_and_send(
            ite_instance.program_buffer
        )
    )
    # load density menu
    ite_instance.load_density_menu = Menu(ite_instance.menu, tearoff=0)
    ite_instance.load_density_menu.add_command(
        label="Execute LoadDensity Script",
        command=lambda: call_load_density_test(
            ite_instance.code_editor_textarea.get(
                "1.0", END
            ),
            ite_instance.program_buffer
        )
    )
    ite_instance.load_density_menu.add_command(
        label="Execute And Send Mail",
        command=lambda: call_load_density_test_with_send(
            ite_instance.code_editor_textarea.get(
                "1.0", END
            ),
            ite_instance.program_buffer
        )
    )
    ite_instance.load_density_menu.add_command(
        label="Execute multi script",
        command=lambda:  call_load_density_test_multi_file(
            ite_instance.program_buffer
        )
    )
    ite_instance.load_density_menu.add_command(
        label="Execute multi script with send",
        command=lambda:  call_load_density_test_multi_file_and_send(
            ite_instance.program_buffer
        )
    )
    # add all menu to Testing Tool menu
    ite_instance.menu.add_cascade(label="APITestka", menu=ite_instance.api_testka_menu)
    ite_instance.menu.add_cascade(label="AutoControl", menu=ite_instance.auto_control_menu)
    ite_instance.menu.add_cascade(label="WebRunner", menu=ite_instance.web_runner_menu)
    ite_instance.menu.add_cascade(label="LoadDensity", menu=ite_instance.load_density_menu)
    # popup menu
    ite_instance.popup_menu.add_separator()
    ite_instance.popup_menu.add_cascade(label="APITestka", menu=ite_instance.api_testka_menu)
    ite_instance.popup_menu.add_cascade(label="AutoControl", menu=ite_instance.auto_control_menu)
    ite_instance.popup_menu.add_cascade(label="WebRunner", menu=ite_instance.web_runner_menu)
    ite_instance.popup_menu.add_cascade(label="LoadDensity", menu=ite_instance.load_density_menu)
