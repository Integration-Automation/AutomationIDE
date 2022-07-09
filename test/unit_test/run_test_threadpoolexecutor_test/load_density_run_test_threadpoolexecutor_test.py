from integration_testing_environment.utils.run_test_executor.run_test_threadpoolexecutor import load_density_executor
test_list = [
    ["loading_test_with_user", {"user_detail_dict": {
        "request_method": "get",
        "request_url": "http://httpbin.org/get"
    },
        "user_count": 50, "spawn_rate": 10, "test_time": 10}
     ],
    ["generate_html"]
]

print(load_density_executor(test_list))
