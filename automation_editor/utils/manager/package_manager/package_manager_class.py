import os


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


package_manager = PackageManager()
