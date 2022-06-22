from flask import Flask, render_template

App = Flask(__name__)

@App.route("/")
@App.route("/index")
def index():
    return render_template("index.html")