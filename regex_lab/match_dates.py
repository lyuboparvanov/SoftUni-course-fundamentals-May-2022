import re

data = input()

pattern = r"(\d{2})([/.-])([A-Z][a-z]+)\2(\d{4})\b"

search_pattern = re.findall(pattern, data)

for match in search_pattern:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
