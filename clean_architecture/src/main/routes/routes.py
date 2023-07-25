from flask import Blueprint, jsonify, request
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
    print(f"\033[91m{request.json()}\033[0m")
    http_response = request_adapter(request, user_resgiter_composer())
    return jsonify(http_response.body), http_response.status_code
