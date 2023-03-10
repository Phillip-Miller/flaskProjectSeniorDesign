from flask import request, jsonify, render_template
import config
import os
from models import User, CacheLocation
from config import db, app

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

with app.app.app_context():
    db_active = False
    for file in os.listdir(os.getcwd()):
        if file.endswith(".db"):
            db_active = True
    if not db_active:
        app.app.logger.info("Making new db")
        config.db.create_all()


@app.route("/")
def home():
    users = User.query.all()
    locations = CacheLocation.query.all()
    return render_template("home.html", locations=locations, users=users)


# change for production env
if __name__ == '__main__':
    # default port 5000 can clash with mac airplay
    app.run(host="0.0.0.0", port=8000, debug=True)
