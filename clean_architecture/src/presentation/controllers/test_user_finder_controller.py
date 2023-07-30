from src.data.tests.user_finder_spy import UserFinderSpy
from src.presentation.controllers.user_finder_controller import UserFinderController
from src.presentation.http_types.http_response import HTTPResponse


class HTTPRequestMock:
    def __init__(self) -> None:
        self.query_params = {"first_name": "John"}


def test_handle_return_correct_response():
    http_request_mock = HTTPRequestMock()
    use_case = UserFinderSpy()
    user_finder_controller = UserFinderController(use_case)

    response = user_finder_controller.handle(http_request_mock)

    assert isinstance(response, HTTPResponse)
    assert response.status_code == 200
    assert isinstance(response.body, dict)
