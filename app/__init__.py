import os
from flask import Flask
from .db import mongodb
from .animals.controller import bp as animal_route


def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
    mongodb.init_app(app=app)
    app.register_blueprint(animal_route, url_prefix='/animals')
    return app
