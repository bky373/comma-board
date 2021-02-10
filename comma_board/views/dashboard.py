from flask import jsonify
from flask_restful import Resource

from comma_board.models import Board


class DashboardResource(Resource):
    def get(self, volume=3):
        result = []
        for board in Board.query:
            articles = board.article_set[:volume]
            if len(articles) < 1: continue

            articles = sorted(articles, key = lambda a: a.date_created, reverse = True)
            for a in articles:
                result.append({
                    'board_id': board.id,
                    'board_name': board.name,
                    'title': a.title,
                    'date_created': a.date_created
                })
        return jsonify(status = "success", result = result)
