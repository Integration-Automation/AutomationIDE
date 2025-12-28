GLOBAL_RULE_TEMPLATE = """
Please conduct a code review according to the following global rules:

1. Readability & Consistency
   - Check indentation, formatting, and comments for clarity.
   - Ensure code style follows team conventions (naming rules, formatting tools).

2. Naming Conventions
   - Variable, function, and class names must be descriptive and meaningful.
   - Maintain semantic clarity and consistency across the codebase.

3. Software Engineering Standards
   - Code should be modular, maintainable, and testable.
   - Avoid duplicate code; encourage refactoring and abstraction.

4. Logic & Correctness
   - Verify correctness of program logic and identify potential bugs.
   - Check boundary conditions and exception handling.

5. Performance & Security
   - Assess for unnecessary performance bottlenecks.
   - Review for security risks (e.g., input validation, resource management).

6. Documentation & Testing
   - Ensure necessary comments and documentation are present.
   - Verify sufficient unit and integration tests are included.
   
7. When scoring, balance conciseness with comprehensiveness; avoid penalizing completeness for being less concise.”

Provide review feedback in a structured bullet-point format, keeping it professional, concise, and with actionable improvement suggestions.
"""
