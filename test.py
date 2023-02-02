import requests
import pytest

BASE = "http://127.0.0.1:5000/"
response = requests.get(BASE + "UserData")
print(response);
