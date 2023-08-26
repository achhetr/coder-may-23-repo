from flask import Blueprint, jsonify

from main import db
from models.tasks import Task
from schemas.tasks import task_schema, tasks_schema

# /task
tasks = Blueprint("task", __name__, url_prefix="/tasks")

# /tasks -> list of tasks
@tasks.route("/", methods=["GET"])
def get_tasks():
    q = db.select(Task)
    tasks = db.session.scalars(q)
    return jsonify(tasks_schema.dump(tasks))
    
# /tasks/<id> -> show task with id
@tasks.route("/<int:task_id>", methods=["GET"])
def get_task(task_id: int):
    q = db.select(Task).filter_by(id=task_id)
    task = db.session.scalar(q)
    response = task_schema.dump(task)

    if response:
        return jsonify(response)

    return jsonify(message=f"Task with id=`{task_id}` not found")

    
# /tasks/<id> -> delete task with id
@tasks.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id: int):
    q = db.select(Task).filter_by(id=task_id)
    task = db.session.scalar(q)
    response = task_schema.dump(task)

    if response:
        db.session.delete(task)
        db.session.commit()
        return jsonify(message=f"Task with id=`{task_id}` deleted successfully!")

    return jsonify(message=f"Cannot delete task with id=`{task_id}`. Not found")

# Creating a task and updating a task
