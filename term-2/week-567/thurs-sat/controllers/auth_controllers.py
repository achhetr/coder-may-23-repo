from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from main import db, bcrypt
from models.users import User
from schemas.users import user_schema

# /auth
auths = Blueprint("auth", __name__, url_prefix="/auth")

# /auths -> Create and register a user
@auths.route("/register", methods=["POST"])
def register_user():
    user_json = user_schema.load(request.json)
    user = User(
        **{
            "email": user_json["email"],
            "admin": True,
            "password": bcrypt.generate_password_hash(user_json["password"]).decode("utf") 
        }
    )
    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=user_json["email"])

    return jsonify({"token": access_token})

@auths.route("/login", methods=["POST"])
@jwt_required()
def login_user():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

    email = request.json["email"]
    password = request.json["password"]

    q = db.select(User).filter_by(email=email)
    user = db.session.scalar(q)
    
    if not user or not bcrypt.check_password_hash(user.password, password):
        return abort(401, description="Incorrect username and password!")

    return jsonify({"message": "success", **user_schema.dump(user)})
