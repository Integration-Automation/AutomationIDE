import sys

import requests
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QLabel, QLineEdit, QComboBox
)
from je_editor import language_wrapper

from automation_ide.automation_editor_ui.extend_ai_gui.ai_gui_global_variable import COT_TEMPLATE_FILES


# Worker Thread 負責傳送資料
class SenderThread(QThread):
    update_response = Signal(str, str)  # (filename, response)

    def __init__(self, files, url):
        super().__init__()
        self.files = files
        self.url = url

    def run(self):
        for file in self.files:
            try:
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read()
                # 傳送到指定 URL
                resp = requests.post(self.url, json={"prompt": content})
                reply_text = resp.text
            except Exception as e:
                reply_text = f"{language_wrapper.language_word_dict.get("cot_gui_error_sending")} {file} {e}"

            # 發送訊號更新 UI
            self.update_response.emit(file, reply_text)


class PromptSenderUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(language_wrapper.language_word_dict.get("cot_gui_window_title"))

        # 檔案清單
        self.files = COT_TEMPLATE_FILES

        # UI 元件
        layout = QVBoxLayout()

        # URL 輸入框
        url_layout = QHBoxLayout()
        url_layout.addWidget(QLabel(language_wrapper.language_word_dict.get("cot_gui_label_api_url")))
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText(language_wrapper.language_word_dict.get("cot_gui_placeholder_api_url"))
        url_layout.addWidget(self.url_input)
        layout.addLayout(url_layout)

        # 傳送資料區域
        self.prompt_view = QTextEdit()
        self.prompt_view.setPlaceholderText(language_wrapper.language_word_dict.get("cot_gui_placeholder_prompt_view"))
        layout.addWidget(QLabel(language_wrapper.language_word_dict.get("cot_gui_label_prompt_area")))
        layout.addWidget(self.prompt_view)

        # 回傳區域
        self.response_selector = QComboBox()  # 改用 ComboBox
        self.response_view = QTextEdit()
        self.response_view.setReadOnly(True)  # 可複製但不可編輯

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.response_selector, 2)
        hbox_layout.addWidget(self.response_view, 5)

        layout.addWidget(QLabel(language_wrapper.language_word_dict.get("cot_gui_label_response_area")))
        layout.addLayout(hbox_layout)

        # 傳送按鈕
        self.send_button = QPushButton(language_wrapper.language_word_dict.get("cot_gui_button_send"))
        layout.addWidget(self.send_button)

        self.setLayout(layout)

        # 綁定事件
        self.response_selector.currentTextChanged.connect(self.show_response)
        self.send_button.clicked.connect(self.start_sending)

        # 儲存回覆
        self.responses = {}

    def show_response(self, filename):
        if filename in self.responses:
            self.response_view.setPlainText(self.responses[filename])

    def start_sending(self):
        # 顯示第一個檔案內容
        if self.files:
            try:
                with open(self.files[0], "r", encoding="utf-8") as f:
                    self.prompt_view.setPlainText(f.read())
            except Exception as e:
                self.prompt_view.setPlainText(
                    f"{language_wrapper.language_word_dict.get("cot_gui_error_read_file")}: {e}")

        # 取得 URL
        url = self.url_input.text().strip()
        if not url:
            self.prompt_view.setPlainText(language_wrapper.language_word_dict.get("cot_gui_error_no_url"))
            return

        # 啟動傳送 Thread
        self.thread = SenderThread(self.files, url)
        self.thread.update_response.connect(self.handle_response)
        self.thread.start()

    def handle_response(self, filename, response):
        self.responses[filename] = response
        self.response_selector.addItem(filename)  # 加入 ComboBox
        # 自動顯示最新回覆
        self.response_selector.setCurrentText(filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PromptSenderUI()
    window.show()
    sys.exit(app.exec())
