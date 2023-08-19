from main import db

class PetOwner(db.Model):
    __tablename__ = "pet_owners"

    id = db.Column(db.Integer, primary_key=True)

    license_number = db.Column(db.String)
    phone_number = db.Column(db.String)
    post_code = db.Column(db.String)
    is_shopkeeper = db.Column(db.Boolean)

