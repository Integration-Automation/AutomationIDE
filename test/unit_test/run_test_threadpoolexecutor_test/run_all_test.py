import sys

from integration_testing_environment.utils.run_test_executor.run_test_threadpoolexecutor import api_testka_executor
from integration_testing_environment.utils.run_test_executor.run_test_threadpoolexecutor import auto_control_executor
from integration_testing_environment.utils.run_test_executor.run_test_threadpoolexecutor import load_density_executor
from integration_testing_environment.utils.run_test_executor.run_test_threadpoolexecutor import web_runner_executor

api_testka_test_action_list = [
    ["test_api_method", {"http_method": "post", "test_url": "http://httpbin.org/post", "params": {"task": "new task"}}],
    ["test_api_method", {"http_method": "post", "test_url": "http://httpbin.org/post",
                         "result_check_dict": {"status_code": 300}}
     ],
    ["generate_html", {"html_name": "default_name"}]
]

autocontrol_test_list = None
if sys.platform in ["win32", "cygwin", "msys"]:
    autocontrol_test_list = [
        ["type_key", {"keycode": 65}],
        ["mouse_left", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["position"],
        ["press_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["release_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["type_key", {"mouse_keycode": "dwadwawda", "dwadwad": 500, "wdawddwawad": 500}],
    ]

elif sys.platform in ["linux", "linux2"]:
    autocontrol_test_list = [
        ["type_key", {"keycode": 38}],
        ["mouse_left", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["position"],
        ["press_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["release_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["type_key", {"mouse_keycode": "dwadwawda", "dwadwad": 500, "wdawddwawad": 500}],
    ]
elif sys.platform in ["darwin"]:
    autocontrol_test_list = [
        ["type_key", {"keycode": 0x00}],
        ["mouse_left", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["position"],
        ["press_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["release_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["type_key", {"mouse_keycode": "dwadwawda", "dwadwad": 500, "wdawddwawad": 500}],
    ]

load_density_test_list = [
    ["loading_test_with_user", {"user_detail_dict": {
        "request_method": "get",
        "request_url": "http://httpbin.org/get"
    },
        "user_count": 50, "spawn_rate": 10, "test_time": 10}
     ],
    ["generate_html"]
]

test_execute_list = [
    ["get_webdriver_manager", {"webdriver_name": "firefox"}],
    ["to_url", {"url": "https://www.google.com"}],
    ["SaveTestObject", {"test_object_name": "q", "object_type": "name"}],
    ["implicitly_wait", {"time_to_wait": 3}],
    ["find_element", {"element_name": "q"}],
    ["click_element"],
    ["implicitly_wait", {"time_to_wait": 3}],
    ["input_to_element", {"input_value": "test 123 test do you read"}],
    ["to_url", {"url": "https://www.google.com"}],
    ["move_to_element", {"element_name": "q"}],
    ["implicitly_wait", {"time_to_wait": 3}],
    ["move_to_element_with_offset", {"element_name": "q", "offset_x": 10, "offset_y": 10}],
    ["move_by_offset", {"offset_x": 10, "offset_y": 10}],
    ["drag_and_drop", {"element_name": "q", "target_element_name": "q"}],
    ["drag_and_drop_offset", {"element_name": "q", "offset_x": 10, "offset_y": 10}],
    ["perform"],
    ["left_click", {"element_name": "q"}],
    ["release", {"element_name": "q"}],
    ["left_click"],
    ["release"],
    ["left_double_click"],
    ["release"],
    ["left_double_click"],
    ["left_click_and_hold"],
    ["press_key", {"keycode_on_key_class": "\ue031"}],
    ["release_key", {"keycode_on_key_class": "\ue031"}],
    ["send_keys", {"keys_to_send": "\ue031"}],
    ["send_keys_to_element", {"element_name": "q", "keys_to_send": "\ue031"}],
    ["perform"],
    ["pause", {"seconds": "3"}],
    ["quit"],
    ["generate_html"]
]

load_density_executor(load_density_test_list)
web_runner_executor(test_execute_list)
api_testka_executor(api_testka_test_action_list)
auto_control_executor(autocontrol_test_list)
