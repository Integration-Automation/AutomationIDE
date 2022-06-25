import sys
from importlib import import_module

try:
    import_module("dwadawdawdaw")
except ModuleNotFoundError as error:
    print(repr(error), file=sys.stderr)

try:
    temp_time_module = import_module("time")
    print(temp_time_module)
    print(dir(temp_time_module))
    temp_time_module.sleep(2)
except ModuleNotFoundError as error:
    print(repr(error), file=sys.stderr)
