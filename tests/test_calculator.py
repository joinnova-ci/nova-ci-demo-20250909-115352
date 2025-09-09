"""
Tests for the broken calculator - these will all fail!
=====================================================

Every test in this file will fail because the calculator functions have bugs.
This is perfect for demonstrating Nova CI-Rescue's ability to:
1. Detect multiple failing tests
2. Analyze what each test expects vs what it gets  
3. Fix all the bugs automatically
4. Verify all tests pass

Run: pytest test_calculator.py -v
Then: nova fix
"""

import pytest
from calculator import (
    add, subtract, multiply, divide, power, modulo,
    absolute, square_root, factorial, max_of_two
)


def test_addition():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(10, -5) == 5


def test_subtraction():
    """Test subtraction function."""
    assert subtract(10, 3) == 7
    assert subtract(5, 5) == 0
    assert subtract(0, 5) == -5
    assert subtract(-2, -8) == 6


def test_multiplication():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(7, 1) == 7


