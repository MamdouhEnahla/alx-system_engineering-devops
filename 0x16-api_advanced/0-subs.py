#!/usr/bin/python3

"""returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Reddit Subscriber Fetcher'}
    res = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if res.status_code == 200:
        return res.json()['data']['subscribers']
    else:
        return 0
