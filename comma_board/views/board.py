from flask import jsonify, Blueprint
from flask_restful import Resource, reqparse, abort, Api

from comma_board import db
from comma_board.models import Board

bp = Blueprint('board', __name__)
api = Api(bp)

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')
parser.add_argument('user_id')


# TODO Marshmallow나 WTForm 찾아보기
def abort_if_empty_input(value):
    if not value:
        abort(400, descritpion = '입력칸이 비어있을 수 없습니다')


def abort_if_name_already_exists(model, name):
    if model.query.filter_by(name = name).first():
        abort(400, descritpion = '이미 같은 이름이 존재합니다')


class BoardResource(Resource):
    def get(self):
        return jsonify(
            status = 200,
            boards = [b.serialized for b in Board.query.order_by(Board.date_created.desc())]
        )  # TODO 다른 직렬화 방법 좀더 찾아보기

    def post(self):
        args = parser.parse_args()
        _name = args.name
        _user_id = 1  # TODO g.user로 변경하기
        # _user_id = args.user_id

        print('000')
        abort_if_empty_input(_name)
        abort_if_name_already_exists(Board, _name)

        board = Board(name = _name, user_id = _user_id)
        db.session.add(board)
        db.session.commit()
        return jsonify(status = 200, board = board.serialized)

    def put(self):
        args = parser.parse_args()
        _id = args.id
        _name = args.name

        abort_if_empty_input(_name)
        abort_if_name_already_exists(Board, _name)

        board = Board.query.filter_by(id = _id).first()
        if not board:
            abort(400, description = '해당 게시판을 찾을 수 없습니다')

        board.name = _name
        db.session.commit()
        return jsonify(status = 200, result = board.serialized)

    def delete(self):
        args = parser.parse_args()
        board = Board.query.filter_by(id = args.id).first()
        if not board:
            abort(400, description = '해당 게시판을 찾을 수 없습니다')

        db.session.delete(board)
        db.session.commit()
        return jsonify(status = 200, result = board.serialized)


api.add_resource(BoardResource, '/boards')
