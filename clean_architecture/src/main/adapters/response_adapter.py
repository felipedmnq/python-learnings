import json
from typing import Callable

from flask import request as flask_request
from loguru import logger
from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse


def response_adapter(request: flask_request, controller: Callable) -> HTTPResponse:
    http_request = HTTPRequest(
        body=request,
        headers=request.headers,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path,
    )

    return controller(http_request)
