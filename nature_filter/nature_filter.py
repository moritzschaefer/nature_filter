"""Main module.

"""

# import xml.etree.ElementTree as ET

import requests

from .feedbridge import Bridge

NATURE_RSS_URL = 'https://www.nature.com/nature.rss'

def nature_filter():
    '''
    Might need to be done recursively
    '''

    # root = ET.fromstring(requests.get(NATURE_RSS_URL).content)
    feed = Bridge(requests.get(NATURE_RSS_URL).content)

    feed.parsed.entries = [e for e in feed.parsed.entries if '/articles/s' in e.link]
    return feed.build_rss_str()

    # for child in root:
    #     if child.keys()[0].endswith('about'):
    #         print(child.items()[0][-1])
    #         if '/articles/d' in child.items()[0][-1]:
    #             print('removed')
    #             root.remove(child)
    # return ET.tostring(root, encoding='utf8', method='xml')
