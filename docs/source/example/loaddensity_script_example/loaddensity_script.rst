====================================
ITE LoadDensity Script Example
====================================

* Script using json and keyword
    * if you want to use python not keyword
    * https://github.com/JE-Chen/LoadDensity

* this is a example
.. code-block:: python
    """
    you can copy this into ite code editor area
    then you can use ite LoadDensity menu to execute this script
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