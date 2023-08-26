from flask import Blueprint, jsonify

from main import db
from models.users import User
from schemas.users import user_schema, users_schema

# /user
users = Blueprint("user", __name__, url_prefix="/users")

# /users -> list of users
@users.route("/", methods=["GET"])
def get_users():
    q = db.select(User)
    users = db.session.scalars(q)
    return jsonify(users_schema.dump(users))
    
# /users/<id> -> show user with id
@users.route("/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    q = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(q)
    response = user_schema.dump(user)

    if response:
        return jsonify(response)

    return jsonify(message=f"User with id=`{user_id}` not found")

    
# /users/<id> -> delete user with id
@users.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    q = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(q)
    response = user_schema.dump(user)

    if response:
        db.session.delete(user)
        db.session.commit()
        return jsonify(message=f"User with id=`{user_id}` deleted successfully!")

    return jsonify(message=f"Cannot delete user with id=`{user_id}`. Not found")

# Creating a user and updating a user
