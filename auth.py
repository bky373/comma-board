from flask import Blueprint, session, jsonify
from flask import flash
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash

from .database.db import get_db

auth_bp = Blueprint('auth', __name__)

parser = reqparse.RequestParser()
parser.add_argument("id")
parser.add_argument("fullname")
parser.add_argument("email")
parser.add_argument("password")


@auth_bp.route('/join')
class AuthJoin(Resource):
    def get(self):
        return jsonify(status = "success")

    def post(self):
        args = parser.parse_args()
        fullname = args['fullname']
        email = args['email']
        password = args['password']
        error = None

        db = get_db()
        if not fullname:
            error = 'fullname이 유효하지 않습니다.'
        elif not email:
            error = 'email이 유효하지 않습니다.'
        elif not password:
            error = 'Password가 유효하지 않습니다.'
        elif db.execute_one(
                "SELECT id FROM `user` WHERE `email` = %s", (args['email'],)
        ) is not None:
            error = '{} 계정은 이미 등록된 계정입니다.'.format(email)

        if error is None:
            result = db.execute_one(
                'INSERT INTO user (fullname, email, password) VALUES (%s, %s, %s)',
                (fullname, email, generate_password_hash(password))
            )
            db.commit()
            return jsonify(status = "success", result = result)

        flash(error)
        return jsonify(status = "fail")


@auth_bp.route('/login')
class AuthLogin(Resource):
    def get(self):
        return jsonify(status = "success")

    def post(self):
        args = parser.parse_args()
        email = args['email']
        password = args['password']
        error = None

        db = get_db()
        user = db.execute_one(
            'SELECT * FROM user WHERE email = %s', (email,)
        )

        if user is None:
            error = '등록되지 않은 계정입니다.'
        elif not check_password_hash(user['password'], password):
            error = 'password가 틀렸습니다.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return jsonify(status = "success")

        flash(error)
        return jsonify(status = "fail")


@auth_bp.route('/logout')
def logout():
    session.clear()
    return jsonify(status = "success")
