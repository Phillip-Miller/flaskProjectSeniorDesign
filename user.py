from datetime import datetime
from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


PEOPLE = {
    "Fairy": {
        "score": 4,
        "username": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "score": 3,
        "username": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "score": 3,
        "username": "Bunny",
        "timestamp": get_timestamp(),
    }
}


def create(User):
    username = User.get("username")
    score = User.get("score", 0)

    if username and username not in PEOPLE:
        PEOPLE[username] = {
            "username": username,
            "score": score,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[username], 201
    else:
        abort(
            406,
            f"Person with last name {username} already exists",
        )


def read_all():
    return list(PEOPLE.values())


def read_one(username):
    if username in PEOPLE:
        return PEOPLE[username]
    else:
        abort(
            404, f"Person with last name {username} not found"
        )


def update(username, user):
    if username in PEOPLE:
        PEOPLE[username]["score"] = user.get("score", PEOPLE[username]["score"])
        PEOPLE[username]["timestamp"] = get_timestamp()
        return PEOPLE[username]
    else:
        abort(
            404,
            f"Person with last name {username} not found"
        )


def delete(username):
    if username in PEOPLE:
        del PEOPLE[username]
        return make_response(
            f"{username} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {username} not found"
        )
