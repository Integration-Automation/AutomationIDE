api_testka_keys: list = [
    "AT_test_api_method", "AT_generate_html", "AT_generate_html_report", "AT_generate_json",
    "AT_generate_json_report", "AT_generate_xml", "AT_generate_xml_report", "AT_execute_action",
    "AT_execute_files", "AT_add_package_to_executor", "AT_add_package_to_callback_executor",
    "AT_flask_mock_server_add_router", "AT_start_flask_mock_server", "AT_scheduler_event_trigger",
    "AT_remove_blocking_scheduler_job", "AT_remove_nonblocking_scheduler_job",
    "AT_start_blocking_scheduler", "AT_start_nonblocking_scheduler",
    "AT_start_all_scheduler", "AT_shutdown_blocking_scheduler", "AT_shutdown_nonblocking_scheduler"
]

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
    "WR_get_webdriver_manager", "WR_change_index_of_webdriver", "WR_quit", "WR_SaveTestObject",
    "WR_CleanTestObject", "WR_set_driver", "WR_set_webdriver_options_capability", "WR_find_element",
    "WR_find_elements", "WR_implicitly_wait", "WR_explict_wait", "WR_to_url",
    "WR_forward", "WR_back", "WR_refresh", "WR_switch", "WR_set_script_timeout", "WR_set_page_load_timeout",
    "WR_get_cookies", "WR_get_cookie", "WR_add_cookie", "WR_delete_cookie", "WR_delete_all_cookies",
    "WR_execute", "WR_execute_script", "WR_execute_async_script", "WR_move_to_element",
    "WR_move_to_element_with_offset", "WR_drag_and_drop", "WR_drag_and_drop_offset", "WR_perform",
    "WR_reset_actions", "WR_left_click", "WR_left_click_and_hold", "WR_right_click",
    "WR_left_double_click", "WR_release", "WR_press_key", "WR_release_key",
    "WR_move_by_offset", "WR_pause", "WR_send_keys", "WR_send_keys_to_element", "WR_scroll",
    "WR_check_current_webdriver", "WR_maximize_window", "WR_fullscreen_window", "WR_minimize_window",
    "WR_set_window_size", "WR_set_window_position", "WR_get_window_position",
    "WR_get_window_rect", "WR_set_window_rect", "WR_get_screenshot_as_png", "WR_get_screenshot_as_base64",
    "WR_get_log", "WR_single_quit", "WR_element_submit", "WR_element_clear", "WR_element_get_property",
    "WR_element_get_dom_attribute", "WR_element_get_attribute",
    "WR_element_is_selected", "WR_element_is_enabled", "WR_input_to_element", "WR_click_element",
    "WR_element_is_displayed", "WR_element_value_of_css_property", "WR_element_screenshot",
    "WR_element_change_web_element", "WR_element_check_current_web_element", "WR_element_get_select",
    "WR_set_record_enable", "WR_generate_html", "WR_generate_html_report", "WR_generate_json",
    "WR_generate_json_report", "WR_generate_xml", "WR_generate_xml_report",
    "WR_execute_action", "WR_execute_files", "WR_add_package_to_executor",
    "WR_add_package_to_callback_executor", "WR_scheduler_event_trigger", "WR_remove_blocking_scheduler_job",
    "WR_remove_nonblocking_scheduler_job", "WR_start_blocking_scheduler", "WR_start_nonblocking_scheduler",
    "WR_start_all_scheduler", "WR_shutdown_blocking_scheduler", "WR_shutdown_nonblocking_scheduler"
]

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
