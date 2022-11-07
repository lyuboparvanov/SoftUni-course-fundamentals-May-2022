import re

sentence = input().lower()
word = input().lower()

pattern = rf"{word}\b"

result = re.findall(pattern, sentence)

print(len(result))