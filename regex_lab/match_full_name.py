import re

data = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

search_pattern = re.findall(pattern, data)

print(' '.join(search_pattern))