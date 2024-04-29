# src/app/__init__.py

import os
from flask import Flask, jsonify, render_template
from flask_migrate import Migrate
from . import database
from flask_login import LoginManager


def create_app(test_config=None, reset=False):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # SQLALCHEMY_DATABASE_URI in database.py,
    )

    # initialize db with app
    database.init_db(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # import the controllers
    from .controllers.views_controller import views
    from .controllers.auth_controller import auth
    from .controllers.team_controller import team
    # register the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(team, url_prefix='/')

    from .models.user import User
    from .models.team import Team

    # Debug: Print the database structure
    # database.print_db_structure(app)

    # create all tables
    database.create_db(app, reset)
    database.check_db(app)

    # login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login_user'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app