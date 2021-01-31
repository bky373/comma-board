import pymysql

from . import secrets


class Database():
    def __init__(self):
        self.db = pymysql.connect(
            user = secrets.dbuser,
            passwd = secrets.dbpass,
            host = secrets.dbhost,
            port = secrets.dbport,
            db = secrets.dbname,
            charset = secrets.dbcharset
        )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={ }):
        self.cursor.execute(query, args)

    def execute_one(self, query, args={ }):
        self.cursor.execute(query, args)
        return self.cursor.fetchone()

    def execute_all(self, query, args={ }):
        self.cursor.execute(query, args)
        return self.cursor.fetchall()

    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()
