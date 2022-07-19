from integration_testing_environment.integration_testing_environment_ui.editor_event.test_executor. \
    load_density.load_density_executor import call_load_density_test

test_str = \
    """
        [
        ["loading_test_with_user", {"user_detail_dict": {
            "request_method": "get",
            "request_url": "http://httpbin.org/get"
        },
            "user_count": 50, "spawn_rate": 10, "test_time": 10}
         ],
        ["generate_html"]
    ]
    """
test_result_dict = call_load_density_test(test_str)
if test_result_dict is not None:
    for execute_detail, execute_return_value in test_result_dict.items():
        print(execute_detail)
        print(execute_return_value)
