from main import ma
from marshmallow import fields

class UserSchema(ma.Schema):
    class Meta:
        fields = "id", "email", "tasks"

    tasks = fields.List(fields.Nested("TaskSchema", exclude=("user",)))


user_schema = UserSchema()
users_schema = UserSchema(many=True)
