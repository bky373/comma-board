import click
from flask import g
from flask.cli import with_appcontext

from .module import Database


def get_db():
    if 'db' not in g:
        g.db = Database()
    return g.db


def close_db(exception=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initailzed the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
