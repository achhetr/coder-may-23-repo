from main import db

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)

    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=False)

    user = db.relationship(
        "User",
        back_populates="comments"
    )

    task = db.relationship(
        "Task",
        back_populates="comments"
    )
