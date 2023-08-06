import pytest


@pytest.fixture(params=[1, 2, 3, 4], autouse=True)
def numbers(request):
    """This fixture retunrs a number."""
    return request.param
