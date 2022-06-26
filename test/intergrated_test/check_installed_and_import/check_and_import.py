import sys
from importlib.util import find_spec
from importlib.util import module_from_spec

temp_test_find_spec = find_spec("je_auto_control")
print(temp_test_find_spec)
if temp_test_find_spec is not None:
    print(temp_test_find_spec.name)
    try:
        autocontrol = module_from_spec(temp_test_find_spec)
        print(autocontrol)
    except ModuleNotFoundError as error:
        print(repr(error), file=sys.stderr)
