from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


# TODO E Write Cache Object Array and API

def create_fake_user_data() -> dict:
    '''
    Create ssample fake user data using data structure defined in deliverables

    Usernames are user1,user2....
    User data structure {User : [[Caches], [Friends]]}
    completedCacheList = ["Immaculata", "Saints", "UC's", "BEC", "SLP"]
    friendsRelations = {1:[2], 2:[1,2], 3:[5], 4:[], 5:[3,2]}

    Useri has completed element i in completedCacheList and dict is
    indexed by user
    '''
    returnDict = {}

    completedCacheList = ["Immaculata", "Saints", "UC's", "BEC", "SLP"]
    friendsRelations = {0: ["user1"], 1: ["user0", "user4"], 2: ["user4"], 3: [], 4: ["user1", "user2"]}

    for userNumber in range(5):
        user_name = "user" + str(userNumber)
        returnDict[user_name] = [[completedCacheList[userNumber]], friendsRelations[userNumber]]
    return returnDict


friendDataStructure = create_fake_user_data()


class UserData(Resource):
    def get(self):
        return friendDataStructure


api.add_resource(UserData, "/UserData")  # configure url to acsess resource


@app.route("/")
def hello_world():
    return "<p>hello world</p>"


# change for production env
if __name__ == '__main__':
    app.run(debug=True)
