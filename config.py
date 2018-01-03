import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Flask Secret Key - also used for Flask-WTF CSRF Protection
SECRET_KEY = os.environ.get('SECRET_KEY') or 'An extremely difficult to guess string.'

# WTF-Flask Settings
WTF_CSRF_ENABLED = True

# SQLAlchemy Settings
SQLALCHEMY_DATABASE_URI = 'mysql://root:administrator@localhost/weather_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')  # currently unused
SQLALCHEMY_RECORD_QUERIES = True

# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 1.0
