import requests as req
from bs4 import BeautifulSoup
import operator
import json


def RedditData():
    query = 'tv'
    time = 'year'

    page = req.get("http://redditlist.com/search?adultfilter=0&searchterm=" + query, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(page.text, "html.parser")

    subreddit_posts = list()

    subreddits = dict()
    subreddit_count = 20

    listings = soup.find_all('div', class_='full-page-listing-item')
    for listing in listings:
        if subreddit_count > 0:
            slug = listing.find(class_='result-item-slug')
            link = slug.find('a')
            subreddit = str(link.text.replace('/r/', ''))

            ranks = listing.find_all(class_='rank-item')
            rank = ranks[1]
            subrank = rank.find(class_='rank-item-value').text

            subreddits[subreddit] = int(subrank)
            subreddit_count -= 1

        else:
            break

    subreddits = sorted(subreddits.items(), key=operator.itemgetter(1))
    subreddits = [s[0] for s in subreddits][:10]

    for subreddit in subreddits:
        page = req.get("https://www.reddit.com/r/" + subreddit + "/top/?sort=top&t=" + time, headers = {'User-agent': 'your bot 0.1'})
        soup = BeautifulSoup(page.text, "html.parser")

        post_count = int(100/len(subreddits))

        table = soup.find(id='siteTable')
        posts = table.find_all(attrs={'data-subreddit': subreddit})
        for post in posts:
            if post_count > 0:
                points = post.find('div', class_='score unvoted').text
                if points == u'\u2022':
                    continue
                points = int(points)

                title = post.find('p', class_='title').find('a').text.encode('utf-8')

                tagline = post.find('p', class_='tagline')
                datetime = tagline.find('time').get('datetime')
                datetime = datetime.replace('T', ' ')
                datetime = datetime.replace('+00:00', '')

                comment_link = post.find('li', class_='first').find('a')
                url = comment_link.get('href').encode('utf-8')
                comment = str(comment_link.text)
                if comment == "comment":
                    num_comments = 0
                else:
                    if ' comments' in comment:
                        num_comments = comment.replace(' comments', '')
                    else:
                        num_comments = comment.replace(' comment', '')
                    num_comments = int(num_comments)

                subreddit_posts.append({"subreddit": "r/"+subreddit, "url": url, "title": title, "datetime": datetime, "comments": num_comments, "points": points})
                post_count -= 1

    data_str = json.dumps(subreddit_posts)
    return data_str

