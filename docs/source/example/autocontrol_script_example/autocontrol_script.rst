====================================
ITE AutoControl Script Example
====================================

* Script using json and keyword
    * if you want to use python not keyword
    * https://python-jeautocontrol.readthedocs.io/en/latest/

* this is a example
.. code-block:: python

    """
    you can copy this into ite code editor area
    then you can use ite AutoControl menu to execute this script
    """
    "windows"
    [
        ["type_key", {"keycode": 65}],
        ["mouse_left", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["position"],
        ["press_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["release_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}]
    ]
    "linux"
    [
        ["type_key", {"keycode": 38}],
        ["mouse_left", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["position"],
        ["press_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["release_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["type_key", {"mouse_keycode": "dwadwawda", "dwadwad": 500, "wdawddwawad": 500}]
    ]
    "macos"
    [
        ["type_key", {"keycode": 0x00}],
        ["mouse_left", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["position"],
        ["press_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["release_mouse", {"mouse_keycode": "mouse_left", "x": 500, "y": 500}],
        ["type_key", {"mouse_keycode": "dwadwawda", "dwadwad": 500, "wdawddwawad": 500}]
    ]