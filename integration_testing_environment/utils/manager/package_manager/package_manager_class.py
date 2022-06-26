from importlib import import_module

import os
import sys
from importlib.util import find_spec


def check_package(installed_package_dict: dict):
    check_list = [
        "je_auto_control",
        "je_load_density",  # load density need in top of api_testka
        "je_api_testka",
        "je_web_runner",
        "je_mail_thunder",
        "je_tk_plot",
    ]
    for package in check_list:
        found_spec = find_spec(package)
        if found_spec is not None:
            try:
                installed_package = import_module(found_spec.name)
                installed_package_dict.update({found_spec.name: installed_package})
            except ModuleNotFoundError as error:
                print(repr(error), file=sys.stderr)


class PackageManager(object):

    def __init__(self):
        os.environ["WDM_LOG"] = "0"
        self.installed_package_dict = {
            "je_auto_control": None,
            "je_api_testka": None,
            "je_load_density": None,
            "je_web_runner": None,
            "je_mail_thunder": None,
            "je_tk_plot": None,
        }
        check_package(self.installed_package_dict)


package_manager = PackageManager()
