import pytest
from functions import cube, multiply, square


class TestClass:
    @pytest.fixture(params=[1, 2, 3, 4], autouse=True)
    def numbers(self, request):
        return request.param

    def test_square_returns_squared_number(self):
        assert square(numbers) == numbers * numbers

    def test_cube_returns_cubed_number(self):
        assert cube(numbers) == numbers * numbers * numbers

    @pytest.mark.skip(reason="Mehotod not implemented yet.")
    def test_multiply_returns_multiplied_number():
        pass
