from integration_testing_environment.utils.run_test_executor.run_test_threadpoolexecutor import api_testka_executor

test_action_list = [
    ["test_api_method", {"http_method": "post", "test_url": "http://httpbin.org/post", "params": {"task": "new task"}}],
    ["test_api_method", {"http_method": "post", "test_url": "http://httpbin.org/post",
                         "result_check_dict": {"status_code": 300}}
     ],
    ["generate_html", {"html_name": "default_name"}]
]
print(api_testka_executor(test_action_list))
