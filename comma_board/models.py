from datetime import datetime

from comma_board import db


class Board(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.now)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_created': self.date_created
        }
