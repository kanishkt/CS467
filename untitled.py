import flask
from flask import Flask
import scrape as t

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = t.RedditData("sports")
    return flask.render_template("index.html", data=data , title="Sports")


@app.route("/tv")
def getTV():
    data = t.RedditData("tv")
    return flask.render_template("index.html", data=data, title="TV")


@app.route("/fashion")
def getFashion():
    data = t.RedditData("fashion")
    return flask.render_template("index.html", data=data, title="Fashion" )


@app.route("/movies")
def getMovies():
    data = t.RedditData("movies")
    return flask.render_template("index.html", data=data, title="Movies")


@app.route("/games")
def getGames():
    data = t.RedditData("games")
    return flask.render_template("index.html", data=data, title="Games")


@app.route("/politics")
def getPolitics():
    data = t.RedditData("politics")
    return flask.render_template("index.html", data=data, title="Politics")


if __name__ == '__main__':
    app.run()
