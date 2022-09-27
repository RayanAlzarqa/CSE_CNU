from pdfminer.high_level import extract_text
import re

references_to_whatever = 0

text = extract_text('CPSC420_Fall2022_McElfresh.pdf').split()

for word in text:
    word = word.lower()
    word = re.sub("[^a-zA-Z]+", "", word)
    if word.lower().find("disability") != -1 or word.lower().find("disabilities") != -1:
        references_to_whatever = references_to_whatever + 1


print(references_to_whatever)

