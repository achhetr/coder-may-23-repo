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

    # cli commands to create default ORMs

    # connect schemas
    ma.init_app(app)

    # creating routes or controllers through blueprints

    return app
