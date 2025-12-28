FIRST_CODE_REVIEW = """
# Code Review Template

## PR Description
{pr_description}}

## Review Rules
Please perform a first-step code review focusing on the following aspects:
1. Code readability (indentation, formatting, comments).
2. Clarity and descriptiveness of variable, function, and class names; avoid overly vague or cryptic naming.
3. Adherence to basic software engineering standards (modularity, maintainability, avoidance of duplicate code).
4. Identification of obvious logical errors or potential bugs.
5. Provide specific improvement suggestions with brief explanations.
6. Focus only on the most obvious issues and avoid deep analysis at this stage.

Respond in a structured, bullet-point format, keeping the feedback concise and professional.

## Code diff to review:
```diff
# Paste your code diff here
{code_diff}
```
"""
