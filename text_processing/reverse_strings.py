def reverse_string(word):
    while word != 'end':
        print(f"{word} = {word[::-1]}")
        word = input()

string = input()
reverse_string(string)