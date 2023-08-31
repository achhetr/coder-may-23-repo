from main import ma
from marshmallow import fields

class TaskSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
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

