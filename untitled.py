import flask
from flask import Flask
import scrape as t
import json
import numpy as np
import requests as req
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = t.RedditData("sports")
    return flask.render_template("index.html", data=data)

@app.route("/tv")
def getTV():
    data = t.RedditData("tv")
    return flask.render_template("index.html", data=data)

@app.route("/fashion")
def getFashion():
    data = t.RedditData("fashion")
    return flask.render_template("index.html", data=data)

@app.route("/movies")
def getMovies():
    data = t.RedditData("movies")
    return flask.render_template("index.html", data=data)

@app.route("/games")
def getGames():
    data = t.RedditData("games")
    return flask.render_template("index.html", data=data)

@app.route("/politics")
def getPolitics():
    data = t.RedditData("politics")
    return flask.render_template("index.html", data=data)



if __name__ == '__main__':
    app.run()
