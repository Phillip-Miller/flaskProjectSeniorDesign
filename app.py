from flask import request, jsonify, render_template
import config
import os
from models import User,Cachelocations
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
    # db.session.add(User('admin', 'admin@example.com'))
    # db.session.add(User('guest', 'guest@example.com'))
    # db.session.commit()
    #
    # users = User.query.all()
    # print(users)


@app.route("/")
def home():
    users = User.query.all()
    locations = Cachelocations.query.all()
    return render_template("home.html", locations=locations, users=users)



# change for production env
if __name__ == '__main__':
    # default port 5000 can clash with mac airplay
    app.run(host="0.0.0.0", port=8000, debug=True)
