import queue
import shutil
import subprocess
import threading
import typing
from queue import Queue
from threading import Thread

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QTextEdit, QWidget
from je_editor import error_color, output_color


class TaskProcessManager(object):
    def __init__(
            self,
            main_window,
            task_done_trigger_function: typing.Callable = None,
            error_trigger_function: typing.Callable = None,
            program_buffer_size: int = 1024000
    ):
        super().__init__()
        # ite_instance param
        self.read_program_error_output_from_thread: [threading.Thread, None] = None
        self.read_program_output_from_thread: [threading.Thread, None] = None
        self.main_window: QWidget = main_window
        self.code_result: QTextEdit = self.main_window.code_result
        self.timer: QTimer = QTimer(self.main_window)
        self.still_run_program: bool = True
        self.program_encoding: str = "utf-8"
        self.run_output_queue: Queue = Queue()
        self.run_error_queue: Queue = Queue()
        self.process: [subprocess.Popen, None] = None
        self.task_done_trigger_function: typing.Callable = task_done_trigger_function
        self.error_trigger_function: typing.Callable = error_trigger_function
        self.program_buffer_size = program_buffer_size

    def start_test_process(self, package: str, exec_str: str):
        # try to find file and compiler
        compiler_path = shutil.which("python")
        if compiler_path is None:
            compiler_path = shutil.which("python3")
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
        )
        self.read_program_output_from_thread.start()
        # program error message queue thread
        self.read_program_error_output_from_thread = Thread(
            target=self.read_program_error_output_from_process,
            daemon=True
        )
        self.read_program_error_output_from_thread.start()
        # start Pyside update
        # start timer
        self.timer = QTimer(self.main_window)
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.pull_text)
        self.timer.start()
        self.main_window.setWindowTitle(package)
        self.main_window.show()

    # Pyside UI update method
    def pull_text(self):
        try:
            self.code_result.setTextColor(error_color)
            if not self.run_error_queue.empty():
                error_message = self.run_error_queue.get_nowait()
                error_message = str(error_message).strip()
                if error_message:
                    self.code_result.append(error_message)
            self.code_result.setTextColor(output_color)
            if not self.run_output_queue.empty():
                output_message = self.run_output_queue.get_nowait()
                output_message = str(output_message).strip()
                if output_message:
                    self.code_result.append(output_message)
        except queue.Empty:
            pass
        if self.process.returncode == 0:
            self.exit_program()
        elif self.process.returncode is not None:
            self.exit_program()
            self.timer.stop()
        if self.still_run_program:
            # poll return code
            self.process.poll()

    # exit program change run flag to false and clean read thread and queue and process
    def exit_program(self):
        self.still_run_program = False
        if self.read_program_output_from_thread is not None:
            self.read_program_output_from_thread = None
        if self.read_program_error_output_from_thread is not None:
            self.read_program_error_output_from_thread = None
        self.print_and_clear_queue()
        if self.process is not None:
            self.process.terminate()

    def print_and_clear_queue(self):
        try:
            for std_output in iter(self.run_output_queue.get_nowait, None):
                std_output = str(std_output).strip()
                if std_output:
                    self.code_result.append(std_output)
            self.code_result.setTextColor(error_color)
            for std_err in iter(self.run_error_queue.get_nowait, None):
                std_err = str(std_err).strip()
                if std_err:
                    self.code_result.append(std_err)
            self.code_result.setTextColor(output_color)
        except queue.Empty:
            pass
        self.run_output_queue = queue.Queue()
        self.run_error_queue = queue.Queue()

    def read_program_output_from_process(self):
        while self.still_run_program:
            program_output_data = self.process.stdout.raw.read(self.program_buffer_size).decode(self.program_encoding)
            if program_output_data.strip() != "":
                self.run_output_queue.put(program_output_data)

    def read_program_error_output_from_process(self):
        while self.still_run_program:
            program_error_output_data = self.process.stderr.raw.read(self.program_buffer_size).decode(
                self.program_encoding)
            if program_error_output_data.strip() != "":
                self.run_error_queue.put(program_error_output_data)

