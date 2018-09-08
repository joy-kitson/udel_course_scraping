#!/usr/bin/python

#based on tutorial from
#https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

import urllib2 as url2
from bs4 import BeautifulSoup as bs

#specify url
quote_page = 'http://www.bloomburg.com/quote/SPX:IND'
quote_page = \
'http://catalog.udel.edu/search_advanced.php?cur_cat_oid=18&ecpage=1&cpage=1&ppage=1&pcpage=1&spage=1&tpage=1&search_database=Search&filter%5Bkeyword%5D=CISC&filter%5B3%5D=1&filter%5B31%5D=1&filter%5B30%5D=1'

#load html
page = url2.urlopen(quote_page)

#parse the html
soup = bs(page, 'html.parser')

#get the <div > of name and get its value
name_box = soup.find('title')#, attrs={'class': 'name'})

#get the name...
name = name_box.text.strip()
print(name)

##...and the price
#price_box = soup.find('div', attrs={'class':'price'})
#price = price_box.text
#print(price)

