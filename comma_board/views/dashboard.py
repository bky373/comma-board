from flask import jsonify
from flask_restful import Resource

from comma_board.models import Board


class DashboardResource(Resource):
    def get(self, count=3):
        result = []
        for board in Board.query:
            articles = sorted(board.article_set[-count:], key = lambda x: x.date_created, reverse = True)
            if len(articles) < 1: continue

            result.append({
                'board_id': board.id,
                'board_name': board.name,
                'titles': list(map(lambda x: { 'title': x.title, 'date_created': x.date_created }, articles))
            })
        return jsonify(status = "success", result = result)
