import os

basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, os.environ['DATABASE_DIR'])
ADMIN_CREDENTIALS = (os.environ['FLASK_USER'], os.environ['FLASK_USER_PASSWD'])
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(database_path, os.environ['DATABASE_FILENAME'])
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False