Structured review
=======================================================

Install the current prthinker package in the selected Python interpreter and the matching JEditor adapter. Use the prthinker menu to review a saved file in Problems or cancel the active review. Findings provide proposed Quick Fixes; progress and terminal state appear in the status bar. Review uses a persistent isolated JSONL subprocess, and preparing the Git diff runs in the background. Settings and credentials are passed through environment variables. Test and approve proposed changes before saving or publishing them.

Select Plugins → prthinker in JEditor, or Automation → prthinker → Review in Problems in PyBreeze. Cancel review requests a terminal state. Install both editor changes together; the shared adapter uses protocol version 1. No review operation creates a pull request.
