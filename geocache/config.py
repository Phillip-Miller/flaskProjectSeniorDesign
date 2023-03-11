# config.py

import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import logging

# # do I make this a factory right here?
# basedir = pathlib.Path(__file__).parent.resolve()
# connex_app = connexion.App(__name__, specification_dir=basedir)
#
# app = connex_app.app  # flask instance!
# app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'geo.db'}"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
# db = SQLAlchemy(app)
# ma = Marshmallow(app)
# app.logger.setLevel(logging.INFO)
