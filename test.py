import requests
import pytest

BASE = "http://127.0.0.1:5000/"


def test_get_user_data():
    expected = friendDataStructure = {"user0": [["Immaculata"], ["user1"]], "user1": [["Saints"], ["user0", "user4"]],
                                      "user2": [["UC's"], ["user4"]], "user3": [["BEC"], []],
                                      "user4": [["SLP"], ["user1", "user2"]]}
    response = requests.get(BASE + "UserData")
    assert (response.json() == expected)
