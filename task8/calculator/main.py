from calculator import operations
from calculator import parser
import math
import sys # Add this import

def format_result(result: float) -> str:
    # Round to 6 decimal places
    rounded_result = round(result, 6)
    # Convert to string and trim trailing zeros and decimal point if not needed
    s = str(rounded_result)
    if '.' in s:
        s = s.rstrip('0')
        if s.endswith('.'):
            s = s.rstrip('.')
    return s

def evaluate_expression(expression: str) -> str:
    try:
        operand1, operator, operand2 = parser.parse(expression)
        if operator == '+':
            result = operations.add(operand1, operand2)
        elif operator == '-':
            result = operations.subtract(operand1, operand2)
        elif operator == '*':
            result = operations.multiply(operand1, operand2)
        elif operator == '/':
            result = operations.divide(operand1, operand2)
        else:
            return "Error: Unknown operator"

        # Check for float limits
        if abs(result) > sys.float_info.max / 2: # Use a threshold to avoid warnings for perfectly valid large numbers
            print("Warning: Result is approaching float max limit.", file=sys.stderr)
        elif abs(result) < sys.float_info.min * 2 and result != 0: # Use a threshold to avoid warnings for perfectly valid small numbers, but not zero
            print("Warning: Result is approaching float min limit (denormalized).", file=sys.stderr)

        return format_result(result)
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def main():
    while True:
        try:
            expression = input("> ")
            if expression.lower() in ["exit", "quit"]:
                break
            
            if not expression.strip():
                continue

            if expression.lower() == "help": # Handle help command
                print("Supported operations: +, -, *, /")
                print("Examples:")
                print("  3 + 4")
                print("  10.5 / 2.5")
                print("  exit")
                continue # Continue to next iteration after printing help
            
            result = evaluate_expression(expression)
            if result.startswith("Error:"): # Check if it's an error message
                print(result, file=sys.stderr) # Print errors to stderr
            else:
                print(result) # Print normal results to stdout

        except (EOFError, StopIteration):
            break


