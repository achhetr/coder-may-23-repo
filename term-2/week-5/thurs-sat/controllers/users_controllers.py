from flask import Blueprint, jsonify

from main import db
from models.users import User

# /user
users = Blueprint("user", __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def get_users():
    return jsonify(message="yes")

