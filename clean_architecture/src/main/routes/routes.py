import json

from flask import Blueprint, jsonify, request
from loguru import logger
from src.domain.models.users import User
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_resgiter_composer

user_routes_bp = Blueprint("user_routes", __name__)


@user_routes_bp.route("/user/find", methods=["GET"])
def find_user():
    http_response = request_adapter(request, user_finder_composer())
    return jsonify(http_response.body), http_response.status_code


@user_routes_bp.route("/user", methods=["POST"])
def register_user():
    user_data = json.loads(request.data.decode("utf-8"))
    logger.info(f"Registering user...{user_data}")

    http_response = request_adapter(request, user_data, user_resgiter_composer())

    return http_response.body, http_response.status_code
