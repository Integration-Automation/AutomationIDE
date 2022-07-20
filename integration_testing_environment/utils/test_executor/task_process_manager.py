import shutil
import subprocess
import typing
from queue import Queue, Empty
from threading import Thread
from tkinter import END, Tk, Button, DISABLED, NORMAL, ttk
from tkinter import Toplevel, Text


class TaskProcessManager(Toplevel):
    def __init__(
            self, title_name: str,
            task_done_trigger_function: typing.Callable = None,
            error_trigger_function: typing.Callable = None,
    ):
        super().__init__()
        # self param
        self.read_program_error_output_from_thread = None
        self.read_program_output_from_thread = None
        self.still_run_program = True
        self.program_encoding = "utf-8"
        self.run_output_queue = Queue()
        self.run_error_queue = Queue()
        self.process = None
        self.task_done_trigger_function = task_done_trigger_function
        self.error_trigger_function = error_trigger_function
        # self tkinter ui
        self.tkinter_text_frame = ttk.Frame(self, padding="3 3 12 12")
        self.tkinter_text = Text(self.tkinter_text_frame, wrap="none")
        self.tkinter_text_scrollbar_y = ttk.Scrollbar(self.tkinter_text_frame, orient="vertical",
                                                      command=self.tkinter_text.yview)
        self.tkinter_text_scrollbar_x = ttk.Scrollbar(self.tkinter_text_frame, orient="horizontal",
                                                      command=self.tkinter_text.xview)
        self.tkinter_text["yscrollcommand"] = self.tkinter_text_scrollbar_y.set
        self.tkinter_text["xscrollcommand"] = self.tkinter_text_scrollbar_x.set
        self.tkinter_text.configure(state=DISABLED)
        self.title(title_name)
        self.tkinter_text_frame.grid(column=0, row=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.tkinter_text.grid(column=0, row=0, sticky="nsew")
        self.tkinter_text_scrollbar_y.grid(column=1, row=0, sticky="ns")
        self.tkinter_text_scrollbar_x.grid(column=0, row=1, sticky="nsew")

    def check_return_code(self):
        try:
            self.tkinter_text.configure(state=NORMAL)
            if not self.run_output_queue.empty():
                self.tkinter_text.insert(END, self.run_output_queue.get_nowait() + "\n")
            if not self.run_error_queue.empty():
                self.tkinter_text.insert(END, self.run_error_queue.get_nowait() + "\n")
            self.tkinter_text.configure(state=DISABLED)
        except Empty:
            pass
        process_return_code = self.process.poll()
        if process_return_code is None:
            self.tkinter_text.after(10, self.check_return_code)
        elif process_return_code == 0:
            self.still_run_program = False
            self.run_output_queue = Queue()
            self.run_error_queue = Queue()
            self.process = None
            if self.task_done_trigger_function is not None:
                self.task_done_trigger_function()
        else:
            self.still_run_program = False
            self.run_output_queue = Queue()
            self.run_error_queue = Queue()
            self.process = None
            if self.error_trigger_function is not None:
                self.error_trigger_function()

    def start_test_process(self, package: str, exec_str: str):
        # try to find file and compiler
        compiler_path = shutil.which("python3")
        if compiler_path is None:
            compiler_path = shutil.which("python")
        self.process = subprocess.Popen(
            [
                compiler_path,
                "-m",
                package,
                "--execute_str",
                exec_str
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        self.still_run_program = True
        # program output message queue thread
        self.read_program_output_from_thread = Thread(
            target=self.read_program_output_from_process,
            daemon=True
        ).start()
        # program error message queue thread
        self.read_program_error_output_from_thread = Thread(
            target=self.read_program_error_output_from_process,
            daemon=True
        ).start()
        self.check_return_code()

    def print_and_clear_queue(self):
        for std_output in iter(self.run_output_queue.get, None):
            self.tkinter_text.insert(END, std_output + "\n")
        for std_err in iter(self.run_error_queue.get, None):
            self.tkinter_text.insert(END, std_err + "\n")
        self.run_output_queue = Queue()
        self.run_error_queue = Queue()

    def read_program_output_from_process(self):
        while self.still_run_program:
            program_output_data = self.process.stdout.raw.read(1024000).decode(self.program_encoding)
            if program_output_data.strip() != "":
                print(program_output_data)
                self.run_output_queue.put(program_output_data)
                print(self.run_output_queue.queue)

    def read_program_error_output_from_process(self):
        while self.still_run_program:
            program_error_output_data = self.process.stderr.raw.read(1024000).decode(self.program_encoding)
            if program_error_output_data.strip() != "":
                print(program_error_output_data)
                self.run_error_queue.put(program_error_output_data)
                print(self.run_error_queue.queue)


if __name__ == "__main__":

    app = Tk()
    api_button = Button(
        app,
        text='je_api_testka',
        command=lambda: TaskProcessManager("je_api_testka").start_test_process(
            "je_api_testka",
            '{"api_testka":[["test_api_method",{ "http_method": "post", "test_url": "http://httpbin.org/post", "params": { "task": "new task" } }], ["test_api_method", { "http_method": "post", "test_url": "http://httpbin.org/post"}]]}'
        )
    )

    load_button = Button(
        app,
        text='load_density',
        command=lambda: TaskProcessManager("je_load_density").start_test_process(
            "je_load_density",
            '{"api_testka":[["test_api_method",{ "http_method": "post", "test_url": "http://httpbin.org/post", "params": { "task": "new task" } }], ["test_api_method", { "http_method": "post", "test_url": "http://httpbin.org/post"}]]}'
        )
    )
    auto_control_button = Button(
        app,
        text='autocontrol',
        command=lambda: TaskProcessManager("je_auto_control").start_test_process(
            "je_auto_control",
            '{"api_testka":[["test_api_method",{ "http_method": "post", "test_url": "http://httpbin.org/post", "params": { "task": "new task" } }], ["test_api_method", { "http_method": "post", "test_url": "http://httpbin.org/post"}]]}'
        )
    )
    web_button = Button(
        app,
        text='webrunner',
        command=lambda: TaskProcessManager("je_web_runner").start_test_process(
            "je_web_runner",
            '{"api_testka":[["test_api_method",{ "http_method": "post", "test_url": "http://httpbin.org/post", "params": { "task": "new task" } }], ["test_api_method", { "http_method": "post", "test_url": "http://httpbin.org/post"}]]}'
        )
    )
    api_button.pack()
    load_button.pack()
    auto_control_button.pack()
    web_button.pack()
    app.mainloop()
