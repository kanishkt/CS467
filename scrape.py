import requests as req
from bs4 import BeautifulSoup
import operator
import json

#TODO: change query and time to accept input

def RedditData():
    query = 'sports'
    page = req.get("http://redditlist.com/search?adultfilter=0&searchterm=" + query, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(page.text, "html.parser")

    subreddits = dict()
    count = 20

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

    subreddits = sorted(subreddits.items(), key=operator.itemgetter(1))
    subreddits = [s[0] for s in subreddits][:10]
    top_posts = list()
    for subreddit in subreddits:
        time = 'day'
        page = req.get("https://www.reddit.com/r/" + subreddit + "/top/?sort=top&t=" + time, headers = {'User-agent': 'your bot 0.1'})
        soup = BeautifulSoup(page.text, "html.parser")

        count = 5

        table = soup.find(id='siteTable')
        posts = table.find_all(attrs={'data-subreddit': subreddit})
        for post in posts:
            if count > 0:
                points = post.find('div', class_='score unvoted').text
                if points == u'\u2022':
                    continue
                points = int(points)
                title = str(post.find('p', class_='title').find('a').text)

                tagline = post.find('p', class_='tagline')
                datetime = tagline.find('time').get('datetime')
                user = str(tagline.find('a').text)

                comment_link = post.find('li', class_='first').find('a')
                url = str(comment_link.get('href'))
                comment = str(comment_link.text)
                if comment == "comment":
                    num_comments = 0
                else:
                    if ' comments' in comment:
                        num_comments = comment.replace(' comments', '')
                    else:
                        num_comments = comment.replace(' comment', '')
                    num_comments = int(num_comments)

                top_posts.append({'url': url, 'subreddit':subreddit, 'title': title, 'user': user, 'datetime': datetime, 'comments': num_comments, 'points': points})
                count -= 1

    data_str = json.dumps(top_posts)
    print data_str

