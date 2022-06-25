from importlib.util import find_spec

temp_test_find_spec = find_spec("dwadawddawddwa")
print(temp_test_find_spec)
temp_test_find_spec = find_spec("je_auto_control")
print(temp_test_find_spec)
print(temp_test_find_spec.name)
