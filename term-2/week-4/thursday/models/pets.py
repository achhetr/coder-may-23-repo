from main import db

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)

    type = db.Column(db.String)
    breed = db.Column(db.String)
    license_number = db.Column(db.String)

