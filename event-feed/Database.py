import sqlite3 as sqlite
import feedparser

class Database:
  def __init__(self, table_name, connection_path):
    self.table_name = table_name
    self.open_connection(connection_path)
    self.create_table()

  def open_connection(self, path):
    self.database_connection = sqlite.connect(path)
    self.database = self.database_connection.cursor()

  def close_connection(self):
    self.database_connection.close()

  def create_table(self):
    self.database.execute(\
      'CREATE TABLE IF NOT EXISTS {} (title TITLE, date DATE)'\
      .format(self.table_name))

  def read_rss_feed(self, url):
    feed = feedparser.parse(url)

    for event in feed['entries']:
      title, date = event['title'], event['published']
      if (title, date) not in self:
        self.add_event(title, date)
      print(title, date)

  #expects (title, date) pair for item
  def __contains__(self, event):
    #select matching events
    self.database.execute(\
      'SELECT * from {} WHERE title=? AND date=?'\
      .format(self.table_name),\
      event)
    
    #check whether or not we found anything
    return bool(self.database.fetchall())

  def add_event(self, title, date):
    self.database.execute(\
      'INSERT INTO {} VALUES (?,?)'\
      .format(self.table_name),\
      (title, date))
    self.database_connection.commit()
    
