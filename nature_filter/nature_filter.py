"""Main module.

"""

import xml.etree.ElementTree as ET

import requests

from .feedbridge import Bridge

NATURE_RSS_URL = 'http://feeds.nature.com/nature/rss/current'

def nature_filter_bridged():
    '''
    Might need to be done recursively, does not work unfortunately
    '''

    feed = Bridge(requests.get(NATURE_RSS_URL).content)

    feed.parsed.entries = [e for e in feed.parsed.entries if '/articles/s' in e.link]
    return feed.build_rss_str()

def nature_filter():
    '''
    Might need to be done recursively
    '''

    root = ET.fromstring(requests.get(NATURE_RSS_URL).content)

    # for node in root.iter():
    #     if some_condition_matches_parent:
    #         for child in list(node.iter()):
    #             if some_condition_matches_child:
    #                 node.remove(child)
    for i in range(100):
        for child in root.iter():
            try:
                attr_key = child.keys()[0]
                attr_item = child.items()[0]
            except IndexError:
                if child.tag.endswith('Seq'):
                    seq=child
                continue
            if attr_key.endswith('about'):
                # print(attr_item[-1])
                if '/articles/d' in attr_item[-1]:
                    # print('removed')
                    root.remove(child)
                    break
            if attr_key.endswith('resource'):
                # print(attr_item[-1])
                if '/articles/d' in attr_item[-1]:
                    # print('removed')
                    seq.remove(child)
                    break

            else:
                pass
                # print(child.tag)
    return ET.tostring(root) # , encoding='utf8', method='xml')
