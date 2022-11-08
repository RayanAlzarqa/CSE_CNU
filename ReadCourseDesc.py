from pdfminer.high_level import extract_text
import re
import os
from csv import reader
from selenium import webdriver
import time
import pandas as pd
from phantomjs import *
import requests  # the lib that handles the url stuff
from bs4 import BeautifulSoup
directory = 'Pdf'


cleaned_tuple = [()]

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
    for index in range(len(list_of_tuples)):
        if index > 0:
            url = f"https://navigator.cnu.edu/StudentScheduleofClasses/socadditional.aspx?term_code=202310&crn={list_of_tuples[index]} "
            driver = webdriver.Firefox()
            driver.get(url)
            time.sleep(5)
            result = driver.find_element('FormView1_COURSE_DESCLabel')
            print(result.text)
        #print()
        #your_data = list()

        #for line in soup.findAll('span', attrs={'id': 'FormView1_COURSE_DESCLabel'}):
        #    your_data.append(line.text)
        #    print(line.text)

            cleaned_tuple.append((course_tuple[3], "Spring23", course_tuple[0], course_tuple[2], "Placeholder Desc",
                                course_tuple[1], course_tuple[10]))

    for course_tuple in cleaned_tuple:
        print(course_tuple)

