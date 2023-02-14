from flask import Flask
from flask_restful import Api, Resource
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# eventually want to mock and insert dummy data instead of storing here

list_of_locations = {1:"Immaculata"}


friendDataStructure = {"user0": [["Immaculata"], ["user1"]], "user1": [["Saints"], ["user0", "user4"]],
                       "user2": [["UC's"], ["user4"]], "user3": [["BEC"], []], "user4": [["SLP"], ["user1", "user2"]]}

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    locationName = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<location %r>' % self.locationName

@app.route('/list_of_locations', methods=['GET'])
def get_information():
    return list_of_locations

@app.route('/list_of_locations', methods=['POST'])
def set_location():
    data = request.get_json()
    print(data)
    loc = location(locationName=data['locationName'])
    db.session.add(loc)
    db.session.commit()
    return 'location created', 201



class UserData(Resource):
    def get(self):
        return friendDataStructure


api.add_resource(UserData, "/UserData")

@app.route("/")
def UniversityGeocache():
    return "<p>University Geocaching Homepage </p>"


# change for production env
if __name__ == '__main__':
    app.run(debug=True)

