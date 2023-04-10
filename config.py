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
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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
