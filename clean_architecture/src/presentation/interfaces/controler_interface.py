from abc import ABC, abstractmethod

from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse


class ControllerInterface(ABC):
    @abstractmethod
    def handle(self, http_request: HTTPRequest) -> HTTPResponse:
        raise NotImplementedError("Should implement handle method.")
