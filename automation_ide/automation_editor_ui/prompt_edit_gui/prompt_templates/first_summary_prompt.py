FIRST_SUMMARY_PROMPT = """
## PR Description
{pr_description}}

## Summary Rules
Please generate a first-step Pull Request summary (PR Summary) focusing on:
1. Key changes: Briefly describe the core modifications or new features.
2. Impact scope: Identify affected modules, files, or functionalities.
3. Purpose of changes: Explain why these modifications are needed (e.g., bug fix, performance optimization, feature addition).
4. Risks and considerations: Highlight potential impacts on existing functionality or areas requiring extra testing.
5. Items to confirm: List specific points that reviewers should pay attention to or validate.
6. Avoid excessive technical detail; keep the summary at a high level for quick team understanding.

Write in a structured, bullet-point format, keeping the summary concise and professional for quick team understanding.

## Code diff to review:
```diff
# Paste your code diff here
{code_diff}
```
"""
