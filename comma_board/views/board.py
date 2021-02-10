from flask import jsonify
from flask_restful import Resource, reqparse, abort

from comma_board import db
from comma_board.models import Board

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')


class BoardList(Resource):
    def get(self):
        boards = Board.query.all()
        return jsonify(status = 200, result = [b.serialized for b in boards])

    def post(self):
        args = parser.parse_args()
        _name = args.name

        if not _name:
            abort(400, description = '게시판 이름이 비어있을 수 없습니다')
        elif Board.query.filter_by(name = _name).first():
            abort(400, description = '이미 같은 이름의 게시판이 존재합니다')

        board = Board(name = _name)
        db.session.add(board)
        db.session.commit()
        return jsonify(status = 200, result = board.serialized)

    def put(self):
        args = parser.parse_args()
        _id = args.id
        _name = args.name

        if not _name:
            abort(400, description = '게시판 이름이 비어있을 수 없습니다')
        elif Board.query.filter_by(name = _name).first():
            abort(400, description = '이미 같은 이름의 게시판이 존재합니다')

        board = Board.query.filter_by(id = _id).first()
        if not board:
            abort(400, description = '해당 게시판을 찾을 수 없습니다')

        board.name = _name
        db.session.commit()
        return jsonify(status = 200, result = board.serialized)

    def delete(self):
        args = parser.parse_args()
        _id = args.id

        board = Board.query.filter_by(id = _id).first()
        if not board:
            abort(400, description = '해당 게시판을 찾을 수 없습니다')

        db.session.delete(board)
        db.session.commit()
        return jsonify(status = 200, result = board.serialized)
