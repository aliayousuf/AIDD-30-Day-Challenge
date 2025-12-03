# Feature Specification: CLI Calculator

**Feature Branch**: `1-cli-calculator`  
**Created**: December 3, 2025  
**Status**: Draft  
**Input**: User description: "Build a simple command-line calculator in Python that performs basic arithmetic operations with clear behavior, predictable floating-point handling, and robust input validation. The calculator is initialized as a Python project using `uv init`, generating `pyproject.toml` and standard project structure.Features & Requirements:1. Supported operations: - Addition: a + b - Subtraction: a - b - Multiplication: a * b - Division: a / b - Operations apply to integers and floating-point numbers.2. Edge cases: - Division by zero → handled gracefully with an error message (no crash). - Overflow / extremely large numbers → return Python’s natural result; if outside practical range, show a warning. - Empty input → prompt user again. - Operations with leading/trailing spaces → allowed. - Negative numbers → fully supported. - Mixed types (int + float) → supported.3. Definition of correctness for floating-point results: - Use Python’s standard `float` arithmetic. - Display results rounded to 6 decimal places. - Internal calculations remain unrounded to avoid cumulative error. - Trailing zeros may be trimmed for display (e.g., `2.500000 → 2.5`).4. CLI interface design: - User runs the calculator with: `python -m calculator` or `python calculator/main.py` - User enters expressions in infix style: - Example: `3 + 4` - Example: `10.5 / 3` - The result is printed immediately. - Typing `exit` or `quit` ends the program. - Help command: `help` prints supported operations and examples.5. Handling invalid inputs: - Invalid syntax → show: `"Error: invalid expression. Type 'help' for usage."` - Unsupported characters or operators → reject with a clear message. - Multiple operators without operands (e.g., `3 ++ 2`) → treat as invalid. - Calculator must never crash due to user input.Project structure (generated via `uv init` and extended): - `pyproject.toml` (project metadata, dependencies) - `calculator/` - `__init__.py` - `main.py` (CLI entrypoint) - `parser.py` (expression parsing) - `operations.py` (core arithmetic) - `tests/` - `test_operations.py` - `test_parser.py` - `test_cli.py`Testing strategy: - Unit tests for each operation (normal + edge cases) - Parser tests for valid + invalid expressions - CLI integration tests using input/output simulation - All tests must pass; aim for ≥80% coverage.Non-functional requirements: - Code uses Python 3.12+ with type hints. - No external libraries for evaluation (no `eval()`). - Clear, readable logic with simple functional style. please improve the specification if required"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Perform Basic Arithmetic (Priority: P1)

As a user, I want to perform basic arithmetic operations (addition, subtraction, multiplication, division) on integers and floating-point numbers through a command-line interface.

**Why this priority**: This is the core functionality of the calculator.

**Independent Test**: Can be fully tested by entering various valid expressions and verifying the output.

**Acceptance Scenarios**:

1.  **Given** the calculator is running, **When** I enter "3 + 4", **Then** the output should be "7".
2.  **Given** the calculator is running, **When** I enter "10.5 / 2", **Then** the output should be "5.25".
3.  **Given** the calculator is running, **When** I enter "5 * -2", **Then** the output should be "-10".
4.  **Given** the calculator is running, **When** I enter "7 - 12.3", **Then** the output should be "-5.3".

---

### User Story 2 - Handle Invalid Inputs Gracefully (Priority: P1)

As a user, I want the calculator to provide clear error messages and not crash when I enter invalid expressions or commands.

**Why this priority**: Ensures the calculator is robust and user-friendly.

**Independent Test**: Can be fully tested by entering various invalid inputs and observing error messages and program stability.

**Acceptance Scenarios**:

1.  **Given** the calculator is running, **When** I enter "3 ++ 2", **Then** the output should be "Error: invalid expression. Type 'help' for usage."
2.  **Given** the calculator is running, **When** I enter "abc", **Then** the output should be "Error: invalid expression. Type 'help' for usage."
3.  **Given** the calculator is running, **When** I enter "5 / 0", **Then** the output should be "Error: Division by zero."
4.  **Given** the calculator is running, **When** I enter an empty string, **Then** I should be prompted again.

---

### User Story 3 - Access Help and Exit (Priority: P2)

As a user, I want to be able to view supported operations and gracefully exit the calculator.

**Why this priority**: Provides essential user guidance and program control.

**Independent Test**: Can be fully tested by entering "help", "exit", or "quit".

**Acceptance Scenarios**:

1.  **Given** the calculator is running, **When** I enter "help", **Then** a message listing supported operations and examples should be displayed.
2.  **Given** the calculator is running, **When** I enter "exit", **Then** the program should terminate.
3.  **Given** the calculator is running, **When** I enter "quit", **Then** the program should terminate.

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: The calculator MUST support addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
-   **FR-002**: The calculator MUST perform operations on both integer and floating-point numbers.
-   **FR-003**: The calculator MUST handle division by zero by displaying an "Error: Division by zero." message.
-   **FR-004**: The calculator MUST display a warning for numbers approaching Python's `float` min/max limits (`sys.float_info.min`, `sys.float_info.max`).
-   **FR-005**: The calculator MUST re-prompt the user if an empty input is provided.
-   **FR-006**: The calculator MUST correctly process expressions with leading or trailing spaces.
-   **FR-007**: The calculator MUST fully support negative numbers in expressions.
-   **FR-008**: The calculator MUST support mixed integer and floating-point types in operations.
-   **FR-009**: The calculator MUST use Python’s standard `float` arithmetic for calculations.
-   **FR-010**: The calculator MUST display results rounded to 6 decimal places for floating-point numbers.
-   **FR-011**: The calculator MUST retain unrounded values for internal calculations to prevent cumulative error.
-   **FR-012**: The calculator MUST trim trailing zeros for display (e.g., `2.500000 → 2.5`).
-   **FR-013**: The calculator MUST be runnable via `python -m calculator` or `python calculator/main.py`.
-   **FR-014**: The calculator MUST accept expressions in infix style (e.g., `3 + 4`).
-   **FR-015**: The calculator MUST print the result immediately after each valid expression.
-   **FR-016**: The calculator MUST terminate when the user types `exit` or `quit`.
-   **FR-017**: The calculator MUST display help information (supported operations and examples) when the user types `help`.
-   **FR-018**: The calculator MUST display "Error: invalid expression. Type 'help' for usage." for invalid syntax.
-   **FR-019**: The calculator MUST reject unsupported characters or operators with a clear error message.
-   **FR-020**: The calculator MUST treat multiple operators without operands as invalid.
-   **FR-021**: The calculator MUST never crash due to user input.
-   **FR-022**: The project MUST be initialized using `uv init`, generating `pyproject.toml` and a standard project structure.
-   **FR-023**: The project structure MUST include `calculator/__init__.py`, `calculator/main.py`, `calculator/parser.py`, `calculator/operations.py`, `tests/test_operations.py`, `tests/test_parser.py`, and `tests/test_cli.py`.
-   **FR-024**: Unit tests MUST be provided for each operation (normal + edge cases).
-   **FR-025**: Unit tests MUST be provided for parser (valid + invalid expressions).
-   **FR-026**: Integration tests MUST be provided for the CLI using input/output simulation.
-   **FR-027**: All tests MUST pass.
-   **FR-028**: Test coverage MUST be ≥80%.
-   **FR-029**: The code MUST use Python 3.12+ with type hints.
-   **FR-030**: The code MUST NOT use external libraries for evaluation (e.g., `eval()`).
-   **FR-031**: The code MUST have clear, readable logic with a simple functional style.
-   **FR-032**: The calculator MUST log errors to console/stderr.

### Key Entities

-   **Expression**: A string representing an arithmetic operation (e.g., "3 + 4").
-   **Result**: A numerical value obtained after evaluating an expression.

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: Users can successfully perform all supported arithmetic operations and receive correct results.
-   **SC-002**: The calculator consistently handles all specified edge cases and invalid inputs without crashing, providing informative messages.
-   **SC-003**: New users can understand how to use the calculator and its features by utilizing the `help` command.
-   **SC-004**: All provided test suites (unit and integration) pass successfully, demonstrating functional correctness and robustness.
-   **SC-005**: Test coverage for the calculator logic is at least 80%, indicating thorough testing.
-   **SC-006**: The calculator adheres to the specified non-functional requirements regarding Python version, type hinting, code style, and avoidance of `eval()`.
-   **SC-007**: All arithmetic operations complete with a response time imperceptible to the user.

## Clarifications

### Session 2025-12-03

- Q: What is the threshold or definition of "practical display range" that should trigger this warning? → A: Near Python's `float` min/max limits (`sys.float_info.min`, `sys.float_info.max`).
- Q: Should the calculator implement any form of logging (e.g., for errors, user input, results) for debugging or auditing purposes? → A: Log errors only to console/stderr.
- Q: Are there any specific performance expectations for the calculator (e.g., maximum response time for an individual calculation, or throughput)? → A: Calculations should be perceived as instantaneous by the user.


