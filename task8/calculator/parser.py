from typing import Tuple, Union

def parse(expression: str) -> Tuple[float, str, float]:
    parts = expression.split() # This already handles multiple spaces
    
    if len(parts) != 3:
        raise ValueError("Invalid expression")
    
    try:
        operand1 = float(parts[0])
        operator = parts[1]
        operand2 = float(parts[2])
    except ValueError:
        raise ValueError("Invalid expression") # Could not convert operands to float

    if operator not in ['+', '-', '*', '/']:
        raise ValueError("Invalid expression") # Unsupported operator
        
    return operand1, operator, operand2