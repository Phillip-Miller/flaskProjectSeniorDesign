import os

from connexion.resolver import RelativeResolver
import pathlib
import connexion
import logging


# @FIXME not sure how to pass in values here so using env variable instead
def create_app(config="config.Config"):
    """
    Acceptable Values:

    "config.Config"
    "config.ProdConfig"
    "config.DevConfig"
    """
    env_value = os.environ.get('FLASK_CONFIG')
    if env_value is not None:
        config = env_value
    basedir = pathlib.Path(__file__).parent.resolve()
    connex_app = connexion.FlaskApp(__name__, specification_dir=basedir)
    connex_app.add_api('swagger.yml', resolver=RelativeResolver('geocache'))
    app = connex_app.app  # flask instance!
    app.config.from_object(config)
    app.logger.setLevel(logging.INFO)

    from geocache.models import db
    db.init_app(app)

    with app.app_context():
        if config == "config.ProdConfig":
            db.session.commit()
            db.drop_all()
        db.create_all()  # does not overwrite so can use each time

    @app.route("/")
    def home():
        return ("Nice job on your first quest -- UG Team")

    return app
