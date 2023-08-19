from flask import Blueprint, jsonify, abort, request

from main import db
from models.pets import Pet
from schemas.pet_schema import pet_schema, pets_schema

pets = Blueprint('pet', __name__, url_prefix="/pet")

@pets.route("/", methods=["POST"])
def create_pet():
    pet = Pet(**pet_schema.load(request.json))

    db.session.add(pet)
    db.session.commit()

    return jsonify(pet_schema.dump(pet))


@pets.route("/", methods=["GET"])
def get_pets():
    q = db.select(Pet)
    pet_list = db.session.scalars(q)
    response = pets_schema.dump(pet_list)

    return jsonify(response)


# localhost:5000/pet/<identifier>
@pets.route("/<int:id>", methods=["GET"])
def get_pet(id: int):
    # q = db.select(Pet).filter_by(id=id)
    # pet = db.session.scalar(q)
    # response = pet_schema.dump(pet)

    pet = Pet.query.filter_by(id=id).first()
    response = pet_schema.dump(pet)

    if not response:
        return jsonify({
            "status_code": 404,
            "message": "Id not found",
        })

    return jsonify(response)


@pets.route("/<int:id>", methods=["DELETE"])
def delete_pet(id: int):
    pet = Pet.query.filter_by(id=id).first()
    response = pet_schema.dump(pet)

    if not response:
        return jsonify({
            "message": "Object not found",
        })

    db.session.delete(pet)
    db.session.commit()

    return jsonify({
            "message": f"Object with {id} deleted",
        })

