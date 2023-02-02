from flask import Flask
from flask_restful import Api, Resource

# eventually want to mock and insert dummy data instead of storing here
friendDataStructure = {"user0": [["Immaculata"], ["user1"]], "user1": [["Saints"], ["user0", "user4"]],
                       "user2": [["UC's"], ["user4"]], "user3": [["BEC"], []], "user4": [["SLP"], ["user1", "user2"]]}

app = Flask(__name__)
api = Api(app)


# TODO E Write Cache Object Array and API

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
