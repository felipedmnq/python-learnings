import pytest
from functions import cube, multiply, square


@pytest.fixture(params=[1, 2, 3, 4], autouse=True)
def numbers(request):
    return request.param


def test_square_returns_squared_number(numbers):
    assert square(numbers) == numbers * numbers


def test_cube_returns_cubed_number(numbers):
    assert cube(numbers) == numbers * numbers * numbers


@pytest.mark.skip(reason="Mehotod not implemented yet.")
def test_multiply_returns_multiplied_number(numbers):
    assert multiply(numbers) == numbers * numbers


def test_square_returns_squared_number(numbers):
    pytest.skip()
    assert square(numbers) == numbers * numbers
