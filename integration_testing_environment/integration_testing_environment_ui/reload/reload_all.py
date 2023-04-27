from integration_testing_environment.utils.manager.package_manager.package_manager_class import check_package, \
    package_manager


def reload_all():
    check_package(package_manager.installed_package_dict)
