import os

from connexion.resolver import RelativeResolver
import pathlib
import connexion
import logging
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def create_app(config="config.Config"):
    """
    Acceptable Values:

    "config.ProdConfig"
    "config.DevConfig"
    """
    basedir = pathlib.Path(__file__).parent.resolve()
    connex_app = connexion.FlaskApp(__name__, specification_dir=basedir)
    connex_app.add_api('swagger.yml', resolver=RelativeResolver('geocache'))
    app = connex_app.app  # flask instance!
    app.config.from_object(config)
    # app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'geo.db')}"
    app.logger.setLevel(logging.INFO)

    migrate = Migrate(app, SQLAlchemy())
    from geocache.models import db
    db.init_app(app)

    with app.app_context():
        db.create_all()  # does not overwrite so can use each time

    @app.route("/")
    def home():
        return ("HelloWorld")

    return app


# change for production env
if __name__ == '__main__':
    # default port 5000 can clash with mac airplay
    my_app = create_app()
    my_app.run(host="0.0.0.0", port=8000, debug=True)
