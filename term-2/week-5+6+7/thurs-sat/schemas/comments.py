from main import ma
from marshmallow import fields

class CommentSchema(ma.Schema):
    class Meta:
        fields = "id", "message", "created_at", "user_id", "task_id", "task"

        load_only = ['user_id', "task_id"]
    
    task = fields.Nested("TaskSchema")


comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
