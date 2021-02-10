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

    from .views import main, auth
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)

    from .views.board import BoardResource
    from .views.board_article import BoardArticleResource
    api.add_resource(BoardResource, '/boards')
    api.add_resource(BoardArticleResource, '/boards/<int:board_id>', '/boards/<int:board_id>/<int:board_article_id>')

    return app
