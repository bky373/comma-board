from flask import jsonify, Blueprint
from flask_restful import reqparse, Resource

from .database.db import get_db

board_bp = Blueprint('board', __name__)

parser = reqparse.RequestParser()
parser.add_argument("id")
parser.add_argument("name")


class Board(Resource):
    def get(self):
        sql = "SELECT id, name FROM `board`"
        db = get_db()
        result = db.execute_all(sql)
        return jsonify(status = "success", result = result)

    def post(self):
        name = parser.parse_args()['name']  # TODO args() 바꾸기
        sql = "INSERT INTO `board` (`name`) VALUES (%s)"
        db = get_db()
        db.execute(sql, (name,))
        db.commit()
        return jsonify(status = "success", result = { "name": name })

    def put(self):
        args = parser.parse_args()
        sql = "UPDATE `board` SET name = %s WHERE `id` = %s"
        db = get_db()
        db.execute(sql, (args['name'], args['id']))
        db.commit()
        return jsonify(status = "success", result = { "id": args["id"], "name": args["name"] })

    def delete(self):
        args = parser.parse_args()
        sql = "DELETE FROM `board` WHERE `id` = %s"
        db = get_db()
        db.execute(sql, (args['id'],))
        db.commit()
        return jsonify(status = "success", result = { "id": args["id"] })
