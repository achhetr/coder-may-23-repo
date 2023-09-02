from main import ma
from marshmallow import fields, validate

class TaskSchema(ma.Schema):
    state = fields.String(load_default='Not Started', validate=validate.OneOf(["Not Started", "In Progress", "Completed"]))

    class Meta:
        fields = (
            "id",
            "name",
            "state",
            "description",
            "due_date",
            "completed_at",
            "user_id",
            "user",
        )

        load_only = ['user_id']

    user = fields.Nested("UserSchema", exclude=("tasks",))


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

