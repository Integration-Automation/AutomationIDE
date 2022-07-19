from integration_testing_environment.integration_testing_environment_ui.editor_event.\
    test_executor.api_testka.api_testka_executor import call_api_testka_test

test_str = \
    """
    [
        ["test_api_method", {"http_method": "post", "test_url": "http://httpbin.org/post", "params": {"task": "new task"}}],
        ["test_api_method", {"http_method": "post", "test_url": "http://httpbin.org/post",
                             "result_check_dict": {"status_code": 300}}
         ],
        ["generate_html", {"html_name": "default_name"}]
    ]
    """
test_result_dict = call_api_testka_test(test_str)
if test_result_dict is not None:
    for execute_detail, execute_return_value in test_result_dict.items():
        print(execute_detail)
        print(execute_return_value)
