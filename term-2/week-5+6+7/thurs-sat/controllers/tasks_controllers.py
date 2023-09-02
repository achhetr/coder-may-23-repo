from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError, DataError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from main import db
from models import Task, User
from schemas.tasks import task_schema, tasks_schema

# /task
tasks = Blueprint("task", __name__, url_prefix="/tasks")

@tasks.errorhandler(KeyError)
def key_error_handler(e):
    return jsonify({"error": f"Key Error - `{e}`"}), 400

@tasks.errorhandler(IntegrityError)
def integrity_error_handler(e):
    return jsonify({"error": f"Integrity Error - `{e}`"}), 400

@tasks.errorhandler(DataError)
def data_error_handler(e):
    return jsonify({"error": f"Data Error - `{e}`"}), 400


# /tasks -> list of tasks
@tasks.route("/", methods=["GET"])
@jwt_required()
def get_tasks():
    email = get_jwt_identity()
    statement = db.select(User).filter_by(email=email)
    user = db.session.scalar(statement)

    q = db.select(Task).filter_by(user_id=user.id)
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
@jwt_required()
def create_tasks():
    email = get_jwt_identity()
    statement = db.select(User).filter_by(email=email)
    user = db.session.scalar(statement)

    task_json = task_schema.load(request.json)
    task = Task(**task_json)
    task.user_id = user.id

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
