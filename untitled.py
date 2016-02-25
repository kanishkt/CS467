import flask
from flask import Flask
import scrape as t

app = Flask(__name__)


@app.route('/')
def index():
    data = t.RedditData("Sports", "year")
    return flask.render_template("index.html", data=data, query="Sports", time="year")

@app.route('/<query>/<time>')
def getVis(query, time="year"):
    data = t.RedditData(query=query, time=time)
    return flask.render_template("index.html", data=data, query=query, time=time)

if __name__ == '__main__':
    app.run()
