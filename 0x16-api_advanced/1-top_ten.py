#!/usr/bin/python3
'''
function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
'''
import requests


def top_ten(subreddit):
    '''
    function that queries the Reddit API
    and prints the titles of the first 10 hot posts
    '''
    url = ("https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit))
    user_agent = {'User-Agent': 'My User Agent Custom'}
    response = requests.get(url, headers=user_agent).json()
    get_children = response.get('data', {}).get('children')
    if response.get('error') == 404:
        print(None)
    else:
        for post in get_children:
            print(post.get('data').get('title'))
