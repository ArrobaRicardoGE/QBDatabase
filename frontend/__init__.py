from flask import Flask
from . import routes


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")
    app.config["API_URL"] = "http://localhost:3001"
    app.register_blueprint(routes.bp)

    return app
