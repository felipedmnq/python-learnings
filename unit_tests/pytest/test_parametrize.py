import math

import pytest
from functions import multiply, pow_, square


@pytest.mark.parametrize("numbers_1,numbers_2,expected_result", [(1, 2, 2), (2, 4, 8)])
def test_multiply_returns_multiplied_number(numbers_1, numbers_2, expected_result):
    assert multiply(numbers_1, numbers_2) == expected_result


@pytest.mark.parametrize("base", [1, 2])
@pytest.mark.parametrize("exponent", [4, 5])
def test_pow_returns_exponentiated_number(base, exponent):
    assert pow_(base, exponent) == math.pow(base, exponent)


@pytest.mark.parametrize(
    "numbers",
    [1, 2, pytest.param(3, marks=pytest.mark.skip), 4, 5],
)
def test_square_returns_multiplied_number(numbers):
    assert square(numbers) == numbers**2


@pytest.mark.parametrize(
    "numbers",
    [
        pytest.param(-1, id="negative"),
        pytest.param(0, id="zero"),
    ],
)
def test_square_returns_multiplied_number(numbers):
    assert square(numbers) == numbers**2
