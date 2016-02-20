from flask import Flask
import praw

app = Flask(__name__)


@app.route('/')
def hello_world():
    r = praw.Reddit(user_agent='my_cool_application')
    submissions = r.get_subreddit('opensource').get_hot(limit=5)
    summary = [str(x) for x in submissions]
    searchQ = r.search('sports', subreddit=None, sort=None, syntax=None, period=None)
    for y in list(searchQ):
        print y.title
    return "hello"

if __name__ == '__main__':
    app.run()
