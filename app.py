from flask import Flask

app = Flask(__name__)
app = Flask(__name__)

#TODO E Wrtie Cache Object Array and API

#TODO P Write friends API and Data Structure
@app.route("/")
def hello_world():
    return "<p>hello world</p>"