"""Structured review saves first and uses the shared process configuration."""

from pybreeze.extend.process_executor.prthinker import structured_review as review
from pybreeze.pybreeze_ui.menu.plugin_menu import build_run_with_menu as save


def test_save_then_start_with_settings(monkeypatch):
    events = []
    window = object()
    monkeypatch.setattr(save, "save_current_file_for_run", lambda _window: events.append("save") or "main.py")
    monkeypatch.setattr(review, "load_setting", lambda: {"backend": "remote"})
    monkeypatch.setattr(review, "environment_for", lambda setting: {"backend": setting["backend"]})
    monkeypatch.setattr(review, "review_current_file", lambda target, **kwargs: events.append((target, kwargs)) or True)
    assert review.review_with_diagnostics(window)
    assert events == ["save", (window, {"environment": {"backend": "remote"}})]


def test_cancelled_save_does_not_start_review(monkeypatch):
    monkeypatch.setattr(save, "save_current_file_for_run", lambda _window: None)
    monkeypatch.setattr(review, "review_current_file", lambda *_args, **_kwargs: (_ for _ in ()).throw(AssertionError()))
    assert review.review_with_diagnostics(object()) is False
