from main import ma

class TaskSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
            "description",
            "due_date",
            "completed_at"
        ) 


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
