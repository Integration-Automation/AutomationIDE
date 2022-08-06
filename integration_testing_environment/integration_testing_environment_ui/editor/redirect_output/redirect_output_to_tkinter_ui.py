from tkinter import NORMAL, END, DISABLED

from integration_testing_environment.utils.manager.redirect_manager.redirect_manager_class import \
    redirect_manager_instance


def redirect_output(ite_instance):
    ite_instance.program_run_result_textarea.configure(state=NORMAL)
    if not redirect_manager_instance.std_out_queue.empty():
        ite_instance.program_run_result_textarea.insert(
            END,
            redirect_manager_instance.std_out_queue.get_nowait(),
        )
    if not redirect_manager_instance.std_err_queue.empty():
        ite_instance.program_run_result_textarea.tag_configure("warning", foreground="red")
        ite_instance.program_run_result_textarea.insert(
            END,
            redirect_manager_instance.std_err_queue.get_nowait(),
            "warning",
        )
    ite_instance.program_run_result_textarea.configure(state=DISABLED)
    ite_instance.program_run_result_textarea.after(10, lambda: redirect_output(ite_instance))
