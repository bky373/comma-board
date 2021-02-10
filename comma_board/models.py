from comma_board import db


class Board(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)
    date_created = db.Column(db.DateTime(), nullable = False)