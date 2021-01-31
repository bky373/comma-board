from flask import Flask
from flask_restful import Api


def create_app(test_config=None):
    app = Flask(__name__)
    api = Api(app)
    # TODO: config 설정

    from .database import db
    with app.app_context():
        db.init_app(app)

    @app.route('/hi')
    def hi():
        return "hi"

    from .board import board_bp, Board
    app.register_blueprint(board_bp)

    api.add_resource(Board, '/boards')

    return app
