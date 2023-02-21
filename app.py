from flask_restful import Api, Resource
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys
from datetime import datetime

# eventually want to mock and insert dummy data instead of storing here
# need to figure out better logging methods
list_of_locations = {1: "Immaculata"}

friendDataStructure = {"user0": [["Immaculata"], ["user1"]], "user1": [["Saints"], ["user0", "user4"]],
                       "user2": [["UC's"], ["user4"]], "user3": [["BEC"], []], "user4": [["SLP"], ["user1", "user2"]]}

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # /// relative path  //// absl
db = SQLAlchemy(app)
db.init_app(app)


# Create Models for DB:
# linked list for data base
# location id int location string
class LocationModel(db.Model):
    id_hash = db.Column(db.String(80), primary_key=True)
    location_name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"Location(id: {self.id_hash}, location: {self.location_name})"
        # return '<location %r>' % self.locationName

    def __init__(self, location_name, id_hash):
        self.locationName = location_name
        self.id_hash = id_hash


class UserModel(db.Model):
    user = db.Column(db.String(80), unique=True, primary_key=True)
    score = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user: str, score: int):
        self.user = user
        self.score = score

    def __str__(self):  # return normal format
        return f"UserData(User: {self.user}, Score: {self.score}, Created: {self.date_created})"

    def __repr__(self):  # return dict format
        return str({"user": self.user, "score": {self.score}, "created": {str(self.date_created)}})


class Location(Resource):
    def get(self):
        return list_of_locations

    def put(self):
        data = request.get_json()
        print(data)
        loc = LocationModel(location_name=data['location_name'], id_hash=data['location_name'])
        db.session.add(loc)
        db.session.commit()
        return 201


api.add_resource(Location, '/list_of_locations')


class UserData(Resource):
    '''
    get(user_hash) returns user_data from db from api call: localhost/UserData/user3 for example
    post(user_hash) adds passed in json to api call: localhost/UserData/user3, {"score" : 100}

    request parsing libary so you can pass more in the functions?

    practicing with smaller dict of just {"score", "3"
    '''

    def get(self, user_hash):
        # TODO return query result
        result = UserModel.query.get(user=user_hash)
        return result

    def put(self, user_hash):
        data = request.json
        if db.session.query(UserModel.user).filter_by(user=user_hash).first() is not None:  # Already Exists
            # @FIXME implement a deep copy? or better way to update a row?
            user = UserModel.query.filter_by(user=user_hash).first()
            db.session.commit()
            return 200
            # log this> jsonify(repr(user))
        else:  # create new resource
            try:
                score = int(data["score"])
                new_user = UserModel(user=user_hash, score=score)
                db.session.add(new_user)
                db.session.commit()
                return 201
            except:
                return 500

    def delete(self, user_hash):
        pass
        # TODO


# adding <> indicates optional parameter one can pass + can add multiple
api.add_resource(UserData, "/UserData/<string:user_hash>")


@app.route("/")
def UniversityGeocache():
    return "<p>University Geocaching Homepage </p>"


# change for production env
if __name__ == '__main__':
    print("Running from main")
    db.create_all()
    app.run(debug=True)
