from flask import jsonify, Blueprint
from flask_restful import reqparse, Resource

from .database.db import get_db

board_article_bp = Blueprint('board_article', __name__)

parser = reqparse.RequestParser()
parser.add_argument("id")
parser.add_argument("title")
parser.add_argument("content")
parser.add_argument("board_id")


# TODO: sqlalchemy 사용 아니면, get_db() 반복 호출 개선
# TODO 전반적으로 기능 detail 개선 (예, get에서 id는 들어왔지만 db에 없을 경우)
class BoardArticle(Resource):
    def get(self, board_id, board_article_id=None):
        db = get_db()
        if board_article_id:
            sql = "SELECT id, title, content FROM `board_article` WHERE `id` = %s"
            result = db.execute_one(sql, (board_article_id,))
        else:
            print('---', board_id)
            sql = "SELECT id, title, content FROM `board_article` WHERE `board_id` = %s"
            result = db.execute_all(sql, (board_id,))
        return jsonify(status = "success", result = result)

    def post(self, board_id):
        args = parser.parse_args()
        sql = "INSERT INTO `board_article` (`title`, `content`, `board_id`) VALUES (%s, %s, %s)"
        db = get_db()
        db.execute(sql, (args['title'], args['content'], board_id))
        db.commit()
        return jsonify(status = "success",
                       result = { "title": args['title'], "content": args['content'] })

    def put(self, board_id, board_article_id):
        args = parser.parse_args()
        sql = "UPDATE `board_article` SET `title` = %s, `content` = %s WHERE `id` = %s AND `board_id` = %s"
        db = get_db()
        db.execute(sql, (args['title'], args['content'], board_article_id, board_id))
        db.commit()
        return jsonify(status = "success",
                       result = { "id": board_article_id, "title": args["title"], "content": args['content'] })

    def delete(self, board_id, board_article_id):
        sql = "DELETE FROM `board_article` WHERE `id` = %s AND `board_id` = %s"
        db = get_db()
        db.execute(sql, (board_article_id, board_id))
        db.commit()
        return jsonify(status = "success", result = { "id": board_article_id })
