"""Flask configuration."""
import json
import os
import pathlib
from os import environ, path
from dotenv import load_dotenv
from connexion.exceptions import OAuthProblem

basedir = pathlib.Path(__file__).parent.resolve()
load_dotenv(path.join(basedir, '.env'))

KEY_DB = json.loads(environ.get('API_KEY_DICT'))


class Config:
    """Base config."""

    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'geocache', 'geo.db')}"  # Windows slashes can be weird
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    FLASK_ENV = 'production'
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.getenv('SECRET_KEY')

    ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
    CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

    # Configure Postgres database based on connection string of the libpq Keyword/Value form
    # https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
    try:
        conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
        conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

        DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
            dbuser=conn_str_params['user'],
            dbpass=conn_str_params['password'],
            dbhost=conn_str_params['host'],
            dbname=conn_str_params['dbname']
        )
        DEBUG = False
        TESTING = False
        SQLALCHEMY_DATABASE_URI = DATABASE_URI
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    except KeyError:
        print("not in production env")
    print(SQLALCHEMY_DATABASE_URI)


class Testing(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'tests', 'test.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def apikey_auth(token, required_scopes):
    info = KEY_DB.get(token, None)
    print(token, info)
    if not info:
        raise OAuthProblem("Invalid token")

    return info
