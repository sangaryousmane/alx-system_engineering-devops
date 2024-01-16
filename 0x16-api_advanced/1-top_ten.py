#!/usr/bin/python3
""" queries the Reddit API and prints the titles-
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ Queries the Reddit API and prints the titles-
    of the first 10 hot posts listed for a given subreddit
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False,
                                params={"limit": 10})

        if response.status_code == 404:
            print("None")
            return
        data = response.json().get("data")    
        [print(title.get("data").get("title")) for title in data.get("children")]
    except Exception as e:
        print(f'Error: {e}')
