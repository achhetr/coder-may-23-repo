from main import ma

class PetSchema(ma.Schema):
    class Meta:
        fields = "id", "type", "breed", "license_number"

pet_schema = PetSchema()
pets_schema = PetSchema(many=True)
