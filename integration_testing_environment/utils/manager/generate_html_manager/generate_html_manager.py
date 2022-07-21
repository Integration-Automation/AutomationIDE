from integration_testing_environment.utils.manager.package_manager.package_manager_class import package_manager


class HTMLReportManager(object):

    def __init__(self):
        self.html_report_manager_dict = {
            "je_auto_control": None,
            "je_api_testka": None,
            "je_load_density": None,
            "je_web_runner": None,
        }
        for package in package_manager.installed_package_dict.keys():
            if package in self.html_report_manager_dict.keys() and package_manager.installed_package_dict.get(
                    package) is not None:
                self.html_report_manager_dict.update(
                    {
                        package: package_manager.installed_package_dict.get(package).generate_html
                    }
                )


html_report_manager = HTMLReportManager()
