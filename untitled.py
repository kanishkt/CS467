import flask
from flask import Flask
import scrape as t
import json
import numpy as np
import requests as req
from bs4 import BeautifulSoup

app = Flask(__name__)

query = 'sports'
page = req.get("https://www.reddit.com/subreddits/search?q=" + query, headers = {'User-agent': 'your bot 0.1'})
soup = BeautifulSoup(page.text, "html.parser")


@app.route('/')
def hello_world():
    data = t.RedditData()
    return flask.render_template("index.html", data=data)

@app.route("/data")
@app.route("/data/<int:ndata>")
def data(ndata=100):
    """
    On request, this returns a list of ``ndata`` randomly made data points.
    :param ndata: (optional)
        The number of data points to return.
    :returns data:
        A JSON string of ``ndata`` data points.
    """
    x = 10 * np.random.rand(ndata) - 5
    y = 0.5 * x + 0.5 * np.random.randn(ndata)
    A = 10. ** np.random.rand(ndata)
    c = np.random.rand(ndata)
    return json.dumps([{"_id": i, "x": x[i], "y": y[i], "area": A[i],
        "color": c[i]}
        for i in range(ndata)])

if __name__ == '__main__':
    app.run()
