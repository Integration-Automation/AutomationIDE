# add command exception
add_command_type_exception_tag: str = "command execute_return_value type should be as method or function"
add_command_not_allow_package_exception_tag: str = "choose to add command package not allow"
# send html report exception
send_html_exception_tag: str = """
make sure you have installed je_mail_thunder \n
can't send html report check login user and password is correct \n
and current working folder have default_name.html (html report default execute_detail) \n
or you should get the function file_path to read
"""
# test executor exception
auto_control_test_executor_exception_tag: str = "can't run AutoControl test"
api_testka_test_executor_exception_tag: str = "can't run APITestka test"
web_runner_test_executor_exception_tag: str = "can't run WebRunner test"
load_density_test_executor_exception_tag: str = "can't run LoadDensity test"
# ui exception
wrong_test_data_format_exception_tag: str = "get the wrong test data format"
# exec exception
exec_error: str = "ITE exec error"
file_not_fond_error: str = "File not found"
compiler_not_found_error: str = "Compiler not found"
not_install_package_error: str = "not install required package"
# json exception
cant_reformat_json_error: str = "Can't reformat json is type right?"
wrong_json_data_error: str = "Can't parser json"
