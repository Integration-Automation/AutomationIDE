TOTAL_SUMMARY_TEMPLATE = """
# Total Summary Template

## Global Rules
{global_rules}

Generate the final code-review summary (PR Total Summary) covering:

1. Overall conclusion: Briefly state the overall review outcome and whether it meets merge criteria.
2. Comprehensive evaluation: Summarize code quality, maintainability, and alignment with team standards.
3. Decision recommendation: Clearly indicate the final recommendation (e.g., approve merge, request changes, comment only).
4. Team follow-up: Suggest any necessary next steps (e.g., additional testing, documentation updates, performance improvements).
5. Do not repeat earlier details; concentrate solely on the final conclusion and recommendation.

Respond in structured bullet points; keep concise and professional, focusing only on the final conclusion.

## First Code Review
{first_code_review}

## First Summary
{first_summary}

## Code Diff
{code_diff}
"""
