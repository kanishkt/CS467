import operator

import datetime
import requests as req
import praw
from bs4 import BeautifulSoup

query = 'sports'
page = req.get("http://redditlist.com/search?adultfilter=0&searchterm=" + query, headers={'User-agent': 'your bot 0.1'})
soup = BeautifulSoup(page.text, "html.parser")

subreddits = dict()
count = 20

listings = soup.find_all('div', class_='full-page-listing-item')


def RedditData():
    subreddits = dict()
    count = 20
    r = praw.Reddit(user_agent='my_cool_application')

    listings = soup.find_all('div', class_='full-page-listing-item')
    for listing in listings:
        if count > 0:
            slug = listing.find(class_='result-item-slug')
            link = slug.find('a')
            subreddit = str(link.text.replace('/r/', ''))

            ranks = listing.find_all(class_='rank-item')
            rank = ranks[1]
            subrank = rank.find(class_='rank-item-value').text

            subreddits[subreddit] = int(subrank)
            count -= 1

        else:
            break

    print subreddits
    subreddits = sorted(subreddits.items(), key=operator.itemgetter(1))
    subreddits = [s[0] for s in subreddits][:10]

    for i in subreddits:
        print i
        submissions = r.get_subreddit(i).get_hot(limit=5)
        for j in list(submissions):
            print j.title
        print 'DONE'


def get_date(submission):
    time = submission.created
    return datetime.datetime.fromtimestamp(time)
