import os
import shutil
import sys
from pathlib import Path

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow
from je_editor import ShellManager


def set_install_menu(ui_we_want_to_set: QMainWindow):
    """
    Build menu include install package feature.
    :param ui_we_want_to_set: main window to add menu.
    :return: None
    """
    ui_we_want_to_set.install_menu = ui_we_want_to_set.menu.addMenu("Install")
    # Try to install Build Tools
    ui_we_want_to_set.install_tool_action = QAction("Install Build Tools")
    ui_we_want_to_set.install_tool_action.triggered.connect(
        lambda: install_build_tools(ui_we_want_to_set)
    )
    ui_we_want_to_set.install_menu.addAction(ui_we_want_to_set.install_tool_action)
    # Try to install AutoControl
    ui_we_want_to_set.install_autocontrol_action = QAction("Install AutoControl")
    ui_we_want_to_set.install_autocontrol_action.triggered.connect(
        lambda: install_autocontrol(ui_we_want_to_set)
    )
    ui_we_want_to_set.install_menu.addAction(ui_we_want_to_set.install_autocontrol_action)
    # Try to install APITestka
    ui_we_want_to_set.install_api_testka = QAction("Install APITestka")
    ui_we_want_to_set.install_api_testka.triggered.connect(
        lambda: install_api_testka(ui_we_want_to_set)
    )
    ui_we_want_to_set.install_menu.addAction(ui_we_want_to_set.install_api_testka)
    # Try to install LoadDensity
    ui_we_want_to_set.install_load_density_action = QAction("Install LoadDensity")
    ui_we_want_to_set.install_load_density_action.triggered.connect(
        lambda: install_load_density(ui_we_want_to_set)
    )
    ui_we_want_to_set.install_menu.addAction(ui_we_want_to_set.install_load_density_action)
    # Try to install WebRunner
    ui_we_want_to_set.install_web_runner_action = QAction("Install WebRunner")
    ui_we_want_to_set.install_web_runner_action.triggered.connect(
        lambda: install_web_runner(ui_we_want_to_set)
    )
    ui_we_want_to_set.install_menu.addAction(ui_we_want_to_set.install_web_runner_action)


def install_package(package_text: str, ui_we_want_to_set: QMainWindow) -> None:
    if sys.platform in ["win32", "cygwin", "msys"]:
        venv_path = Path(os.getcwd() + "/venv/Scripts")
    else:
        venv_path = Path(os.getcwd() + "/venv/bin")
    if venv_path.is_dir() and venv_path.exists():
        compiler_path = shutil.which(
            cmd="python3",
            path=str(venv_path)
        )
    else:
        compiler_path = shutil.which(cmd="python3")
    if compiler_path is None:
        compiler_path = shutil.which(
            cmd="python",
            path=str(venv_path)
        )
    else:
        compiler_path = shutil.which(cmd="python")
    shell_manager = ShellManager()
    shell_manager.main_window = ui_we_want_to_set
    shell_manager.later_init()
    shell_manager.exec_shell([f"{compiler_path}", "-m", "pip", "install", f"{package_text}"])


def install_build_tools(ui_we_want_to_set: QMainWindow) -> None:
    install_package("setuptools", ui_we_want_to_set)
    install_package("build", ui_we_want_to_set)
    install_package("wheel", ui_we_want_to_set)


def install_autocontrol(ui_we_want_to_set: QMainWindow) -> None:
    install_package("je_auto_control", ui_we_want_to_set)


def install_api_testka(ui_we_want_to_set: QMainWindow) -> None:
    install_package("je_api_testka", ui_we_want_to_set)


def install_load_density(ui_we_want_to_set: QMainWindow) -> None:
    install_package("je_load_density", ui_we_want_to_set)


def install_web_runner(ui_we_want_to_set: QMainWindow) -> None:
    install_package("je_web_runner", ui_we_want_to_set)
