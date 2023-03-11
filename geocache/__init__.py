from flask import render_template
from models import User, CacheLocation
import pathlib
import connexion
import logging


def create_app(config_filename=None):
    basedir = pathlib.Path(__file__).parent.resolve()
    connex_app = connexion.App(__name__, specification_dir=basedir)
    app = connex_app.app  # flask instance!
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'geo.db'}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.logger.setLevel(logging.INFO)
    # app.add_api(basedir / "swagger.yml")
    connex_app.add_api('swagger.yml')

    from models import db
    db.init_app(app)

    # with app.app.app_context():
    #     db_active = False
    #     for file in os.listdir(config.basedir):  # refers to where file located not where its being run from
    #         if file.endswith(".db"):
    #             db_active = True
    #     if not db_active:
    #         app.app.logger.info("Making new db")
    #         config.db.create_all()

    @app.route("/")
    def home():
        users = User.query.all()
        locations = CacheLocation.query.all()
        return render_template("home.html", locations=locations, users=users)

    return app


# # change for production env
if __name__ == '__main__':
    # default port 5000 can clash with mac airplay
    my_app = create_app()
    my_app.run(host="0.0.0.0", port=8000, debug=True)
