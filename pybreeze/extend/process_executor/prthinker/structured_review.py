"""Use the shared diagnostic review session / 使用共用的診斷審查工作階段。"""

from je_editor.pyside_ui.review.prthinker_actions import cancel_review
from je_editor.pyside_ui.review.prthinker_actions import review_current_file

from pybreeze.extend.prthinker_extend.prthinker_setting import environment_for, load_setting


def review_with_diagnostics(main_window):
    """Reuse configuration and subprocess isolation / 沿用設定及子行程隔離。"""
    from pybreeze.pybreeze_ui.menu.plugin_menu.build_run_with_menu import save_current_file_for_run
    if save_current_file_for_run(main_window) is None:
        return False
    return review_current_file(main_window, environment=environment_for(load_setting()))


def cancel_diagnostic_review(main_window):
    cancel_review(main_window)
