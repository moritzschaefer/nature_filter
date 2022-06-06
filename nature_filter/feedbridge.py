#!/usr/bin/env python
# Connects feedparser to feedgen allowing round-trip creation
# and parsing of RSS and Atom feeds.
# from https://github.com/leonardr/botfriend/blob/6157a873c4158ccfdda4bf021059bddf14217654/botfriend/feedbridge.py

import datetime
import pdb
import sys

import dateutil
import feedparser
from feedgen.feed import FeedGenerator


class Bridge(object):

    NO_VALUE = object()

    def __init__(self, feed):

        self.raw = feed
        self.parsed = feedparser.parse(self.raw)
        self.feed = FeedGenerator()

    def build_rss_str(self):
        self._build_feed()
        self._build_entries()
        return self.feed.rss_str(pretty=True)  # atom would require to manually sed feed.id, otherwise atom fails

    def _build_feed(self):
        f = self.parsed.feed

        for field in [
                'id', 'title', 'subtitle', 'updated', 'rights', 'generator',
                'docs', 'language', ('xml_lang', 'language'),
                ('authors', 'author'), ('links', 'link')
        ]:
            self._copy(f, self.feed, field)

        if f.get('image'):
            image_kwargs = {}
            for image_field in 'url', 'title', 'link', 'width', 'height', 'description':
                ignore, value = self._setter(f.image, self.feed, image_field)
                if value is not self.NO_VALUE:
                    image_kwargs[image_field] = value

            if image_kwargs:
                self.feed.image(**image_kwargs)

    def _build_entries(self):
        for entry in self.parsed.entries:
            self._build_entry(entry)


    def _build_entry(self, parsed):
        built = self.feed.add_entry(order='append')

        # TODO: 'tag' is not supported in feedgen
        for field in [
            'id', 'title', 'updated', 'summary', 'published',
            ('links', 'link')
        ]:
            self._copy(parsed, built, field)

        permalink = parsed.get('link')
        if permalink:
            built.guid(permalink, False)

    def _setter(self, feedparser_obj, feedgen_obj, field):
        if isinstance(field, tuple):
            field, method_name = field
        else:
            method_name = field
        setter = getattr(feedgen_obj, method_name, None)
        value = feedparser_obj.get(field, self.NO_VALUE)
        return setter, value

    def _copy(self, feedparser_obj, feedgen_obj, field):
        setter, value = self._setter(feedparser_obj, feedgen_obj, field)
        if value is self.NO_VALUE:
            return
        if not isinstance(value, list):
            value = [value]
        for v in value:
            if field == 'updated':
                v = dateutil.parser.parse(v)
                v = v.replace(tzinfo=datetime.timezone.utc)
                v.tzinfo
            setter(v)
        if field in feedparser_obj: # Temporary cleanup
            del feedparser_obj[field]
