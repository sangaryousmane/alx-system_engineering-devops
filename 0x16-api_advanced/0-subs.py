#!/usr/bin/python3
""" This script queries the Reddit API and -
returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ Number of subscribers from Reddit API
    """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            subscribers = data.get("data")
            return subscribers.get("subscribers")
        else:
            return 0
    except Exception as e:
        print(f'Error: {e}')
