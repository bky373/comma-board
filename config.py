import mysecrets

DB_URL = 'mysql+pymysql://{user}:{pw}@{host}:{port}/{db}?charset=utf8'.format(
    user = mysecrets.dbuser,
    pw = mysecrets.dbpass,
    host = mysecrets.dbhost,
    port = mysecrets.dbport,
    db = mysecrets.dbname
)

SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'fwowfhowadsfowl' # TODO 추후 변경
