import re

pattern = r'\d+'

while True:
    sentence = input()
    if sentence:
        searched_items = re.findall(pattern, sentence)
        if searched_items:
            print(' '.join(searched_items), end = ' ')
    else:
        break

