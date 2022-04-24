from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/counter")
def cow():
    return render_template("counter.html", title="Counter")

