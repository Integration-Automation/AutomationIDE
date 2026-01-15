JUDGE_TEMPLATE = """
# Code Review Judge Template

## Global Rules
{global_rules}

Please conduct a code review for the Pull Request using the following scoring mechanism:

Score range: 1–5.

Six evaluation dimensions:
1. Readability
    - 1: Code is very hard to understand, lacks comments, inconsistent naming.
    - 2: Some parts are readable, but many unclear sections remain; comments are minimal.
    - 3: Code is generally clear, naming is reasonable, but structure or documentation needs improvement.
    - 4: Code is well-structured, consistent naming, good comments, but could be refined further.
    - 5: Code is highly readable, elegantly structured, with complete naming and thorough documentation.


2. Maintainability
    - 1: Code is tightly coupled, not modular, difficult to maintain or extend.
    - 2: Some modularity exists, but duplication or design flaws make maintenance challenging.
    - 3: Basic modularity is present, maintainable but with potential issues or redundancies.
    - 4: Well-designed and modular, easy to maintain, with minor room for improvement.
    - 5: Highly modular, clean design, easy to extend and maintain long-term.

3. Correctness
    - 1: Contains obvious logical errors or bugs, insufficient testing.
    - 2: Mostly correct, but significant edge cases remain unhandled.
    - 3: Code is largely correct, only minor edge cases are missing.
    - 4: Logically sound, well-tested, stable, with small improvements possible.
    - 5: Fully correct, logically rigorous, thoroughly tested, highly stable.

4. Conciseness
    - 1: None of the review is related to the code change or identified topics.
    - 2: Some of the review is related to the identified topics and static analysis feedback.
    - 3: Roughly half of the review addresses relevant topics without excessive digression.
    - 4: Most of the review effectively addresses identified topics without unnecessary content.
    - 5: The entire review precisely addresses identified topics with optimal brevity.


5. Comprehensiveness
    - 1: Review fails to address any identified topics or static analysis findings.
    - 2: Review covers at least one code smell, linter warning, or important topic.
    - 3: Review addresses approximately half of the identified topics.
    - 4: Review covers most identified topics, including code smells and linter warnings.
    - 5: Review comprehensively addresses virtually all identified topics and static analysis findings.

6. Relevance
    Relevance = (2 * Conciseness * Comprehensiveness) / (Conciseness + Comprehensiveness)


Note: Scores of 2 and 4 indicate intermediate quality between the defined levels.

Reviewers should:
- Assign a score (1–5) for each dimension.
- Provide brief reasoning for each score.
- Conclude with an average score and overall recommendation.

## Total Summary
{total_summary}

## First Code Review
{first_code_review}

## Code Diff
{code_diff}
"""