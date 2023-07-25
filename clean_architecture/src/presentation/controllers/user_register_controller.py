from loguru import logger
from src.domain.models.users import User
from src.domain.use_cases.user_registry import UserRegistryInterface
from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controler_interface import ControllerInterface


class UserRegisterController(ControllerInterface):
    def __init__(self, user_register: UserRegistryInterface) -> None:
        self.__user_register = user_register

    def handle(self, http_request: HTTPRequest) -> HTTPResponse:
        first_name = http_request.body["first_name"]
        last_name = http_request.body["last_name"]
        age = http_request.body["age"]
        email = http_request.body["email"]

        user = User(first_name=first_name, last_name=last_name, age=age, email=email)

        response = self.__user_register.register_user(user)

        return HTTPResponse(status_code=200, body={"data": response})
