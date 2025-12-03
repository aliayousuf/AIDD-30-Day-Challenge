import pytest
from calculator import operations

def test_add():
    assert operations.add(1, 2) == 3
    assert operations.add(0.1, 0.2) == pytest.approx(0.3)
    assert operations.add(-1, 1) == 0

def test_subtract():
    assert operations.subtract(5, 3) == 2
    assert operations.subtract(0.5, 0.2) == pytest.approx(0.3)
    assert operations.subtract(1, 1) == 0

def test_multiply():
    assert operations.multiply(2, 3) == 6
    assert operations.multiply(0.5, 4) == 2.0
    assert operations.multiply(-1, 5) == -5

def test_divide():
    assert operations.divide(6, 3) == 2
    assert operations.divide(1, 2) == 0.5
    assert operations.divide(10, 4) == 2.5
    with pytest.raises(ValueError, match="Division by zero"):
        operations.divide(1, 0)
