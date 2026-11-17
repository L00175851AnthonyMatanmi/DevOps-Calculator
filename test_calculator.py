import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    # a fresh Calculator for every test keeps the tests independent
    return Calculator()


# ---- add ----

def test_add_positive_numbers(calc):
    assert calc.add(2, 3) == 5


def test_add_negative_numbers(calc):
    assert calc.add(-2, -3) == -5


# ---- subtract ----

def test_subtract(calc):
    assert calc.subtract(10, 4) == 6


# ---- multiply ----

def test_multiply(calc):
    assert calc.multiply(6, 7) == 42


def test_multiply_by_zero(calc):
    assert calc.multiply(5, 0) == 0


# ---- divide ----

def test_divide(calc):
    assert calc.divide(10, 4) == 2.5


def test_divide_by_zero_raises_error(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)


# ---- power ----

def test_power(calc):
    assert calc.power(2, 3) == 8


def test_power_with_zero_exponent(calc):
    assert calc.power(9, 0) == 1


# ---- square root ----

def test_square_root(calc):
    assert calc.square_root(16) == 4


def test_square_root_of_negative_raises_error(calc):
    with pytest.raises(ValueError, match="negative number"):
        calc.square_root(-4)