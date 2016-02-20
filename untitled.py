from flask import Flask
import scrape as t
import requests as req
from bs4 import BeautifulSoup

app = Flask(__name__)

query = 'sports'
page = req.get("https://www.reddit.com/subreddits/search?q=" + query, headers = {'User-agent': 'your bot 0.1'})
soup = BeautifulSoup(page.text, "html.parser")


@app.route('/')
def hello_world():
    t.RedditData()
    return "hello"

if __name__ == '__main__':
    app.run()
