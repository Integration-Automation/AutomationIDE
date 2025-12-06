import os
import sys

from PySide6.QtCore import QFileSystemWatcher
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QComboBox, QTextEdit, QLineEdit, QPushButton, QLabel, QGroupBox, QMessageBox
)

from automation_ide.automation_editor_ui.prompt_edit_gui.prompt_templates.first_code_review import FIRST_CODE_REVIEW
from automation_ide.automation_editor_ui.prompt_edit_gui.prompt_templates.first_summary_prompt import \
    FIRST_SUMMARY_PROMPT
from automation_ide.automation_editor_ui.prompt_edit_gui.prompt_templates.global_rule import GLOBAL_RULE_TEMPLATE
from automation_ide.automation_editor_ui.prompt_edit_gui.prompt_templates.judge import JUDGE_TEMPLATE
from automation_ide.automation_editor_ui.prompt_edit_gui.prompt_templates.total_summary import TOTAL_SUMMARY_TEMPLATE


class PromptEditor(QWidget):
    def __init__(self, prompt_files=None, parent=None):
        super().__init__(parent)
        self.prompt_files = prompt_files or [
            "global_rule.md",
            "first_summary_prompt.md",
            "first_code_review.md",
            "judge.md",
            "total_summary.md"
        ]

        # 對應檔案名稱與模板內容
        self.templates = {
            "global_rule.md": GLOBAL_RULE_TEMPLATE,
            "first_summary_prompt.md": FIRST_SUMMARY_PROMPT,
            "first_code_review.md": FIRST_CODE_REVIEW,
            "judge.md": JUDGE_TEMPLATE,
            "total_summary.md": TOTAL_SUMMARY_TEMPLATE,
        }

        self.setWindowTitle("Prompt Editor")  # 視窗標題：Prompt 編輯器

        # --- Layouts (版面配置) ---
        main_layout = QVBoxLayout(self)
        top_layout = QHBoxLayout()
        editor_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        # --- AI URL input box (AI URL 輸入框) ---
        self.url_label = QLabel("AI URL:")
        self.url_input = QLineEdit()
        top_layout.addWidget(self.url_label)
        top_layout.addWidget(self.url_input)

        # --- ComboBox for selecting files (下拉選單選擇檔案) ---
        self.file_selector = QComboBox()
        self.file_selector.addItems(self.prompt_files)
        self.file_selector.currentIndexChanged.connect(self.load_file_content)

        # --- Left Editable panel (左邊編輯區塊) ---
        self.left_editor = QTextEdit()
        left_group = QGroupBox("Edit File Content")  # 左邊編輯檔案內容
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.left_editor)
        left_group.setLayout(left_layout)

        # --- Right Editable panel (右邊可編輯區塊) ---
        self.editable_panel = QTextEdit()
        editable_group = QGroupBox("Edit Prompt (Editable)")  # 編輯 Prompt (可編輯)
        editable_layout = QVBoxLayout()
        editable_layout.addWidget(self.editable_panel)
        editable_group.setLayout(editable_layout)

        editor_layout.addWidget(left_group, 1)
        editor_layout.addWidget(editable_group, 1)

        # --- Buttons ---
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_prompt)

        self.create_button = QPushButton("Create File")
        self.create_button.clicked.connect(self.create_file)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_file)

        self.reload_button = QPushButton("Reload")
        self.reload_button.clicked.connect(lambda: self.load_file_content(self.file_selector.currentIndex()))

        bottom_layout.addWidget(self.file_selector)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.reload_button)
        bottom_layout.addWidget(self.save_button)
        bottom_layout.addWidget(self.create_button)
        bottom_layout.addWidget(self.send_button)

        # --- Combine layouts (組合版面配置) ---
        main_layout.addLayout(top_layout)
        main_layout.addLayout(editor_layout)
        main_layout.addLayout(bottom_layout)

        # --- FileSystemWatcher (檔案監控器) ---
        self.watcher = QFileSystemWatcher(self.prompt_files)
        self.watcher.fileChanged.connect(self.on_file_changed)

        # 預設載入第一個檔案
        self.load_file_content(0)

    def load_file_content(self, index):
        """載入選擇的檔案內容到左邊編輯區"""
        filename = self.prompt_files[index]
        self.current_file = filename
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
            self.left_editor.setPlainText(content)
        else:
            self.left_editor.setPlainText(f"(File {filename} does not exist)")

    def create_file(self):
        """建立目前選擇的檔案，若不存在則用模板內容建立"""
        filename = self.current_file
        if os.path.exists(filename):
            QMessageBox.information(self, "Info", f"File {filename} already exists, no need to create")
            return

        template_content = self.templates.get(filename, "")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(template_content)

        QMessageBox.information(self, "Success", f"File {filename} has been created")
        self.load_file_content(self.file_selector.currentIndex())

    def on_file_changed(self, path):
        """當檔案被外部修改時即時更新"""
        if path == self.current_file:
            self.load_file_content(self.file_selector.currentIndex())

    def save_file(self):
        """將左邊編輯區內容儲存到目前檔案"""
        if not hasattr(self, "current_file"):
            QMessageBox.warning(self, "Error", "No file selected")
            return

        content = self.left_editor.toPlainText()
        with open(self.current_file, "w", encoding="utf-8") as f:
            f.write(content)
        QMessageBox.information(self, "Success", f"File {self.current_file} saved")

    def send_prompt(self):
        """模擬發送 prompt 到 AI URL"""
        ai_url = self.url_input.text().strip()
        prompt_text = self.editable_panel.toPlainText().strip()

        if not ai_url:
            QMessageBox.warning(self, "Warning", "Please enter AI URL")
            return
        if not prompt_text:
            QMessageBox.warning(self, "Warning", "Please enter the prompt to send")
            return

        # 成功提示
        QMessageBox.information(self, "Sending Prompt",
                                f"Sending prompt to {ai_url}:\n\n{prompt_text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = PromptEditor()
    editor.showMaximized()
    sys.exit(app.exec())
