#!/usr/bin/python3
""" contains top_ten function """

import requests

def top_ten(subreddit):
    """function that Displays the titles of the first 10 hot posts listed
    for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "RedditTestApi/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    for item in results.get("children", []):
        print(item.get("data", {}).get("title"))

