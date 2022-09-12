====================================
ITE WebRunner Script Example
====================================

* Script using json and keyword
    * if you want to use python not keyword
    * https://webrunner-dev.readthedocs.io/en/latest/?badge=latest

* this is a example
.. code-block:: python

    """
    you can copy this into ite code editor area
    then you can use ite WebRunner menu to execute this script
    """
    [
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
        ["quit"]
    ]