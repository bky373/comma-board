from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    from .views import main
    app.register_blueprint(main.bp)

    from .views.board import BoardList
    api.add_resource(BoardList, '/boards')

    return app
