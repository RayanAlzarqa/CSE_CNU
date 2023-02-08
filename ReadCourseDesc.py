#import urllib3
#from pdfminer.high_level import extract_text
#import re
import os
from csv import reader
from selenium import webdriver
#import time

import requests  # the lib that handles the url stuff
from bs4 import BeautifulSoup
directory = 'Pdf'


cleaned_tuple = [()]

example = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    with open(f, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj) # ('CRN', 'Course', 'Section', 'Title', 'Hours', 'Area of LLC', 'Type', 'Days',
        # 'Time', 'Location', 'Instructor', 'Seats Still Available', 'STATUS', '')
        # Get all rows of csv from csv_reader object as list of tuples
        list_of_tuples = list(map(tuple, csv_reader))
        # display all rows of csv

    # Need it as "course_title","semester","courseID","section","course_desc","department","N.Sections","year",
    # "clean_course_desc"

    # Given as "CRN,Course,Section,Title,Hours,Area of LLC,Type,Days,Time,Location,Instructor,
    # Seats Still Available,STATUS"
    for course_tuple in list_of_tuples[1:]:
        try:
            url = f"https://navigator.cnu.edu/StudentScheduleofClasses/socadditional.aspx?term_code=202310&crn={int(course_tuple[0])} "
            #print(url + '\n')
            r = requests.get(url)
            #print(r)
            driver = webdriver.Firefox()
            driver.get(url)

            html = driver.page_source
            page = driver.execute_script('return document.body.innerHTML')

            soup = BeautifulSoup(''.join(page), 'html.parser')
            #soup = BeautifulSoup(r.content, 'html5lib')

            span = soup.find("span", id='FormView1_COURSE_DESCLabel')
            text = span.text

            driver.close()

            #your_data = list()
           # for line in soup.findAll('span', attrs={'id': 'FormView1_COURSE_DESCLabel'}):
            #    your_data.append(line.text)
            #    print(line.text)

            cleaned_tuple.append((course_tuple[3], "Spring23", course_tuple[0], course_tuple[2], text,
                                  course_tuple[1], course_tuple[10]))
            if example == 10:
                break
            example += 1
        except:
            print(f'couldn\'t read crn {course_tuple[0]} moving on to next one \n')
    for course_tuple in cleaned_tuple:
        print(course_tuple)

