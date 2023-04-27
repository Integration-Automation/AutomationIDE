import sys
from importlib.util import find_spec
from importlib.util import module_from_spec

temp_spec_list = list()

for package in [
    "je_auto_control", "je_web_runner", "je_api_testka",
    "je_load_density", "je_mail_thunder", "je_editor"
]:
    temp_test_find_spec = find_spec(package)
    print(temp_test_find_spec)
    if temp_test_find_spec is not None:
        print(temp_test_find_spec.name)
        try:
            package_module = module_from_spec(temp_test_find_spec)
            print(package_module)
        except ModuleNotFoundError as error:
            print(repr(error), file=sys.stderr)
