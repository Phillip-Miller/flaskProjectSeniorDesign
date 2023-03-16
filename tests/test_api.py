# these all mess with the database need to somehow create a temp database when using these + clean database after
def test_location_api_status(client):
    api_get = client.get("/api/location")
    assert api_get.status == "200 OK"

    data = {"cachename": "myCache"}
    api_post_incomplete_object = client.post("/api/location", json=data)
    assert api_post_incomplete_object.status == "400 BAD REQUEST"

    data = {"cachename": "myCache", "difficulty": 4, "latitude": 3, "longitude": 43}
    api_post_complete_object = client.post("/api/location", json=data)
    assert api_post_complete_object.status == "201 CREATED"


def test_user_api_status(client):
    api_get = client.get("/api/user")
    assert api_get.status == "200 OK"

    data = {"undefined_key_value": "myUser"}
    api_post_incomplete_object = client.post("/api/user", json=data)
    assert api_post_incomplete_object.status == "400 BAD REQUEST"

    data = {"username": "myUser"}
    api_post_complete_object = client.post("/api/user", json=data)
    assert api_post_complete_object.status == "201 CREATED"
