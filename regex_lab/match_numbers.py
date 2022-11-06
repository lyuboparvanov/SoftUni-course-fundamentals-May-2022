import re


pattern = r"(^|(?<=\s))-?(0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
data = input()

search_pattern = re.finditer(pattern, data)

for match in search_pattern:
    print(match.group(), end=' ')