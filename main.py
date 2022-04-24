# Import what we need from flask
from flask import Flask, render_template, redirect, url_for

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/count")
def counter():
    return render_template("counter.html", title="Counter")