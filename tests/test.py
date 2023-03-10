import random

import requests
import pytest
import math

BASE = "http://127.0.0.1:5000/"
global_user = "user3"


def test_put_user_data():
    user3 = {"visited_locations": ["UC's"], "friends": ["user4"]}
    response = requests.put(BASE + "UserData/user3", user3)
    assert (response.status_code == 200)


#     not finished put on puts can attach a dictionary to pass as well outside of url params


def test_get_user_data():
    friendDataStructure = {"user0": [["Immaculata"], ["user1"]], "user1": [["Saints"], ["user0", "user4"]],
                           "user2": [["UC's"], ["user4"]], "user3": [["BEC"], []],
                           "user4": [["SLP"], ["user1", "user2"]]}
    response = requests.get(BASE + "UserData/" + global_user)
    assert (response.json() == friendDataStructure[global_user])


# change for production env
if __name__ == '__main__':
    response = requests.put(BASE + "UserData/user3", json={"score": "5"})
    print(f"{response.json()}")
