import pytest
from calculator import parser

@pytest.mark.parametrize("expression, expected_parts", [
    ("1 + 2", (1.0, "+", 2.0)),
    ("10 - 5", (10.0, "-", 5.0)),
    ("2 * 3", (2.0, "*", 3.0)),
    ("10 / 2", (10.0, "/", 2.0)),
    ("1.5 + 2.5", (1.5, "+", 2.5)),
    ("-1 + -2", (-1.0, "+", -2.0)),
    ("  3   +   4  ", (3.0, "+", 4.0)), # Should handle extra spaces
])
def test_parse_valid_expressions(expression, expected_parts):
    # This test will initially fail because the placeholder parse function
    # might not correctly handle all these cases, especially leading/trailing spaces.
    # The current placeholder `parse` function *does* split, but not strip.
    # We will refine the parse function later.
    result = parser.parse(expression)
    assert result == expected_parts

def test_parse_invalid_expressions_raises_error():
    with pytest.raises(ValueError, match="Invalid expression"):
        parser.parse("1 +")
    with pytest.raises(ValueError, match="Invalid expression"):
        parser.parse("1 + 2 + 3")
    with pytest.raises(ValueError, match="Invalid expression"):
        parser.parse("abc + 2")
    with pytest.raises(ValueError, match="Invalid expression"):
        parser.parse("")
    with pytest.raises(ValueError, match="Invalid expression"):
        parser.parse("  ")
    with pytest.raises(ValueError, match="Invalid expression"):
        parser.parse("1 % 2")
    with pytest.raises(ValueError, match="Invalid expression"):
        parser.parse("1 $ 2")
    with pytest.raises(ValueError, match="Invalid expression"):
        parser.parse("1 ++ 2")
