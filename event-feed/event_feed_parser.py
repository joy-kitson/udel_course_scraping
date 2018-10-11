#!/usr/bin/python3

#built based off of tutorial found at:
#https://fedoramagazine.org/never-miss-magazines-article-build-rss-notification-system/

import sqlite3 as sqlite
import smtplib
from email.mime.text import MIMEText

import feedparser
from Database import Database

TABLE_NAME = 'calendar'
DB_PATH = '/var/tmp/{}_rss.sqlite'.format(TABLE_NAME)
RSS_URL = 'https://fedoramagazine.org/feed/'
#RSS_URL = 'https://events.udel.edu/calendar?event_types[]=8140/.rss'

def main():
  database = Database(TABLE_NAME, DB_PATH)
  database.read_rss_feed(RSS_URL)
  database.close_connection()

if __name__ == '__main__':
  main()
