from flask import Blueprint, jsonify

from main import db
from models.tasks import Task

# /task
tasks = Blueprint("task", __name__, url_prefix="/tasks")

@tasks.route("/", methods=["GET"])
def get_tasks():
    return jsonify(message="yes")

