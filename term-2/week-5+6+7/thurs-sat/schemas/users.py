from main import ma
from marshmallow import fields, validate

class UserSchema(ma.Schema):
    email = fields.Email(
        required=True,
        validate=validate.Length(min=6, max=15, error="Careful this email is valid")
    )

    class Meta:
        fields = "id", "email", "password", "admin", "tasks"

    tasks = fields.List(fields.Nested("TaskSchema", exclude=("user",)))


user_schema = UserSchema()
users_schema = UserSchema(many=True)
