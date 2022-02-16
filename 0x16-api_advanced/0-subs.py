#!/usr/bin/python3
'''
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
'''

import json
import requests


def number_of_subscribers(subreddit):
    '''
    function that queries the Reddit API and returns the number of subscribers
    '''
    url = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
    user_agent = {'User-Agent': 'My User Agent Custom'}
    response = requests.get(url, headers=user_agent).json()
    if response.get('error') == 404:
        return 0
    return response.get('data').get('subscribers')
