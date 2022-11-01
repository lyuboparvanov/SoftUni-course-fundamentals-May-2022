vowels = ['a', 'o', 'u', 'e', 'i']

word = input()

result = [char for char in word if char.lower() not in vowels]
print(''.join(result))