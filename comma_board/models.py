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


class BoardArticle(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), nullable = False)
    content = db.Column(db.Text, nullable = False)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id', ondelete = 'CASCADE'))
    board = db.relationship('Board', backref = db.backref('article_set', cascade = 'all, delete-orphan'))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.now)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'board_id': self.board_id,
            'date_created': self.date_created
        }
