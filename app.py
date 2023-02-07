from flask import Flask
from flask_restful import Api, Resource

# eventually want to mock and insert dummy data instead of storing here
list_of_locations = []

friendDataStructure = {"user0": [["Immaculata"], ["user1"]], "user1": [["Saints"], ["user0", "user4"]],
                       "user2": [["UC's"], ["user4"]], "user3": [["BEC"], []], "user4": [["SLP"], ["user1", "user2"]]}

app = Flask(__name__)
api = Api(app)

# TODO E Write Cache Object Array and API

class Location(object):
    def __init__(self,name):
        self.name = name
    # getter / setter
    def get_name(self):
        return self.name
    def set_Name(self, newName):
        if newName < 0:
            return
        self.name = newName
    def __str__(self):
        return str(self.name)

class Locations(object):
    def __init__(self, locations):
        self.locations = locations
    def delete(self, item):
        self.locations.remove(item)
    def __str__(self):
        x = []
        for Location in self.locations:
            x.append(str(Location))
        return str(x)

gym = Location("gym")
lib = Location("lib")
lab = Location("lab")

list_of_locations = Locations([gym, lib, lab])

#testing below
print(list_of_locations)
list_of_locations.delete(gym)
print(list_of_locations)

class UserData(Resource):
    def get(self):
        return friendDataStructure

api.add_resource(UserData, "/UserData")
api.add_resource(Location, "/CacheObjectLocations")


@app.route("/")
def UniversityGeocache():
    return "<p>University Geocaching Homepage </p>"


# change for production env
if __name__ == '__main__':
    app.run(debug=True)
