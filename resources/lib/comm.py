import requests
import random
import urllib
import config
import utils

from classes import MenuItem

def fetch_url(url):

    headers = {
        # Add more headers here as needed
        'User-Agent': config.USER_AGENT
    }

    res = requests.get(url, headers=headers).text
    res = res.encode('utf-8', 'ignore')
    return res

def get_videos(params):

    # Use this if you need to create pages
    page = int(params.get('page', 0))
    start = page * config.PAGE_SIZE
    end = start + config.PAGE_SIZE

    # Implement second level here, ex:
    # data = json.loads(fetch_url(config.VIDEOS_URL.format(params['category'])))

    listing = []

    for video in config.PUBLIC_TEST_VIDEOS[start:end]:

        menu_item = MenuItem(playable=True)
        menu_item.title = video['title']
        menu_item.url = video['source']
        menu_item.description = video['description']
        menu_item.thumb = video['thumb']
        menu_item.icon = video['thumb']

        listing.append(menu_item)

    return listing

def get_categories():
    # Implement first level here, ex:
    # data = json.loads(fetch_url(config.CATEGORIES_URL))

    listing = []

    for category in range(1, 9):

        menu_item = MenuItem()
        menu_item.title = 'Random videos %d' % category
        menu_item.description = 'Description for %s' % menu_item.title
        menu_item.icon = 'https://picsum.photos/300/200?r=%d' % random.randint(0, 10000)
        menu_item.thumb = menu_item.icon

        listing.append(menu_item)

    return listing
