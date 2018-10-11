#!/usr/bin/python

import sys
import re

def is_lecture(course_row):
    try:
        course_id = course_row.split(',')[0].replace('\n','')
        return 'LEC' in course_id
    except:
        return False

def not_after_course(course_row, number=220):
    try:
        course_id = course_row.split(',')[0].replace('\n','')
        course_num = int(course_id[5:7])
        print(course_num)
        return course_num <= 220
    except:
        False

def filter_csv(in_filename, out_filename, include):
    with open(in_filename, 'r') as in_file:
        with open(out_filename, 'w') as out_file:
            for line in in_file:
                print(line)
                if include(line):
                    out_file.write(line)

def main():
    #parse commandline args
    in_csv_filename = sys.argv[1]
    out_csv_filename = 'filtered_' + in_csv_filename
    if len(sys.argv) > 2:
        out_csv_filename = sys.argv[2]

    filter_csv(in_csv_filename, out_csv_filename, \
        is_lecture)
        #lambda row: is_lecture(row) and not_after_course(row))

if __name__ == '__main__':
    main()
