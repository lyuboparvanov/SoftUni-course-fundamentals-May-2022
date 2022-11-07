import re

while True:
    data = input()
    if data:

        pattern = r"www\.[A-Za-z0-9\-]+\.[a-z\.]+\b"
        result = re.findall(pattern, data)
        if result:
            print(''.join(result))
    else:
        break

