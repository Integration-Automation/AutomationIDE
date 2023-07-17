api_testka_keys: list = [
    "test_api_method", "generate_html", "generate_html_report", "generate_json",
    "generate_json_report", "generate_xml",
    "generate_xml_report", "execute_action", "execute_files", "add_package_to_executor",
    "flask_mock_server_add_router",
    "start_flask_mock_server"]

auto_control_keys: list = [
    "AC_mouse_left", "AC_mouse_right", "AC_mouse_middle", "AC_click_mouse", "AC_get_mouse_table",
    "AC_get_mouse_position", "AC_press_mouse", "AC_release_mouse", "AC_mouse_scroll",
    "AC_set_mouse_position", "AC_get_special_table", "AC_get_keyboard_keys_table",
    "AC_type_keyboard", "AC_press_keyboard_key", "AC_release_keyboard_key", "AC_check_key_is_press",
    "AC_write", "AC_hotkey", "AC_locate_all_image", "AC_locate_image_center",
    "AC_locate_and_click", "AC_screen_size", "AC_screenshot", "AC_set_record_enable", "AC_generate_html",
    "AC_generate_json", "AC_generate_xml", "AC_generate_html_report", "AC_generate_json_report",
    "AC_generate_xml_report", "AC_record", "AC_stop_record", "AC_execute_action",
    "AC_execute_files", "AC_add_package_to_executor", "AC_add_package_to_callback_executor",
    "AC_create_project", "AC_shell_command", "AC_execute_process", "AC_scheduler_event_trigger",
    "AC_remove_blocking_scheduler_job", "AC_remove_nonblocking_scheduler_job",
    "AC_start_blocking_scheduler", "AC_start_nonblocking_scheduler", "AC_start_all_scheduler",
    "AC_shutdown_blocking_scheduler", "AC_shutdown_nonblocking_scheduler"
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
    "execute_action", "execute_files", "add_package_to_executor", "add_package_to_callback_executor"]

load_density_keys: list = [
    "start_test", "generate_html", "generate_html_report", "generate_json", "generate_json_report", "generate_xml",
    "generate_xml_report", "execute_action", "execute_files", "add_package_to_executor"]

automation_file_keys: list = [
    "create_file", "copy_file", "rename_file", "remove_file", "copy_all_file_to_dir",
    "copy_specify_extension_file", "copy_dir", "create_dir", "remove_dir_tree", "zip_dir", "zip_file", "zip_info",
    "zip_file_info", "set_zip_password", "unzip_file", "read_zip_file", "unzip_all", "drive_later_init",
    "drive_search_all_file", "drive_search_field", "drive_search_file_mimetype", "drive_upload_dir_to_folder",
    "drive_upload_to_folder", "drive_upload_dir_to_drive", "drive_upload_to_drive",
    "drive_add_folder", "drive_share_file_to_anyone", "drive_share_file_to_domain",
    "drive_share_file_to_user", "drive_delete_file", "drive_download_file", "drive_download_file_from_folder",
    "execute_action", "execute_files", "add_package_to_executor"]

mail_thunder_keys: list = [
    "MT_smtp_later_init", "MT_smtp_create_message_with_attach_and_send", "MT_smtp_create_message_and_send",
    "MT_smtp_quit", "MT_imap_later_init", "MT_imap_select_mailbox", "MT_imap_search_mailbox",
    "MT_imap_mail_content_list", "MT_imap_output_all_mail_as_file", "MT_imap_quit",
    "MT_set_mail_thunder_os_environ", "MT_get_mail_thunder_os_environ", "MT_add_package_to_executor",
    "MT_scheduler_event_trigger", "MT_remove_blocking_scheduler_job", "MT_remove_nonblocking_scheduler_job",
    "MT_start_blocking_scheduler", "MT_start_nonblocking_scheduler", "MT_start_all_scheduler",
    "MT_shutdown_blocking_scheduler", "MT_shutdown_nonblocking_scheduler"
]

package_keyword_list = {
    "je_auto_control": auto_control_keys,
    "je_load_density": load_density_keys,
    "je_api_testka": api_testka_keys,
    "je_web_runner": web_runner_keys,
    "automation_file": automation_file_keys,
    "mail_thunder": mail_thunder_keys,
}
