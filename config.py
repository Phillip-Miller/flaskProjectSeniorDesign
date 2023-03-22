"""Flask configuration."""
import os
import pathlib
from os import environ, path
from dotenv import load_dotenv

basedir = pathlib.Path(__file__).parent.resolve()
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""

    SECRET_KEY = environ.get('SECRET_KEY')
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
