from src.domain.use_cases.user_finder import UserFinderInterface
from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controler_interface import ControllerInterface


class UserFinderController(ControllerInterface):
    def __init__(self, user_finder: UserFinderInterface) -> None:
        self.__user_finder = user_finder

    def handle(self, http_request: HTTPRequest) -> HTTPResponse:
        first_name = http_request.path_params["first_name"]
        response = self.__user_finder.find_user(first_name)

        return HTTPResponse(status_code=200, body={"data": response})
