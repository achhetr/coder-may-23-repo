from flask import Blueprint
from datetime import datetime
import time

from main import db, bcrypt
from models import Task, User, Comment

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables are created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables are dropped")

@db_commands.cli.command("seed")
def seed_db():
    # create User objects
    user1 = User(
        email = "akash1@jit.com.au",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )
    user2 = User(
        email = "akash1@dillon.com.au",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )

    # add all users object to db
    db.session.add_all([
        user1, user2,
    ])
    # commit db for users
    db.session.commit()

    # create Task objects
    time_1_day_later = int(time.time()) + (24 * 60 * 60)
    task1 = Task(
        name = "first task",
        description = "Explaining students about ORM",
        due_date = datetime.fromtimestamp(time_1_day_later),
        completed_at = None,
        state = "In Progress",
        user_id = user1.id,
    )

    task2 = Task(
        name = "second task",
        description = "Explaining students about Blueprint",
        due_date = datetime.fromtimestamp(time_1_day_later),
        completed_at = datetime.now(),
        state = "Completed",
        user_id = user2.id,
    )

    time_1_day_ago = int(time.time()) - (24 * 60 * 60)
    time_2_day_ago = int(time.time()) - (24 * 60 * 60 * 2)
    task3 = Task(
        name = "third task",
        description = "Explaining students about Association",
        due_date = datetime.fromtimestamp(time_1_day_ago),
        completed_at = datetime.fromtimestamp(time_2_day_ago),
        user_id = user1.id,
        state = "Completed",
    )

    # add tasks object to db
    db.session.add_all([
        task1, task2, task3,
    ])

    # commit db for tasks
    db.session.commit()

    # comments
    comment1 = Comment(
        message = "Teach Flask",
        created_at = datetime.now(),
        task_id = task1.id,
        user_id = user2.id,
    )

    comment2 = Comment(
        message = "Teach Flask",
        created_at = datetime.now(),
        task_id = task1.id,
        user_id = task1.user_id,
    )

    # add comments object to db
    db.session.add_all([
        comment1, comment2,
    ])

    db.session.commit()

    # log if seed is succeeded
    print("Database has been seeded")

