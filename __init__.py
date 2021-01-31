from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    # TODO: config 설정

    from .database import db
    with app.app_context():
        db.init_app(app)

    @app.route('/hi')
    def hi():
        return "hi"

    return app
