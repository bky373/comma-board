from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def register_blueprints(app):
    from .views import main, auth, board, board_article, dashboard
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(board.bp)
    app.register_blueprint(board_article.bp)
    app.register_blueprint(dashboard.bp)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    register_blueprints(app)

    return app
