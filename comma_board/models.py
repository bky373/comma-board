from datetime import datetime

from comma_board import db


class Board(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'), nullable = False)
    user = db.relationship('User', backref = db.backref('board_set'))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.now)
    date_modified = db.Column(db.DateTime, nullable = False, default = datetime.now) # TODO 수정 기능 만들기

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
            'date_created': self.date_created,
            'date_modified': self.date_created,
        }


class BoardArticle(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), nullable = False)
    content = db.Column(db.Text, nullable = False)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id', ondelete = 'CASCADE'))
    board = db.relationship('Board', backref = db.backref('article_set', cascade = 'all, delete-orphan'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'), nullable = False)
    user = db.relationship('User', backref = db.backref('article_set'))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.now)
    date_modified = db.Column(db.DateTime, nullable = False, default = datetime.now) # TODO 수정 기능 만들기

    @property
    def serialized(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'board_id': self.board_id,
            'user_id': self.user_id,
            'date_created': self.date_created,
            'date_modified': self.date_modified
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(32), nullable = False)
    email = db.Column(db.String(64), unique = True, nullable = False)
    password = db.Column(db.String(128), nullable = False)
    date_joined = db.Column(db.DateTime, nullable = False, default = datetime.now)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'email': self.email,
            'date_joined': self.date_joined
        }
