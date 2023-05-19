api_testka_keys: list = [
    "test_api_method", "generate_html", "generate_html_report", "generate_json",
    "generate_json_report", "generate_xml",
    "generate_xml_report", "execute_action", "execute_files", "add_package_to_executor",
    "flask_mock_server_add_router",
    "start_flask_mock_server"
]
auto_control_keys: list = [
    "mouse_left", "mouse_right", "mouse_middle", "click_mouse", "get_mouse_table", "get_mouse_position", "press_mouse",
    "release_mouse", "mouse_scroll", "set_mouse_position", "get_special_table", "get_keyboard_keys_table",
    "type_keyboard",
    "press_keyboard_key", "release_keyboard_key", "check_key_is_press", "write", "hotkey", "locate_all_image",
    "locate_image_center", "locate_and_click", "screen_size", "screenshot", "set_record_enable", "generate_html",
    "generate_json", "generate_xml", "generate_html_report", "generate_json_report", "generate_xml_report", "record",
    "stop_record", "execute_action", "execute_files", "add_package_to_executor", "add_package_to_callback_executor",
    "create_project"
]
web_runner_keys: list = [
    "get_webdriver_manager", "change_index_of_webdriver", "quit", "SaveTestObject", "CleanTestObject", "set_driver",
    "set_webdriver_options_capability", "find_element", "find_elements", "implicitly_wait", "explict_wait", "to_url",
    "forward", "back", "refresh", "switch", "set_script_timeout", "set_page_load_timeout", "get_cookies", "get_cookie",
    "add_cookie", "delete_cookie", "delete_all_cookies", "execute", "execute_script", "execute_async_script",
    "move_to_element", "move_to_element_with_offset", "drag_and_drop", "drag_and_drop_offset", "perform",
    "reset_actions",
    "left_click", "left_click_and_hold", "right_click", "left_double_click", "release", "press_key", "release_key",
    "move_by_offset", "pause", "send_keys", "send_keys_to_element", "scroll", "check_current_webdriver",
    "maximize_window",
    "fullscreen_window", "minimize_window", "set_window_size", "set_window_position", "get_window_position",
    "get_window_rect", "set_window_rect", "get_screenshot_as_png", "get_screenshot_as_base64", "get_log", "single_quit",
    "element_submit", "element_clear", "element_get_property", "element_get_dom_attribute", "element_get_attribute",
    "element_is_selected", "element_is_enabled", "input_to_element", "click_element", "element_is_displayed",
    "element_value_of_css_property", "element_screenshot", "element_change_web_element",
    "element_check_current_web_element", "element_get_select", "set_record_enable", "generate_html",
    "generate_html_report", "generate_json", "generate_json_report", "generate_xml", "generate_xml_report",
    "execute_action", "execute_files", "add_package_to_executor", "add_package_to_callback_executor"
]

load_density_keys: list = [
    "start_test", "generate_html", "generate_html_report", "generate_json", "generate_json_report", "generate_xml",
    "generate_xml_report", "execute_action", "execute_files", "add_package_to_executor"
]

package_keyword_list = {
    "je_auto_control": auto_control_keys,
    "je_load_density": load_density_keys,
    "je_api_testka": api_testka_keys,
    "je_web_runner": web_runner_keys
}
