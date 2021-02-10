from flask import jsonify
from flask_restful import Resource, reqparse, abort

from comma_board import db
from comma_board.models import Board, BoardArticle

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('content')
parser.add_argument('board_id')


class BoardArticleResource(Resource):  # TODO 클래스명이 모델명과 겹치는 데 어떻게 작명해야 할지..
    def get(self, board_id=None, board_article_id=None):
        if not board_article_id:
            articles = BoardArticle.query.filter_by(board_id = board_id).all()
            if not articles:  # 해당 게시판 내 글이 하나도 없다면
                abort(400, description = "해당 게시판에 글이 존재하지 않습니다")
            result = [a.serialized for a in articles]
        else:  # board_article_id가 주어질 경우
            article = BoardArticle.query.filter_by(id = board_article_id).first()
            if not article:  # 해당 id의 글이 없다면
                abort(400, description = "해당하는 게시물이 없습니다")
            result = article.serialized
        return jsonify(status = 200, result = result)

    def post(self, board_id):
        args = parser.parse_args()
        _title = args.title
        _content = args.content

        if not _title or not _content:
            abort(400, description = "제목 또는 내용이 비어있을 수 없습니다")

        board = Board.query.filter_by(id = board_id).first()
        article = BoardArticle(title = _title, content = _content)
        board.article_set.append(article)  # board의 article_set에 현재 article을 더해줌
        db.session.commit()
        return jsonify(status = 200, result = article.serialized)

    def put(self, board_id, board_article_id=None):
        args = parser.parse_args()
        _title = args.title
        _content = args.content
        _board_id = args.board_id

        if not _title or not _content:
            abort(400, description = "제목 또는 내용이 비어있을 수 없습니다")

        if not board_article_id:
            abort(400, description = "해당하는 게시물이 없습니다")

        article = BoardArticle.query.filter_by(id = board_article_id, board_id = board_id).first()
        if not article:  # 해당 id의 글이 없다면
            abort(400, description = "해당하는 게시물이 없습니다")

        article.title = _title
        article.content = _content
        article.board_id = _board_id
        db.session.commit()
        return jsonify(status = 200, result = article.serialized)

    def delete(self, board_id, board_article_id=None):
        if not board_article_id:
            board = Board.query.filter_by(id = board_id).first()
            if not board:
                abort(400, description = "해당하는 게시판이 없습니다")
            result = { 'deleted': [a.serialized for a in board.article_set] }
            db.session.query(BoardArticle).filter(BoardArticle.board_id == board_id).delete()
        else:  # board_article_id가 주어질 경우
            article = BoardArticle.query.filter_by(id = board_article_id, board_id = board_id).first()
            if not article:
                abort(400, description = "해당하는 게시물이 없습니다")
            result = article.serialized
            db.session.delete(article)
        db.session.commit()
        return jsonify(status = 200, result = { 'deleted': result })
