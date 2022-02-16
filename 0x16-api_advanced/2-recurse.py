#!/usr/bin/python3
'''
function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
'''
import requests


def recurse(subreddit, hot_list=[], after="None"):
    '''
     recursive function that queries the Reddit API and returns a
     list containing the titles of all hot articles for a given subreddit
    '''

    if after:
        url = ("https://www.reddit.com/r/{}/hot.json".format(subreddit))

    url = ("https://www.reddit.com/r/{}/hot.json?after={}".
           format(subreddit, after))
    user_agent = {'User-Agent': 'My User Agent Custom'}
    response = requests.get(url, headers=user_agent).json()
    get_children = response.get('data').get('children')
    get_after = response.get('data', {}).get('after')
    if response.get('error') == 404:
        return None
    else:
        for post in get_children:
            hot_list.append(post.get('data').get('title'))
        if not get_after:
            return hot_list
        return recurse(subreddit, hot_list, after)
