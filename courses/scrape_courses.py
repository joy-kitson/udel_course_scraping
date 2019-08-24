#!/usr/bin/python2

import urllib2 as url2
from bs4 import BeautifulSoup
from pprint import pprint
import sys
import re

PAGE_NAME = sys.argv[1:]
#'https://udapps.nss.udel.edu/CoursesSearch/search-results?term=2188&search_type=A&course_sec=CISC&session=All&course_title=&instr_name=&text_info=All&instrtn_mode=All&time_start_hh=&time_start_ampm=&credit=Any&keyword=&subj_area_code=&college='
#'http://catalog.udel.edu/content.php?filter%5B27%5D=CISC&filter%5B29%5D=&filter%5Bcourse_type%5D=-1&filter%5Bkeyword%5D=&filter%5B32%5D=1&filter%5Bcpage%5D=1&cur_cat_oid=18&expand=&navoid=1251&search_database=Filter#acalog_template_course_filter'

TIME_REGEX = r'([0-9]+:[0-9]+[A,P]M)\s*-\s*([0-9]+:[0-9]+[A,P]M)' 

def write_courses_to_csv(page_url, csv_name='courses.csv'):
    #load html
    page = url2.urlopen(page_url)

    #and parse it
    soup = BeautifulSoup(page, 'html.parser')

    #get andprint the page's title
    title_box = soup.find('title')
    print('Page Title: {}'.format(title_box.text))

    #get the table of clases
    table_box = soup.find('table', attrs={'id':'results-2198'})

    #extract the rows
    rows = table_box.find_all('tr')

    #and write data to csv
    with open(csv_name, 'a+') as csv:
        for row in rows:
            #get all of the data from the row...
            row_data = row.find_all('td')
            
            #filter out unneeded rows
            #row_data = filter(row_data )
            
            #...and write it to csv
            for i in range(len(row_data)):
                datum = row_data[i]

                #only include lectures
                if i == 0 and 'LEC' not in datum.text:
                    break
                
                text = datum.text.strip()
               
                #only keep the first line of text
                text = text.split('\n')[0]

                match = re.match(TIME_REGEX, text)
                if match:
                    for t in match.groups():
                        csv.write(u'"{}",'.format(t).encode('utf8'))
                else:
                    csv.write(u'"{}",'.format(text).encode('utf8'))

                if i == len(row_data) - 1:
                    csv.write(u'\n'.encode('utf8'))

def main():
    for url in sys.argv[1:]:
        write_courses_to_csv(url)

if __name__ == '__main__':
    main()
