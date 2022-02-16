#!/usr/bin/python3
'''
function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
'''

import requests
import json


def top_ten(subreddit):
    '''
    function that queries the Reddit API
    and prints the titles of the first 10 hot posts
    '''
    url = ("https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit))
    user_agent = {'User-Agent': 'My User Agent Custom'}
    response = requests.get(url, headers=user_agent).json()
    if response.get('error') == 400:
        print ('None')
    else:
        for post in response.get('data').get('children'):
            print(post.get('data').get('title'))
