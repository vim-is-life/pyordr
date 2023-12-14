#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():
        from . import routes

        # need this for routes to work
        app.register_blueprint(routes.main_blueprint)

        db.create_all()

        return app
