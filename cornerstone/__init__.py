from os.path import dirname, abspath
from flask import Flask

from .routes_config import load_routes

PROJECT_ROOT_PATH = dirname(dirname(abspath(__file__)))


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    load_routes(app)
    return app
