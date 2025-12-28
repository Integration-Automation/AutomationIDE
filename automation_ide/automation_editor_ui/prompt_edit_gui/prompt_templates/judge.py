JUDGE_TEMPLATE = """
Please conduct a code review for the Pull Request using the following scoring mechanism:

Score range: Minimum 1, Maximum 5.

Six evaluation dimensions:
1. Readability
   - 1: Code is hard to understand, lacks comments and consistency.
   - 3: Code is generally clear, naming is reasonable, but improvements are needed.
   - 5: Code is highly readable, well-structured, with complete naming and documentation.

2. Maintainability
   - 1: Code is tightly coupled, lacks modularity, and is difficult to maintain.
   - 3: Code has basic modularity, maintainable but with duplication or potential issues.
   - 5: Code is well-designed, modular, and easy to extend and maintain.

3. Correctness
   - 1: Contains obvious logical errors or bugs, insufficient testing.
   - 3: Code is mostly correct, with minor edge cases unhandled.
   - 5: Code is logically sound, thoroughly tested, and highly stable.

4. Conciseness
   - 1: Code is verbose, with unnecessary duplication.
   - 3: Code is fairly concise but could be optimized further.
   - 5: Code is highly concise, avoids redundancy, and is elegantly structured.

5. Comprehensiveness
   - 1: Missing essential functionality or tests, insufficient coverage.
   - 3: Functionality and tests are mostly complete but with some gaps.
   - 5: Functionality and tests are fully comprehensive, with complete documentation.

6. Relevance
   - 1: Changes do not align with requirements, unnecessary code included.
   - 3: Changes mostly align with requirements but with minor deviations.
   - 5: Changes fully align with requirements, precisely addressing the problem.

Reviewers should assign a score (1–5) for each dimension, provide brief reasoning, and conclude with an average score and overall recommendation.
"""