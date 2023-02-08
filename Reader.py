from pdfminer.high_level import extract_text
import re
import os

directory = 'Pdf'

class_and_ref = {}
# "course_title","semester","courseID","section","course_desc","department","N.Sections","year","clean_course_desc"
keyword_list = ["sustainability","sustainable","climate change","hunger"]

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if os.path.isfile(f):
        print(f)

    references_to_whatever = 0

    text = extract_text(f).split()

    for word in text:
        word = word.lower()
        word = re.sub("[^a-zA-Z] + ", "", word)
        for keyword in keyword_list:
            if word.lower().find(keyword) != -1 :  # climate change, environment, Race
                references_to_whatever = references_to_whatever + 1

    new_key = ""
    for i in range(2):
        new_key = new_key + re.sub("[^a-zA-Z0-9]+", "", text[i]) + " "

    class_and_ref[new_key] = references_to_whatever

print("Dictionary is:", class_and_ref)

for key in class_and_ref:
    if class_and_ref[key] > 0:
        print("Classes with a sustainability focus: ", key, "\n")
