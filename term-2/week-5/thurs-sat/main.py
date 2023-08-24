from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def init_app():
    # create flask app instance
    app = Flask(__name__)

    # app config
    app.config.from_object("config.app_config")

    # connect to DB
    db.init_app(app)

    # connect schemas
    ma.init_app(app)

    # connect CLI commands -> blueprint
    from commands import db_commands
    app.register_blueprint(db_commands)

    # connect blueprint controllers
    from controllers import registered_controllers

    for controller in registered_controllers:
        app.register_blueprint(controller)

    return app
