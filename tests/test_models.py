from geocache import models


def test_new_location():
    # database inits id and timestamp not model
    location = models.CacheLocation(cachename="test_cache", longitude=-179, latitude=89.954, hints="try this",
                                    trivia="Founded 1808", difficulty=10, radius=5)
    assert location.cachename == "test_cache"


def test_new_user():
    user_with_score = models.User(username="schmeichel", score=10)
    assert user_with_score.score == 10
