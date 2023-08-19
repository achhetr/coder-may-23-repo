from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def init_app():
    app = Flask(__name__)

    # config
    app.config.from_object("config.app_config")

    # connect db through orm
    db.init_app(app)

    # connect schemas
    ma.init_app(app)

    # cli commands to create default ORMs
    from commands import db_commands
    app.register_blueprint(db_commands)

    # creating routes or controllers through blueprints
    from controllers import registered_controllers

    for controller in registered_controllers:
        app.register_blueprint(controller)

    return app
