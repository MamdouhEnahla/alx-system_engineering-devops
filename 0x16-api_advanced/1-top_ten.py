#!/usr/bin/python3

"""Gets top 10 most hot posts of a subreddit using reddit api."""
import requests


def top_ten(subreddit):
    """Gets top 10 most hot posts of a subreddit using reddit api."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Reddit Post Fetcher"}
    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        return None
