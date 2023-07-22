from src.data.tests.user_register_spy import UserRegisterSpy
from src.presentation.controllers.user_register_controller import UserRegisterController
from src.presentation.http_types.http_response import HTTPResponse


class HTTPRequestMock:
    def __init__(self) -> None:
        self.body = {
            "first_name": "John",
            "last_name": "Doe",
            "age": 30,
            "email": "test@test.com",
        }


def test_handle():
    http_request_mock = HTTPRequestMock()
    use_case = UserRegisterSpy()
    user_register_controller = UserRegisterController(use_case)
    # fake_user = {
    #     "type": "User",
    #     "count": 1,
    #     "attributes": {
    #         **http_request_mock.body,
    #     },
    # }

    response = user_register_controller.handle(http_request_mock)

    print(f"\033[033m{response}\033[0m")
