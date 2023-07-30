import pytest
from functions import cube, multiply, square


@pytest.mark.xfail(raises=NotImplementedError, reason="Mehotod not implemented yet.")
def test_multiply_returns_multiplied_number():
    assert multiply(numbers_1, numbers_2) == expected_result
