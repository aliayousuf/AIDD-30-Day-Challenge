# Quickstart: CLI Calculator

## Running the Calculator

The calculator can be run using `python -m calculator` from the project root or directly via `python calculator/main.py`.

### Prerequisites

- Python 3.12+ installed
- `uv` package manager (recommended for dependency management)

### Installation

1.  Navigate to the project's root directory.
2.  (Optional, but recommended) Create a virtual environment using `uv`:
    ```bash
    uv venv
    uv pip install -r requirements.txt # if a requirements.txt exists
    ```
    or simply:
    ```bash
    uv sync
    ```

### Usage

Once started, the calculator will prompt you for input.

```bash
python -m calculator
# or
python calculator/main.py
```

### Commands

- **Arithmetic Expressions**: Enter expressions in infix style.
    - Supported operations: `+`, `-`, `*`, `/`
    - Examples:
        - `3 + 4`
        - `10.5 / 2.5`
        - `5 * -2`
        - `7 - 12.3`
    - Results are displayed immediately after each valid expression. Floating-point results are rounded to 6 decimal places with trailing zeros trimmed for display.

- **`help`**: Displays information about supported operations and examples.

- **`exit` or `quit`**: Terminates the calculator program.

### Example Session

```
$ python -m calculator
> 3 + 4
7
> 10.5 / 3
3.5
> 5 * -2
-10
> 7 - 12.3
-5.3
> help
Supported operations: +, -, *, /
Examples:
  3 + 4
  10.5 / 2.5
  exit
> 5 / 0
Error: Division by zero.
> invalid input
Error: invalid expression. Type 'help' for usage.
> exit
```