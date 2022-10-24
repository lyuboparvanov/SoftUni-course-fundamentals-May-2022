key = int(input())
n = int(input())
word = ''
for _ in range(n):
    current_letter = input()
    word += chr(ord(current_letter)+ key)
print(word)