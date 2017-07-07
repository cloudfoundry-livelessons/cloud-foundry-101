import os
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    JOKE = os.environ.get('JOKE', "No Joke.")
    return JOKE

PORT = os.environ.get('PORT', 8080)
HOST = "0.0.0.0"

app.run(HOST, PORT)
