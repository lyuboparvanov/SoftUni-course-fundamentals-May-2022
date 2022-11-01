word = input()
word = int(word.replace('.', '')) + 1
word = str(word)

result = [num for num in word]
print('.'.join(result))

