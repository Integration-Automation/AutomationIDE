from integration_testing_environment.intergration_testing_environment_cli.cli.extend_cli import ITECLI
from integration_testing_environment.intergration_testing_environment_ui.editor.extend_je_editor_ui import ITEUI


def start_ite_as_cli():
    ITECLI()


def start_ite_with_ui():
    ITEUI().start_editor()
