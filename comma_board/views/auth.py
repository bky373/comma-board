from flask import Blueprint, request, jsonify, session, g, abort
from werkzeug.security import generate_password_hash, check_password_hash

from comma_board import db
from comma_board.models import User

bp = Blueprint('auth', __name__, url_prefix = '/auth')


@bp.route('/signup', methods = ('GET', 'POST'))
def signup():
    if request.method == 'POST':
        data = request.get_json()
        _fullname = data['fullname']
        _email = data['email']
        _password = data['password']

        # TODO 입력값 유효 체크 기능 개선하기
        if not _fullname:
            abort(400, description = "이름이 유효하지 않습니다")
        if not _password:
            abort(400, description = "비밀번호가 유효하지 않습니다")
        if not _email:
            abort(400, description = "이메일이 유효하지 않습니다")
        if User.query.filter_by(email = _email).first():
            abort(400, description = "이미 등록된 이메일입니다")

        user = User(fullname = _fullname, email = _email, password = generate_password_hash(_password))
        db.session.add(user)
        db.session.commit()
        return jsonify(status = "success", result = user.serialized)
    return jsonify(status = "success", msg = "signup get method called")


@bp.route('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        data = request.get_json()
        _email = data['email']
        _password = data['password']

        user = User.query.filter_by(email = _email).first()
        if not user:
            abort(400, description = "등록되지 않은 계정입니다")
        elif not check_password_hash(user.password, _password):
            abort(400, description = "비밀번호가 올바르지 않습니다")

        session.clear()
        session['user_id'] = user.id
        return jsonify(status = "success", result = user.serialized)
    return jsonify(status = "success", msg = "login get method called")


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id = user_id).first()


@bp.route('/logout')
def logout():
    session.clear()
    return jsonify(status = "success", msg = "logout success")
