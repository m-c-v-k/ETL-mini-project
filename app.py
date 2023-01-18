#! python3

# Importing necessary libraries
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello Flask!"
