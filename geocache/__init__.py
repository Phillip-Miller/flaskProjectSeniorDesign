import os

from connexion.resolver import RelativeResolver
import pathlib
import connexion
import logging


def create_app(config_filename=None):
    basedir = pathlib.Path(__file__).parent.resolve()
    connex_app = connexion.FlaskApp(__name__, specification_dir=basedir)
    app = connex_app.app  # flask instance!
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'geo.db'}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.logger.setLevel(logging.INFO)
    
    connex_app.add_api('swagger.yml', resolver=RelativeResolver('geocache'))

    from geocache.models import db
    db.init_app(app)

    with app.app_context():
        db_active = False
        for file in os.listdir(basedir):  # basedir where init is located
            if file == "geo.db":
                db_active = True
        if not db_active:
            app.logger.info("Making new db")
            db.create_all()

    @app.route("/")
    def home():
        return ("HelloWorld")

    return app


# # change for production env
if __name__ == '__main__':
    # default port 5000 can clash with mac airplay
    my_app = create_app()
    my_app.run(host="0.0.0.0", port=8000, debug=True)
