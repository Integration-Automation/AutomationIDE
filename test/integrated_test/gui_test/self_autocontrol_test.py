# need AutoControl Package
import time

from je_auto_control import locate_and_click

time.sleep(2)

"""
開啟 GUI 本身 然後依序測試以下元件及動作
把每個選單的選項點開
程式碼執行元件、API Testing、 GUI Testing、WEB Testing、 Load Testing
"""
def open_file_to_test(file_png: str):
    time.sleep(1)

    locate_and_click(
        "../../test_source/file.png",
        mouse_keycode="mouse_left",
        detect_threshold=0.9
    )

    time.sleep(1)

    locate_and_click(
        "../../test_source/openfile.png",
        mouse_keycode="mouse_left",
        detect_threshold=0.9
    )

    time.sleep(1)

    locate_and_click(
        "../../test_source/test_script_source.png",
        mouse_keycode="mouse_left",
        detect_threshold=0.9
    )

    locate_and_click(
        "../../test_source/test_script_source.png",
        mouse_keycode="mouse_left",
        detect_threshold=0.9
    )

    time.sleep(1)

    locate_and_click(
        file_png,
        mouse_keycode="mouse_left",
        detect_threshold=0.9
    )

    time.sleep(1)

    locate_and_click(
        "../../test_source/open.png",
        mouse_keycode="mouse_left",
        detect_threshold=0.9
    )


locate_and_click(
    "../../test_source/resize.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

open_file_to_test("../../test_source/test_py.png")

time.sleep(1)

locate_and_click(
    "../../test_source/run.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(1)

locate_and_click(
    "../../test_source/run_program.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(10)

open_file_to_test("../../test_source/test_cmd.png")

time.sleep(1)

locate_and_click(
    "../../test_source/run.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(1)

locate_and_click(
    "../../test_source/run_on_shell.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(10)

open_file_to_test("../../test_source/apitestka_script_json.png")

time.sleep(1)

locate_and_click(
    "../../test_source/apitestka.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(1)

locate_and_click(
    "../../test_source/execute_apitestka_script.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(5)

locate_and_click(
    "../../test_source/close_white.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

open_file_to_test("../../test_source/autocontrol_script_json.png")

time.sleep(1)

locate_and_click(
    "../../test_source/autocontrol.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(1)

locate_and_click(
    "../../test_source/execute_autocontrol_script.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(5)

locate_and_click(
    "../../test_source/close_white.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

open_file_to_test("../../test_source/webrunner_script_json.png")

time.sleep(1)

locate_and_click(
    "../../test_source/webrunner.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(1)

locate_and_click(
    "../../test_source/execute_webrunner_script.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(20)

open_file_to_test("../../test_source/load_density_script_json.png")

time.sleep(2)

locate_and_click(
    "../../test_source/load_density.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(1)

locate_and_click(
    "../../test_source/execute_load_density_script.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(15)

locate_and_click(
    "../../test_source/close_white.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)

time.sleep(1)

locate_and_click(
    "../../test_source/close1.png",
    mouse_keycode="mouse_left",
    detect_threshold=0.9
)
