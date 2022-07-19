import sys

from integration_testing_environment.integration_testing_environment_ui.editor_event. \
    test_executor.auto_control.auto_control_executor import call_auto_control_test

test_str = None
if sys.platform in ["win32", "cygwin", "msys"]:
    test_str = \
        """
            [
            ["type_key", {"keycode": 65}],
            ["mouse_left", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
            ["position"],
            ["press_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
            ["release_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
            ["type_key", {"mouse_keycode": "dwadwawda", "dwadwad": 500, "wdawddwawad": 500}],
            ["generate_html"]
        ]
        """
elif sys.platform in ["linux", "linux2"]:
    test_str = \
        """
            [
            ["type_key", {"keycode": 38}],
            ["mouse_left", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
            ["position"],
            ["press_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
            ["release_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
            ["type_key", {"mouse_keycode": "dwadwawda", "dwadwad": 500, "wdawddwawad": 500}],
            ["generate_html"]
        ]
        """
elif sys.platform in ["darwin"]:
    test_str = \
        """
        [
        ["type_key", {"keycode": 0x00}],
        ["mouse_left", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["position"],
        ["press_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["release_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["type_key", {"mouse_keycode": "dwadwawda", "dwadwad": 500, "wdawddwawad": 500}],
        ["generate_html"]
    ]
        """
test_result_dict = call_auto_control_test(test_str)
if test_result_dict is not None:
    for execute_detail, execute_return_value in test_result_dict.items():
        print(execute_detail)
        print(execute_return_value)

