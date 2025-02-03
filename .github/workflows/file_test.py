import pytest # noqa: F401 


def test_calc_addition():
    """Test the result of 2 + 4."""
    output = 2 + 4
    assert output == 6


def test_calc_subtraction():
    """Test the result of 2 - 4."""
    output = 2 - 4
    assert output == -2


def test_calc_multiply():
    """Test the result of 2 * 4."""
    output = 2 * 4
    assert output == 8


def test_coucou():
    """Test if the output returns 'hello'."""
    output = 'hello'
    assert output == 'hello'
