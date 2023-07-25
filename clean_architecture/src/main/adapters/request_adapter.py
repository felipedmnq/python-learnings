from typing import Callable

from flask import request as flask_request
from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse


def request_adapter(request: flask_request, controller: Callable) -> HTTPResponse:
    body = None
    print(f"\033[93m{request.data}\033[0m")
    if request.data:
        body = request.json

    print(f"\033[92m{body}\033[0m")

    http_request = HTTPRequest(
        body=body,
        headers=request.headers,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path,
    )

    return controller(http_request)
