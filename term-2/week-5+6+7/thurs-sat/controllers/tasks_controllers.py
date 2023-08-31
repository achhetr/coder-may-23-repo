from flask import Blueprint, jsonify, request

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

# /tasks -> Creating a task
@tasks.route("/", methods=["POST"])
def create_tasks():
    task_json = task_schema.load(request.json)
    task = Task(**task_json)
    db.session.add(task)
    db.session.commit()

    return jsonify(task_schema.dump(task))

# /tasks/<id> -> Updating a task with id
@tasks.route("/<int:task_id>", methods=["PUT"])
def update_tasks(task_id: int):
    q = db.select(Task).filter_by(id=task_id)
    task = db.session.scalar(q)
    response = task_schema.dump(task)

    if response:
        task_json = task_schema.load(request.json)
        task.name = task_json["name"]
        task.description = task_json["description"]
        task.due_date = task_json["due_date"]
        task.completed_at = task_json.get("completed_at")
        task.user_id = task_json["user_id"]
        db.session.commit()
        return jsonify(task_schema.dump(task))

    return jsonify(message=f"Cannot update task with id=`{task_id}`. Not found")
