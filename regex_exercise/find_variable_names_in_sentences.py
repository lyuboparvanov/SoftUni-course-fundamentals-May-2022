import re

pattern = r"\b\_([A-Za-z0-9]+\b)"

data = input()

result = re.findall(pattern, data)

print(','.join(result))