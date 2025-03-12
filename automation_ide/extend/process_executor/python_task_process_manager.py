import json
import queue
import subprocess
import sys
import threading
import typing
from pathlib import Path
from queue import Queue
from threading import Thread

from PySide6.QtCore import QTimer
from je_editor.pyside_ui.main_ui.save_settings.user_color_setting_file import actually_color_dict
from je_editor.utils.venv_check.check_venv import check_and_choose_venv

from automation_ide.automation_editor_ui.show_code_window.code_window import CodeWindow


class TaskProcessManager(object):
    def __init__(
            self,
            main_window: CodeWindow,
            task_done_trigger_function: typing.Callable = None,
            error_trigger_function: typing.Callable = None,
            program_buffer_size: int = 1024,
            program_encoding: str = "utf-8"
    ):
        super().__init__()
        self.compiler_path = None
        # ite_instance param
        self.read_program_error_output_from_thread: [threading.Thread, None] = None
        self.read_program_output_from_thread: [threading.Thread, None] = None
        self.main_window: CodeWindow = main_window
        self.timer: QTimer = QTimer(self.main_window)
        self.still_run_program: bool = True
        self.program_encoding: str = program_encoding
        self.run_output_queue: Queue = Queue()
        self.run_error_queue: Queue = Queue()
        self.process: [subprocess.Popen, None] = None

        self.task_done_trigger_function: typing.Callable = task_done_trigger_function
        self.error_trigger_function: typing.Callable = error_trigger_function
        self.program_buffer_size = program_buffer_size

    def renew_path(self) -> None:
        if self.main_window.python_compiler is None:
            # Renew compiler path
            if sys.platform in ["win32", "cygwin", "msys"]:
                venv_path = Path(str(Path.cwd()) + "/venv/Scripts")
            else:
                venv_path = Path(str(Path.cwd()) + "/venv/bin")
            self.compiler_path = check_and_choose_venv(venv_path)
        else:
            self.compiler_path = self.main_window.python_compiler

    def start_test_process(self, package: str, exec_str: str):
        self.renew_path()
        if sys.platform in ["win32", "cygwin", "msys"]:
            exec_str = json.dumps(exec_str)
            args = [
                self.compiler_path,
                "-m",
                package,
                "--execute_str",
                exec_str
            ]
        else:
            args = " ".join([f"{self.compiler_path}", f"-m {package}", "--execute_str", f"{exec_str}"])
        self.process: subprocess.Popen = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            encoding=self.program_encoding
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
        self.main_window.setWindowTitle(package)
        self.main_window.show()
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.pull_text)
        self.timer.start()

    # Pyside UI update method
    def pull_text(self):
        try:
            self.main_window.code_result.setTextColor(actually_color_dict.get("normal_output_color"))
            if not self.run_output_queue.empty():
                output_message = self.run_output_queue.get_nowait()
                output_message = str(output_message).strip()
                if output_message:
                    self.main_window.code_result.append(output_message)
            self.main_window.code_result.setTextColor(actually_color_dict.get("error_output_color"))
            if not self.run_error_queue.empty():
                error_message = self.run_error_queue.get_nowait()
                error_message = str(error_message).strip()
                if error_message:
                    self.main_window.code_result.append(error_message)
            self.main_window.code_result.setTextColor(actually_color_dict.get("normal_output_color"))
        except queue.Empty:
            pass
        if self.process is not None:
            if self.process.returncode == 0:
                if self.timer.isActive():
                    self.timer.stop()
                self.exit_program()
            elif self.process.returncode is not None:
                if self.timer.isActive():
                    self.timer.stop()
                self.exit_program()
            if self.still_run_program:
                # poll return code
                self.process.poll()
        else:
            if self.timer.isActive():
                self.timer.stop()

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
            self.main_window.code_result.append(f"Task exit with code {self.process.returncode}")
            self.process = None

    def print_and_clear_queue(self):
        self.run_output_queue = queue.Queue()
        self.run_error_queue = queue.Queue()

    def read_program_output_from_process(self):
        while self.still_run_program:
            self.process: subprocess.Popen
            program_output_data = self.process.stdout.read(self.program_buffer_size)
            if self.process:
                self.process.stdout.flush()
            if program_output_data.strip() != "":
                self.run_output_queue.put(program_output_data)

    def read_program_error_output_from_process(self):
        while self.still_run_program:
            program_error_output_data = self.process.stderr.read(self.program_buffer_size)
            if self.process:
                self.process.stderr.flush()
            if program_error_output_data.strip() != "":
                self.run_error_queue.put(program_error_output_data)
