# Data Model: CLI Calculator

## Entities

### Expression
- **Description**: Represents a user-provided arithmetic expression.
- **Type**: `str`
- **Validation**:
    - Must not be empty (FR-005).
    - Must conform to infix notation with supported operators and operands (FR-014, FR-018, FR-019, FR-020).
    - Can include leading/trailing spaces (FR-006).

### ParsedExpression
- **Description**: An intermediate representation of the expression after parsing, ready for evaluation. This could be a list or tuple of tokens, or an Abstract Syntax Tree (AST).
- **Type**: `tuple[Union[float, str], ...]` or `AST` (NEEDS IMPLEMENTATION DEFINITION)
- **Fields**:
    - `operand1`: `float` or `int`
    - `operator`: `str` (e.g., '+', '-', '*', '/')
    - `operand2`: `float` or `int`
- **Validation**:
    - Ensures valid numerical operands and a single, supported operator.

### Result
- **Description**: The numerical outcome of an evaluated expression.
- **Type**: `float` (internal calculations), `str` (display)
- **Representation**:
    - Internally: Python's standard `float` (FR-009).
    - Display: Rounded to 6 decimal places, with trailing zeros trimmed (FR-010, FR-012).
- **Edge Cases**:
    - Division by zero results in a specific error message (FR-003).
    - Near `sys.float_info.min` or `sys.float_info.max` triggers a warning (FR-004).