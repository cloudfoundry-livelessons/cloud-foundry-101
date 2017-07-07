import os
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hi!"

PORT = os.environ.get('PORT', 8080)
HOST = "0.0.0.0"
app.run(HOST, PORT)