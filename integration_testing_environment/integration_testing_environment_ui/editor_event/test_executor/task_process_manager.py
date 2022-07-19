import shutil
from queue import Queue, Empty
from threading import Thread
from tkinter import END

from integration_testing_environment.utils.manager.package_manager.package_manager_class import package_manager

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

import subprocess


class TaskProcessManager(object):
    def __init__(self, subprocess_result_text):
        self.read_program_error_output_from_thread = None
        self.read_program_output_from_thread = None
        self.still_run_program = True
        self.program_encoding = "utf-8"
        self.run_output_queue = Queue()
        self.run_error_queue = Queue()
        self.text = subprocess_result_text
        self.process = None

    def check_return_code(self):
        try:
            if self.run_output_queue is not None:
                self.text.insert(END, self.run_output_queue.get_nowait() + "\n")
            if self.run_error_queue is not None:
                self.text.insert(END, self.run_error_queue.get_nowait() + "\n")
        except Empty:
            pass
        process_return_code = self.process.poll()
        if process_return_code is None:
            self.text.after(10, self.check_return_code)
        elif process_return_code == 0:
            self.still_run_program = False
            self.process = None
            print("success")
        else:
            self.still_run_program = False
            print("failed")

    def start_test_process(self):
        # try to find file and compiler
            compiler_path = shutil.which("python3")
            if compiler_path is None:
                compiler_path = shutil.which("python")
            self.process = subprocess.Popen(
                [compiler_path, "-m", "je_api_testka", "--execute_str",
                 '{"api_testka":[["test_api_method",{ "http_method": "post", "test_url": "http://httpbin.org/post", "params": { "task": "new task" } }], ["test_api_method", { "http_method": "post", "test_url": "http://httpbin.org/post"}]]}'],
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
        self.run_output_queue = Queue()
        self.run_error_queue = Queue()

    def read_program_output_from_process(self):
        while self.still_run_program:
            program_output_data = self.process.stdout.raw.read(1024000).decode(self.program_encoding)
            if program_output_data.strip() != "":
                print(program_output_data)
                self.run_output_queue.put_nowait(program_output_data)

    def read_program_error_output_from_process(self):
        while self.still_run_program:
            program_error_output_data = self.process.stderr.raw.read(1024000).decode(self.program_encoding)
            if program_error_output_data.strip() != "":
                print(program_error_output_data)
                self.run_error_queue.put_nowait(program_error_output_data)


app = tk.Tk()
text = tk.Text(app, wrap="none")
manager = TaskProcessManager(text)
button = tk.Button(
    app,
    text='Start',
    command=manager.start_test_process
)
text.pack()
button.pack()

app.mainloop()
