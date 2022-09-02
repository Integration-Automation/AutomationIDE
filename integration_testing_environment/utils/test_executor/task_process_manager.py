import shutil
import subprocess
import threading
import tkinter
import typing
from queue import Queue, Empty
from threading import Thread
from tkinter import END, DISABLED, NORMAL, ttk
from tkinter import Toplevel, Text


class TaskProcessManager(object):
    def __init__(
            self, title_name: str,
            task_done_trigger_function: typing.Callable = None,
            error_trigger_function: typing.Callable = None,
            use_theme=None,
            program_buffer_size: int = 1024000
    ):
        super().__init__()
        # ite_instance param
        self.read_program_error_output_from_thread: [threading.Thread, None] = None
        self.read_program_output_from_thread: [threading.Thread, None] = None
        self.still_run_program: bool = True
        self.program_encoding: str = "utf-8"
        self.run_output_queue: Queue = Queue()
        self.run_error_queue: Queue = Queue()
        self.process: [subprocess.Popen, None] = None
        self.task_done_trigger_function: typing.Callable = task_done_trigger_function
        self.error_trigger_function: typing.Callable = error_trigger_function
        # ui
        self.title_name: str = title_name
        self.tkinter_top_level: [tkinter.Toplevel, None] = None
        self.tkinter_text_frame: [tkinter.Frame, None] = None
        self.tkinter_text: [tkinter.Text, None] = None
        self.tkinter_text_scrollbar_y: [tkinter.Scrollbar, None] = None
        self.tkinter_text_scrollbar_x: [tkinter.Scrollbar, None] = None
        self.style: ttk.Style = ttk.Style()
        if use_theme is not None:
            self.style.theme_use(use_theme)
        self.program_buffer_size = program_buffer_size

    def set_ui(self):
        # ite_instance tkinter ui
        self.tkinter_top_level = Toplevel()
        self.tkinter_text_frame = ttk.Frame(self.tkinter_top_level, padding="3 3 12 12")
        self.tkinter_text = Text(self.tkinter_text_frame, wrap="none")
        self.tkinter_text_scrollbar_y = ttk.Scrollbar(self.tkinter_text_frame, orient="vertical",
                                                      command=self.tkinter_text.yview)
        self.tkinter_text_scrollbar_x = ttk.Scrollbar(self.tkinter_text_frame, orient="horizontal",
                                                      command=self.tkinter_text.xview)
        self.tkinter_text["yscrollcommand"] = self.tkinter_text_scrollbar_y.set
        self.tkinter_text["xscrollcommand"] = self.tkinter_text_scrollbar_x.set
        self.tkinter_text.configure(state=DISABLED)
        self.tkinter_top_level.title(self.title_name)
        self.tkinter_text_frame.grid(column=0, row=0, sticky="nsew")
        self.tkinter_text.grid(column=0, row=0, sticky="nsew")
        self.tkinter_text_scrollbar_y.grid(column=1, row=0, sticky="ns")
        self.tkinter_text_scrollbar_x.grid(column=0, row=1, sticky="nsew")
        self.tkinter_text.tag_configure("warning", foreground="red")
        self.tkinter_text.bind("<1>", lambda event: self.tkinter_text.focus_set())
        self.tkinter_text_frame.columnconfigure(0, weight=1)
        self.tkinter_text_frame.rowconfigure(0, weight=1)
        self.tkinter_top_level.columnconfigure(0, weight=1)
        self.tkinter_top_level.rowconfigure(0, weight=1)
        self.tkinter_top_level.protocol("WM_DELETE_WINDOW", self.close_task_ui_event)

    def check_return_code(self):
        try:
            self.tkinter_text.configure(state=NORMAL)
            if not self.run_output_queue.empty():
                self.tkinter_text.insert(END, self.run_output_queue.get_nowait() + "\n")
            if not self.run_error_queue.empty():
                self.tkinter_text.insert(END, self.run_error_queue.get_nowait(), "warning")
            self.tkinter_text.configure(state=DISABLED)
        except Empty:
            pass
        process_return_code = self.process.poll()
        if process_return_code is None:
            self.tkinter_text.after(10, self.check_return_code)
        elif process_return_code == 0:
            self.still_run_program = False
            self.print_and_clear_queue()
            self.process = None
            if self.task_done_trigger_function is not None:
                self.task_done_trigger_function()
        else:
            self.still_run_program = False
            self.print_and_clear_queue()
            self.process = None
            if self.error_trigger_function is not None:
                self.error_trigger_function()

    def start_test_process(self, package: str, exec_str: str):
        # try to find file and compiler
        compiler_path = shutil.which("python")
        if compiler_path is None:
            compiler_path = shutil.which("python3")
        self.set_ui()
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
        try:
            self.tkinter_text.configure(state=NORMAL)
            for std_output in iter(self.run_output_queue.get_nowait, None):
                self.tkinter_text.insert(END, std_output + "\n")
            for std_err in iter(self.run_error_queue.get_nowait, None):
                self.tkinter_text.insert(END, std_err, "warning", "\n")
            self.tkinter_text.configure(state=DISABLED)
        except Empty:
            pass
        self.run_output_queue = Queue()
        self.run_error_queue = Queue()

    def close_task_ui_event(self):
        if self.tkinter_top_level is not None:
            self.tkinter_top_level.destroy()
        self.still_run_program = False
        if self.process is not None:
            self.process.terminate()

    def read_program_output_from_process(self):
        while self.still_run_program:
            program_output_data = self.process.stdout.raw.read(self.program_buffer_size).decode(self.program_encoding)
            if program_output_data.strip() != "":
                self.run_output_queue.put(program_output_data)

    def read_program_error_output_from_process(self):
        while self.still_run_program:
            program_error_output_data = self.process.stderr.raw.read(self.program_buffer_size).decode(self.program_encoding)
            if program_error_output_data.strip() != "":
                self.run_error_queue.put(program_error_output_data)
