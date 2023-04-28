import os
import sys
from importlib import import_module
from importlib.util import find_spec


class PackageManager(object):

    def __init__(self):
        os.environ["WDM_LOG"] = "0"
        self.installed_package_dict = {
            "je_auto_control": None,
            "je_load_density": None,
            "je_api_testka": None,
            "je_web_runner": None,
            "je_mail_thunder": None,
        }
        self.syntax_check_list = [
            "je_auto_control",
            "je_load_density",
            "je_api_testka",
            "je_web_runner"
        ]
        try:
            import je_load_density
            import je_web_runner
            import je_auto_control
            import je_api_testka
            self.installed_package_dict.update(
                {
                    "je_api_testka": je_api_testka,
                    "je_web_runner": je_web_runner,
                    "je_auto_control": je_auto_control,
                    "je_load_density": je_load_density,
                }
            )
        except ImportError:
            pass

    # This will make subprocess deadlock so emm we don't use this
    def check_package(self):
        for package, value in self.installed_package_dict.items():
            found_spec = find_spec(package)
            if found_spec is not None and value is None:
                try:
                    installed_package = import_module(found_spec.name)
                    self.installed_package_dict.update({found_spec.name: installed_package})
                except ModuleNotFoundError as error:
                    print(repr(error), file=sys.stderr)


package_manager = PackageManager()
