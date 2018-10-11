#!/usr/bin/python

import feedparser

url='https://events.udel.edu/calendar?event_types%5B%5D=8140'
rss='{}/.rss'.format(url)

data = feedparser.parse(rss)
