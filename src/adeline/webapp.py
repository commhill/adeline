"""
Entry point for Flask
"""
from flask import Flask
from flask_login import LoginManager  # type: ignore
from flask_migrate import Migrate  # type: ignore
from flask_sqlalchemy import SQLAlchemy

from adeline.api import api as api_blueprint


def init_blueprints(webapp: Flask) -> None:
    """
    Register all of the blueprints

    :param webapp: the flask instance.
    """
    webapp.register_blueprint(api_blueprint, url_prefix="/api")


def init_app() -> Flask:
    """
    Initialize a Flask app and set config.
    """
    webapp: Flask = Flask(__name__)

    if "SQLALCHEMY_DATABASE_URI" not in webapp.config:
        # Use sqlite when in local dev mode
        webapp.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tmp/adeline-webapp.db"

    init_blueprints(webapp)

    return webapp


def init_db(webapp: Flask) -> SQLAlchemy:
    """
    Initialize and migrate the database.

    :param webapp: the flask instance
    :returns: the database instance
    """
    db_session: SQLAlchemy = SQLAlchemy(webapp)
    Migrate(webapp, db_session)

    return db_session


def init_login_manager(webapp: Flask) -> LoginManager:
    """
    Setup the login manager for users

    :param webapp: the flask instance.
    :returns: the login manager
    """
    return LoginManager(webapp)


app: Flask = init_app()
db: SQLAlchemy = init_db(app)
login_manager: LoginManager = init_login_manager(app)


@app.route("/health_check")
def health_check() -> str:
    """
    Just a basic endpoint for health checking.

    :returns: "GOOD" if healthy, otherwise "BAD".
    """
    return "GOOD"


def main() -> None:
    """
    The main entry point.
    """
    app.run()
