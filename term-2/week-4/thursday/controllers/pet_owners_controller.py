from flask import Blueprint, jsonify

from main import db
from models.pet_owners import PetOwner
from schemas.pet_owner_schema import pet_owner_schema, pet_owners_schema

pet_owners = Blueprint('pet_owner', __name__, url_prefix="/pet_owner")

@pet_owners.route("/", methods=["GET"])
def get_pet_owners():
    q = db.select(PetOwner)
    pet_owners_list = db.session.scalars(q)
    response = pet_owners_schema.dump(pet_owners_list)

    return jsonify(response)
