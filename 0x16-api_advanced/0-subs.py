#!/usr/bin/python3
""" contains a function that queries the Reddit API."""
import requests

def number_of_subscribers(subreddit):
    """function that returns the number of subscriber"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "RedditApiTest/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")

