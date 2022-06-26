from integration_testing_environment.utils.manager.package_manager.package_manager_class import package_manager


class ExecutorManager(object):

    def __init__(self):
        self.executor_manager_dict = {
            "je_auto_control": None,
            "je_api_testka": None,
            "je_load_density": None,
            "je_web_runner": None,
        }
        for package in package_manager.installed_package_dict.keys():
            if package in self.executor_manager_dict.keys() and package_manager.installed_package_dict.get(
                    package) is not None:
                self.executor_manager_dict.update(
                    {
                        package: package_manager.installed_package_dict.get(package).execute_action
                    }
                )
        """
        self.executor_dict = dict()
        for executor in self.executor_manager_dict.keys():
            if executor is not None and self.executor_manager_dict.get(
                executor
            ) is not None:
                pass
        """


executor_manager = ExecutorManager()
