from flask import Blueprint

from main import db
from models import PetOwner, Pet

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables are created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables are dropped")

@db_commands.cli.command("seed")
def seed_db():
    # pets
    pet1 = Pet(
        type = "snake",
        breed = "viper",
        license_number = "0123dead"
    )
    pet2 = Pet(
        type = "snake",
        breed = "cobra",
        license_number = "0132dead"
    )
    pet3 = Pet(
        type = "snake",
        breed = "rattle_snake",
        license_number = "0321dead"
    )

    # pet owners
    pet_owner1 = PetOwner(
        license_number = "OWNSNAKE1",
        phone_number = "0012",
        post_code = "1234",
        is_shopkeeper = True
    )
    pet_owner2 = PetOwner(
        license_number = "OWNSNAKE2",
        phone_number = "0022",
        post_code = "2234",
        is_shopkeeper = False
    )

    db.session.add(pet1)
    db.session.add(pet2)
    db.session.add(pet3)
    db.session.add(pet_owner1)
    db.session.add(pet_owner2)

    # db.session.add_all([pet1, pet2, pet3, pet_owner1, pet_owner2])
    db.session.commit()

    print('Table is seeded with pets and pet_owners!')

